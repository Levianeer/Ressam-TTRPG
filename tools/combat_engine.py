#!/usr/bin/env python3
"""
Ressam combat-resolution engine, built against the Oppose/Effect/Press system
(core/combat/maneuvers.md, core/combat/combat.md, core/equipment/weapons.md,
core/equipment/armor.md, as those files read on 2026-08-09 - the rework that
replaced the old three-roll Parry/Block/Dodge Maneuver system). Standalone -
no imports from any of the deleted balance_sim.py/encounter_sim.py/
bestiary_sim.py/danger_estimate.py/chain_sim.py/rest_pressure_sim.py.

This is a shared engine, not a report generator - tools/creature_rating.py and
tools/encounter_rating.py both import it and add their own Monte Carlo/tier
logic on top. `run_fight()` handles both a 1-on-1 duel and an N-vs-M group
fight identically (a duel is just N=1/M=1).

Modeling choices, made explicit up front rather than buried:

  - **Dynamic Oppose funding, not a fixed per-Build "Style."** maneuvers.md's
    Oppose table says a defender picks "whichever fits what you're defending
    with when you react" - so `best_oppose()` re-evaluates the Weapon
    Skill/STR Ward/DEX Ward options fresh on every single defended attack
    (legality, Measure mismatch, crit-bypass) and always picks the best
    legal option. This is a more faithful read of the actual rule than a
    fixed-Style model would be. Block and Evasion are no longer trained
    Skills (see core/character/attributes_and_skills.md's 2026 rework) - the
    STR/DEX Ward options are flat Attribute rolls now, no rank field on
    `Build` gates them beyond having the right equipment.
  - **Measure is stateless across a fight.** The real rule tracks one shared
    measure per *pair* of engaged combatants, moved by the Shift Effect or
    the Shift Measure Minor Action. A random-retarget group fight (no
    battlemap, no stable pairing - same simplification the old group sims
    already made) has no meaningful persistent pairing to track a measure
    for. Every single exchange here instead computes its own measure fresh,
    as "the longer of the two weapons involved" (the rule's own opening
    default: "An exchange begins at the longer weapon's Measure Band"),
    which still makes dagger-vs-pike mismatches bite, just without
    Shift's carry-over. Consequence: the fixed Effect policy below never
    picks Shift (it would do nothing under this model) and substitutes
    Control/Recover instead - see EFFECT POLICY.
  - **Effect selection is a fixed, documented policy, not optimized play.**
    On Dominant (2 picks): Control+Strike when Strike is legal at the
    current measure, else Control+Recover. On Stopped (1 pick): Strike when
    legal, else Recover. This is the same "always take the aggressive
    default" convention balance_sim.py used for its old Riposte-first
    policy - not a claim about optimal play.
  - **Control is tracked as one global flag per Build, not per-attacker
    pair.** The real rule is "disadvantage on THEIR next roll against YOU
    specifically." Modeling a full attacker-defender Control matrix in an
    N-vs-M random-retarget fight is a lot of state for a rare edge case
    (two different attackers both landing Control on the same target in the
    same round); a single flag - consumed by whichever roll that Build makes
    next, attack or Oppose - is the practical approximation.
  - **Control+Strike's Disadvantage lands on the target's attempt to Oppose
    that Strike**, not on the Strike's own attack roll. maneuvers.md's own
    worked example (Toma vs. the bandit) is genuinely ambiguous on this
    point taken as a single sentence, but the very next sentence - "the
    bandit still has a Reaction... spends it to Oppose Toma's Strike" -
    only makes narrative sense if Control's Disadvantage is what's waiting
    for him there. That's the reading this engine implements.
  - **Recover only regains a spent Reaction.** Its other option (disengage
    safely, ending the current measure engagement) is positional - the same
    "no battlemap" cut the old tools made for Push Back/Stagger/Reposition.
  - **Press's recursion is naturally bounded by the Reaction pool itself**,
    not an artificial cap - every re-Oppose and every Strike-triggers-a-
    nested-exchange consumes a Reaction from a pool that refreshes at most
    to 3/round, so a chain terminates on its own once both sides run dry.
    A small `_MAX_EXCHANGE_DEPTH` guard exists purely as a defensive
    backstop against a logic bug, not as a documented rule simplification.
  - **A defender always Opposes when legal and a Reaction remains** - no
    modeling of a defender strategically holding a Reaction in reserve.
  - Out of scope, same cuts the old tools documented: Reactive Casting and
    all spellcasting, AoE attacks, Trauma, the Dying/Death Clock/
    Stabilization track (0 Wounds = removed from the fight for outcome
    purposes), ranged approach/kiting distance (every fight here is treated
    as already engaged, like the old group sims - only balance_sim.py's
    retired 1v1-only kiting scenario modeled that, and it's not being
    ported), Seek the Seam and other Feats that alter the resolution math
    itself (Feats only show up here via `max_wounds`).

Usage as a library:
    from combat_engine import Build, Weapon, Shield, run_fight, BASELINE_PC

Usage as a script: smoke-tests BASELINE_PC against itself.
    python3 tools/combat_engine.py
"""

