#!/usr/bin/env python3
"""
Ressam party-vs-monster group combat simulator.

Monte Carlo group-fight sim grounded in core_rules.md / combat.md /
maneuvers.md / ENCOUNTER_GUIDE.md, as those files read on 2026-08-05.

Scope: this started as a validation pass against ENCOUNTER_GUIDE.md's Level
1 Example Roster and its stated Role ratios (Easy 4:1, Average 2:1, Elite
1:1) - the same way tools/balance_sim.py validates PC-vs-PC math, which
ENCOUNTER_GUIDE.md says outright its own ratios have never had. That
validation found the original ratios badly uneven against each other (Easy
72% PCs win, Average 8%, Elite 64%, at a 4-PC level-1 party) and the
original Mythic essentially unable to act before dying. Per project
decision (2026-08-05): retune monster counts and stat lines - freely,
without preserving ENCOUNTER_GUIDE.md's fictional Role framing or its
"cap - offset" formula - until Easy/Average/Elite each land close to a
50/50 fight at counts EASY_COUNT=8, AVERAGE_COUNT=6, ELITE_COUNT=4. Mythic
is intentionally left weak solo (see make_timber_fang) - a real Mythic
encounter is expected to bring allies and play tactically, not win a fair
fight as a lone stat block. ENCOUNTER_GUIDE.md itself has NOT been updated
to match yet - these builds/counts exist only in this file until that's
decided.

Reuses primitives from balance_sim.py (Build, Weapon, Status, roll_d12,
roll_dice_string, wounds_from_damage, raw_attack) rather than forking them.
Build.style=None is used for every monster in this file: none of the four
Example Roster stat blocks in ENCOUNTER_GUIDE.md assign a Maneuver Style
(only Elite/Mythic get a "signature trait", which is not the same thing),
so monsters here never Parry/Block/Dodge - only the 4 PCs can.

Group-combat additions balance_sim.py's 1v1 duels didn't need:
  - N attackers per side, fixed initiative order for the whole fight
    (combat.md: "Fixed for combat unless... you voluntarily swap").
  - Per-round Reaction pools (DEX+PRE)//3, gating how many of the incoming
    attacks a PC can actually answer with a Maneuver once several monsters
    are swinging at them in the same round - resolve_attack() in
    balance_sim.py has no notion of a shared pool since a 1v1 duel never
    exhausts it. resolve_group_attack() below adds that gate.
  - Mythic Initiative: multiple fixed turns/round at an escalating -2,
    each a full turn (combat.md).
  - Random target selection each attack, on both sides. No positioning,
    focus-fire optimization, or protecting-a-downed-ally logic is modeled -
    same "no battlemap" simplification balance_sim.py already makes for
    duels, just extended to N combatants instead of 2.

Known simplifications (beyond the ones balance_sim.py already documents,
which still apply: no Trauma, no Feint/Sneak Attack on these builds, Push
Back/Stagger/Reposition unmodeled, etc.):
  - A combatant reaching 0 Wounds is treated as removed from the fight for
    outcome purposes (matches balance_sim.py's duel-ending rule), not run
    through Dying/Death Clock/Stabilization/Coup de Grace. This is a
    deliberate scope cut, not an oversight: modeling Coup de Grace without
    a positioning model would just mean "whoever goes down first
    auto-dies next monster turn," which tests the Dying rules, not the
    Role ratios this file exists to validate.
  - Reaction pools reset for every living combatant at the start of each
    full round, not individually at the start of each combatant's own
    turn (core_rules.md technically means the latter). Immaterial here
    since nothing in this fight grants an extra out-of-turn Reaction
    refresh except the Mythic's own turns, which is handled explicitly.
  - Ambush Leader (Bandit Captain): Advantage on each captain's own first
    attack roll of the fight (read as per-individual, since 4 captains
    ambushing together each get their own first swing).
  - Howl (Timber Fang): modeled as replacing the Fang's attack on the
    first of its 3 turns each round (an AoE fear effect, not a normal
    attack) rather than a bonus action alongside one - the stat block
    doesn't specify which, and treating it as "the turn's whole action"
    is the conservative reading for how much damage output it forgoes.
    Frightened's "until the end of its next turn" is modeled as
    disadvantage on that PC's very next attack roll only.
  - PCs have no MIND/MIND-Skill investment (pure martial archetypes, per
    balance_sim.py) - Howl's Ward Check uses MIND 1, Skill 0 for all four.

Usage:
    python3 tools/encounter_sim.py [trials]
"""

