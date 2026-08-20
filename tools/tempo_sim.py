#!/usr/bin/env python3
"""Monte Carlo simulator for the Tempo Pool combat system (exchange_draft.md, 2026-08-23).

Replaces exchange_sim.py and exchange_solver.py, which model Bands, declarations
and the Cycle - none of which exist any more.

Built to answer one question - *is emptying your Tempo Pool on offence dominant?*
(no: it loses 81-19 to holding a die back) - and then used for the balance work in
log items 33-39. It now reports four things that matter:

  * STR/DEX balance across the Attribute field   (target: flat; see the WARNING below)
  * average fight length            (target: ~3 rounds at party scale; currently 2.7)
  * attacks declared per turn                     (currently 2.8, p90 of 4)
  * stalled matchups                              (target: 0)
  * whether dumping the pool beats holding it     (target: ~50%)

READ THIS BEFORE TRUSTING A NUMBER:
  * A stall is a BROKEN STATE, not a draw. Averaging stalls in as 0.5 hid a real
    fault for two whole items. They are counted separately now - keep it that way.
  * Spread carries about +/-2 points of seed noise. Under 5 points is nothing.
  * A policy table that pins every build at one hold cannot find a dominant
    policy. Reporting "dumping vs holding is ~51%" was true and measured the
    wrong end of the curve; the BEST-HOLD sweep is what finds the turtle.
  * THE SAME TRAP CAUGHT THE STR/DEX TABLE, 2026-08-23. Pinned at hold 1 it reads
    a spread of 4.8 and looks solved. Let BOTH sides pick their best hold and the
    real figure is 12.7, DEX ahead - because extra dice buy offence AND defence
    while die size only buys quality. The printed field table below is the pinned
    one and is NOT the balance number. Solve both sides before believing it.
  * A duel cannot price a rule that limits DEFENDING, because the worth of a
    held die scales with how many people are attacking you. Use gang_fight().
  * Damage adds STR for every MELEE weapon as of 2026-08-23 - the Fencing Blades
    carve-out was deleted. Missiles still add DEX, and nothing here models them.
    Item 39's bug was hardcoding STR while the draft said otherwise; the draft now
    says STR, so cross-check before assuming this line is stale again.

Model scope: no terrain, no movement, no Feats, no casters, no off-hand tools,
no Conditions. Both fighters are Adjacent with weapons that act there at 0,
for the whole fight. Reach is deliberately excluded - it is a separate question and
mixing it in would confound this one.

Run bare to reproduce the report:  python3 tools/tempo_sim.py
"""

import random
import itertools
from dataclasses import dataclass, field

# --- Two switches, both added 2026-08-21 after the first run found that the
# --- STR ladder, not the pool policy, is what is actually broken. See the log.
LADDERS = {
    "draft":      {1: 4, 2: 6, 3: 8, 4: 10, 5: 12},   # ADOPTED - one rung per STR point.
                                                      # Item 40 raised the floor to 1d6;
                                                      # item 47 reverted it, because the
                                                      # problem it fixed had already been
                                                      # fixed by items 42-46 and the raised
                                                      # floor was handing the largest pool
                                                      # a free upgrade (field spread 21.5
                                                      # against 5.4).
    "floor_1d6":  {1: 6, 2: 6, 3: 8, 4: 10, 5: 12},   # item 40's floor, for reproducing
    "up1":        {1: 6, 2: 8, 3: 10, 4: 12, 5: 12},  # dead rung at the TOP instead
    "mid":        {1: 6, 2: 8, 3: 8, 4: 10, 5: 12},   # dead rung in the MIDDLE instead
    "compressed": {1: 6, 2: 8, 3: 8, 4: 10, 5: 10},   # half the spread
}
LADDER = "draft"
ATTACKER_WINS_TIES = False   # draft says ties go to the defender

TEMPO_DIE = LADDERS[LADDER]

# wounds_and_survival.md - damage after AR converts to Wounds.
#
# ADOPTED 2026-08-21 (log item 45, exchange_draft.md "Armour and Wounds"): the
# bands are NO LONGER KEYED TO STR. 1 Wound on 1-7, 2 on 8-14, 3 on 15+, for
# everybody - the row the live file already prints for STR 1, applied to all.
# The STR keying had to go because AR could not matter while it was there: a hit
# cut from 8 damage to 2 was still exactly 1 Wound, so AR reduced damage and the
# table threw the reduction away (log items 35-36, 42).
#
# Set FLAT_WOUND_BANDS = False to restore the OLD STR-keyed table. The flat one
# is what shipped in the 2026-08-23 merge, so True is now the published rule.
FLAT_WOUND_BANDS = True
FLAT_BANDS = (9, 18)            # 1 Wound to 9, 2 Wounds to 18, 3 beyond.
                                # WIDENED (7,14) -> (8,16) on 2026-08-22 (log item 49),
                                # then (8,16) -> (9,18) the same day (log item 52) to buy
                                # back the length that deleting Evasion cost: duel 1.59 ->
                                # 1.72 rounds, party 2.68 -> 2.78, for 0.2 points of
                                # spread. Item 49's note on the earlier step:
                                # Length and STR/DEX spread are the SAME DIAL here - the
                                # curve is about 0.15 rounds per point of spread, measured
                                # at (7,14) (8,16) (9,18) (10,20).
WOUND_BANDS = {                 # the published, STR-keyed table - superseded
    1: (7, 13),
    2: (8, 14),
    3: (9, 15),
    4: (10, 16),
    5: (11, 17),
}

OPENING_MARGIN = 5
# --- ADOPTED 2026-08-23: THERE ARE NO CRITICAL HITS. Measured firing on 0.00% of
# --- landed blows for any fighter below STR 5, and not fixable by lowering the
# --- threshold: the margin ceiling between equals is (die size - 1), and a roll
# --- high enough to clear a big margin is a roll the defender declines to answer,
# --- which pins it at UNANSWERED_MARGIN. Set CRITS = True with a CRIT_MARGIN to
# --- reproduce the pre-deletion figures.
CRITS = False
CRIT_MARGIN = 10        # inert while CRITS is False

# Instrument. PAID_DEFENCE_RATE is the fraction of attacks answered by a defence
# somebody SPENT A DIE ON, rather than by the free Dodge. It exists because a
# configuration can post an excellent build-balance figure purely by making the
# free Dodge so good that nobody ever pays - balance achieved by deleting the
# defensive half of the pool, which is the core of the design. Check it before
# believing any spread number. Healthy is roughly 25-50%; 0% is a dead system.
STATS = {"attacks": 0, "paid_defences": 0}


def paid_defence_rate():
    return STATS["paid_defences"] / max(1, STATS["attacks"])


def reset_stats():
    STATS["attacks"] = 0
    STATS["paid_defences"] = 0
# --- Dodge off the Tempo Die (log item 37). Dodge rolls its own fixed die, the
# --- same for everybody, so defence does not scale with STR. Set DODGE_DIE to
# --- None to restore the old behaviour (Dodge rolls the Tempo Die).
DODGE_DIE = 8         # fixed die for every Dodge, free or committed (ADOPTED)
DODGE_FLAT = 2        # every Dodge adds this
DODGE_COMMIT_DEX = True   # a committed Dodge also adds DEX; the free one does not
# --- CANDIDATE 2026-08-22: Dodge becomes EVASION, a static score sitting beside
# --- AR, and the committed Dodge is deleted. This is a partial revert of item 34.
# --- The defender does NOT roll unless they spend a die on a Parry or a Block.
# --- Encoded as a (die=1, bonus=E-1) pair so every comparison in the resolver
# --- works unchanged: roll(1) is always 1, so the total is always exactly E.
# --- ADOPTED 2026-08-22 (log item 52): there is NO unpaid defence at all. An
# --- attack nobody spends a die on simply lands. This deletes Evasion, which
# --- item 49 had reinstated the same day - see the log for why that is not a
# --- flip-flop: Evasion was measured stopping ~6% of the attacks it was left to
# --- answer, so what item 52 removes is a number that was not doing anything.
# --- Set UNPAID_DEFENCE = True with PASSIVE_EVASION = True to restore item 49.
UNPAID_DEFENCE = False    # False = nothing is free. True = fall back on free_defence().
UNANSWERED_MARGIN = 5     # margin credited to an unanswered attack. The draft pays an
                          # Opening (5) and never a critical. NOTE: this simulator does
                          # not model the ATTACKER'S Opening at all - only Shock and the
                          # defender's Riposte - so 0 and 5 measure identically here.
                          # The choice between them was made on fiction, not on a number,
                          # and the log says so. Do not cite a measurement for it.