import random
from dataclasses import dataclass, field

D12 = 12
_MAX_EXCHANGE_DEPTH = 20  # defensive backstop only - see module docstring

DOMINANT, STOPPED, MINIMIZED, FAILED = "dominant", "stopped", "minimized", "failed"

BAND_RANK = {"grip": 0, "near": 1, "far": 2}


def roll_d12(disadvantage=False):
    a, b = random.randint(1, D12), random.randint(1, D12)
    return min(a, b) if disadvantage else a


def roll_dice_string(spec):
    bonus = 0
    if "+" in spec:
        spec, b = spec.split("+")
        bonus = int(b)
    n, d = spec.lower().split("d")
    return sum(random.randint(1, int(d)) for _ in range(int(n))) + bonus


def wounds_from_damage(after_ar, STR):
    """STR-keyed Wound Threshold bands (wounds_and_survival.md)."""
    if after_ar <= 0:
        return 0
    if after_ar <= 6 + STR:
        return 1
    if after_ar <= 12 + STR:
        return 2
    return 3


def reactions_of(build):
    """combat.md's Action Economy table."""
    if build.DEX >= 5:
        return 3
    if build.DEX >= 3:
        return 2
    return 1


def initiative(build):
    return roll_d12() + build.DEX


# ---------------------------------------------------------------------------
# Weapons / Shields
# ---------------------------------------------------------------------------

@dataclass
class Weapon:
    name: str
    dice: str          # weapon's own damage only - Attribute is added at resolution time
    attribute: str      # 'STR' or 'DEX' - which Attribute funds this weapon's Attack/damage
    crit_floor: int = 12   # natural roll that starts a crit threat; 12 = no expansion
    band: str = "grip"      # 'grip' / 'near' / 'far' - Measure Bands table (weapons.md)
    ranged: bool = False
    two_handed: bool = False

    def roll_damage(self):
        return roll_dice_string(self.dice)


@dataclass
class Shield:
    name: str
    guard: int
    grip_exempt: bool = False  # Buckler only - keeps full Guard at Grip measure


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

@dataclass
class Build:
    name: str
    STR: int = 0  # absorbs the old Endurance
    DEX: int = 0  # absorbs the old Precision
    MIND: int = 0
    CHA: int = 0
    ARC: int = 0
    FAI: int = 0
    weapon: Weapon = None
    weapon_skill: int = 0  # rank in whichever of the 5 STR/2 DEX weapon Skills matches `weapon`
    shield: Shield = None
    armor_ar: int = 0
    armor_penalty: int = 0
    max_wounds: int = 3
    mythic_turns: int = 1  # 1 = normal creature; >1 = Mythic Initiative(X)

    def attribute_value(self):
        return self.STR if self.weapon.attribute == "STR" else self.DEX

    @property
    def evasion(self):
        return 5 + self.DEX - self.armor_penalty

    def attack_roll(self, disadvantage=False):
        natural = roll_d12(disadvantage)
        return natural, natural + self.weapon_skill

    def is_crit(self, natural):
        return natural >= self.weapon.crit_floor


