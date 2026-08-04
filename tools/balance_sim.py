#!/usr/bin/env python3
"""
Ressam PvP combat balance simulator.

Monte Carlo duel sim grounded in core_rules.md / combat.md / maneuvers.md /
equipment/armor.md / equipment/weapons.md, as those files read on 2026-08-03.

Scope, deliberately: PC vs PC only. ENCOUNTER_GUIDE.md's monster tables are
known-stale (pending its own rebalance pass per TODO.md) and are not used
here. This tool answers "does the core math produce sane fights between
players," not "are monsters calibrated."

Maneuver Effects ARE modeled (Riposte, Exploit Opening, and one signature
Effect per Style), since they're a real chunk of the balance, not garnish.
Fixed effect-selection policy per Style (documented at EFFECT_POLICY below) -
this is a modeling choice, not a claim about optimal play:
  - Stopped (1 pick): always Riposte - an immediate free attack is the
    highest-value single pick in a pure damage race.
  - Dominant (2 picks): Riposte + one signature Effect per style -
    Parry -> Guard Break, Block -> Push Back, Dodge -> Untouchable.
    (Bind Weapon, Stagger, and Reposition are not modeled - see below.)

Known simplifications:
  - Riposte's bonus attack cannot itself be answered with a Maneuver, and
    doesn't chain into further Effects - avoids unbounded recursion. A real
    table could keep escalating; this sim caps it at one bonus swing.
  - Push Back and Stagger are positional Effects with no clean numeric
    translation absent a movement/range model. Push Back is approximated as
    "melee attacker skips their next attack" (closing distance again);
    Stagger is not modeled at all (Speed 0 is a no-op between two
    already-adjacent combatants, which is arguably a real signal: Stagger
    reads weaker than Push Back specifically in stand-and-trade duels).
    Reposition (Dodge's other signature) is likewise positional and unmodeled.
  - Reactive Casting and all spellcasting - every build here is martial.
  - Temp Wounds, Trauma, the Death Clock / Coup de Grace - first character
    to hit 0 Wounds simply loses the duel.
  - Wound Penalty is combat-irrelevant by design ("no combat death spiral")
    and so isn't modeled mid-fight.
  - Firearms (misfire, reload) are out of scope; Longbow stands in for
    "ranged" archetypes.
  - A Dominant/Stopped Parry does not degrade armor, same as Dodge - per
    the user's call, since maneuvers.md states Dodge's exemption explicitly
    but is silent on Parry. Block's "always degrades" is explicit and kept.
  - Point-buy legality against the progression table isn't enforced; build
    stats below are hand-picked to sit within each level's caps, not
    derived from spending the exact budget.

Usage:
    python3 tools/balance_sim.py [trials]
"""

import random
import sys
from dataclasses import dataclass, field
from itertools import combinations

D12 = 12


def roll_d12(advantage=False, disadvantage=False):
    net = int(advantage) - int(disadvantage)
    a, b = random.randint(1, D12), random.randint(1, D12)
    if net > 0:
        return max(a, b)
    if net < 0:
        return min(a, b)
    return a


def roll_dice_string(spec):
    bonus = 0
    if "+" in spec:
        spec, b = spec.split("+")
        bonus = int(b)
    n, d = spec.lower().split("d")
    n = int(n)
    total = sum(random.randint(1, int(d)) for _ in range(n))
    return total + bonus


@dataclass
class Weapon:
    name: str
    dice: str          # e.g. "1d12", "2d4+2"
    attribute: str      # 'STR' or 'PRE' - which attribute the Skill Category uses
    crit_floor: int     # natural roll that starts a crit threat (12 = no expansion)
    ranged: bool = False

    def roll_damage(self):
        return roll_dice_string(self.dice)


@dataclass
class Status:
    """Transient per-character flags carried between attack instances."""
    next_attack_advantage: bool = False       # Exploit Opening
    next_attack_disadvantage: bool = False    # Bind Weapon (unused by current policy)
    skip_next_attack: bool = False            # Push Back (melee attacker only)
    reaction_disabled: bool = False           # Guard Break (blocks Parry/Block only)
    incoming_attack_disadvantage: bool = False  # Untouchable