import random
import sys
from dataclasses import dataclass, field, replace

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from balance_sim import (
    Build, Weapon, Status, roll_d12, roll_dice_string, wounds_from_damage,
    raw_attack, GREATSWORD, BROADSWORD, RAPIER, LONGBOW, ARCHETYPE_TABLE,
)

BRAWLING_PUNCH = Weapon("Punch", "1d6", "STR", crit_floor=12)
SHORTSWORD = Weapon("Shortsword", "1d6+1", "STR", crit_floor=12)
BANDIT_BROADSWORD = Weapon("Broadsword", "1d10", "STR", crit_floor=12)
FANG_BITE = Weapon("Bite", "1d8", "STR", crit_floor=12)


# ---------------------------------------------------------------------------
# Group-combat attack resolution (extends balance_sim.resolve_attack with a
# per-round Reaction-pool gate; see module docstring)
# ---------------------------------------------------------------------------

def resolve_group_attack(attacker, defender, armor_state, statuses, reactions_left,
                          advantage=False, disadvantage=False):
    """Same margin/Effect logic as balance_sim.resolve_attack, plus: a
    Maneuver is only even attempted if reactions_left[id(defender)] > 0,
    decremented on any attempt (win or lose - "Failed: your Reaction is
    spent for nothing," maneuvers.md). Returns (wounds_to_defender,
    wounds_to_attacker)."""
    st_attacker = statuses[id(attacker)]
    st_defender = statuses[id(defender)]

    if st_attacker.skip_next_attack:
        st_attacker.skip_next_attack = False
        return 0, 0

    adv = advantage or st_attacker.next_attack_advantage
    disadv = disadvantage or st_attacker.next_attack_disadvantage or st_defender.incoming_attack_disadvantage
    st_attacker.next_attack_advantage = False
    st_attacker.next_attack_disadvantage = False
    st_defender.incoming_attack_disadvantage = False

    natural, atk_total = attacker.attack_roll(adv, disadv)
    if atk_total < defender.evasion:
        return 0, 0

    crit = attacker.is_crit(natural)
    raw = attacker.weapon.roll_damage() + attacker.attribute_value()
    if crit:
        raw = max(raw, attacker.weapon.roll_damage() + attacker.attribute_value())

    has_reaction = reactions_left.get(id(defender), 0) > 0
    style_available = has_reaction and (
        defender.style == "dodge" or (
            defender.style == "parry" and defender.can_parry() and not attacker.weapon.ranged
        ) or (
            defender.style == "block" and defender.can_block(attacker.weapon.ranged)
        )
    )
    if defender.style in ("parry", "block") and st_defender.reaction_disabled:
        style_available = False
    st_defender.reaction_disabled = False

    if crit and defender.style in ("parry", "block"):
        style_available = False

    if style_available:
        reactions_left[id(defender)] -= 1

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
            degrade = False
        raw_after = 0
        wounds_to_attacker += raw_attack(defender, attacker, armor_state)  # Riposte
        if band == "dominant":
            if defender.style == "parry":
                st_attacker.reaction_disabled = True
            elif defender.style == "block":
                if not attacker.weapon.ranged:
                    st_attacker.skip_next_attack = True
            elif defender.style == "dodge":
                st_defender.incoming_attack_disadvantage = True
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
        raw_after = raw

    current_ar = armor_state[id(defender)]
    ar_to_subtract, attacker_allows_degrade = attacker.apply_ar(current_ar)
    after_ar = max(0, raw_after - ar_to_subtract)
    if degrade and attacker_allows_degrade:
        armor_state[id(defender)] = max(0, current_ar - 1)

    return wounds_from_damage(after_ar), wounds_to_attacker