def band_mismatch(mover_band, other_band):
    """0 = matches, 1 = one band off (Disadvantage), 2 = two off (illegal)."""
    return abs(BAND_RANK[mover_band] - BAND_RANK[other_band])


# ---------------------------------------------------------------------------
# Fight state (per-fight, mutable, keyed by id(build))
# ---------------------------------------------------------------------------

@dataclass
class _State:
    wounds: dict = field(default_factory=dict)
    armor: dict = field(default_factory=dict)
    guard: dict = field(default_factory=dict)
    reactions_max: dict = field(default_factory=dict)
    reactions_left: dict = field(default_factory=dict)
    controlled: dict = field(default_factory=dict)  # id -> bool, see module docstring

    def take_control(self, bid):
        flag = self.controlled.get(bid, False)
        self.controlled[bid] = False
        return flag

    def set_control(self, bid):
        self.controlled[bid] = True


def _init_state(builds):
    st = _State()
    for b in builds:
        st.wounds[id(b)] = b.max_wounds
        st.armor[id(b)] = b.armor_ar
        st.guard[id(b)] = b.shield.guard if b.shield else 0
        st.reactions_max[id(b)] = reactions_of(b)
        st.reactions_left[id(b)] = st.reactions_max[id(b)]
        st.controlled[id(b)] = False
    return st


# ---------------------------------------------------------------------------
# Oppose funding
# ---------------------------------------------------------------------------

def _legal_oppose_options(defender, attacker, crit):
    """Returns a list of (funding_name, bonus, disadvantage) tuples - every
    Oppose option `defender` could legally fund against this attack right
    now, per the Oppose table (maneuvers.md): a trained Weapon Skill, or a
    flat, untrained STR Ward / DEX Ward (Block and Evasion no longer exist
    as Skills - see maneuvers.md's Funding table)."""
    options = []

    if not crit and not attacker.weapon.ranged and defender.weapon_skill >= 1:
        mm = band_mismatch(defender.weapon.band, attacker.weapon.band)
        if mm < 2:
            options.append(("weapon", defender.weapon_skill, mm == 1))

    has_shield = defender.shield is not None
    has_two_handed_block = defender.weapon.two_handed
    if not crit and (has_shield or has_two_handed_block):
        if not attacker.weapon.ranged or has_shield:
            options.append(("str_ward", defender.STR, False))

    options.append(("dex_ward", defender.DEX - defender.armor_penalty, False))

    return options


def _best_oppose(defender, attacker, crit):
    options = _legal_oppose_options(defender, attacker, crit)
    if not options:
        return None
    # Expected-value heuristic to pick between options when Disadvantage is
    # in play (E[d12]=6.5, E[min of two d12]~=4.96) - Disadvantage isn't a
    # flat penalty, so comparing raw bonuses alone would pick badly.
    def score(opt):
        _, bonus, disadv = opt
        return bonus + (4.96 if disadv else 6.5)
    return max(options, key=score)


def _oppose_roll(funding, extra_disadvantage=False):
    _name, bonus, mismatch_disadv = funding
    natural = roll_d12(mismatch_disadv or extra_disadvantage)
    return natural + bonus


def _effective_guard(defender, st, current_measure_is_grip):
    if defender.shield is None:
        return 0
    if st.controlled.get(id(defender)):
        return 0  # Control zeroes Guard against them until cleared
    g = st.guard[id(defender)]
    if current_measure_is_grip and not defender.shield.grip_exempt:
        g = max(0, g - 2)
    return g


def _tier_for(margin):
    if margin >= 3:
        return DOMINANT
    if margin >= 0:
        return STOPPED
    if margin >= -2:
        return MINIMIZED
    return FAILED


def _pick_effects(tier, strike_legal):
    """Fixed policy - see EFFECT POLICY in the module docstring."""
    if tier == DOMINANT:
        return ["control", "strike"] if strike_legal else ["control", "recover"]
    return ["strike"] if strike_legal else ["recover"]