@dataclass
class Build:
    name: str
    level: int
    STR: int
    PRE: int
    END: int
    DEX: int
    weapon: Weapon
    weapon_skill: int
    armor_ar: int
    armor_penalty: int      # after Armorer reduction already applied
    agility_skill: int
    style: str               # 'parry', 'block', or 'dodge'
    shields_skill: int = 0
    shield_ar_bonus: int = 0
    two_handed_block: bool = False  # Block via a Two-Handed weapon, not a shield
    seek_the_seam: bool = False  # Seek the Seam feat (martial_feats.md): Dagger/Knife hits
                                  # bypass half AR and never degrade armor
    CHA: int = 1
    deception_skill: int = 0    # >0 means this build has the Feint feat (martial_feats.md) and
                                  # attempts it every round before attacking - a free Minor Action,
                                  # doesn't touch the shared Reaction pool
    insight_skill: int = 0
    sneak_attack_dice: str = None  # Sneak Attack feat (martial_feats.md, reinstated):
                                    # bonus damage die when a melee attack lands with Advantage

    def apply_ar(self, current_ar):
        """Returns (AR to subtract from this hit, whether the hit degrades armor)."""
        if self.seek_the_seam:
            return current_ar // 2, False
        return current_ar, True

    def attribute_value(self):
        return self.STR if self.weapon.attribute == "STR" else self.PRE

    @property
    def wounds_max(self):
        return self.END

    @property
    def evasion(self):
        return 5 + self.agility_skill + self.DEX - self.armor_penalty

    def attack_roll(self, advantage=False, disadvantage=False):
        natural = roll_d12(advantage, disadvantage)
        if self.weapon_skill <= 0:
            return natural, natural  # untrained: 1d12 alone
        total = natural + self.weapon_skill + self.attribute_value()
        return natural, total

    def is_crit(self, natural):
        return natural >= self.weapon.crit_floor

    def can_parry(self):
        return self.weapon_skill >= 1  # melee weapon in hand, 1+ rank

    def can_block(self, incoming_ranged):
        if self.shields_skill < 1:
            return False
        if self.two_handed_block:
            return not incoming_ranged  # Two-Handed weapon only blocks melee
        return True  # shield blocks both melee and ranged

    def style_roll(self):
        if self.style == "parry":
            natural = roll_d12()
            return natural + self.weapon_skill + self.attribute_value()
        if self.style == "block":
            natural = roll_d12()
            return natural + self.shields_skill + self.END
        if self.style == "dodge":
            natural = roll_d12()
            return natural + self.agility_skill + self.DEX
        raise ValueError(self.style)


def initiative(build):
    return roll_d12() + (build.PRE + build.DEX) // 2


def attempt_feint(attacker, defender, statuses):
    """Feint (martial_feats.md, gated behind +2 ranks in Deception): Minor
    Action, Deception vs static Insight (Contested Check - only the
    instigator rolls, ties favor the instigator). On success, grants
    Advantage on all of the attacker's weapon attacks this turn - modeled
    here as Advantage on their one attack this round. Costs no Major Action
    and no Reaction, so it's attempted every round for free by any build
    that's taken the feat (deception_skill > 0)."""
    if attacker.deception_skill <= 0:
        return
    feint_roll = roll_d12() + attacker.deception_skill + attacker.CHA
    static_insight = 5 + defender.insight_skill + defender.CHA
    if feint_roll >= static_insight:
        statuses[id(attacker)].next_attack_advantage = True


def wounds_from_damage(after_ar):
    if after_ar >= 16:
        return 3
    if after_ar >= 10:
        return 2
    if after_ar >= 1:
        return 1
    return 0