PASSIVE_EVASION = True    # only consulted when UNPAID_DEFENCE is True (log item 49).
EVASION_FLAT = 0          # Evasion = EVASION_FLAT + DEX*EVASION_DEX - Armor Penalty.
                          # 0 is the swept best: every flat above it re-opens the turtle
                          # stall and skews the field toward STR.
EVASION_DEX = 1.0         # how much DEX the static score carries. 0.0 = flat for all.
COMMITTED_DODGE = False   # ADOPTED 2026-08-22: a Tempo Die buys Parry or Block only.
COMMIT_DEX_FRACTION = 1.0 # how much of DEX the committed Dodge adds. 1.0 = the draft.
                      # 0.5 (round down) is the "tax DEX instead of reverting the
                      # ladder floor" candidate of log item 47.
POOL_CAP = None       # hard ceiling on Tempo Pool size, or None. The other item-47
                      # candidate: it binds only on DEX 5, which is a DEX tax with a
                      # hard edge - see the law item 35 paid for.
RIGID_HALF_WEAR = False  # True: Rigid armour loses 1 durability every SECOND hit.
                      # Candidate replacement for the Rigid/Flexible split living in the
                      # Penalty formula, where any gap at all re-sinks plate (item 43).
GUARD_SOAK = False    # DELETED FROM THE DRAFT 2026-08-22 (log item 50), kept as a switch.
                      # A shield reducing damage by its Guard even on a LOST defence was
                      # the one clause making Block a different RULE from Parry rather
                      # than a different modifier on the same roll. Measured on the day
                      # it was deleted and worth under a point: Guard 1, 42.5 -> 42.7%;
                      # Guard 2, 54.8 -> 54.9%; Guard 3, 66.5 -> 67.3%. It fires rarely
                      # because you only pay for a defence that can change the outcome,
                      # so a PAID defence that loses is itself rare.
AP_ON_ATTACK = False  # True: Armor Penalty also subtracts from your ATTACK rolls. Under
                      # a static Evasion this is the only lever found that re-prices armour,
                      # because Penalty against one static number is nearly free (2026-08-22).
AP_ON_ALL_DEFENCES = False  # True: Armor Penalty applies to Parry and Block too, not
                      # just the Dodge. One rule instead of two, and it lets the Penalty
                      # numbers themselves be much smaller.
FREE_DODGE_AP = 1.0   # fraction of Armor Penalty charged against the FREE Dodge.
                      # 1.0 = as the draft is written. The free Dodge is the most-rolled
                      # thing in the game, so this is where most of armour's cost lands.
DURABILITY = True     # armor.md: every successful hit costs 1 durability, and current
                      # AR EQUALS current durability. Modelled from 2026-08-21 (item 42);
                      # before that AR was a constant, which is not what the file says.
                      # Set False to reproduce the older, wrong figures.
ONE_COMMIT_PER_ROUND = False  # may you buy more than one committed Dodge between your
                      # own turns? False = as the draft is written. See the BEST-HOLD
                      # sweep below: at False, "attack once, bank the rest" is the
                      # dominant strategy for every high-DEX build and turtle mirrors
                      # run 38 rounds at 91% stalls. Log item 40.
POOL_BONUS = 1        # Tempo Pool = DEX + POOL_BONUS
FREE_DODGE_MOD = 0    # only used when DODGE_DIE is None (legacy Tempo-Die Dodge)
SEQ_PENALTY = 0       # DELETED 2026-08-21 (log item 35). Kept as a switch so the
                      # finding can be reproduced: at -2 the STR/DEX spread is
                      # 55 points, at 0 it is 21. Every attack now rolls alike.


def wounds_from(damage: int, defender_str: int) -> int:
    if damage <= 0:
        return 0
    one, two = FLAT_BANDS if FLAT_WOUND_BANDS else WOUND_BANDS[defender_str]
    if damage <= one:
        return 1
    if damage <= two:
        return 2
    return 3


def roll(sides: int) -> int:
    return random.randint(1, sides)


def roll_def(sides: int, disadv: bool) -> int:
    """A defence roll. Disadvantage is roll-twice-take-lower and does not stack."""
    return min(roll(sides), roll(sides)) if disadv else roll(sides)


def ev_die(sides: int, disadv: bool) -> float:
    """Expected value of that roll. E[min of two dN] = (N+1)(2N+1)/(6N)."""
    if disadv:
        return (sides + 1) * (2 * sides + 1) / (6.0 * sides)
    return (sides + 1) / 2.0


# --------------------------------------------------------------------------
# Ranged - added 2026-08-23, modelling exchange_draft.md "There is no defense
# against a ranged attack" and its "Loading" subsection.
#
# A shot is NOT an Exchange. It cannot be Parried, it takes no Opening, and it
# causes no Shock. It is one roll against a flat Shot DC set by the situation,
# never by the target - so nothing on the defender's sheet answers an arrow and
# the only counters are positional.
#
# Rate of fire comes off the weapon, not the pool: firing empties the weapon, and
# reloading costs the Minor Action you have one of, plus the weapon's dice. Two
# shots a turn is therefore the ceiling for everybody, and what differs is price.
# --------------------------------------------------------------------------
SHOT_DC = 7               # clear, inside normal range
SHOT_DC_ADJACENT = 2      # +2, and a Two-Handed missile weapon cannot shoot at all
MAX_SHOTS_PER_TURN = 2    # one Minor Action = one reload = two shots
SHOT_CAUSES_SHOCK = False # ADOPTED 2026-08-23: Shock is melee only. True to test the
                          # alternative - a shot stripping a die as a melee blow does.


def shots_affordable(c) -> int:
    """How many shots this combatant can pay for, given the loading rules.

    Shot 1 costs 1 die from the loaded weapon. Shot 2 costs a reload (Minor Action
    + reload_cost dice) plus another 1. Capped at MAX_SHOTS_PER_TURN because there
    is only one Minor Action."""
    budget = max(0, c.pool - c.policy.hold)
    if budget < 1:
        return 0
    if MAX_SHOTS_PER_TURN < 2 or budget < 2 + c.build.reload_cost:
        return 1
    return 2


def shot_cost(n: int, reload_cost: int) -> int:
    """Dice for a sequence of n shots, reloads included."""
    return 0 if n <= 0 else n + max(0, n - 1) * reload_cost


def shoot(shooter, target, adjacent: bool = False) -> None:
    """One shot. No contest, no defence, no Opening - just the DC."""
    dc = SHOT_DC + (SHOT_DC_ADJACENT if adjacent else 0)
    total = roll(shooter.build.die) + shooter.build.skill
    margin = total - dc
    if margin < 0:
        return
    n, sides, flat = shooter.build.missile
    raw = sum(roll(sides) for _ in range(n)) + flat + shooter.build.dex
    if CRITS and margin >= CRIT_MARGIN:
        raw = max(raw, sum(roll(sides) for _ in range(n)) + flat + shooter.build.dex)
    dmg = max(0, raw - target.ar)
    if DURABILITY:
        target.hits_taken += 1
        wears = not (RIGID_HALF_WEAR and target.build.rigid and target.hits_taken % 2 == 0)
        if RIGID_ZERO_WEAR and target.build.rigid and dmg == 0:
            wears = False
        if wears:
            target.ar = max(0, target.ar - shooter.build.ar_degrade)
    if dmg:
        target.wounds -= wounds_from(dmg, target.build.str_)
    if SHOT_CAUSES_SHOCK:
        apply_shock(target)


# --------------------------------------------------------------------------
# Fighters
# --------------------------------------------------------------------------