# ---------------------------------------------------------------------------
# Core exchange resolution
# ---------------------------------------------------------------------------

def _apply_raw_hit(attacker, defender, atk_total, natural, crit, st, halved=False):
    raw = attacker.weapon.roll_damage() + attacker.attribute_value()
    if crit:
        raw = max(raw, attacker.weapon.roll_damage() + attacker.attribute_value())
    if halved:
        raw //= 2
    current_ar = st.armor[id(defender)]
    after_ar = max(0, raw - current_ar)
    st.wounds[id(defender)] -= wounds_from_damage(after_ar, defender.STR)
    st.armor[id(defender)] = max(0, current_ar - 1)  # every connecting hit degrades armor 1


def _resolve_hit(attacker, atk_total, natural, defender, st, target_oppose_disadvantage=False, depth=0):
    """Attacker's roll already beat defender's Evasion. Handles Oppose,
    Margin, Shield Guard, Effects (including a Strike's own nested
    sub-exchange), and Press - recursively, bounded by the shared Reaction
    pool (see module docstring)."""
    if depth > _MAX_EXCHANGE_DEPTH:
        _apply_raw_hit(attacker, defender, atk_total, natural, attacker.is_crit(natural), st)
        return

    crit = attacker.is_crit(natural)
    funding = None
    if st.reactions_left[id(defender)] > 0:
        funding = _best_oppose(defender, attacker, crit)

    if funding is None:
        _apply_raw_hit(attacker, defender, atk_total, natural, crit, st)
        return

    st.reactions_left[id(defender)] -= 1
    control_disadv = st.take_control(id(defender))
    roll = _oppose_roll(funding, target_oppose_disadvantage or control_disadv)
    margin = roll - atk_total
    _apply_margin(attacker, defender, atk_total, natural, crit, margin, funding, st, depth)


def _apply_margin(attacker, defender, atk_total, natural, crit, margin, funding, st, depth):
    current_measure = max(BAND_RANK.get(defender.weapon.band, 0), BAND_RANK.get(attacker.weapon.band, 0))
    is_grip = current_measure == BAND_RANK["grip"]
    tier = _tier_for(margin)

    if tier in (MINIMIZED, FAILED):
        guard = _effective_guard(defender, st, is_grip)
        if guard > 0:
            margin += guard
            tier = _tier_for(margin)
            st.guard[id(defender)] = max(0, st.guard[id(defender)] - 1)

        if tier in (MINIMIZED, FAILED) and st.reactions_left[id(defender)] > 0:
            # Press: defender spends another Reaction to re-Oppose instead
            # of accepting this losing result.
            st.reactions_left[id(defender)] -= 1
            control_disadv = st.take_control(id(defender))
            roll = _oppose_roll(funding, control_disadv)
            margin = roll - atk_total
            _apply_margin(attacker, defender, atk_total, natural, crit, margin, funding, st, depth + 1)
            return

    if tier in (DOMINANT, STOPPED):
        strike_legal = band_mismatch(defender.weapon.band, attacker.weapon.band) < 2 or attacker.weapon.ranged
        chosen = _pick_effects(tier, strike_legal)
        if "control" in chosen:
            st.set_control(id(attacker))
        if "recover" in chosen:
            st.reactions_left[id(defender)] = min(st.reactions_max[id(defender)], st.reactions_left[id(defender)] + 1)
        if "strike" in chosen:
            # A ranged attacker has no Measure Band of its own to mismatch
            # against - Bands are a melee concept (weapons.md) - so a Strike
            # back at one is never Measure-penalized, per the "Strike vs. a
            # ranged original attacker treated as always-legal" simplification
            # in the module docstring.
            strike_disadv = (not attacker.weapon.ranged
                              and band_mismatch(defender.weapon.band, attacker.weapon.band) == 1)
            natural2, atk_total2 = defender.attack_roll(disadvantage=strike_disadv)
            if atk_total2 >= attacker.evasion:
                # "control" paired with "strike": Disadvantage lands on the
                # target's attempt to Oppose THIS strike - see module docstring.
                target_disadv = "control" in chosen
                _resolve_hit(defender, atk_total2, natural2, attacker, st,
                             target_oppose_disadvantage=target_disadv, depth=depth + 1)
        return

    # Still Minimized or Failed, and nothing left to Press with: hit lands.
    _apply_raw_hit(attacker, defender, atk_total, natural, crit, st, halved=(tier == MINIMIZED))