def raw_attack(attacker, defender, armor_state, advantage=False, disadvantage=False):
    """A single attack roll with no Maneuver reaction available to the
    defender (used for Riposte's bonus swing). Always degrades armor on a
    connecting hit, same as a Failed Maneuver would. Returns wounds dealt."""
    natural, atk_total = attacker.attack_roll(advantage, disadvantage)
    if atk_total < defender.evasion:
        return 0
    crit = attacker.is_crit(natural)
    raw = attacker.weapon.roll_damage() + attacker.attribute_value()
    if crit:
        raw = max(raw, attacker.weapon.roll_damage() + attacker.attribute_value())
    current_ar = armor_state[id(defender)]
    ar_to_subtract, should_degrade = attacker.apply_ar(current_ar)
    after_ar = max(0, raw - ar_to_subtract)
    if should_degrade:
        armor_state[id(defender)] = max(0, current_ar - 1)
    return wounds_from_damage(after_ar)


def resolve_attack(attacker, defender, armor_state, statuses, adjacent=True):
    """Full attack + Maneuver resolution. Returns (wounds_to_defender, wounds_to_attacker).

    `adjacent=False` is used by the kiting approach phase (see
    simulate_kiting_duel): the defender has no melee reach yet, so Riposte
    isn't physically possible even on a won Maneuver - Exploit Opening is
    substituted instead. Parry itself is unconditionally unavailable against
    a ranged attack regardless of adjacency (maneuvers.md: "Restrictions:
    Melee attacks only") - this was a bug in the first cut of this sim,
    which let Parry answer a Longbow shot.
    """
    st_attacker = statuses[id(attacker)]
    st_defender = statuses[id(defender)]

    if st_attacker.skip_next_attack:
        st_attacker.skip_next_attack = False
        return 0, 0

    advantage = st_attacker.next_attack_advantage
    disadvantage = st_attacker.next_attack_disadvantage or st_defender.incoming_attack_disadvantage
    st_attacker.next_attack_advantage = False
    st_attacker.next_attack_disadvantage = False
    st_defender.incoming_attack_disadvantage = False

    natural, atk_total = attacker.attack_roll(advantage, disadvantage)
    if atk_total < defender.evasion:
        return 0, 0  # missed passive Evasion entirely, no Maneuver needed

    crit = attacker.is_crit(natural)
    raw = attacker.weapon.roll_damage() + attacker.attribute_value()
    if crit:
        raw = max(raw, attacker.weapon.roll_damage() + attacker.attribute_value())

    # Sneak Attack (martial_feats.md): once per turn, a melee hit landed with
    # Advantage. If Advantage and Disadvantage both applied and cancelled out
    # (stacking rule, core_rules.md), that's not "with Advantage" anymore.
    if attacker.sneak_attack_dice and not attacker.weapon.ranged and advantage and not disadvantage:
        raw += roll_dice_string(attacker.sneak_attack_dice)

    style_available = defender.style == "dodge" or (
        defender.style == "parry" and defender.can_parry() and not attacker.weapon.ranged
    ) or (
        defender.style == "block" and defender.can_block(attacker.weapon.ranged)
    )
    if defender.style in ("parry", "block") and st_defender.reaction_disabled:
        style_available = False  # Guard Break - Dodge is unaffected, already excluded above
    st_defender.reaction_disabled = False

    if crit and defender.style in ("parry", "block"):
        style_available = False  # crits bypass Parry/Block entirely; Dodge is unaffected

    band = None
    if style_available:
        margin = defender.style_roll() - atk_total
        if margin >= 3:
            band = "dominant"
        elif margin >= 0:
            band = "stopped"
        elif margin >= -2:
            band = "minimized"
        else:
            band = "failed"

    wounds_to_attacker = 0
    degrade = True

    if band in ("dominant", "stopped"):
        if defender.style in ("dodge", "parry"):
            degrade = False  # see module docstring re: Parry-vs-Dodge armor call
        raw_after = 0

        # Effect selection (see EFFECT_POLICY docstring at top of file).
        if adjacent:
            wounds_to_attacker += raw_attack(defender, attacker, armor_state)  # Riposte
        else:
            st_defender.next_attack_advantage = True  # Riposte not reachable - Exploit Opening instead
        if band == "dominant":
            if defender.style == "parry":
                st_attacker.reaction_disabled = True          # Guard Break
            elif defender.style == "block":
                if not attacker.weapon.ranged:
                    st_attacker.skip_next_attack = True         # Push Back
            elif defender.style == "dodge":
                st_defender.incoming_attack_disadvantage = True  # Untouchable
            else:
                st_defender.next_attack_advantage = True
    elif band == "minimized":
        if defender.style == "parry":
            raw_after = max(0, raw - roll_dice_string(defender.weapon.dice))
        elif defender.style == "block":
            reduction = (
                defender.shield_ar_bonus
                if not defender.two_handed_block
                else defender.shields_skill // 2
            )
            raw_after = max(0, raw - reduction)
        elif defender.style == "dodge":
            raw_after = raw // 2
        else:
            raw_after = raw
    else:
        raw_after = raw  # Failed reaction, or no reaction attempted: full damage

    current_ar = armor_state[id(defender)]
    ar_to_subtract, attacker_allows_degrade = attacker.apply_ar(current_ar)
    after_ar = max(0, raw_after - ar_to_subtract)
    if degrade and attacker_allows_degrade:
        armor_state[id(defender)] = max(0, current_ar - 1)

    return wounds_from_damage(after_ar), wounds_to_attacker


