#!/usr/bin/env python3
"""
Ressam creature Power Score / XP reward calculator - first draft, not wired
into core/bestiary.md yet.

The idea (from a 2026-08-07 design conversation): Pathfinder ties a single
number (CR, or PF2e's Level) to both "how strong is this creature" and "how
much XP does it award," via a curve borrowed from nowhere else in the game.
Ressam doesn't need a borrowed curve - core/character/progression_&_rewards.md
already prices exactly the currency an NPC stat block is built from
(Attribute points, Skill points, Feats), one row per PC Level. This script
runs a finished stat block backward through that same table to find the
lowest PC Level that could legally afford it - the "Effective Level" - then
reads both a Power Score and an XP reward straight off that table, no new
math invented.

Effective Level = the MAX of four independent per-axis checks (a creature is
exactly as expensive as its single most demanding trait, not the average of
all of them - "no free lunches"):
  - Attribute Points: sum of all 8 Attributes vs. the level's cumulative
                 ATTR Points column. Skill ranks never count against this -
                 Attribute Points and Skill Points are two separate budgets
                 with no conversion between them (character_creation.md's
                 "Distribute Points").
  - Skill Points:  sum of all Skill ranks vs. the level's cumulative SKILL
                 Points column, checked independently of Attribute Points.
  - Attribute Cap: highest single Attribute vs. the level's ATTR Cap column.
  - Feats:         Feat count vs. the level's cumulative Feats column, or
                    Level 5 flat if any Feat is a Prestige Feat
                    (progression_&_rewards.md: "Can take a Prestige Feat"
                    first appears at Level 5) - whichever is higher.

There is no separate Skill Cap axis (the 2026-08-08 Skill/Attribute split
removed the level-gated Skill cap table entirely): a Skill's Rank can never
exceed its own governing Attribute's score, full stop (core_rules.md). That's
a build-legality check, not a level lookup - `score()` below flags any skill
that violates it via `illegal_skills` rather than folding it into the
level-axis max.

Untrained override: an NPC with zero ranks in every Skill, zero Feats, and
no Prestige Feat can never express its Attributes in an Attack or Skill
Check at all - under the current Skill Check Formula, Attribute never
contributes to that roll at all, only Skill does, exactly as core/bestiary.md's
own Peasant entry calls out ("even swinging a weapon it trained with its
whole life adds nothing beyond the flat 1d12"). Running the raw four-axis
rule against Peasant without this override scored it Effective Level 1 off
its Attribute Points/Attribute Cap alone (Attribute sum 6, within Level 1's
18-point Attribute budget) - technically true but combat-irrelevant, since
those Attributes never touch the dice. This override was found BY running
the calculator, not designed in up front; it only fires when Skill and Feat
investment are both truly zero, so it never touches Bandit/Knight/the
Pyromancer below.

XP reward = Total XP delta from Effective Level to Effective Level + 1 -
what it costs a PC to climb past this creature's own power tier, not the
creature's own Total XP (its cost to exist, not its value as a kill).
Lands inside progression_&_rewards.md's existing Minor/Average/Grand bands
with zero tuning for Peasant (30 XP, Minor floor) and Bandit (90 XP,
Average), and just past Grand's 105-300 ceiling for a single Knight (330
XP) - matching each entry's own flavor text without having been fit to it
on purpose.

Usage:
    python3 tools/power_score.py
"""

from dataclasses import dataclass, field


# level: (total_xp, attr_points, skill_points, attr_cap, feats) - attr_points
# and skill_points are two separate budgets, no conversion between them
# (character_creation.md's "Distribute Points").
# Source: core/character/progression_&_rewards.md's advancement table.
LEVEL_TABLE = {
    1:  (30,   18, 12, 4, 2),
    2:  (120,  18, 14, 4, 2),
    3:  (270,  18, 16, 4, 2),
    4:  (480,  19, 18, 4, 3),
    5:  (750,  19, 20, 4, 3),
    6:  (1080, 19, 22, 4, 4),
    7:  (1470, 19, 24, 4, 4),
    8:  (1920, 20, 26, 5, 4),
    9:  (2430, 20, 28, 5, 5),
    10: (3000, 20, 30, 5, 5),
    11: (3630, 20, 32, 5, 5),
    12: (4320, 21, 34, 5, 6),
}
MAX_LEVEL = 12