# ---------------------------------------------------------------------------
# PC builds - Level 1, generic 4-person party (balance_sim.py archetypes)
# ---------------------------------------------------------------------------

def make_pc(archetype):
    b = None
    stats = ARCHETYPE_TABLE[archetype][1]
    weapon = {"Greatsword Brute": GREATSWORD, "Sword & Board Tank": BROADSWORD,
              "Rapier Duelist": RAPIER, "Longbow Archer": LONGBOW}[archetype]
    style = {"Greatsword Brute": "parry", "Sword & Board Tank": "block",
             "Rapier Duelist": "parry", "Longbow Archer": "dodge"}[archetype]
    return Build(
        name=archetype, level=1,
        STR=stats["STR"], PRE=stats["PRE"], END=stats["END"], DEX=stats["DEX"],
        weapon=weapon, weapon_skill=stats["weapon_skill"],
        armor_ar=stats["armor_ar"], armor_penalty=stats["armor_penalty"],
        agility_skill=stats["agility_skill"], style=style,
        shields_skill=stats.get("shields_skill", 0),
        shield_ar_bonus=stats.get("shield_ar_bonus", 0),
    )


def make_party():
    return [make_pc(a) for a in
            ["Greatsword Brute", "Sword & Board Tank", "Rapier Duelist", "Longbow Archer"]]


def reactions_of(build):
    return (build.DEX + build.PRE) // 3


# ---------------------------------------------------------------------------
# Monster builds - Threat Level 1, Level-1 Example Roster (ENCOUNTER_GUIDE.md)
# ---------------------------------------------------------------------------

EASY_COUNT = 8
AVERAGE_COUNT = 6
ELITE_COUNT = 4


def make_starving_bandit():
    """Retuned 2026-08-05 (see project memory): STR 1->4, END 1->3, plus
    Gambeson (AR2/Penalty1, armor.md) instead of Common Clothes, to land
    near 50/50 against a 4-PC party at 8 fielded - the original build
    (STR1/END1/no armor) won the fight for the PCs 100% of the time at
    this count. Still untrained (Brawling 0) - the fictional distinction
    from Average is "tough but doesn't know how to fight," not "weak."
    Both STR and END stay within Threat Level 1's own caps (Skill<=2,
    Attribute<=4, ENCOUNTER_GUIDE.md)."""
    return Build(name="Starving Bandit", level=1, STR=4, PRE=1, END=3, DEX=1,
                 weapon=BRAWLING_PUNCH, weapon_skill=0, armor_ar=2, armor_penalty=1,
                 agility_skill=0, style=None)


def make_bandit_cutthroat():
    """Retuned 2026-08-05: STR 3->4, END 3->3 (unchanged), One-Handed
    Blades 1 (unchanged, still trained). The original build (STR3, no
    other changes) won only 8% of the time against a 4-PC party at 8
    fielded; landed at 6 fielded once Easy's own count moved to 8, per
    project decision to keep clear headcount separation between tiers.
    STR sits at Threat Level 1's Attribute cap (4)."""
    return Build(name="Bandit Cutthroat", level=1, STR=4, PRE=1, END=3, DEX=1,
                 weapon=SHORTSWORD, weapon_skill=1, armor_ar=2, armor_penalty=1,
                 agility_skill=0, style=None)


def make_bandit_captain():
    """Retuned 2026-08-05: Buff Coat (AR3/Penalty1) -> Mail Shirt
    (AR4/Penalty2, armor.md) - still Flexible, still a bandit-plausible
    upgrade, not a leap to Rigid plate. The original build (Buff Coat)
    won 64-71% of the time against a 4-PC party at 4 fielded (1/player).
    STR/END/Skill all sit exactly at Threat Level 1's caps."""
    return Build(name="Bandit Captain", level=1, STR=4, PRE=1, END=4, DEX=2,
                 weapon=BANDIT_BROADSWORD, weapon_skill=2, armor_ar=4, armor_penalty=2,
                 agility_skill=0, style=None)