def melee_phase(a, b, wounds, armor, statuses, start_round=1, max_rounds=50):
    """Standard adjacent, alternating-turn dueling until someone hits 0 Wounds.
    Shared by the plain duel and by the tail end of the opening scenarios
    below, once distance has closed to zero or the ambush hit has landed."""
    init_a, init_b = initiative(a), initiative(b)
    order = [a, b] if init_a >= init_b else [b, a]

    for rnd in range(start_round, max_rounds + 1):
        for attacker in order:
            defender = b if attacker is a else a
            attempt_feint(attacker, defender, statuses)
            dmg_to_defender, dmg_to_attacker = resolve_attack(attacker, defender, armor, statuses)
            wounds[id(defender)] -= dmg_to_defender
            wounds[id(attacker)] -= dmg_to_attacker
            if wounds[id(defender)] <= 0:
                return ("a" if attacker is a else "b"), rnd
            if wounds[id(attacker)] <= 0:
                return ("b" if attacker is a else "a"), rnd
    return "draw", max_rounds


def simulate_duel(a, b, max_rounds=50):
    """Returns ('a'|'b'|'draw', rounds_elapsed). Both start adjacent - the
    baseline stand-and-trade duel, no opening advantage for either side."""
    wounds = {id(a): a.wounds_max, id(b): b.wounds_max}
    armor = {id(a): a.armor_ar, id(b): b.armor_ar}
    statuses = {id(a): Status(), id(b): Status()}
    return melee_phase(a, b, wounds, armor, statuses)


def simulate_ambush_duel(ambusher, other, max_rounds=50):
    """The Skirmisher's identity: closes via Stealth and opens with a
    Surprise Round - core_rules.md's Surprise: "Surprised creatures cannot
    take actions or Reactions during Round 1... Act normally from Round 2."
    One free, fully unanswerable hit, then a normal adjacent duel from
    round 2. Returns ('a'=ambusher | 'b'=other | 'draw', rounds_elapsed)."""
    wounds = {id(ambusher): ambusher.wounds_max, id(other): other.wounds_max}
    armor = {id(ambusher): ambusher.armor_ar, id(other): other.armor_ar}
    statuses = {id(ambusher): Status(), id(other): Status()}

    dmg = raw_attack(ambusher, other, armor)
    wounds[id(other)] -= dmg
    if wounds[id(other)] <= 0:
        return "a", 1

    return melee_phase(ambusher, other, wounds, armor, statuses, start_round=2, max_rounds=max_rounds)