TOTAL_XP, ATTR_POINTS, SKILL_POINTS, ATTR_CAP, FEATS = range(5)

# Skill -> governing Attribute (core_rules.md's Skill Categories table).
# A Skill's Rank can never exceed this Attribute's current score - the sole
# Skill cap in the game, checked per-skill in score() below.
SKILL_ATTRIBUTE = {
    # STR - Brawn & Melee
    "Blades": "STR", "Hafted Weapons": "STR", "Polearms": "STR", "Brawling": "STR",
    # PRE - Finesse & Ranged
    "Archery": "PRE", "Marksmanship": "PRE", "Thrown": "PRE",
    # END - Defense & Survival
    "Athletics": "END", "Armorer": "END", "Survival": "END", "Shields": "END", "Riding": "END",
    # DEX - Adroitness & Subterfuge
    "Acrobatics": "DEX", "Stealth": "DEX", "Lockpicking": "DEX",
    "Sleight of Hand": "DEX", "Crafting": "DEX", "Perception": "DEX",
    # MIND - Intellectual
    "Alchemy": "MIND", "Enchanting": "MIND", "Spell Crafting": "MIND", "Historic Lore": "MIND",
    "Medical Lore": "MIND", "Nature Lore": "MIND", "Identify": "MIND",
    # ARC - Arcane Schools
    "Arcane Lore": "ARC", "Aeromancy": "ARC", "Geomancy": "ARC", "Hydromancy": "ARC",
    "Pyromancy": "ARC", "Shadowmancy": "ARC",
    # FAI - Divine Schools
    "Religious Lore": "FAI", "Benediction": "FAI", "Invocation": "FAI", "Necration": "FAI",
    "Cultivation": "FAI", "Subjugation": "FAI",
    # CHA - Socialising & Interaction
    "Persuasion": "CHA", "Deception": "CHA", "Intimidation": "CHA", "Leadership": "CHA",
    "Animal Handling": "CHA", "Insight": "CHA", "Performance": "CHA",
}


def total_xp(level):
    if level <= 0:
        return 0
    return LEVEL_TABLE[level][TOTAL_XP]


def _min_level_for(value, column):
    """Lowest PC Level (1-12) whose `column` covers `value`. 0 (or
    negative) always means "no level required." Returns MAX_LEVEL + 1 if
    no level up to 12 covers it (creature exceeds the game's own ceiling)."""
    if value <= 0:
        return 0
    for level in range(1, MAX_LEVEL + 1):
        if LEVEL_TABLE[level][column] >= value:
            return level
    return MAX_LEVEL + 1


@dataclass
class Creature:
    name: str
    attributes: dict            # STR/PRE/END/DEX/MIND/CHA/ARC/FAI -> value
    skills: dict = field(default_factory=dict)  # skill name -> rank
    feats: int = 0
    has_prestige_feat: bool = False


@dataclass
class PowerScore:
    name: str
    attr_points_level: int
    skill_points_level: int
    attr_cap_level: int
    feat_level: int
    untrained_override: bool
    illegal_skills: list
    effective_level: int
    power_score_xp: int
    xp_reward: int