def resolve_attack(attacker, defender, st, disadvantage=False):
    """Top-level entry point: attacker's Major Action attack against
    defender. Mutates `st` in place; returns nothing."""
    control_disadv = st.take_control(id(attacker))
    natural, atk_total = attacker.attack_roll(disadvantage=disadvantage or control_disadv)
    if atk_total < defender.evasion:
        return  # clean miss, no Reaction spent
    _resolve_hit(attacker, atk_total, natural, defender, st)


# ---------------------------------------------------------------------------
# Group fight (1v1 is just len(side_a)==len(side_b)==1)
# ---------------------------------------------------------------------------

@dataclass
class _Combatant:
    build: Build
    side: str
    alive: bool = True


def _initiative_slots(combatants):
    slots = []
    for c in combatants:
        base = initiative(c.build)
        slots.append((base, c.build.DEX, c, 0))
        for i in range(1, c.build.mythic_turns):
            slots.append((base - 2 * i, c.build.DEX, c, i))
    slots.sort(key=lambda s: (s[0], s[1]), reverse=True)
    return slots


def run_fight(side_a, side_b, max_rounds=30):
    """side_a/side_b: lists of Build. Returns ('a'|'b'|'draw', rounds_elapsed,
    a_losses, b_losses)."""
    combatants = [_Combatant(b, "a") for b in side_a] + [_Combatant(b, "b") for b in side_b]
    st = _init_state([c.build for c in combatants])
    slots = _initiative_slots(combatants)

    for rnd in range(1, max_rounds + 1):
        for c in combatants:
            st.reactions_left[id(c.build)] = st.reactions_max[id(c.build)]

        for _, _, c, turn_idx in slots:
            if not c.alive:
                continue
            if c.build.mythic_turns > 1:
                st.reactions_left[id(c.build)] = st.reactions_max[id(c.build)]

            live_a = [x for x in combatants if x.side == "a" and x.alive]
            live_b = [x for x in combatants if x.side == "b" and x.alive]
            if not live_a or not live_b:
                break

            opponents = live_b if c.side == "a" else live_a
            target = random.choice(opponents)
            resolve_attack(c.build, target.build, st)

            for x in combatants:
                if x.alive and st.wounds[id(x.build)] <= 0:
                    x.alive = False

        live_a = [x for x in combatants if x.side == "a" and x.alive]
        live_b = [x for x in combatants if x.side == "b" and x.alive]
        a_losses = len(side_a) - len(live_a)
        b_losses = len(side_b) - len(live_b)
        if not live_b:
            return "a", rnd, a_losses, b_losses
        if not live_a:
            return "b", rnd, a_losses, b_losses

    live_a = [x for x in combatants if x.side == "a" and x.alive]
    live_b = [x for x in combatants if x.side == "b" and x.alive]
    return "draw", max_rounds, len(side_a) - len(live_a), len(side_b) - len(live_b)


# ---------------------------------------------------------------------------
# Shared weapon/shield/armor reference data (weapons.md / armor.md), for
# tools/creature_rating.py, tools/encounter_rating.py, and BASELINE_PC below.
# ---------------------------------------------------------------------------