def simulate_kiting_duel(archer, pursuer, start_distance=90, speed=30, max_rounds=50):
    """The Archer's identity: opens at range and gets free/lightly-contested
    shots while the melee side closes. Pursuer Dashes every round it isn't
    yet adjacent (Major Action, no attack, +speed movement - core_rules.md's
    Dashing); the archer fires (Major Action) then retreats by its normal
    Move afterward (movement can split before/after an action). Net closure
    is therefore one `speed` per round (2x pursuer Dash minus 1x archer
    retreat) - a deliberate modeling choice, not a rule, since the rules
    don't resolve continuous-distance kiting explicitly. Once distance
    reaches 0, resolves as a normal adjacent duel.
    Returns ('a'=archer | 'b'=pursuer | 'draw', rounds_elapsed)."""
    wounds = {id(archer): archer.wounds_max, id(pursuer): pursuer.wounds_max}
    armor = {id(archer): archer.armor_ar, id(pursuer): pursuer.armor_ar}
    statuses = {id(archer): Status(), id(pursuer): Status()}

    distance = start_distance
    rnd = 0
    while distance > 0 and rnd < max_rounds:
        rnd += 1
        dmg_to_pursuer, dmg_to_archer = resolve_attack(
            archer, pursuer, armor, statuses, adjacent=False
        )
        wounds[id(pursuer)] -= dmg_to_pursuer
        wounds[id(archer)] -= dmg_to_archer
        if wounds[id(pursuer)] <= 0:
            return "a", rnd
        if wounds[id(archer)] <= 0:
            return "b", rnd
        distance -= speed

    return melee_phase(archer, pursuer, wounds, armor, statuses, start_round=rnd + 1, max_rounds=max_rounds)


# ---------------------------------------------------------------------------
# Weapon definitions (equipment/weapons.md)
# ---------------------------------------------------------------------------

GREATSWORD = Weapon("Greatsword", "1d12", "STR", crit_floor=11)
BROADSWORD = Weapon("Broadsword", "1d10", "STR", crit_floor=12)
RAPIER = Weapon("Rapier", "1d8", "PRE", crit_floor=10)
DAGGER = Weapon("Dagger", "1d4", "PRE", crit_floor=9)
LONGBOW = Weapon("Longbow", "1d8", "PRE", crit_floor=11, ranged=True)

# ---------------------------------------------------------------------------
# Archetypes x level snapshots (level 1 / 4 / 8 / 12, matching the
# progression table's skill/attribute cap breakpoints)
# ---------------------------------------------------------------------------