def score(creature: Creature) -> PowerScore:
    attr_sum = sum(creature.attributes.values())
    attr_max = max(creature.attributes.values(), default=0)
    skill_sum = sum(creature.skills.values())
    skill_max = max(creature.skills.values(), default=0)

    attr_points_level = _min_level_for(attr_sum, ATTR_POINTS)
    skill_points_level = _min_level_for(skill_sum, SKILL_POINTS)
    attr_cap_level = _min_level_for(attr_max, ATTR_CAP)
    feat_level = _min_level_for(creature.feats, FEATS)
    if creature.has_prestige_feat:
        feat_level = max(feat_level, 5)

    # Skill legality: a Skill's Rank can never exceed its own governing
    # Attribute's score (core_rules.md) - not a level axis, a hard build
    # rule. Flagged rather than folded into effective_level so a violation
    # reads as "fix this build," not "this creature is just higher-level."
    illegal_skills = []
    for skill_name, rank in creature.skills.items():
        governing = SKILL_ATTRIBUTE.get(skill_name)
        if governing is None:
            continue
        attr_value = creature.attributes.get(governing, 0)
        if rank > attr_value:
            illegal_skills.append((skill_name, rank, governing, attr_value))

    effective_level = max(attr_points_level, skill_points_level, attr_cap_level, feat_level)

    untrained_override = (skill_sum == 0 and skill_max == 0
                           and creature.feats == 0
                           and not creature.has_prestige_feat)
    if untrained_override:
        effective_level = 0

    power_xp = total_xp(effective_level)
    xp_reward = (total_xp(effective_level + 1) - power_xp
                 if effective_level <= MAX_LEVEL else 0)

    return PowerScore(creature.name, attr_points_level, skill_points_level,
                       attr_cap_level, feat_level, untrained_override,
                       illegal_skills, effective_level, power_xp, xp_reward)


# ---------------------------------------------------------------------------
# core/bestiary.md's three existing entries, transcribed as-is.
# ---------------------------------------------------------------------------

PEASANT = Creature(
    name="Peasant",
    attributes=dict(STR=1, PRE=1, END=1, DEX=1, MIND=1, CHA=1, ARC=0, FAI=0),
)

BANDIT = Creature(
    name="Bandit",
    attributes=dict(STR=3, PRE=2, END=2, DEX=2, MIND=1, CHA=1, ARC=0, FAI=0),
    skills={"Blades": 2, "Intimidation": 1, "Perception": 1},
)

KNIGHT = Creature(
    name="Knight",
    attributes=dict(STR=4, PRE=3, END=4, DEX=3, MIND=1, CHA=1, ARC=0, FAI=1),
    skills={"Blades": 4, "Shields": 3, "Athletics": 2, "Riding": 2, "Perception": 1},
    feats=2,  # Tough, Second Wind - both General Feats, no Prestige gate
)

# Hypothetical - stress-tests the Attribute axis (never bound by any of the
# three martial NPCs above, since all three sit at or under a Level 1
# Attribute budget) and the Prestige Feat gate (also never exercised
# above). A battle-mage who burns her own Wounds instead of Mana - Blood-
# Rule (core/feats/prestige_feats.md) requires END 4+, +2 ranks in any
# magic school, +2 ranks in Medical Lore, and per progression_&_rewards.md
# is only legal to take at Level 5+.
PYROMANCER = Creature(
    name="Hypothetical - Blood-Rule Pyromancer",
    attributes=dict(STR=2, PRE=2, END=4, DEX=2, MIND=3, CHA=1, ARC=5, FAI=0),
    skills={"Pyromancy": 4, "Medical Lore": 2, "Perception": 1},
    feats=2,  # Blood-Rule (Prestige) + 1 General Feat
    has_prestige_feat=True,
)

# --- Universal bestiary batch (2026-08-07), generated per user request ---

SKELETON = Creature(
    name="Skeleton",
    attributes=dict(STR=2, PRE=1, END=2, DEX=1, MIND=0, CHA=0, ARC=0, FAI=0),
    skills={"Blades": 1},
)

WOLF = Creature(
    name="Wolf",
    attributes=dict(STR=2, PRE=1, END=2, DEX=3, MIND=1, CHA=1, ARC=0, FAI=0),
    skills={"Brawling": 2, "Perception": 2},
)

GUARD = Creature(
    name="Guard",
    attributes=dict(STR=3, PRE=1, END=3, DEX=1, MIND=1, CHA=1, ARC=0, FAI=0),
    skills={"Polearms": 2, "Shields": 2, "Perception": 1},
)