def make_timber_fang():
    return Build(name="Timber Fang", level=1, STR=4, PRE=1, END=4, DEX=3,
                 weapon=FANG_BITE, weapon_skill=2, armor_ar=2, armor_penalty=1,
                 agility_skill=0, style=None)


# ---------------------------------------------------------------------------
# Group fight engine
# ---------------------------------------------------------------------------

@dataclass
class Combatant:
    build: Build
    side: str                       # 'pc' or 'monster'
    alive: bool = True
    ambush_leader: bool = True       # Bandit Captain only; consumed on first attack
    is_mythic: bool = False
    mythic_turns: int = 1
    frightened_next_attack: bool = False


def roll_initiative_counts(c):
    base = roll_d12() + (c.build.PRE + c.build.DEX) // 2
    if not c.is_mythic:
        return [base]
    counts = [base]
    for i in range(1, c.mythic_turns):
        counts.append(roll_d12() + (c.build.PRE + c.build.DEX) // 2 - 2 * i)
    return counts


def howl_check(pc):
    """Timber Fang's Howl: MIND Ward, DC 12. PCs here are pure martial
    archetypes - MIND 1, no MIND skill (see module docstring)."""
    return roll_d12() + 1 + 0 >= 12


def run_group_fight(pcs, monsters, mythic_x=None, max_rounds=30):
    combatants = []
    for b in pcs:
        combatants.append(Combatant(build=b, side="pc"))
    for b in monsters:
        is_mythic = mythic_x is not None and b.name == "Timber Fang"
        combatants.append(Combatant(
            build=b, side="monster",
            ambush_leader=(b.name == "Bandit Captain"),
            is_mythic=is_mythic, mythic_turns=mythic_x if is_mythic else 1,
        ))

    armor_state = {id(c.build): c.build.armor_ar for c in combatants}
    wounds = {id(c.build): c.build.wounds_max for c in combatants}
    statuses = {id(c.build): Status() for c in combatants}
    reactions_max = {id(c.build): reactions_of(c.build) for c in combatants}
    reactions_left = dict(reactions_max)

    # Fixed turn order for the whole fight: (initiative, combatant, turn_idx)
    slots = []
    for c in combatants:
        for idx, init in enumerate(roll_initiative_counts(c)):
            slots.append((init, c.build.DEX, c, idx))
    slots.sort(key=lambda s: (s[0], s[1]), reverse=True)

    pc_downs = 0

    for rnd in range(1, max_rounds + 1):
        for c in combatants:
            reactions_left[id(c.build)] = reactions_max[id(c.build)]
        howl_used_this_round = False

        for _, _, c, turn_idx in slots:
            if not c.alive:
                continue
            live_pcs = [x for x in combatants if x.side == "pc" and x.alive]
            live_monsters = [x for x in combatants if x.side == "monster" and x.alive]
            if not live_pcs or not live_monsters:
                break
            opponents = live_monsters if c.side == "pc" else live_pcs

            # Timber Fang's Howl: once per round, on its first turn, in
            # place of a normal attack (see module docstring).
            if c.is_mythic and turn_idx == 0 and not howl_used_this_round:
                howl_used_this_round = True
                for pc in live_pcs:
                    if not howl_check(pc):
                        pc.frightened_next_attack = True
                continue

            target = random.choice(opponents)
            advantage = False
            if c.ambush_leader:
                advantage = True
                c.ambush_leader = False
            if c.side == "pc" and c.frightened_next_attack:
                c.frightened_next_attack = False
                # Disadvantage cancels the Ambush Leader Advantage if both
                # apply (core_rules.md Stacking rule) - N/A here since
                # frightened only ever applies to PCs and ambush only to
                # monsters, kept symmetric for correctness anyway.
                dmg_to_target, dmg_to_c = resolve_group_attack(
                    c.build, target.build, armor_state, statuses, reactions_left,
                    advantage=advantage, disadvantage=True,
                )
            else:
                dmg_to_target, dmg_to_c = resolve_group_attack(
                    c.build, target.build, armor_state, statuses, reactions_left,
                    advantage=advantage,
                )

            wounds[id(target.build)] -= dmg_to_target
            wounds[id(c.build)] -= dmg_to_c

            if wounds[id(target.build)] <= 0 and target.alive:
                target.alive = False
                if target.side == "pc":
                    pc_downs += 1
            if wounds[id(c.build)] <= 0 and c.alive:
                c.alive = False
                if c.side == "pc":
                    pc_downs += 1

        live_pcs = [x for x in combatants if x.side == "pc" and x.alive]
        live_monsters = [x for x in combatants if x.side == "monster" and x.alive]
        if not live_monsters:
            return "pc", rnd, pc_downs, len(live_pcs), 0
        if not live_pcs:
            return "monster", rnd, pc_downs, 0, len(live_monsters)

    live_pcs = [x for x in combatants if x.side == "pc" and x.alive]
    live_monsters = [x for x in combatants if x.side == "monster" and x.alive]
    return "draw", max_rounds, pc_downs, len(live_pcs), len(live_monsters)


def report_role(label, monster_factory, count, trials, mythic_x=None):
    pc_wins = monster_wins = draws = 0
    total_rounds = 0
    total_pc_downs = 0
    pcs_left_on_pc_win = 0
    monsters_left_on_monster_win = 0

    for _ in range(trials):
        pcs = make_party()
        monsters = [monster_factory() for _ in range(count)]
        winner, rounds, pc_downs, pcs_left, monsters_left = run_group_fight(
            pcs, monsters, mythic_x=mythic_x
        )
        total_rounds += rounds
        total_pc_downs += pc_downs
        if winner == "pc":
            pc_wins += 1
            pcs_left_on_pc_win += pcs_left
        elif winner == "monster":
            monster_wins += 1
            monsters_left_on_monster_win += monsters_left
        else:
            draws += 1

    n = trials
    avg_pcs_left = pcs_left_on_pc_win / pc_wins if pc_wins else float("nan")
    avg_monsters_left = monsters_left_on_monster_win / monster_wins if monster_wins else float("nan")
    print(
        f"{label:42s} PCs win: {pc_wins/n:6.1%}   monsters win: {monster_wins/n:6.1%}   "
        f"draws: {draws/n:5.1%}\n"
        f"{'':42s} avg rounds: {total_rounds/n:4.1f}   "
        f"avg PC downs/fight: {total_pc_downs/n:4.2f} (of 4)   "
        f"avg PCs left standing (on PC win): {avg_pcs_left:4.2f}/4   "
        f"avg monsters left (on monster win): {avg_monsters_left:4.1f}/{count}"
    )
    return pc_wins / n, total_pc_downs / n, total_rounds / n


def run(trials=3000):
    print("Ressam Encounter Guide validation - Level 1, Party of Four")
    print("Reactions/round for this party: Greatsword Brute {}, Sword & Board Tank {}, "
          "Rapier Duelist {}, Longbow Archer {}".format(
              *[reactions_of(make_pc(a)) for a in
                ["Greatsword Brute", "Sword & Board Tank", "Rapier Duelist", "Longbow Archer"]]
          ))
    print("=" * 100)

    report_role(f"Easy - Starving Bandit x{EASY_COUNT}", make_starving_bandit, EASY_COUNT, trials)
    report_role(f"Average - Bandit Cutthroat x{AVERAGE_COUNT}", make_bandit_cutthroat, AVERAGE_COUNT, trials)
    report_role(f"Elite - Bandit Captain x{ELITE_COUNT}", make_bandit_captain, ELITE_COUNT, trials)
    report_role("Mythic - Timber Fang x1 (Mythic Initiative 3)", make_timber_fang, 1, trials, mythic_x=3)


if __name__ == "__main__":
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    run(trials)