ARCHETYPE_TABLE = {
    "Greatsword Brute": {  # Full Plate, Parry (a melee weapon in hand qualifies)
        1: dict(STR=4, PRE=1, END=3, DEX=1, weapon_skill=2, armor_ar=8,
                armor_penalty=7, agility_skill=0),
        4: dict(STR=4, PRE=1, END=4, DEX=1, weapon_skill=3, armor_ar=8,
                armor_penalty=6, agility_skill=0),
        8: dict(STR=5, PRE=1, END=5, DEX=1, weapon_skill=5, armor_ar=8,
                armor_penalty=5, agility_skill=0),
        12: dict(STR=5, PRE=1, END=5, DEX=2, weapon_skill=5, armor_ar=8,
                 armor_penalty=4, agility_skill=1),
    },
    "Sword & Board Tank": {  # Broadsword + Kite Shield, Block
        1: dict(STR=3, PRE=1, END=4, DEX=1, weapon_skill=2, armor_ar=7,
                armor_penalty=6, agility_skill=0, shields_skill=2, shield_ar_bonus=3),
        4: dict(STR=4, PRE=1, END=4, DEX=1, weapon_skill=3, armor_ar=7,
                armor_penalty=5, agility_skill=0, shields_skill=3, shield_ar_bonus=3),
        8: dict(STR=5, PRE=1, END=5, DEX=1, weapon_skill=5, armor_ar=7,
                armor_penalty=4, agility_skill=0, shields_skill=5, shield_ar_bonus=3),
        12: dict(STR=5, PRE=1, END=5, DEX=2, weapon_skill=5, armor_ar=7,
                 armor_penalty=3, agility_skill=0, shields_skill=5, shield_ar_bonus=3),
    },
    "Rapier Duelist": {  # Buff Coat + Buckler, Parry
        1: dict(STR=1, PRE=4, END=2, DEX=2, weapon_skill=2, armor_ar=3,
                armor_penalty=1, agility_skill=0),
        4: dict(STR=1, PRE=4, END=3, DEX=2, weapon_skill=3, armor_ar=3,
                armor_penalty=0, agility_skill=1),
        8: dict(STR=1, PRE=5, END=3, DEX=3, weapon_skill=5, armor_ar=3,
                armor_penalty=0, agility_skill=1),
        12: dict(STR=1, PRE=5, END=4, DEX=4, weapon_skill=5, armor_ar=3,
                 armor_penalty=0, agility_skill=2),
    },
    "Dagger Skirmisher": {  # Gambeson (or none), Dodge
        1: dict(STR=1, PRE=2, END=2, DEX=4, weapon_skill=2, armor_ar=2,
                armor_penalty=1, agility_skill=2),
        4: dict(STR=1, PRE=2, END=3, DEX=4, weapon_skill=3, armor_ar=2,
                armor_penalty=0, agility_skill=3),
        8: dict(STR=1, PRE=3, END=3, DEX=5, weapon_skill=5, armor_ar=2,
                armor_penalty=0, agility_skill=5),
        12: dict(STR=1, PRE=3, END=4, DEX=5, weapon_skill=5, armor_ar=2,
                 armor_penalty=0, agility_skill=5),
    },
    "Longbow Archer": {  # Buff Coat, Dodge (Parry/Block don't apply at range)
        1: dict(STR=1, PRE=4, END=2, DEX=2, weapon_skill=2, armor_ar=3,
                armor_penalty=1, agility_skill=0),
        4: dict(STR=1, PRE=4, END=3, DEX=2, weapon_skill=3, armor_ar=3,
                armor_penalty=0, agility_skill=1),
        8: dict(STR=1, PRE=5, END=3, DEX=3, weapon_skill=5, armor_ar=3,
                armor_penalty=0, agility_skill=2),
        12: dict(STR=1, PRE=5, END=4, DEX=4, weapon_skill=5, armor_ar=3,
                 armor_penalty=0, agility_skill=3),
    },
}

WEAPONS = {
    "Greatsword Brute": GREATSWORD,
    "Sword & Board Tank": BROADSWORD,
    "Rapier Duelist": RAPIER,
    "Dagger Skirmisher": DAGGER,
    "Longbow Archer": LONGBOW,
}
STYLES = {
    "Greatsword Brute": "parry",
    "Sword & Board Tank": "block",
    "Rapier Duelist": "parry",
    "Dagger Skirmisher": "dodge",
    "Longbow Archer": "dodge",
}
TWO_HANDED_BLOCK = set()  # none of these archetypes block via a 2H weapon


def make_build(archetype, level):
    stats = ARCHETYPE_TABLE[archetype][level]
    weapon = WEAPONS[archetype]
    return Build(
        name=f"{archetype} L{level}",
        level=level,
        STR=stats["STR"], PRE=stats["PRE"], END=stats["END"], DEX=stats["DEX"],
        weapon=weapon,
        weapon_skill=stats["weapon_skill"],
        armor_ar=stats["armor_ar"],
        armor_penalty=stats["armor_penalty"],
        agility_skill=stats["agility_skill"],
        style=STYLES[archetype],
        shields_skill=stats.get("shields_skill", 0),
        shield_ar_bonus=stats.get("shield_ar_bonus", 0),
        two_handed_block=archetype in TWO_HANDED_BLOCK,
        # Seek the Seam (martial_feats.md): +3 ranks in Daggers & Knives prerequisite
        seek_the_seam=(archetype == "Dagger Skirmisher" and stats["weapon_skill"] >= 3),
    )