@dataclass
class Build:
    name: str
    str_: int
    dex: int
    skill: int
    ar: int
    armor_penalty: int
    dmg_dice: tuple           # (count, sides, flat) e.g. (1, 6, 2) for 1d6 + 2
    guard: int = 0            # shield; 0 = none. Added to the Parry - and measured, it is
                              # the largest number on any gear in the chapter: no shield to
                              # Guard 3 is 30.3 -> 66.5% in a duel, a bigger swing than the
                              # whole armour ladder produces.
    max_wounds: int = 4       # Medium. Small 3 / Medium 4 / Large 5 as of 2026-08-21
    mind: int = 3             # Initiative = 5 + MIND, static (exchange_draft.md)
    rigid: bool = False       # Rigid armour. With RIGID_HALF_WEAR it sheds durability
                              # every second hit instead of every hit.
    missile: tuple = None     # (count, sides, flat) for the missile weapon, or None.
                              # Damage adds DEX - the one surviving Attribute carve-out.
    reload_cost: int = 1      # Tempo Dice a reload costs ON TOP of the Minor Action.
                              # 0 = thrown (Object Interaction instead), 1 = sling/bow,
                              # 2 = crossbow, 3 = firearm. exchange_draft.md "Loading".
    reload_major: bool = False  # MEASURED AND REJECTED for man-portable weapons
                              # 2026-08-23. A Major-Action reload fires once every two
                              # turns, which is 2.5 shots in a five-round fight against a
                              # bow's 8.5: party win 47% with an arquebus against 73% for
                              # a fourth melee PC, and 30% for a pistol. To break even at
                              # that rate a shot would need ~25 damage; 4d4+DEX is 14.
                              # KEPT ONLY FOR THE HACKBUT, which is emplaced and crew-
                              # served and which no PC is expected to carry.
    missile_2h: bool = True   # Two-Handed missile: cannot shoot while Adjacent, and
                              # leaves no hand free, so no sidearm Parry while held.
    sidearm: bool = False     # carries something that can Parry Adjacent (a dagger).
    ar_degrade: int = 1       # durability this weapon strips per landed hit. The draft:
                              # "A War Maul and every firearm cost it 2 instead of 1."
                              # Missed until 2026-08-23, which understated every firearm.
    dmg_attr: str = "str"     # Attribute added to damage. CHANGED 2026-08-23: melee is
                              # STR for EVERY weapon and every Skill, Fencing Blades
                              # included - the DEX carve-out is gone. Only MISSILE
                              # weapons take DEX. Measured, deleting the melee carve-out
                              # closed the STR/DEX maximin gap from +23.7 to +12.7, and
                              # unlike the escalating-cost candidates it left the field a
                              # gentle slope instead of a hump. Nothing here models
                              # missiles, so "dex" is unreachable in the default field.

    @property
    def die(self) -> int:
        return LADDERS[LADDER][self.str_]

    @property
    def pool_size(self) -> int:
        n = self.dex + POOL_BONUS
        return min(n, POOL_CAP) if POOL_CAP else n

    @property
    def free_dodge(self) -> int:
        """Passive Evasion was deleted 2026-08-21. The free Dodge replaces it:
        a real roll, at -2, with no cost and no requirement."""
        return self.dex - self.armor_penalty + FREE_DODGE_MOD

    def damage(self) -> int:
        n, sides, flat = self.dmg_dice
        attr = self.dex if self.dmg_attr == "dex" else self.str_
        return sum(roll(sides) for _ in range(n)) + flat + attr


@dataclass
class Policy:
    """How a fighter spends the pool.

    hold      - dice kept back on your own turn, never spent attacking.
                0 = dump everything. pool_size-1 = one attack a turn.
    atk_type  - 'measured' | 'press' | 'feint' | 'mixed'
    def_floor - stop defending when the pool drops to this. 0 = defend while able.
    def_smart - only spend a die when the attack would otherwise land. The
                attacker rolls first and the total is public, so this is legal
                play, not clairvoyance.
    """
    name: str
    hold: int
    atk_type: str = "measured"
    def_floor: int = 0
    def_smart: bool = True


@dataclass
class Combatant:
    build: Build
    policy: Policy
    wounds: int = field(init=False)
    pool: int = field(init=False)
    ar: int = field(init=False)                           # CURRENT AR = current durability
    hits_taken: int = field(default=0, init=False)        # for RIGID_HALF_WEAR
    used_commit: bool = field(default=False, init=False)  # committed Dodge taken this round
    press_debt: bool = field(default=False, init=False)   # -2 def until next turn
    off_balance: bool = field(default=False, init=False)  # -2 def until end of their turn
    cancelled: int = field(default=0, init=False)         # declared attacks a Riposte took
    shock_carry: int = field(default=0, init=False)       # Shock that landed on an empty pool
    blocked: bool = field(default=False, init=False)      # paid a defence against THIS attack
    loaded: bool = field(default=True, init=False)        # missile weapon has a shot in it

    def __post_init__(self):
        self.wounds = self.build.max_wounds
        self.pool = self.build.pool_size
        self.ar = self.build.ar

    @property
    def alive(self) -> bool:
        return self.wounds > 0

    def refresh(self):
        # The draft's refill floor: nothing takes you below 1 die at the top of
        # your own turn. Only Ambushed does, and this simulator has no surprise.
        self.pool = max(1, self.build.pool_size - self.shock_carry)
        self.shock_carry = 0
        self.used_commit = False
        self.press_debt = False
        self.cancelled = 0

    def def_penalty(self) -> int:
        """Flat modifiers on your defence. Sources moved to Disadvantage drop out."""
        return ((-PRESS_DEBT if (self.press_debt and not PRESS_DEBT_DISADV) else 0)
                + (-2 if (self.off_balance and not OFF_BALANCE_DISADV) else 0))

    def def_disadv(self) -> bool:
        """Is any source giving your defence roll Disadvantage? They do not stack."""
        return ((self.press_debt and PRESS_DEBT_DISADV)
                or (self.off_balance and OFF_BALANCE_DISADV))

    def free_defence(self):
        """(die, bonus) for the unpaid defence. Costs nothing, always available."""
        if PASSIVE_EVASION:
            # Static Evasion. die=1 so the roll is always exactly the score.
            ev = (EVASION_FLAT + int(self.build.dex * EVASION_DEX)
                  - int(self.build.armor_penalty * FREE_DODGE_AP) + self.def_penalty())
            return 1, ev - 1
        if DODGE_DIE is None:
            return self.build.die, self.build.free_dodge + self.def_penalty()
        ap = int(self.build.armor_penalty * FREE_DODGE_AP)
        return DODGE_DIE, DODGE_FLAT - ap + self.def_penalty()

    def paid_defences(self):
        """Every defence a Tempo Die can buy, as (die, bonus).

        As of 2026-08-22 (log item 50) there is exactly ONE, and the draft now says
        so too: Parry and Block were merged. This function had always written them
        as a single line - die + Skill + Guard - so every figure in log items 33-49
        was measured against the merged rule. The merge cost nothing because nothing
        here ever distinguished them; what it removed was two rows of rules text."""
        ap_all = self.build.armor_penalty if AP_ON_ALL_DEFENCES else 0
        out = [(self.build.die,
                self.build.skill + self.build.guard - ap_all + self.def_penalty())]
        if not COMMITTED_DODGE:
            pass                   # no committed Dodge: a die buys Parry or Block only
        elif DODGE_DIE is None:
            out.append((self.build.die,
                        self.build.dex - self.build.armor_penalty + self.def_penalty()))
        else:
            out.append((DODGE_DIE, DODGE_FLAT - self.build.armor_penalty
                        + (int(self.build.dex * COMMIT_DEX_FRACTION)
                           if DODGE_COMMIT_DEX else 0) + self.def_penalty()))
        if ONE_COMMIT_PER_ROUND and self.used_commit:
            out = out[:1]          # the committed Dodge is spent; Parry/Block remain
        return out

    def commit_is_best(self):
        """Would the paid defence chosen right now be the committed Dodge? Used only
        to charge ONE_COMMIT_PER_ROUND against the right option."""
        opts = self.paid_defences()
        if len(opts) < 2:
            return False
        ev = lambda o: (o[0] + 1) / 2.0 + o[1]
        return ev(opts[1]) > ev(opts[0])

    def best_paid(self):
        """Compare EXPECTED TOTALS, not bonuses - the options roll different dice.
        (This is the bug that produced the bogus 12.2-point figure in item 36.)
        Disadvantage applies to every option equally, so it cannot change the pick."""
        return max(self.paid_defences(), key=lambda o: (o[0] + 1) / 2.0 + o[1])