GIANT_RAT = Creature(
    name="Giant Rat",
    attributes=dict(STR=1, PRE=1, END=1, DEX=2, MIND=0, CHA=0, ARC=0, FAI=0),
    skills={"Brawling": 1, "Stealth": 1},
)

ARCHER = Creature(
    name="Archer",
    attributes=dict(STR=1, PRE=3, END=2, DEX=2, MIND=1, CHA=1, ARC=0, FAI=0),
    skills={"Archery": 2, "Perception": 2},
)

ZOMBIE = Creature(
    name="Zombie",
    attributes=dict(STR=3, PRE=1, END=2, DEX=0, MIND=0, CHA=0, ARC=0, FAI=0),
    skills={"Brawling": 1},
)

GIANT_SPIDER = Creature(
    name="Giant Spider",
    attributes=dict(STR=2, PRE=1, END=1, DEX=3, MIND=0, CHA=0, ARC=0, FAI=0),
    skills={"Brawling": 2, "Stealth": 2},
)

BEAR = Creature(
    name="Bear",
    attributes=dict(STR=4, PRE=1, END=4, DEX=1, MIND=0, CHA=0, ARC=0, FAI=0),
    skills={"Brawling": 3},
)

# The "extreme test" (2026-08-07): a Mythic-tier Wyrm, Attribute 5 / Skill 5
# (the actual PC-parity ceiling), plus Mythic Initiative(4) - which this
# calculator has NO way to represent at all. See tools/creature_rating.py and
# tools/encounter_rating.py for why that gap is the actual finding here.
WYRM = Creature(
    name="Wyrm",
    attributes=dict(STR=5, PRE=2, END=5, DEX=3, MIND=3, CHA=2, ARC=0, FAI=0),
    # Perception capped at 3, not 4 - DEX-governed, and DEX is 3 (a Skill
    # can never exceed its own governing Attribute, core_rules.md).
    skills={"Brawling": 5, "Perception": 3},
    feats=2,  # Tough, Second Wind - both General Feats, no Prestige gate
)


GIANT_VULTURE = Creature(
    name="Giant Vulture",
    attributes=dict(STR=2, PRE=1, END=1, DEX=3, MIND=1, CHA=0, ARC=0, FAI=0),
    skills={"Brawling": 2, "Perception": 2},
)

MIMIC = Creature(
    name="Mimic",
    attributes=dict(STR=3, PRE=1, END=3, DEX=1, MIND=1, CHA=0, ARC=0, FAI=0),
    skills={"Brawling": 2},
)


def main():
    cols = [
        ("Creature", "<32"), ("AttrPts", ">7"), ("SkillPts", ">8"), ("AttrCap", ">7"), ("Feat", ">5"),
        ("EffLvl", ">7"), ("PowerXP", ">8"), ("XP Reward", ">10"),
    ]
    header = "  ".join(f"{name:{fmt}}" for name, fmt in cols)
    print(header)
    print("-" * len(header))
    for creature in (PEASANT, BANDIT, GUARD, WOLF, GIANT_RAT, ARCHER, SKELETON, ZOMBIE,
                     GIANT_SPIDER, BEAR, GIANT_VULTURE, MIMIC, KNIGHT, PYROMANCER, WYRM):
        s = score(creature)
        row = [
            s.name, s.attr_points_level, s.skill_points_level, s.attr_cap_level,
            s.feat_level, s.effective_level,
            s.power_score_xp, s.xp_reward,
        ]
        print("  ".join(f"{val:{fmt}}" for val, (_, fmt) in zip(row, cols)))
        if s.untrained_override:
            print(f"{'':<32}  (untrained override: zero Skills/Feats -> Effective Level forced to 0)")
        if s.illegal_skills:
            for skill_name, rank, governing, attr_value in s.illegal_skills:
                print(f"{'':<32}  ILLEGAL: {skill_name} {rank} exceeds {governing} {attr_value}")


if __name__ == "__main__":
    main()