def report_matchup(name_a, name_b, sim_fn, n, **sim_kwargs):
    a_wins = b_wins = draws = 0
    total_rounds = 0
    level = sim_kwargs.pop("level")
    for _ in range(n):
        a, b = make_build(name_a, level), make_build(name_b, level)
        winner, rounds = sim_fn(a, b, **sim_kwargs)
        total_rounds += rounds
        if winner == "a":
            a_wins += 1
        elif winner == "b":
            b_wins += 1
        else:
            draws += 1
    avg_rounds = total_rounds / n
    print(
        f"{name_a:22s} vs {name_b:22s}  "
        f"{name_a.split()[0]}: {a_wins/n:5.1%}   "
        f"{name_b.split()[0]}: {b_wins/n:5.1%}   "
        f"draws: {draws/n:4.1%}   avg rounds: {avg_rounds:4.1f}"
    )


def run(trials_per_matchup=2000):
    levels = [1, 4, 8, 12]
    archetypes = list(ARCHETYPE_TABLE.keys())

    for level in levels:
        print(f"\n{'=' * 70}\nLEVEL {level} - baseline (both start adjacent)\n{'=' * 70}")
        for name_a, name_b in combinations(archetypes, 2):
            report_matchup(name_a, name_b, simulate_duel, trials_per_matchup, level=level)

        print(f"\n--- LEVEL {level} - Dagger Skirmisher opens with a Surprise ambush ---")
        for opponent in archetypes:
            if opponent == "Dagger Skirmisher":
                continue
            report_matchup(
                "Dagger Skirmisher", opponent, simulate_ambush_duel, trials_per_matchup, level=level
            )

        print(f"\n--- LEVEL {level} - Longbow Archer opens at range (kiting, start_distance=90ft) ---")
        for opponent in archetypes:
            if opponent == "Longbow Archer":
                continue
            report_matchup(
                "Longbow Archer", opponent, simulate_kiting_duel, trials_per_matchup,
                level=level, start_distance=90, speed=30,
            )


SNEAK_ATTACK_DICE_OPTIONS = ["1d4", "1d6", "1d8", "2d6"]


def make_sneak_attack_build(level, dice):
    """Dagger Skirmisher variant with the reinstated Sneak Attack feat
    (martial_feats.md - finalized at DEX 4+, 1d6, dice param kept for
    what-if sweeps). Feint (deception_skill), now its own feat gated behind
    +2 ranks in Deception rather than a free Basic Move, is what actually
    grants the Advantage Sneak Attack requires - a free Minor Action, so
    it's attempted every round via attempt_feint(). Gated from L4+ only,
    matching the existing +3-ranks-in-weapon-Skill schedule used for Seek
    the Seam - Sneak Attack's own prerequisites (DEX 4+, +3 Stealth, +3
    weapon Skill) aren't met before then either."""
    b = make_build("Dagger Skirmisher", level)
    if b.weapon_skill >= 3:
        b.deception_skill = b.weapon_skill
        b.CHA = 2
        b.sneak_attack_dice = dice
    return b


def run_sneak_attack_sweep(trials_per_matchup=3000):
    levels = [4, 8, 12]
    opponents = ["Greatsword Brute", "Sword & Board Tank"]

    for level in levels:
        print(f"\n--- LEVEL {level} - Dagger Skirmisher with Sneak Attack (Feint-enabled) ---")
        for opponent in opponents:
            for dice in SNEAK_ATTACK_DICE_OPTIONS:
                a_wins = b_wins = draws = 0
                total_rounds = 0
                for _ in range(trials_per_matchup):
                    a = make_sneak_attack_build(level, dice)
                    b = make_build(opponent, level)
                    winner, rounds = simulate_duel(a, b)
                    total_rounds += rounds
                    if winner == "a":
                        a_wins += 1
                    elif winner == "b":
                        b_wins += 1
                    else:
                        draws += 1
                n = trials_per_matchup
                print(
                    f"  vs {opponent:20s}  Sneak Attack {dice:4s}  "
                    f"Dagger: {a_wins/n:5.1%}   {opponent.split()[0]}: {b_wins/n:5.1%}   "
                    f"avg rounds: {total_rounds/n:4.1f}"
                )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "sneak":
        trials = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
        run_sneak_attack_sweep(trials)
    else:
        trials = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
        run(trials)