# --------------------------------------------------------------------------
# Resolution
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# How Press and Measured modify the attack roll (log item 47, was open question 7)
# --------------------------------------------------------------------------
# The draft wrote both as a flat +2 / -2. Against a 1d4 that is half the die and
# against a 1d12 a sixth, so the same rule was worth three times as much to a weak
# fighter as to a strong one: blanket-Press beat blanket-Measured 71.5% at 1d4 and
# 32.2% at 1d12, a 39-point range.
#
# THE TWO HALVES ARE NOT THE SAME PROBLEM, and this is the finding:
#
#   * PRESS's +2 is free to change. Making it proportional costs nothing anywhere
#     (field spread 5.4 -> 5.7, inside noise) and cuts the range to 15.0.
#   * MEASURED's -2 IS LOAD-BEARING and must stay flat. The mixed heuristic uses
#     Measured for most attacks, so its modifier is effectively a term in every
#     attack roll - and a flat term in every roll costs a small die more win
#     probability than a large one, which is currently the main thing holding STR
#     and DEX level. Making it proportional costs 15 POINTS of field spread
#     (5.4 -> 20.6) and hands the game to the high-DEX build. See item 47.
#
# ADOPTED: Press rolls the Tempo Die twice and takes the higher. Measured keeps its
# flat -2. Press's defensive debt also stays at -2 (measured at -1: worse, 33.2).
#
# PRESS_MODE alternatives, all measured, none adopted:
#   "flat2"  - the draft as written, +2. Range 39.3.
#   "flat3"  - +3. Range 45.4: it is a SHAPE fault, not a size fault.
#   "step"   - one die size up. Dies at the ends of the ladder.
#   "adv"    - ADOPTED. Roll twice, take the higher.
PRESS_MODE = "adv"
MEASURED_FLAT = -2    # LOAD-BEARING. See above before touching this.
PRESS_DEBT = 2        # Press: -PRESS_DEBT to your own defences until your next turn.
# --- 2026-08-22 (item 52 follow-up): flat modifiers on a DEFENCE roll are now as
# --- disproportionate as flat modifiers on an attack roll, because item 52 deleted
# --- the unpaid defence - every defence is a Parry, and a Parry rolls the Tempo Die.
# --- Item 7's finding that "flat numbers are safe on defence" was a property of the
# --- static Evasion it was measured against, and it does not survive that deletion.
OFF_BALANCE_DISADV = True    # ADOPTED: Feint's Off-Balance is Disadvantage, not -2.
PRESS_DEBT_DISADV = False    # candidate: Press's own defensive debt, likewise.

# --------------------------------------------------------------------------
# Log item 48 - three changes borrowed from The Riddle of Steel
# --------------------------------------------------------------------------
# DECLARE_UP_FRONT - the whole attack sequence is declared and PAID as one Major
#   Action, before any of it is answered. This is the instrument that finally
#   reduces attacks per turn WITHOUT taxing DEX: it caps nothing, it removes the
#   ADAPTIVE LOOP. You can no longer swing, watch it go badly, and stop; and a
#   winning Measured can no longer refund a die into another attack this turn.
#   Attacks/turn 3.85 -> 2.95 for 2 points of spread, which is inside noise.
#   Every hard cap measured instead: 29.3 at 3 attacks, 21.9 at 2, 52.0 at 1.
# SHOCK - a landed hit automatically strips 1 Tempo Die. REPLACES the attacker's
#   margin-5 Strip Tempo Opening rather than stacking with it, so the Opening menu
#   loses an entry. Costs nothing and slightly helps balance (7.7 -> 6.7).
# RIPOSTE_MODE - what a defender's won-by-5 buys. "cancel" is adopted: the free
#   swing AND one of the attacker's remaining declared attacks is cancelled, so
#   tempo actually changes hands. Measured alternatives: "strip" (a Tempo Die
#   instead of the cancel) is 8.7 - it taxes the pool, which is DEX's resource -
#   and "only" (the cancel with no free swing) is 17.2 and swings hard to DEX.
DECLARE_UP_FRONT = True
SHOCK = True
# --- 2026-08-23 candidate: attacks cost MORE the further into the sequence they are.
# --- The Nth attack of a turn costs ATTACK_COST(N) dice, so a sequence of N costs the
# --- running total. This exists because the maximin sweep found DEX still ~25 points
# --- ahead after Shock's carry came out: extra dice buy offence AND defence at once,
# --- while die size only buys quality. Charging superlinearly for offence is the one
# --- lever that hits that directly. NOT the same thing as SEQ_PENALTY, which was an
# --- escalating penalty on the ROLL and blew the spread out to 55 (log item 35).
ESCALATING_COST = "flat"   # "flat" = every attack costs 1 (as the draft is written)
                           # "linear" = 1, 2, 3, 4 ...  (running total 1, 3, 6, 10)
                           # "soft"   = 1, 1, 2, 2, 3, 3 (running total 1, 2, 4, 6, 9, 12)