WEAPONS = {
    "Dagger": Weapon("Dagger", "1d4", "DEX", crit_floor=9, band="grip"),
    "Knife": Weapon("Knife", "1d4", "DEX", crit_floor=10, band="grip"),
    "Shortsword": Weapon("Shortsword", "1d6+1", "STR", crit_floor=10, band="grip"),
    "Scimitar": Weapon("Scimitar", "1d6", "DEX", crit_floor=10, band="grip"),
    "Broadsword": Weapon("Broadsword", "1d10", "STR", crit_floor=12, band="grip"),
    "Mace": Weapon("Mace", "1d8", "STR", crit_floor=12, band="grip"),
    "Club": Weapon("Club", "1d6", "STR", crit_floor=12, band="grip"),
    "Longsword": Weapon("Longsword", "1d6+2", "STR", crit_floor=11, band="near"),
    "Greatsword": Weapon("Greatsword", "1d12", "STR", crit_floor=11, band="near", two_handed=True),
    "Rapier": Weapon("Rapier", "1d8", "DEX", crit_floor=10, band="near"),
    "Spear": Weapon("Spear", "1d6", "STR", crit_floor=12, band="near"),
    "Quarterstaff": Weapon("Quarterstaff", "1d6", "STR", crit_floor=12, band="near"),
    "Pike": Weapon("Pike", "1d8", "STR", crit_floor=12, band="far", two_handed=True),
    "Halberd": Weapon("Halberd", "1d10", "STR", crit_floor=12, band="far", two_handed=True),
    "Glaive": Weapon("Glaive", "2d4", "STR", crit_floor=11, band="far", two_handed=True),
    "Shortbow": Weapon("Shortbow", "1d6", "DEX", crit_floor=10, ranged=True, two_handed=True),
    "Longbow": Weapon("Longbow", "1d8", "DEX", crit_floor=11, ranged=True, two_handed=True),
    "Punch": Weapon("Punch", "1d4", "STR", crit_floor=12, band="grip"),
    "Bite": Weapon("Bite", "1d8", "STR", crit_floor=12, band="grip"),
}

SHIELDS = {
    "Buckler": Shield("Buckler", 1, grip_exempt=True),
    "Heater Shield": Shield("Heater Shield", 2),
    "Pavise": Shield("Pavise", 3),
}

# (AR, Penalty) - armor.md's Armor Table.
ARMORS = {
    "None": (0, 0),
    "Gambeson": (2, 1),
    "Buff Coat": (3, 1),
    "Mail Shirt": (4, 2),
    "Chain Mail": (5, 2),
    "Brigandine": (6, 3),
    "Breastplate": (6, 6),
    "Half-Plate": (7, 7),
    "Full Plate": (8, 8),
}

# ---------------------------------------------------------------------------
# BASELINE_PC - the one fixed reference build every rating is made against.
# Level 1, roughly legal against power_score.LEVEL_TABLE[1]'s point budget
# (not fit to the exact cap - a plain measuring stick, not a built-out
# character): STR 3, DEX 2, MIND 1, CHA 1 - STR/DEX already fold in the old
# END 3/PRE 2 (floor-averaged per the 6-Attribute rework, see
# core/character/attributes_and_skills.md). Broadsword + Cleaving Blades 3,
# Mail Shirt + Heater Shield (STR Ward now covers what Block Skill 2 used to
# fund - no separate rank needed). No Feats.
# ---------------------------------------------------------------------------

def make_baseline_pc():
    return Build(
        name="Baseline PC", STR=3, DEX=2, MIND=1, CHA=1,
        weapon=WEAPONS["Broadsword"], weapon_skill=3,
        shield=SHIELDS["Heater Shield"],
        armor_ar=ARMORS["Mail Shirt"][0], armor_penalty=ARMORS["Mail Shirt"][1],
        max_wounds=3,
    )


BASELINE_PC = make_baseline_pc()


def main():
    wins = losses = draws = 0
    total_rounds = 0
    trials = 2000
    for _ in range(trials):
        winner, rounds, _, _ = run_fight([make_baseline_pc()], [make_baseline_pc()])
        total_rounds += rounds
        if winner == "a":
            wins += 1
        elif winner == "b":
            losses += 1
        else:
            draws += 1
    print(f"Baseline PC vs. itself, {trials} trials (sanity check - should land near 50/50):")
    print(f"  a: {wins/trials:.1%}  b: {losses/trials:.1%}  draws: {draws/trials:.1%}  "
          f"avg rounds: {total_rounds/trials:.1f}")


if __name__ == "__main__":
    main()