def seq_cost(n: int) -> int:
    """Total dice for a sequence of n attacks."""
    if ESCALATING_COST == "linear":
        return n * (n + 1) // 2
    if ESCALATING_COST == "soft":
        return sum((i + 1) // 2 for i in range(1, n + 1))
    return n


def max_attacks(budget: int) -> int:
    """Most attacks affordable out of `budget` dice."""
    n = 0
    while seq_cost(n + 1) <= budget:
        n += 1
    return n


SHOCK_ON_ABSORBED = True  # 2026-08-23: the draft says Shock fires "whether the blow
                      # wounded them or their armor ate the whole of it". The old code
                      # only fired it when damage got through, which silently exempted
                      # exactly the high-AR targets armour is NOT supposed to protect.
                      # False reproduces the pre-08-23 figures.
SHOCK_CARRY = False   # DELETED FROM THE DRAFT 2026-08-23, kept as a switch. Shock
                      # landing on an already-empty pool used to carry a die into the
                      # next refill. Modelled for the first time on 2026-08-23 and it
                      # was doing one thing: taxing small pools. A pool-2 build ate a
                      # carry on 84% of its turns at 42% of a turn each; a pool-6 build
                      # on 33% at 5%. STR/DEX maximin spread 38.3 with it, 25.3 without,
                      # and it bought nothing in party win rate (78.4 vs 76.5) or fight
                      # length (1.98 either way). Set True to reproduce the old figures.
PLAIN_ATTACKS_CRIT = True  # only meaningful while CRITS is True. A plain attack was
                      # ruled a real contest with a real margin, so it criticalled like
                      # any other; criticals were then deleted outright the same day.
RIGID_ZERO_WEAR = True  # 2026-08-23: the ADOPTED Rigid/Flexible rule - a blow that deals
                      # no damage at all after AR costs Rigid armour no durability. This
                      # is what separates Breastplate from Brigandine at the same AR 6,
                      # and it was not modelled: RIGID_HALF_WEAR is a DIFFERENT, rejected
                      # candidate and was left False.
RIPOSTE_MODE = "cancel"   # "cancel" (adopted) | "strip" | "only" | "swing" (old)
DIE_LADDER = [4, 6, 8, 10, 12]


def _stepped(die: int, direction: int) -> int:
    i = DIE_LADDER.index(die) if die in DIE_LADDER else 0
    return DIE_LADDER[max(0, min(len(DIE_LADDER) - 1, i + direction))]


def type_roll(die: int, atype: str) -> int:
    """The attack's die result INCLUDING whatever Press/Measured does to it."""
    if atype == "feint":
        return roll(die)
    if atype == "measured":
        return roll(die) + MEASURED_FLAT
    if PRESS_MODE == "adv":
        return max(roll(die), roll(die))
    if PRESS_MODE == "flat2":
        return roll(die) + 2
    if PRESS_MODE == "flat3":
        return roll(die) + 3
    if PRESS_MODE == "step":
        return roll(_stepped(die, 1))
    raise ValueError(PRESS_MODE)


def choose_type(atk: Combatant, dfn: Combatant, n_left: int) -> str:
    t = atk.policy.atk_type
    if t != "mixed":
        return t
    # A plausible thinking-player heuristic rather than a solved policy:
    # finish with a Press, set up with a Feint when you have follow-ups, else Measured.
    if dfn.wounds <= 1:
        return "press"
    if n_left >= 2 and dfn.pool > 0:
        return "feint"
    return "measured"


def attack(atk: Combatant, dfn: Combatant, seq_index: int, n_left: int,
           prepaid: bool = False) -> None:
    """One Exchange. seq_index is 0 for the first attack of the turn.

    prepaid: the die was already spent when the sequence was DECLARED, so do not
    charge it again. See DECLARE_UP_FRONT."""
    if not prepaid:
        atk.pool -= 1
    atype = choose_type(atk, dfn, n_left)

    seq_pen = SEQ_PENALTY * seq_index   # zero as adopted; see the constant
    a_total = (type_roll(atk.build.die, atype) + atk.build.skill + seq_pen
               - (atk.build.armor_penalty if AP_ON_ATTACK else 0))

    if atype == "press":
        atk.press_debt = True

    # --- the defence -------------------------------------------------------
    # As adopted (item 52) there is nothing free: a Tempo Die buys a Parry, and
    # an attack nobody pays for lands at UNANSWERED_MARGIN. Under UNPAID_DEFENCE
    # the defender instead falls back on free_defence() - Evasion, or the older
    # free Dodge, depending on PASSIVE_EVASION.
    d_disadv = dfn.def_disadv()
    p_die, p_bon = dfn.best_paid()
    p_ev = ev_die(p_die, d_disadv) + p_bon
    if UNPAID_DEFENCE:
        f_die, f_bon = dfn.free_defence()
        f_ev = ev_die(f_die, d_disadv) + f_bon
        free_can_stop = not (a_total > f_bon + 1)    # free roll already stops it
    else:
        f_die = f_bon = None
        f_ev, free_can_stop = -99, False
    defended = (dfn.pool > dfn.policy.def_floor
                and p_ev > f_ev
                and not free_can_stop
                and a_total <= p_bon + p_die)        # paid roll can still stop it
    STATS["attacks"] += 1
    dfn.blocked = defended
    if defended:
        STATS["paid_defences"] += 1
        if dfn.commit_is_best():
            dfn.used_commit = True
        dfn.pool -= 1
        margin = a_total - (roll_def(p_die, d_disadv) + p_bon)
        hit = margin > 0
    elif UNPAID_DEFENCE:
        margin = a_total - (roll_def(f_die, d_disadv) + f_bon)
        hit = margin > 0
    else:
        margin, hit = UNANSWERED_MARGIN, True

    dfn.off_balance = False

    if not hit:
        # Only a defence you paid for can take an Opening.
        if -margin >= OPENING_MARGIN and defended:
            take_riposte(dfn, atk)
        return

    dmg = dfn_damage(atk, dfn, atype, crit=(CRITS and margin >= CRIT_MARGIN))
    if atype == "feint":
        dfn.off_balance = True
        dmg = 0
    if atype != "feint":
        if dmg:
            dfn.wounds -= wounds_from(dmg, dfn.build.str_)
        if SHOCK_ON_ABSORBED or dmg:
            apply_shock(dfn)                  # armour protects Wounds, never tempo

    if atype == "measured":
        # The refund goes back to the pool. Under DECLARE_UP_FRONT the sequence is
        # already fixed, so it can only ever fund DEFENCE - which is what the
        # chapter's own prose always claimed Measured was for.
        atk.pool += 1

    if margin >= OPENING_MARGIN and atype != "feint" and not SHOCK:
        dfn.pool = max(0, dfn.pool - 1)   # the old Strip Tempo Opening, replaced by Shock


def apply_shock(c: Combatant) -> None:
    """A landed melee blow costs its target a die. If the pool is already empty the
    Shock carries into the next refill - one die at most, however many blows land."""
    if not SHOCK:
        return
    if c.pool > 0:
        c.pool -= 1
    elif SHOCK_CARRY:
        c.shock_carry = 1


def dfn_damage(atk: Combatant, dfn: Combatant, atype: str, crit: bool) -> int:
    """A landed blow is resolved against CURRENT AR, and then costs 1 durability.

    armor.md: "Every successful hit against you reduces your armor's durability
    by 1" and "your current AR equals your current durability". A Feint deals no
    damage and is not treated as a hit here. This is why heavy armour is worth
    less than its AR suggests: **the protection decays inside the fight and the
    Armor Penalty does not.**"""
    if atype == "feint":
        return 0
    raw = atk.build.damage()
    if crit:
        raw = max(raw, atk.build.damage())
    if atype == "press":
        raw += 2
    soak = dfn.build.guard if (GUARD_SOAK and dfn.build.guard and dfn.blocked) else 0
    out = max(0, raw - dfn.ar - soak)
    if DURABILITY:
        dfn.hits_taken += 1
        wears = not (RIGID_HALF_WEAR and dfn.build.rigid and dfn.hits_taken % 2 == 0)
        if RIGID_ZERO_WEAR and dfn.build.rigid and out == 0:
            wears = False                     # a blow it absorbed entirely costs it nothing
        if wears:
            dfn.ar = max(0, dfn.ar - atk.build.ar_degrade)
    return out


def take_riposte(winner: Combatant, loser: Combatant) -> None:
    """The defender's Opening. Under RIPOSTE_MODE "cancel" it does two things:
    a free plain attack, AND one of the attacker's remaining declared attacks is
    cancelled - which is what makes it a transfer of tempo rather than one more
    swing. Lowering the margin instead was measured and is worth almost nothing."""
    if RIPOSTE_MODE in ("cancel", "strip", "only"):
        loser.cancelled += 1
    if RIPOSTE_MODE == "strip":
        loser.pool = max(0, loser.pool - 1)
    if RIPOSTE_MODE != "only":
        riposte(winner, loser)


def riposte(winner: Combatant, loser: Combatant) -> None:
    """A plain attack: no type, and it can neither take an Opening nor give one.

    It DOES Shock, being a melee blow that landed, which was missing before
    2026-08-23 and understated the Riposte in every figure the file printed before
    then. It no longer criticals, because nothing does - see CRITS."""
    total = roll(winner.build.die) + winner.build.skill
    p_die, p_bon = loser.best_paid()
    if UNPAID_DEFENCE:
        f_die, f_bon = loser.free_defence()
        free_can_stop = not (total > f_bon + 1)
    else:
        f_die = f_bon = None
        free_can_stop = False
    defended = (loser.pool > loser.policy.def_floor
                and not free_can_stop
                and total <= p_bon + p_die)
    if defended:
        if loser.commit_is_best():
            loser.used_commit = True
        loser.pool -= 1
        margin = total - (roll(p_die) + p_bon)
    elif UNPAID_DEFENCE:
        margin = total - (roll(f_die) + f_bon)
    else:
        margin = UNANSWERED_MARGIN
    if margin > 0:
        raw = winner.build.damage()
        if CRITS and PLAIN_ATTACKS_CRIT and margin >= CRIT_MARGIN:
            raw = max(raw, winner.build.damage())
        dmg = max(0, raw - loser.ar)
        if DURABILITY:
            loser.hits_taken += 1
            wears = not (RIGID_HALF_WEAR and loser.build.rigid and loser.hits_taken % 2 == 0)
            if RIGID_ZERO_WEAR and loser.build.rigid and dmg == 0:
                wears = False
            if wears:
                loser.ar = max(0, loser.ar - 1)
        if dmg:
            loser.wounds -= wounds_from(dmg, loser.build.str_)
        if SHOCK_ON_ABSORBED or dmg:
            apply_shock(loser)


def take_turn(actor: Combatant, foe: Combatant) -> None:
    take_turn_multi(actor, [foe], "focus")


def duel(a_build: Build, a_pol: Policy, b_build: Build, b_pol: Policy,
         a_first: bool = True, max_rounds: int = 40):
    a = Combatant(a_build, a_pol)
    b = Combatant(b_build, b_pol)
    order = (a, b) if a_first else (b, a)
    rounds = 0
    for rounds in range(1, max_rounds + 1):
        for actor in order:
            foe = b if actor is a else a
            if not (a.alive and b.alive):
                break
            take_turn(actor, foe)
        if not (a.alive and b.alive):
            break
    if a.alive and not b.alive:
        return 1, rounds
    if b.alive and not a.alive:
        return 0, rounds
    return None, rounds


def gang_fight(d_build, d_hold, peer_build, n_attackers, max_rounds=30):
    """One fighter against N identical attackers, all Adjacent, no terrain.

    Added 2026-08-21 (log item 40). Everything before this modelled 1v1 only, and
    the value of a HELD die scales with how many people are attacking you - so
    every policy figure taken in a duel understates the case for holding dice, and
    a rule that prices holding cannot be judged without this case.
    """
    D = Combatant(d_build, Policy("d", hold=d_hold, atk_type="mixed"))
    A = [Combatant(peer_build, Policy("a", hold=0, atk_type="mixed"))
         for _ in range(n_attackers)]
    for rd in range(1, max_rounds + 1):
        living = [x for x in A if x.alive]
        if not living:
            return "win", rd
        take_turn(D, living[0])
        for a in A:
            if not a.alive:
                continue
            if not D.alive:
                return "lose", rd
            take_turn(a, D)
        if not D.alive:
            return "lose", rd
    return "stall", max_rounds


def gang_winrate(d_build, d_hold, peer_build, n_attackers, n=2000):
    w = sum(1 for _ in range(n)
            if gang_fight(d_build, d_hold, peer_build, n_attackers)[0] == "win")
    return w / n


def winrate(a_build, a_pol, b_build, b_pol, n=4000):
    """Symmetrised across turn order, so first-mover advantage does not
    contaminate the policy comparison."""
    wins = draws = 0
    total_rounds = 0
    for i in range(n):
        r, rd = duel(a_build, a_pol, b_build, b_pol, a_first=(i % 2 == 0))
        total_rounds += rd
        if r == 1:
            wins += 1
        elif r is None:
            draws += 1
    decided = n - draws
    return (wins / decided if decided else float("nan")), total_rounds / n, draws / n


# --------------------------------------------------------------------------
# Party scale - 4 PCs against N monsters
# --------------------------------------------------------------------------
# Added 2026-08-21 (log item 41). The duel and the gang harness are both edge
# cases for a party game, and they disagree about whether holding dice back is
# correct. This is the case the rules are actually used in, and it is the only
# one where the two forces that price a held die BOTH exist:
#
#   * holding dice makes you personally harder to kill (the duel says so), and
#   * holding dice means the enemy is still alive on somebody else's turn.
#
# A duel cannot see the second one, because in a duel the only person your
# offence protects is you. That is why turtling can be individually rational
# and collectively wrong, and why this harness reports BOTH numbers.


def initiative_order(*groups):
    """Static Initiative = 5 + MIND, highest first. Ties broken once, randomly."""
    everyone = [c for g in groups for c in g]
    return sorted(everyone, key=lambda c: (-(5 + c.build.mind), random.random()))


def pick_target(foes, mode):
    """Who an attacker swings at. Targeting is first-order at party scale - it is
    the difference between four fights and one fight - so it is a parameter."""
    if mode == "focus":          # finish the wounded: concentrate fire
        return min(foes, key=lambda f: f.wounds)
    if mode == "softest":        # go for the squishiest thing you can reach
        return min(foes, key=lambda f: f.build.max_wounds + f.build.ar)
    return random.choice(foes)   # "spread"


def take_turn_multi(actor, foes, mode):
    """One turn's attack sequence, re-picking a target when the current one drops.

    Under DECLARE_UP_FRONT the whole sequence is declared and paid as one Major
    Action before any of it is answered, so the attacker cannot adapt mid-turn and
    a Measured refund cannot extend the turn. Without it, the loop runs on the live
    pool - which is what let a two-die fighter average 2.9 attacks and reach six."""
    actor.refresh()
    if DECLARE_UP_FRONT:
        budget = max(0, actor.pool - actor.policy.hold)
        declared = max_attacks(budget)
        actor.pool -= seq_cost(declared)           # paid as one Major Action
        for i in range(declared):
            if not actor.alive or not any(f.alive for f in foes):
                return
            if actor.cancelled > 0:                # a Riposte took this one
                actor.cancelled -= 1
                continue
            attack(actor, pick_target([f for f in foes if f.alive], mode),
                   seq_index=i, n_left=declared - i - 1, prepaid=True)
        return
    i = 0
    while actor.pool > actor.policy.hold and actor.alive and i < 12:
        live = [f for f in foes if f.alive]
        if not live:
            return
        if actor.cancelled > 0:
            actor.cancelled -= 1
            i += 1
            continue
        attack(actor, pick_target(live, mode), seq_index=i,
               n_left=max(0, actor.pool - actor.policy.hold - 1))
        i += 1


def ranged_turn(actor, foes, mode, engaged: bool) -> None:
    """A missile-armed combatant's turn, tracking whether the weapon is loaded.

    If something is on them and the weapon is Two-Handed, the bow is useless: they
    fight with the sidearm if they have one and do nothing if they do not.

    A weapon whose reload wants the MAJOR Action cannot be reloaded and fired in the
    same turn - reloading IS the turn - so it fires once every two."""
    actor.refresh()
    b = actor.build
    if engaged and b.missile_2h:
        if b.sidearm:
            n = max_attacks(max(0, actor.pool - actor.policy.hold))
            actor.pool -= seq_cost(n)
            for i in range(n):
                live = [f for f in foes if f.alive]
                if not live or not actor.alive:
                    return
                attack(actor, pick_target(live, mode), seq_index=i,
                       n_left=n - i - 1, prepaid=True)
        return

    if not actor.loaded:
        # Nothing to shoot. Put one in, if you can pay for it.
        if actor.pool - actor.policy.hold >= b.reload_cost:
            actor.pool -= b.reload_cost
            actor.loaded = True
        if b.reload_major:
            return          # the reload WAS the Major Action; no shot this turn
        if not actor.loaded:
            return

    used_minor = False
    shots = 0
    while shots < MAX_SHOTS_PER_TURN and actor.alive:
        if not actor.loaded:
            if b.reload_major or used_minor:
                break       # one Minor Action a round, and a Major reload ends the turn
            if actor.pool - actor.policy.hold < 1 + b.reload_cost:
                break
            actor.pool -= b.reload_cost
            actor.loaded = True
            used_minor = True
        if actor.pool - actor.policy.hold < 1:
            break
        live = [f for f in foes if f.alive]
        if not live:
            return
        actor.pool -= 1
        actor.loaded = False
        shoot(actor, pick_target(live, mode), adjacent=engaged)
        shots += 1


def skirmish(pc_builds, pc_policies, mon_build, n_mon, mon_policy, standoff=0,
             pc_target="focus", mon_target="focus", max_rounds=20):
    """A fight that opens at distance and closes.

    `standoff` is how many rounds the party gets before contact. During those the
    missile-armed shoot and nobody else does anything - which is exactly what an
    approach across open ground looks like, and exactly what a bow is bought for.
    After contact everything runs as normal, and a monster that attacks a PC marks
    that PC engaged for the rest of the fight.

    There is no map here and no movement. `standoff` is a dial standing in for both,
    so read it as 'how much closing time the ground gave us', not as a distance."""
    pcs = [Combatant(b, p) for b, p in zip(pc_builds, pc_policies)]
    mons = [Combatant(mon_build, mon_policy) for _ in range(n_mon)]
    order = initiative_order(pcs, mons)
    pcset = set(id(c) for c in pcs)
    engaged = {id(c): False for c in pcs}
    rd = 0
    for rd in range(1, max_rounds + 1):
        contact = rd > standoff
        for c in order:
            if not c.alive:
                continue
            mine = id(c) in pcset
            foes = mons if mine else pcs
            if not any(f.alive for f in foes):
                break
            if mine:
                if c.build.missile:
                    ranged_turn(c, foes, pc_target, engaged[id(c)])
                elif contact:
                    take_turn_multi(c, foes, pc_target)
                else:
                    c.refresh()          # closing; no attack to make yet
            else:
                if not contact:
                    c.refresh()          # closing
                    continue
                live = [f for f in foes if f.alive]
                if live:
                    tgt = pick_target(live, mon_target)
                    engaged[id(tgt)] = True
                take_turn_multi(c, foes, mon_target)
        if not any(m.alive for m in mons) or not any(p.alive for p in pcs):
            break
    won = any(p.alive for p in pcs) and not any(m.alive for m in mons)
    return won, rd, [p.alive for p in pcs]


def party_fight(pc_builds, pc_policies, mon_build, n_mon, mon_policy,
                pc_target="focus", mon_target="focus", max_rounds=20):
    """Returns (party_won, rounds, [survived?] per PC in pc_builds order)."""
    pcs = [Combatant(b, p) for b, p in zip(pc_builds, pc_policies)]
    mons = [Combatant(mon_build, mon_policy) for _ in range(n_mon)]
    order = initiative_order(pcs, mons)
    pcset = set(id(c) for c in pcs)
    rd = 0
    for rd in range(1, max_rounds + 1):
        for c in order:
            if not c.alive:
                continue
            mine = id(c) in pcset
            foes = mons if mine else pcs
            if not any(f.alive for f in foes):
                break
            take_turn_multi(c, foes, pc_target if mine else mon_target)
        if not any(m.alive for m in mons) or not any(p.alive for p in pcs):
            break
    won = any(p.alive for p in pcs) and not any(m.alive for m in mons)
    return won, rd, [p.alive for p in pcs]


def party_stats(pc_builds, pc_policies, mon_build, n_mon, mon_policy,
                n=1500, **kw):
    """(party win rate, mean rounds, per-PC survival rate)."""
    wins = 0
    tot = 0
    surv = [0] * len(pc_builds)
    for _ in range(n):
        w, rd, alive = party_fight(pc_builds, pc_policies, mon_build, n_mon,
                                   mon_policy, **kw)
        wins += w
        tot += rd
        for i, a in enumerate(alive):
            surv[i] += a
    return wins / n, tot / n, [x / n for x in surv]


def standard_party():
    """A plausible four-PC line, not a balanced field. Each is the build the
    chapter's own worked examples describe, plus the back-liner the Casters
    section says exists and is badly off in melee."""
    return [
        Build("Strong",  str_=4, dex=2, skill=3, ar=4, armor_penalty=2,
              dmg_dice=(1, 6, 2), mind=2),                       # two-hander
        Build("Shield",  str_=3, dex=3, skill=3, ar=4, armor_penalty=2,
              dmg_dice=(1, 6, 2), guard=2, mind=3),              # sword and board
        Build("Quick",   str_=2, dex=4, skill=3, ar=2, armor_penalty=1,
              dmg_dice=(1, 8, 0), mind=3),                       # fencer - STR damage
                                                                 # since 2026-08-23
        Build("Backline", str_=2, dex=2, skill=1, ar=1, armor_penalty=0,
              dmg_dice=(1, 4, 0), max_wounds=3, mind=5),         # caster in melee
    ]


def peer():
    """A PEER, not a mook. STR 3 / DEX 3 / Skill 3 with a full Tempo Pool is a
    build made on the player's own axis, and anything on that axis is about as
    dangerous as a PC regardless of what Level it is nominally worth - Attributes
    and Skills share one cap across every character in the game. Numbers of these
    therefore measure a SYMMETRIC fight, not encounter difficulty.

    There is deliberately no weak-creature tier here: `core/bestiary/` predates
    both the 8-to-6 Attribute rework and the Tempo Pool, so there is nothing
    current to calibrate one against. Do not invent one and call it a mook."""
    return Build("Peer", str_=3, dex=3, skill=3, ar=3, armor_penalty=1,
                 dmg_dice=(1, 6, 2), mind=3)


# --------------------------------------------------------------------------
# Builds under test
# --------------------------------------------------------------------------

# Longsword (1d6 + 2), Mail Shirt (AR 4, penalty -2) - the log's reference build,
# carried forward so figures stay comparable in spirit to the old document.
# Each build carries the weapon its Attributes suit - the quick build takes the
# finer blade (Rapier 1d8) for the better die, not for an Attribute of its own.
# ALL MELEE DAMAGE ADDS STR as of 2026-08-23; only missiles add DEX.
BASELINE = Build("Baseline", str_=3, dex=2, skill=3, ar=4, armor_penalty=2,
                 dmg_dice=(1, 6, 2), dmg_attr="str")
QUICK    = Build("Quick",    str_=2, dex=4, skill=3, ar=2, armor_penalty=1,
                 dmg_dice=(1, 8, 0))
STRONG   = Build("Strong",   str_=5, dex=1, skill=3, ar=4, armor_penalty=2,
                 dmg_dice=(1, 6, 2), dmg_attr="str")


# ADOPTED 2026-08-21 (log item 46, revising item 45). Penalty is banded from AR
# alone - AR 5-7 is -1, 8-10 is -2, 11-13 is -3 - and the whole AR ladder rose to
# pay for a scale that starts at -1 instead of at nothing.
#
# ONE POINT OF ARMOR PENALTY COSTS 3-4 POINTS OF AR (+4 at the light end, +3 at the
# heavy end). That rate is the design constant, and anything added to this table has
# to respect it or the entry is a trap. Bands are three AR wide, which prices a
# Penalty point at exactly 3 - so the BOTTOM RUNG OF EVERY BAND pays a whole Penalty
# point for a single point of AR and is the weakest entry on the ladder. That is
# structural and unavoidable while Penalty is an integer stepped off AR; what item 46
# fixed was that under item 45's ladder those bottom rungs dipped BELOW WEARING
# NOTHING (Chain Mail -1.8 points against bare, in every seed). Raising every AR by
# one lifts the whole sawtooth clear of zero without changing a single rule.
#
# ARMOURS_45 is item 45's ladder, kept to reproduce that finding.
# ARMOURS_OLD is core/equipment/armor.md as published.
ARMOURS = {
    # name:            (AR, Penalty)
    # REVISED 2026-08-22 (log item 49). Under the static Evasion, Armor Penalty is
    # charged against ONE number the defender was not relying on, instead of against
    # every defence roll - so a Penalty point is worth roughly 1 AR, not 3-4, and
    # items 45-46's inflated AR ladder ran away (bare 44%, Full Plate 76% in a duel).
    # AR reverts to core/equipment/armor.md AS PUBLISHED and Penalty is re-derived in
    # bands of three AR. Measured at party scale, three seeds: monotone, every armour
    # beats bare, 70% bare to 94% Full Plate.
    "none":            (0, 0),
    "Gambeson":        (2, 1),
    "Buff Coat":       (3, 1),
    "Mail Shirt":      (4, 1),
    "Chain Mail":      (5, 2),
    "Brigandine":      (6, 2),
    "Breastplate":     (6, 2),      # RIGID
    "Half-Plate":      (7, 2),
    "Full Plate":      (8, 3),
}
ARMOURS_46 = {                       # items 45-46's inflated ladder, tuned against the
    # free Dodge. Kept to reproduce those findings; wrong under a static Evasion.
    "none": (0, 0), "Gambeson": (5, 1), "Buff Coat": (6, 1), "Mail Shirt": (7, 1),
    "Chain Mail": (8, 2), "Brigandine": (9, 2), "Breastplate": (10, 2),
    "Half-Plate": (11, 3), "Full Plate": (12, 3),
}
ARMOURS_45 = {                       # item 45's ladder - three rungs at or below bare
    "none": (0, 0), "Gambeson": (4, 1), "Buff Coat": (5, 1), "Mail Shirt": (6, 1),
    "Chain Mail": (7, 2), "Brigandine": (8, 2), "Breastplate": (9, 2),
    "Half-Plate": (10, 3), "Full Plate": (11, 3),
}
ARMOURS_OLD = {                      # core/equipment/armor.md as published
    "none": (0, 0), "Gambeson": (2, 1), "Buff Coat": (3, 1), "Mail Shirt": (4, 2),
    "Chain Mail": (5, 2), "Brigandine": (6, 3), "Breastplate": (6, 6),
    "Half-Plate": (7, 7), "Full Plate": (8, 8),
}


RIGID_ARMOURS = {"Breastplate", "Half-Plate", "Full Plate"}


def armoured(name, str_=3, dex=3, skill=3, **kw):
    ar, pen = ARMOURS[name]
    kw.setdefault("rigid", name in RIGID_ARMOURS)
    return Build(name, str_=str_, dex=dex, skill=skill, ar=ar, armor_penalty=pen,
                 dmg_dice=kw.pop("dmg_dice", (1, 6, 2)), **kw)


def field_builds():
    """The STR-to-DEX ladder used for balance work: same 6 Attribute points, same
    Skill, same armour. Only the STR/DEX split and the weapon differ."""
    out = []
    for st, dx in ((5, 1), (4, 2), (3, 3), (2, 4), (1, 5)):
        # Melee damage adds STR whatever the weapon (2026-08-23). The quick build
        # still carries the finer blade - a better die, no Attribute of its own.
        dice, attr = ((1, 6, 2), "str") if st >= dx else ((1, 8, 0), "str")
        out.append(Build(f"S{st}/D{dx}", str_=st, dex=dx, skill=3, ar=3,
                         armor_penalty=1, dmg_dice=dice, dmg_attr=attr))
    return out


def policies_for(build: Build):
    p = build.pool_size
    out = []
    for hold in range(0, p):
        label = "dump" if hold == 0 else f"hold {hold}"
        out.append(Policy(label, hold=hold, atk_type="mixed"))
    return out


def main():
    random.seed(20260821)

    print("=" * 78)
    print("TEMPO POOL SIM - is dumping the pool on offence dominant?")
    print("exchange_draft.md as of 2026-08-23. 1v1, Adjacent, no reach, no Feats.")
    print("NOTE: the STR/DEX table below is pinned at hold 1 and UNDERSTATES the gap.")
    print("The maximin figure (both sides solving) is 12.7 points, DEX ahead.")
    print("=" * 78)

    for build in (BASELINE, QUICK, STRONG):
        pols = policies_for(build)
        print(f"\n--- {build.name}: STR {build.str_} (1d{build.die}), DEX {build.dex} "
              f"(pool {build.pool_size}), Skill {build.skill}, AR {build.ar}")
        print("    mirror match, row policy vs column policy, row's win rate\n")
        head = "    " + "".join(f"{p.name:>10}" for p in pols)
        print(head)
        for pa in pols:
            row = f"{pa.name:>10}"[-10:]
            cells = []
            for pb in pols:
                wr, _, dr = winrate(build, pa, build, pb, n=1500)
                cells.append("     stall" if dr > 0.5 else f"{wr*100:>9.1f}%")
            print(f"{row}" + "".join(cells))

    print("\n" + "=" * 78)
    print("ATTACK TYPE, held constant - is Measured simply correct?")
    print("=" * 78)
    for build in (BASELINE, QUICK, STRONG):
        print(f"\n--- {build.name} (pool {build.pool_size})")
        types = ["measured", "press", "mixed"]  # pure feint never deals damage; it lives inside "mixed"
        best_hold = 1 if build.pool_size > 2 else 0
        print(f"    both sides holding {best_hold}; row type vs column type\n")
        print("    " + "".join(f"{t:>10}" for t in types))
        for ta in types:
            cells = []
            for tb in types:
                pa = Policy(ta, hold=best_hold, atk_type=ta)
                pb = Policy(tb, hold=best_hold, atk_type=tb)
                wr, _, dr = winrate(build, pa, build, pb, n=1500)
                cells.append("     stall" if dr > 0.5 else f"{wr*100:>9.1f}%")
            print(f"{ta:>10}" + "".join(cells))

    print("\n" + "=" * 78)
    print("STR vs DEX - identical gear, identical Skill, same 6 Attribute points")
    print("A balanced split shows a FLAT mean column, and it now does: about 6 points")
    print("of spread over three seeds, down from 55 before the escalating penalty went.")
    print("Item 52 (no unpaid defence at all) IMPROVED this - 7.2 to 5.7 - while making")
    print("the armour ladder monotone. Deleting Evasion cost length, not balance; the")
    print("Wound bands at (9, 18) are what bought the length back.")
    print("=" * 78)
    field = field_builds()
    print("\n    " + "".join(f"{x.name:>10}" for x in field) + "      mean")
    stalls = 0
    for a in field:
        cells, tot = [], []
        for b in field:
            pa = Policy("m", hold=1 if a.pool_size > 2 else 0, atk_type="mixed")
            pb = Policy("m", hold=1 if b.pool_size > 2 else 0, atk_type="mixed")
            wr, _, dr = winrate(a, pa, b, pb, n=1200)
            if dr > 0.5:
                stalls += 1
                cells.append("     stall")
                tot.append(0.5)
            else:
                cells.append(f"{wr*100:>9.1f}%")
                tot.append(wr)
        print(f"{a.name:>8}" + "".join(cells) + f"{sum(tot)/len(tot)*100:>10.1f}%")
    print(f"\n    stalled matchups: {stalls}   (a stall is a broken state, not a draw -")
    print("    do NOT let it average in as 0.5; that hid a real fault once already)")
    print("    Spread carries about +/-2 points of seed noise. Under 5 points is nothing.")

    print("\n" + "=" * 78)
    print("CROSS-BUILD - quick vs strong, each playing its best hold")
    print("=" * 78)
    for a, b in itertools.combinations((BASELINE, QUICK, STRONG), 2):
        best = {}
        for build in (a, b):
            scores = []
            for pol in policies_for(build):
                wr, _, _ = winrate(build, pol, build, Policy("mid", hold=1, atk_type="mixed"), n=1200)
                scores.append((0.0 if wr != wr else wr, pol))
            best[build.name] = max(scores, key=lambda x: x[0])[1]
        wr, rounds, dr = winrate(a, best[a.name], b, best[b.name], n=4000)
        print(f"  {a.name} ({best[a.name].name}) vs {b.name} ({best[b.name].name}): "
              f"{wr*100:.1f}% | mean {rounds:.2f} rounds | stalls {dr*100:.0f}%")

    print("\n" + "=" * 78)
    print("BEST-HOLD SWEEP - is 'attack once, bank the rest' simply correct?")
    print("The STR vs DEX table above pins everyone at hold 1, which is the WRONG END")
    print("of the curve and hid this for six log items. Here each build plays its best")
    print("hold against a fixed S3/D3 at hold 1. A healthy system has no build much")
    print("above ~55%, and no turtle mirror running long.")
    print("=" * 78 + "\n")
    field = field_builds()
    ref = field[2]
    best_holds = []
    for a in field:
        best = None
        for ha in range(0, a.pool_size):
            wr, _, _ = winrate(a, Policy("a", hold=ha, atk_type="mixed"),
                               ref, Policy("b", hold=1, atk_type="mixed"), n=700)
            if best is None or wr > best[0]:
                best = (wr, ha)
        best_holds.append(best)
        print(f"    {a.name:>8}  best hold {best[1]}  ->  {best[0]*100:>5.1f}%")
    wr, mrd, mst = winrate(field[4], Policy("t", hold=best_holds[4][1], atk_type="mixed"),
                           field[4], Policy("t", hold=best_holds[4][1], atk_type="mixed"),
                           n=1200)
    print(f"\n    S1/D5 mirror at its own best hold: {mrd:.1f} rounds, "
          f"{mst*100:.0f}% stalls")
    print("    (under the free Dodge this read ~89% at hold 4 and a 40-round, 100%-stall")
    print("     mirror; the committed Dodge's +DEX was the engine, and item 49 deleted it)")

    print("\n" + "=" * 78)
    print("OUTNUMBERED - one fighter against N identical S3/D3 attackers")
    print("The case where a held die is worth most, and the one nothing modelled")
    print("until 2026-08-21. Read it before pricing anything that limits defending.")
    print("=" * 78 + "\n")
    for n_att in (2, 3):
        row = []
        for a in field:
            best = max(((gang_winrate(a, h, ref, n_att, n=1500), h)
                        for h in range(0, a.pool_size)), key=lambda x: x[0])
            row.append((a.name, best))
        print(f"    vs {n_att}:  " + "  ".join(
            f"{nm} {w*100:>4.1f}%@h{h}" for nm, (w, h) in row))
    print("\n    Every build loses 2v1 and no build survives 3v1, and item 49 made this")
    print("    WORSE - an exhausted fighter used to roll 1d8+2 and now meets a static")
    print("    2-4. The quick build fell from 34% to 7% against two. That is a DESIGN")
    print("    DECISION, not a bug - but the chapter's prose treats being outnumbered")
    print("    as a pressure rather than as decisive, and measured it is decisive.")

    print("\n" + "=" * 78)
    print("PARTY SCALE - 4 PCs vs N PEERS. The case the rules are actually used in,")
    print("and the one that overturns the duel's verdict on holding dice back.")
    print("=" * 78 + "\n")
    party, mk = standard_party(), peer()
    pnames = [b.name for b in party]
    pol = lambda h: Policy("p", hold=h, atk_type="mixed")

    print("    N PEERS vs the party - a symmetric-axis fight, NOT an encounter curve:")
    for n_mon in (2, 3, 4, 5):
        wr, rds, _ = party_stats(party, [pol(1)] * 4, mk, n_mon, pol(1), n=1000)
        print(f"      vs {n_mon} peers: {wr*100:>5.1f}%  ({rds:.1f} rds)")
    print("    -> steep, but this is what SYMMETRIC fights do. It says nothing")
    print("       about encounter design until a weaker creature tier exists.")

    print("\n    holding dice back, vs 3 peers (a fight the party wins):")
    for h in (0, 1, 2, 3):
        wr, rds, _ = party_stats(party, [pol(h)] * 4, mk, 3, pol(1), n=1000)
        print(f"      everyone holds {h}: {wr*100:>5.1f}%  ({rds:.1f} rds)")
    print("    -> monotone DOWN. The duel says hold 3 wins 95%; here it wins 28%.")

    print("\n    one PC turtles, the other three hold 1, vs 3 peers:")
    pools = [b.pool_size for b in party]
    for i, nm in enumerate(pnames):
        holds = [1, 1, 1, 1]
        holds[i] = pools[i] - 1
        wr, _, surv = party_stats(party, [pol(h) for h in holds], mk, 3, pol(1), n=1000)
        print(f"      {nm:>9} turtles: party {wr*100:>5.1f}%   own survival {surv[i]*100:>4.1f}%")
    print("    -> it does not even pay the turtler, EXCEPT for the Backline, whose")
    print("       attacks are worth less than its dice. That is the caster, and it")
    print("       is the behaviour the chapter's Casters section describes.")

    print("\n    targeting, vs 3 peers - the largest dial measured anywhere:")
    for mt, pt in (("focus", "focus"), ("focus", "spread"),
                   ("softest", "focus"), ("spread", "focus")):
        wr, _, _ = party_stats(party, [pol(1)] * 4, mk, 3, pol(1), n=1000,
                               mon_target=mt, pc_target=pt)
        print(f"      monsters {mt:>7}, PCs {pt:>6}: {wr*100:>5.1f}%")
    print("    -> 24 points from the monsters' targeting alone. No rule change")
    print("       measured in this project moves a number that far.")

    print("\n" + "=" * 78)
    print("FIGHT LENGTH and DEFENCE SPEND, self-mirror at each hold")
    print("=" * 78)
    for build in (BASELINE, QUICK, STRONG):
        print(f"\n  {build.name} (pool {build.pool_size}):")
        for pol in policies_for(build):
            _, rounds, dr = winrate(build, pol, build, pol, n=2000)
            print(f"    {pol.name:>8}: mean {rounds:.2f} rounds | stalls {dr*100:.0f}%")


if __name__ == "__main__":
    main()
