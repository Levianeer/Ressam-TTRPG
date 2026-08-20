#!/usr/bin/env python3
"""Monte Carlo for the Exchange system proposed in `exchange_draft.md`.

DRAFT-STAGE TOOL. The Exchange is not merged into core/. This is the source of
every number quoted in that file's "What simulation found" section - run it bare
to reproduce them all:

    python3 tools/exchange_sim.py

Reuses combat_engine's damage/wound/gear model so results stay comparable to the
existing tooling. Does NOT reuse its resolution path - Oppose, Margin tiers,
Effects and the Press are all deleted by the draft.

WHAT IS MODELLED
  - Advance / Hold / Withdraw declared simultaneously. Advance beats Withdraw,
    Withdraw beats Hold, Hold beats Advance.
  - Displacement is the sum of both declarations (Advance -1, Hold 0, Withdraw +1).
  - The winner attacks if the new measure is inside their weapon's Bands - or one
    Band off at Disadvantage, when GRADUATED is on.
  - Opportunity Attacks when an Advancing fighter crosses into a threatened zone.
    A Mirror never provokes - see MIRROR_PROVOKES. Leaving a zone provokes only
    on a Move Action, which is outside the Exchange loop, so a Withdraw is free
    and always has been here (log item 25).
  - Economy: one Exchange per turn, answering is free, Reactions buy follow-ups
    after a win. OAs draw on the same pool, so the two compete. A Mirror blow
    costs the responder a Reaction and the initiator nothing - see MIRROR_COST,
    which the tool answered by omission until 2026-08-17.
  - Shields: Buckler edits the Cycle at every Band; Heater edits it and adds AR,
    and both die at Close.

WHAT IS NOT
  - More than two combatants, terrain, casters, ranged attackers.
  - Any Feat, Condition, or Trauma.
  - Player skill at reading an opponent. See Fighter.declare - the declaration
    policy is the single largest confound in this tool.

READING THE OUTPUT
  Matrix cells are symmetrised: `run_fight` gives the row weapon the first turn
  of every round, and that is worth 13-23 points on average, so a raw cell mixes
  weapon strength with the first-mover penalty. See `matrix`. Verdicts reached
  off the raw view before 2026-08-17 were re-derived; the spread-based ones all
  held, and four attribution claims turned out to be backwards - Opportunity
  Attacks, the costs of pricing the riposte, the shield Cycle edit's value
  against flat AR, and the Buckler against polearms.
"""

import random
import statistics
from collections import Counter

from combat_engine import (
    WEAPONS, ARMORS, Build, Weapon, roll_d12, wounds_from_damage,
)

ADVANCE, HOLD, WITHDRAW = "Advance", "Hold", "Withdraw"
DECLS = (ADVANCE, HOLD, WITHDRAW)
SHIFT = {ADVANCE: -1, HOLD: 0, WITHDRAW: +1}
BEATS = {ADVANCE: WITHDRAW, WITHDRAW: HOLD, HOLD: ADVANCE}

# --- configuration the report sweeps over ---------------------------------
GRADUATED = True     # one Band off may still attack, at Disadvantage
# Lever 5, REJECTED - kept so the rejection stays reproducible. Which direction
# the one Band of slop runs. 'both' is the draft as written. 'down' makes it
# asymmetric: you may fight one Band INSIDE your weapon's pair (crowded,
# Disadvantage) but never one Band OUTSIDE it - you cannot lengthen a stick.
# Appealing because it states "reach beats anything below it" by directionalising
# a rule that already exists rather than adding one, it sharpens the reach ladder
# (Pike 59->62%), and every dead exchange it adds is OUTWARD - the approach, not
# a lockup. Rejected on four counts:
#   - It is the whole two-hander class, not one weapon: Longsword 51->43%,
#     Greatsword 61->53%, Quarterstaff 49->40%, Rapier 45->38%.
#   - It is positional, not a dice artifact - with every weapon on identical
#     dice the Longsword still falls 48->40%, below the sidearms at 45%.
#   - It is not robust. At loose declaration play (BIAS 0.40) the effect vanishes
#     entirely; on a longer track (MAX_MEASURE 5) it reverses.
#   - It breaks the shield economy. A raw one-hander vs a two-hander goes
#     40->50%, so the shield Cycle edit - calibrated when that baseline was 25% -
#     overshoots to 69/31. Dropping the edit fixes the rout (50%) but leaves the
#     two-hander at 45% anyway and leaves the Buckler with no mechanic at all.
# The law underneath: symmetric slop pays the middle of the track, directional
# slop pays the ends. Neither is neutral; there is no version that pays nobody.
GRAD_DIR = "down"    # 'both' | 'down' - ADOPTED 2026-08-19: down (lever 5)
OA_MODE = "once"     # 'off' | 'once' | 'perband'

# RULED AND REVERTED 2026-08-19, same day - see log item 24. Exempting Mirrors
# from Opportunity Attacks was adopted to stop one Exchange producing four
# attack rolls, then measured: it makes OAs inert. On and off match within a
# point on every weapon, and OA volume falls 90-96%, because an Advance Mirror
# is the only declaration pair that moves the Measure two Bands and so is where
# nearly every threat-boundary crossing happens. Kept as a switch because the
# measurement is worth being able to re-take; True is the adopted rule.
MIRROR_PROVOKES = True
BIAS = 0.75          # how strongly a fighter favours its preferred declaration
MAX_MEASURE = 4      # set by use_bands(); one step past the outermost Band

# Lever 3c, ADOPTED. On an Advance/Advance double hit the longer weapon strikes first,
# and it strikes at the measure it HAD rather than the collapsed one - the pike
# lands on the way in. Set False to recover the simultaneous double hit.
# The narrower reading (strike first, but at the new measure) is a no-op for
# polearms: a double hit collapses two Bands, dumping them past their own reach.
REACH_ORDER = True

# Lever 1, REJECTED - kept so the rejection stays reproducible. Gives polearms a
# Cycle edit so their Withdraw is not simply run through. Both settings overshoot
# catastrophically; see the draft's "What simulation found".
#   'none' | 'tie'  (vs a polearm, Advance only ties Withdraw)
#           | 'flip' (vs a polearm, Withdraw beats Advance)
POLEARM_EDIT = "none"

# ADOPTED. The responder pays a Reaction to convert a won read into an attack.
# Defending stays free - nobody is ever locked out - but hitting back costs.
# Restores the principle the current rules already run on, where Oppose costs a
# Reaction. Best single result against the weapon-spread problem: 21-78% -> 20-68%.
RIPOSTE_COSTS_REACTION = True

# Lever 4, REJECTED as a core rule - kept reproducible, and worth revisiting as a
# Feat. "Shorten" / haft the weapon: a fighter about to strike at
# a measure INSIDE their weapon's Bands may spend Reactions to slide their Band
# pair down one step each - half-swording, choking up the spear. Only a weapon
# with haft to spare can do it (min(bands) > 0), and nothing can ever lengthen,
# so the asymmetry is the point: a long weapon can play at a short weapon's
# measure by paying for it, a short weapon can never play at a long one's.
#   'off'   | 'on'    (a Reaction per Band stepped down)
#           | 'weak'  (as 'on', but a shortened strike rolls damage twice, lower)
#           | 'flat'  (one Reaction buys any depth - no counting at the table)
#           | 'clean' (keeps GRADUATED's free Disadvantaged step; a Reaction
#                      upgrades that step to a clean strike. Smallest version.)
# Every pricing came out neutral-to-negative, for one reason: GRADUATED is
# already a free step down the track, so hafting fires on 0.4% of exchanges, and
# where it does fire the Reaction is worth more spent on a riposte. Priced at a
# Reaction this is a trap option. Its real home is a Martial Feat, where it is an
# opt-in purchase rather than a core rule everyone must learn.
SHORTEN = "off"

# REJECTED - kept so the rejection stays reproducible. Lets the initiator declare
# Hold as freely as the responder, i.e. Holding no longer wastes their turn. It
# does perfectly fix the first-mover asymmetry (~50/50 for every weapon) and then
# detonates everything else: spread 21-78% -> 6-93%, empty exchanges to 41-52%,
# fights stall. The obligation to act is the system's clock.
INITIATOR_MAY_HOLD = False

# Reactions per round by DEX 0..5. combat.md's Action Economy table is
# [1,1,1,2,2,3] - and the step from DEX 2 to DEX 3 DOUBLES the pool, with the
# baseline build sitting one point below it. That single breakpoint is worth
# +4 to +14 points of win rate to every weapon tested, because the same pool
# funds ripostes, follow-ups and Opportunity Attacks. Swap curves here to test
# flattening it; `reactions()` replaces combat_engine.reactions_of throughout.
REACTION_CURVES = {
    "current":    [1, 1, 1, 2, 2, 3],   # combat.md as written
    "flat-2":     [2, 2, 2, 2, 2, 2],   # decoupled: DEX buys no Reactions at all
    "flat-3":     [3, 3, 3, 3, 3, 3],
    "half":       [1, 1, 2, 2, 3, 3],   # 1 + floor(DEX/2)
    "base2-half": [2, 2, 3, 3, 4, 4],   # 2 + floor(DEX/2) - same slope, higher floor
    "base2-third":[2, 2, 2, 3, 3, 3],   # one breakpoint, from a base of 2
    "early":      [1, 2, 2, 3, 3, 4],   # first step arrives at DEX 1 instead of 3
}
REACTION_CURVE = "current"


def reactions(build):
    c = REACTION_CURVES[REACTION_CURVE]
    return c[max(0, min(len(c) - 1, build.DEX))]


# Turn order is the largest single effect in the system: the fighter who acts
# first wins 41% of a sidearm mirror and 37% of a polearm one, and across the
# matrix the gap averages 20 points and peaks at 33. The cause is not a rule but
# an incentive - the initiator spent a Major Action so cannot afford to Hold, and
# Hold beats Advance. Relieving them (INITIATOR_MAY_HOLD) fixes it and stalls the
# game, because the obligation to act is the only clock the system has. These are
# attempts to fix it while PRESERVING that obligation.
#   'none'      as drafted
#   'initiative' the initiator strikes first in an Advance/Advance double hit,
#                overriding the longer weapon. Narrow - fires on ~13%.
#   'reaction'   initiating grants one extra Reaction for that Exchange. Pure
#                economy compensation; the Cycle is untouched.
#   'passivity'  nobody may declare Hold twice in a row. Attacks the RESPONDER's
#                free Hold rather than subsidising the initiator - the same shape
#                as the non-combativity rules real fencing rulesets carry.
#   'norepeat'   the harsher version: no declaration twice in a row at all.
#   'consolation' the initiator who LOSES a read gets a Reaction back.
# Tokens combine: "passivity+consolation" applies both.
#
# ALL REJECTED, and kept reproducible. What each measured, against a baseline
# turn-order gap of 21% and a spread of 19-81%:
#   passivity            gap 16%, spread 23-77%, empty 38->28%. The best single
#                        result, and rejected on cognitive overhead - it asks a
#                        player to remember their last declaration, and this
#                        system's whole claim is that it does not ask for that.
#   norepeat             gap 17%, spread 27-73% (the narrowest anything produced)
#                        - but it forbids sustained aggression, and the draft
#                        states elsewhere that a swordsman who simply keeps
#                        Advancing will not let you go. Contradicts the system.
#   reaction             overshoots hard. At a base of 1 Reaction, granting the
#                        initiator +1 DOUBLES their pool: mirror 41% -> 58%.
#   consolation          worth almost nothing alone (gap 20% vs 21%). On top of
#                        passivity it reaches gap 14% with mirrors 45/51/37 -
#                        the designated next step if turn order is ever reopened.
# Note also that the REACTION FLOOR is itself a turn-order lever: raising it from
# 1 to 2 moves the Broadsword mirror from 41% to 63% with nothing else changed.
# Any future change there silently reopens this.
TURN_FIX = "none"

# What a Hold/Hold mirror produces. ADOPTED: 'trade'. Both fighters attack at the
# current measure if their weapon reaches, SIMULTANEOUSLY - neither is moving, so
# there is no basis for an ordering, and resolving in sequence hands the win to
# whoever is checked first (that bug made this change look like a turn-order fix
# when it is the opposite; see below).
#
# Adopted because it is the best result found against the empty exchange - 30% to
# 17% across the matrix, beating the Reaction floor (21%) and the passivity rule
# (28%) - and because it costs NEGATIVE rules overhead: it deletes a row from the
# Mirrors table rather than adding one, and deletes the odd row at that. Two
# fighters standing their ground at a measure where both can reach, doing nothing
# to each other, was always the strange square on that grid.
#
# It does NOT fix turn order; it makes it worse, gap 21% -> 29%. Trading blows
# rewards whoever was going to Hold anyway, and that is the responder - the
# initiator is pushed toward Advance and gains nothing from the Hold mirror.
# Costs: fights run 2.7 -> 2.3 rounds, and two lethal mirrors instead of one.
HOLD_MIRROR = "trade"      # 'standoff' | 'trade' - ADOPTED: trade

# What a Mirror blow costs. ADOPTED 2026-08-17: 'responder'.
#
# The draft priced the riposte - converting a won read on somebody else's turn -
# at one Reaction, and never said what a Mirror blow costs, because a Mirror is
# not a won read. The tool answered 'free' by omission for as long as it existed,
# and every figure taken before this date was measured under that answer.
#
# It is not a small omission. Advance/Advance fires on 21% of exchanges and Hold/Hold
# on 13% - together about a third, against 26% for the ripostes the economy
# actually charges for. Mirror blows are MORE COMMON than the priced action.
#
#   'free'      nobody pays. What the tool did by omission. Leaves the reach
#               ladder at 16 points with the top two classes 2 apart, so reach
#               barely reads - see the Hold/Hold note above, which is half the
#               cause. REJECTED once reach dominance became the stated goal.
#   'both'      both fighters pay. REJECTED outright: empty exchanges 17% -> 32%,
#               undoing the Hold/Hold trade adopted to pull that number down
#               from 30%. Pays for the same fix twice and lands worse than
#               before it.
#   'responder' ADOPTED. The initiator's Major Action already bought their blow,
#               exactly as it does for a won read, so only the responder pays.
#               Ladder 16 -> 29 points, fights 2.3 -> 2.55 rounds (toward the
#               3-5 target), empty exchanges hold at 17%, and the Greatsword
#               goes back to losing all four polearm matchups.
#
# The counterplay does not vanish, it relocates: bare, a Broadsword falls 45% ->
# 35% against a Spear, but a Buckler puts it at 53% and a Heater 58% - down from
# 61/65%, which closes open item 7's "shields answer polearms at 64-69%" as well.
# You answer a spear with a shield, not by running at it with a knife.
#
# THE PRICE, and it cannot be tuned away: on 17% of exchanges somebody stands in
# a Mirror unable to afford the swing. Raising the Reaction pool fixes that and
# gives back the ladder it bought - at flat 3 the ladder is 16 points again and
# polearms sit BELOW arming reach. Reach dominance and a comfortable Reaction
# pool are the same dial. See open item 6.
MIRROR_COST = "free"       # 'free' | 'responder' | 'both' - P2 REVERTED 2026-08-19, see log item 22

# ===========================================================================
# THE OPEN CALLS REWORK - candidate, 2026-08-19
# ===========================================================================
# Two levers, aimed at one measured target. `exchange_solver.py`'s O6 localised
# the entire 30-40 point cost of exposing a declaration to ONE state: the
# contested approach. Long and Far are already saddle points - exposure is worth
# nothing there - because at those Measures neither side has a choice worth
# hiding. Middle, contested, swings 30 points, and that one state is what makes
# the whole fight unplayable face up.
#
# Both levers attack the same thing: the follower's ability, on seeing your
# declaration, to leave you somewhere you have no move at all. Neither touches
# the Cycle, Tempo, Mirrors or the economy.
#
# ---------------------------------------------------------------------------
# REACH_CURVE - Advantage / normal / Disadvantage, instead of a wall
#
# 'classic'  as drafted: two Bands at normal, one Band inward at Disadvantage
#            under lever 5, nothing anywhere else.
# 'graded'   each weapon owns three Bands on a curve - Advantage at its outer
#            Band, normal at its inner one, Disadvantage one Band further in,
#            and nothing beyond that in either direction.
#
#                    Close        Middle       Long         Far
#     Sidearms       normal       ADVANTAGE    -            -
#     Arming reach   Disadvantage normal       ADVANTAGE    -
#     Polearms       -            Disadvantage normal       ADVANTAGE
#
# Three properties this shape has that a flat "-2 per Band" does not:
#   - It adds no arithmetic. Advantage and Disadvantage are already defined
#     game-wide, so the whole curve costs one table and no new mechanic.
#   - Every weapon prefers its OUTER Band, so "inside the point hurts you" is a
#     universal rather than a polearm exception.
#   - The hard outer wall survives untouched (lever 5's principle: nothing
#     lengthens a stick), and so does the polearm's dead zone at Close - which
#     is deliberate, because dragging a pike to Close is the entire win
#     condition of a short weapon (items 13 and 14).
# 'flat'     item 28's tuning pass. Every Band of mismatch costs a FLAT
#            REACH_PENALTY off the roll, and you are locked out only past
#            REACH_SLOP_IN / REACH_SLOP_OUT Bands of it. No Advantage, no
#            Disadvantage from reach at all.
#
# Why this shape for a margin gate. Under a binary gate a lockout cost you the
# exchanges you won a read in - about a third. Under margin a lockout means you
# do not even CONTEST, so the other fighter strikes unopposed every single beat,
# and that is what inverts the ladder (item 28). Lockouts are therefore the
# dominant term to tune, and their asymmetry is the specific fault: under
# `classic` with lever 5, a sidearm at Long is locked out outright while an
# arming weapon or polearm one Band too close merely takes Disadvantage.
#
# REACH_SLOP_OUT = 0 restores lever 5's hard outer wall ("nothing lengthens a
# stick"). 1 reads as a lunge or a passing step, which is a real thing a fencer
# does and buys back the symmetry a margin gate wants.
REACH_CURVE = "flat"       # 'classic' | 'graded' | 'flat' - ADOPTED, item 29
REACH_PENALTY = 2          # ADOPTED - swept; the lockout is the dial, not this
REACH_SLOP_IN = 2          # ADOPTED - Bands INSIDE your reach you may still attack at
REACH_SLOP_OUT = 1         # ADOPTED - a lunge. 0 is lever 5's hard wall.

# Does fighting at a mismatched Band cost you your expanded crit range?
#
# This exists because of one measured asymmetry. Disadvantage suppresses crits
# hard - a crit floor of 11 fires on 16.7% of straight rolls and 2.8% of
# Disadvantaged ones - while a FLAT penalty does not touch them at all. So
# swapping `classic` for `flat` quietly hands an expanded-crit weapon its crit
# range back in exactly the Band where it is supposed to be struggling, and the
# weapons with expanded crit ranges are the arming class.
#
# Fictionally it is the easier half to defend: a blow struck from a distance
# your weapon was not made for is not a precise one.
MISMATCH_NO_CRIT = False

# ---------------------------------------------------------------------------
# ADVANCE_ALWAYS_CLOSES - a committed approach cannot be cancelled
#
# As drafted, the two steps add, so an Advance into a Withdraw nets ZERO: the
# man giving ground cancels the approach outright, spends nothing, and risks
# nothing. Against an opponent who can see the declaration coming he does it
# every time, and the approach never happens.
#
# With this on, an Advance closes at least one Band whatever the other side
# declared - Advance/Withdraw goes 0 -> -1, and nothing else moves. Giving
# ground still buys a beat, it just no longer buys immunity. The counter
# degrades from a DENIAL to a DELAY, and a delay can be priced into an open
# decision where a denial cannot.
#
# Only applies to an advancer who actually stepped: a fighter who has spent
# their reactive step is rooted and closes nothing.
#
# The known cost, to be read off the ladder rather than argued: polearms lose
# kiting. A spear can no longer hold a sidearm at arm's length indefinitely,
# only tax the approach.
ADVANCE_ALWAYS_CLOSES = True     # ADOPTED 2026-08-19, item 27

# ===========================================================================
# TEMPO_MODE - the margin hybrid, candidate 2026-08-19
# ===========================================================================
# Takes the GEOMETRY from the Exchange and the RESOLUTION from Oppose.
#
# 'binary'  as drafted. The Cycle gates the blow: take the Tempo or do nothing.
# 'margin'  the Cycle BIASES one opposed roll instead of gating it. Both
#           fighters roll `1d12 \+ Weapon Skill`, the read winner adds
#           CYCLE_BONUS, and the difference says what happened.
#
# THE LINE THAT MAKES THIS A SYNTHESIS RATHER THAN A REBUILD OF OPPOSE:
# margin never buys movement. Displacement stays unconditional and free, exactly
# as drafted - both fighters step per their own declaration whatever the roll
# says. Margin only decides what happens AT the Band they both arrived in. The
# moment margin can Shift someone, steps 2 and 3 stop being independent and the
# system has been rebuilt into the thing it replaced.
#
# One roll does three jobs, which is where the table time goes:
#   - the Band's own Advantage/Disadvantage is applied to it (REACH_CURVE),
#   - the total is your bid for the Tempo,
#   - and the same total is checked against the opponent's Passive Evasion.
#
# A fighter whose weapon does not reach the Band they are standing in does not
# roll at all. "A won Tempo is worthless at the wrong Band" survives in its
# strongest form: you do not even get to contest.
#
# Mirrors stop being a special case. Nobody won the read, so nobody adds the
# bonus, and the dice decide - which deletes the Mirrors table rather than
# rewriting it. Lever 3c keeps its home: on an Advance/Advance collapse the
# longer weapon contests from the Measure it HELD.
TEMPO_MODE = "margin"     # 'binary' | 'margin' - ADOPTED 2026-08-19, item 29

# Under 'margin', may a fighter whose weapon does NOT reach still contest the
# Tempo? Striking and contesting are different thresholds: you can fend a man
# off with the haft, a crossguard, or a shoulder without being able to hurt him
# from there.
#
# False was the first draft and it is why margin+closes routs polearms - a
# spearman let inside contributes literally nothing, so the sidearm strikes
# UNCONTESTED every beat, where the binary gate at least let him deny half of
# them by winning reads.
#
# True lets him roll, at whatever his Band is worth, and win the Tempo without
# a strike behind it - which is exactly what "a won Tempo is worthless at the
# wrong Band" always meant, and is a denial rather than a blow.
CONTEST_OUT_OF_REACH = False

# What giving ground is worth on the opposed roll, under 'margin'.
#
# ADVANCE_ALWAYS_CLOSES deliberately removes the withdrawer's ability to deny an
# approach on the MAP, because that denial is what makes an open declaration
# unplayable. This gives the compensation back on the ROLL instead, which is the
# only place it can go without re-coupling displacement to the read: giving
# ground with the point on line is a defensive act, not a rout, and a fighter
# doing it should be harder to land on.
#
# It is symmetric - anyone may Withdraw - but it is worth more to a long weapon,
# because a long weapon that gives ground is still standing in its own Band.
WITHDRAW_BONUS = 0

# What winning the read is worth on the opposed roll. This is the whole dial
# between "the Cycle is everything" (high) and "the Cycle is flavour" (0).
# At \+2 the read winner takes the Tempo about 64% of the time rather than 100%.
CYCLE_BONUS = 2

# Margin tiers, in points of difference on the opposed roll. Two d12s differ by
# 0 about 8% of the time, by 1-2 about 29%, and by 8\+ about 14%.
#   <= BIND      nobody dictated. Both strike, simultaneously - the double hit
#                survives as an outcome you can roll into rather than a rule.
#   <= TRADE     contested. The winner strikes, the loser strikes back at
#                Disadvantage. This is what replaces the binary gate.
#   >= DOMINANT  the winner strikes and the margin buys DOMINANT_EFFECT.
#   otherwise    a clean strike by the winner alone.
MARGIN_BIND = 0
MARGIN_TRADE = 2
MARGIN_DOMINANT = 8

# What a dominant margin buys. In the real system this is what STANCE
# pre-declares, so nobody picks from a menu mid-crisis - the point of the whole
# hybrid. Modelled here as a single effect because the balance question is what
# a dominant margin is WORTH, not which flavour of it a player chose.
#   'extra'  damage rolled twice, take the higher (the crit path)
#   'none'   nothing - the tier collapses into a clean strike
DOMINANT_EFFECT = "extra"  # 'extra' | 'none'

# ---------------------------------------------------------------------------
# MUTUAL_SWING - CANDIDATE 2026-08-19. "Everybody swings; the read sets order."
#
# The draft gates ATTACKING on the read: take the Tempo or do nothing. That gate
# is the whole reason exposure is fatal (item 18, Finding 2 - a fighter whose
# declaration is known wins about one fight in a hundred). If losing the read is
# worth nothing, the Cycle counter is always the best response, and an open
# declaration is a solved game.
#
# This setting moves the read from GATING the blow to ORDERING it. Both fighters
# attack if their weapon reaches the Band they now stand in; the read winner
# lands first and the loser lands after. A Mirror stops being a special case -
# it is simply the Exchange where nobody had priority, and reach breaks the tie
# exactly as lever 3c already says it does.
#
#   'off'       the draft as written - only the read winner attacks.
#   'priority'  both attack, winner first, loser unmodified.
#   'disadv'    both attack, winner first, loser at Disadvantage.
#
# The bet is that this makes open declaration survivable, because winning the
# read stops being the only currency: the counter on the Cycle and the counter
# on the MAP become different declarations, and step 3's independence from step
# 2 - the draft's own load-bearing idea - starts doing the work secrecy did.
MUTUAL_SWING = "off"       # 'off' | 'priority' | 'disadv'

# What a swing inside an Exchange costs under MUTUAL_SWING.
#
#   'free'      nobody pays for either blow. The Reaction pool goes back to
#               funding follow-ups and Opportunity Attacks only, so DEX still
#               buys aggression across a crowded round rather than buying
#               permission to defend yourself. This is the proposal as argued.
#   'responder' whoever's turn it is not pays 1 Reaction to swing at all - the
#               current riposte rule generalised to both blows.
#   'loser'     only the fighter who lost the read pays.
MUTUAL_COST = "free"       # 'free' | 'responder' | 'loser'

# ---------------------------------------------------------------------------
# DECL_ORDER - who says it first, once declarations are OPEN.
#
# Only `exchange_solver.py` can act on this, because only there is there a
# policy that conditions on what the other side already said; the sim's own
# heuristic declares blind either way.
#
#   'ab'        call order, which is what this file has always used.
#   'defender'  the responder declares first and the initiator commits into it.
#               This is the honest reading of "action beats reaction" - you CAN
#               see how a man is standing, what you cannot do is answer the
#               thrust once it is launched - and it is the opposite of letting
#               the defender answer something already on the table.
DECL_ORDER = "ab"          # 'ab' | 'defender'

# ---------------------------------------------------------------------------
# REACTIVE_STEP - how one declaration relates to several attackers.
#
# You declare fresh in every Exchange, so every read stays live and the duel is
# untouched, but you may only DISPLACE once per round on someone else's turn.
# After that your declaration still resolves on the Cycle - Displacement is
# independent of it - while you stand rooted.
#
# 'unlimited' is the old behaviour and what every figure before 2026-08-17 was
# measured under. In a duel the difference is entirely the follow-up chain: the
# loser of a pressed exchange can no longer keep Withdrawing away from it.
REACTIVE_STEP = "once"     # 'unlimited' | 'once' - ADOPTED: once

# ---------------------------------------------------------------------------
# FOLLOWUP_INITIATOR - who counts as the initiator inside a follow-up Exchange?
#
# MIRROR_COST = "responder" exempts "the initiator". On your own turn that is
# unambiguous. In a follow-up thrown on somebody ELSE'S turn it is not: the
# thrower paid a Reaction rather than a Major Action, so the draft's stated
# reason ("their Major Action already bought the blow") does not reach them.
#
# 'thrower' - whoever spent to make this Exchange happen is the initiator. The
#             exemption follows the payment, which is the principle the economy
#             actually runs on. This is what every figure was measured under.
# 'turn'    - the initiator is always whoever's turn it is, so a responder who
#             wins a read and presses still pays for Mirror blows in the chain.
FOLLOWUP_INITIATOR = "thrower"   # 'thrower' | 'turn'

# ---------------------------------------------------------------------------
# POLICY - adaptive vs. a printed Intent line.
#
# 'adaptive' recomputes the preferred declaration every Exchange from the
# current Measure: the fighter wants the step that leaves them in Band. That is
# the tool's original model, and it is a THINKING opponent.
#
# 'static' fixes the preference once, by reach class, and rolls the same
# weighted line at every Measure regardless of where the fight actually is.
# That is what a monster's printed Intent line does. The difference between the
# two is the price of the mook tier.
POLICY = "adaptive"        # 'adaptive' | 'static'
RESIDUE = "even"           # 'even' | 'skewed' - how the non-preferred weight splits
STATIC_WANT = {"Sidearms": "Advance", "Arming": "Hold", "Polearms": "Hold"}

# Band layouts. N Bands contain N-1 adjacent pairs, so N Bands supports exactly
# N-1 two-Band reach classes. That arithmetic drives the draft's Band count.
_SHORT = ["Dagger", "Knife", "Punch", "Bite"]
_SIDE = ["Shortsword", "Scimitar", "Broadsword", "Mace", "Club"]
_TWOH = ["Longsword", "Greatsword", "Rapier", "Quarterstaff"]
_POLE = ["Spear", "Halberd", "Glaive"]


def _layout(outer, pairs):
    t = {}
    for group, bands in pairs:
        for w in group:
            t[w] = set(bands)
    return outer, t


BAND_SETS = {
    # As first drafted: 4 Bands, the extremes own a single Band each.
    "draft4": _layout(4, [(_SHORT, {0}), (_SIDE, {0, 1}), (_TWOH, {1, 2}),
                          (_POLE, {2, 3}), (["Pike"], {3})]),
    # Recommended: 4 Bands, three reach classes, every weapon owns two.
    "three": _layout(4, [(_SHORT, {0, 1}), (_SIDE, {0, 1}), (_TWOH, {1, 2}),
                         (_POLE, {2, 3}), (["Pike"], {2, 3})]),
    # The alternative: 6 Bands buys back five distinct reach classes.
    "six": _layout(6, [(_SHORT, {0, 1}), (_SIDE, {1, 2}), (_TWOH, {2, 3}),
                       (_POLE, {3, 4}), (["Pike"], {4, 5})]),
}
WEAPON_BANDS = {}


def use_bands(name):
    global MAX_MEASURE, WEAPON_BANDS
    MAX_MEASURE, table = BAND_SETS[name]
    WEAPON_BANDS = {k: set(v) for k, v in table.items()}


use_bands("three")

# Hand counts, straight from `core/equipment/weapons.md` rather than from
# combat_engine's flat two_handed flag, which was too coarse to model shields.
# The rulebook has three states, not two:
#   - Two-Handed        Greatsword, Pike, Halberd, Glaive, Estoc, War Maul...
#                       No shield, ever. This is the class the design intends
#                       when it says "two-handers cannot use shields."
#   - Versatile         Longsword, Quarterstaff, Spear. One-handed by default at
#                       the smaller die, or two-handed at the bigger one. Taking
#                       a shield is legal AND ALREADY PRICED - you drop a die
#                       step to free the hand. The earlier model ignored this
#                       entirely, using the one-handed profile even bare, which
#                       undersold every Versatile weapon fighting without a shield.
#   - One-handed        Sidearms and the Rapier. Shield costs them nothing.
VERSATILE = {                 # weapon: (one-handed dice, two-handed dice)
    "Longsword":    ("1d6+2", "1d8+2"),
    "Quarterstaff": ("1d6",   "2d4"),
    "Spear":        ("1d6",   "1d8"),
}


def profile(name, has_shield):
    """The damage dice this weapon actually uses in this loadout."""
    if name not in VERSATILE:
        return WEAPONS[name]
    one, two = VERSATILE[name]
    w = WEAPONS[name]
    return Weapon(w.name, one if has_shield else two, w.attribute,
                  crit_floor=w.crit_floor, band=w.band, ranged=w.ranged,
                  two_handed=w.two_handed)


def can_shield(name):
    return not WEAPONS[name].two_handed


# Guard died with Margin. These are the mechanics the draft settles on instead.
SHIELD_AR = {"Buckler": 0, "Heater": 0, "Dagger": 0}   # all AR removed 2026-08-19

# What each off-hand tool DOES, as a verb rather than a number. Adopted after
# pricing and Band coverage both failed to tell a Buckler from a Heater under
# lever 5 (see log items 21 and 23): they were the same mechanic at different
# prices, which is the near-duplicate failure Niches exists to catch.
#
#   'entry'   Advance no longer loses to Hold. You advance BEHIND the thing -
#             mobile cover, which is what a war shield is for.
#   'mirror'  in a Mirror, the blow coming at you is at Disadvantage. You cover
#             and strike in one motion - the single-time action a fist-shield
#             exists to enable, and it works in the one place nothing else does.
SHIELD_EFFECT = {"Heater": "entry", "Buckler": "mirror", "Dagger": "entry"}

# How often the Buckler's cover is available. A heater is heavy: one committed
# movement of it per round. A buckler is a fist-sized thing on the end of your
# arm and is never out of position, so it works every time - but only in the
# collision, which is roughly a quarter of exchanges and therefore lands in the
# "nudge" band rather than the "invert" band lever 1 identified.
MIRROR_COVER_LIMIT = "always"      # 'once' | 'always'
# How hard the Buckler's cover is. All of these are live candidates; the old
# "a shield may reduce damage, it may never erase it" line came from a durability
# shield that ate ANY lost read and won 97% of fights - a different mechanic, and
# not authority over a Mirror-only cover.
#   'disadv'   the incoming blow is at Disadvantage
#   'half'     the incoming blow does half damage
#   'negate'   the incoming blow does not happen
#   'negadv'   negated, but only in an Advance Mirror (the double hit)
#   'instead'  negated, and you do not swing either - you cover INSTEAD of
#              striking, which is a parry rather than a free ride
MIRROR_COVER_KIND = "half"     # ADOPTED - see log item 23

# Which Measure Bands each off-hand tool can actually parry in. This is the axis
# the three are told apart on, and it is physical rather than numeric:
#   Heater  dies at Close - a big shield is an obstruction once someone is inside
#   Buckler works everywhere - that is what a dedicated parrying shield is for
#   Dagger  works only once the fight is close. You cannot parry a spear with a
#           knife at spear range. Consequence worth noting: the anti-polearm rout
#           is a Long/Far phenomenon, so an off-hand Dagger cannot reproduce it.
OFFHAND_BANDS = {
    "Buckler": lambda m: True,
    "Heater": lambda m: m > 0,
    "Dagger": lambda m: m <= 1,
}

# How the shield's Cycle edit is paid for. ADOPTED: 'once'.
#
# The bar this was tuned against is derived, not assumed: a shield and a
# two-hander compete for the same hand, so the two-hander prices the hand. Bare
# Broadsword 45%, Greatsword 62% - a two-hander is worth +13 to +16, so a shield
# worth about that is a fair trade. Unpriced ('free') it was worth +20/+28, which
# is why nobody would ever take a two-hander.
#
#   'off'      no edit at all - flat AR only. REJECTED: kills the Buckler
#              outright, which at 0 AR becomes worth exactly +0.
#   'free'     a live shield always stops Advance losing to Hold. The draft as
#              first written. REJECTED: +20/+28, and routs a Spear 84%.
#   'reaction' the bearer spends a Reaction to force the tie. REJECTED, and it
#              was close - best absolute numbers of the four (Heater 51% vs a
#              Greatsword) - but rationing the edit makes AR relatively more
#              valuable, so the Heater starts beating the Buckler 53/47 and
#              "to beat a Heater, get inside it" inverts. Also loads a fifth job
#              onto the Reaction pool, which already funds four.
#   'once'     ADOPTED. Once per round, no Reaction cost. With Heater AR cut
#              2 -> 1 this lands both shields on the bar (+15 / +17), keeps
#              sword-and-board even with a two-hander (48%), keeps the Buckler
#              ahead of the Heater (59%), and fires on ~20% of exchanges - back
#              in the "nudge" band lever 1 identified rather than the "invert"
#              band. One clause of rules text and no new arithmetic.
#   'save'     once per round, and it forgives ANY lost read, not just Advance
#              into Hold - "a shield forgives you for being wrong about the line"
#              taken literally. REJECTED reluctantly: it is the better SENTENCE,
#              with no matchup to memorise, but it measures +21/+26 and cannot be
#              tuned down by cutting AR, because the Buckler has none to cut. The
#              mechanic is too strong at any shield stat.
SHIELD_MODE = "once"       # both tools free, once per round - see log item 23

# CANDIDATE. What a Buckler does, as distinct from a Heater.
#
#   'tie'   both shields edit the same leg: Advance no longer loses to Hold.
#           They are told apart only by which Bands they cover, which lever 5
#           made worthless for the Buckler - a sidearm can no longer chase a
#           long weapon outward, so the fight sits at Long and the Buckler's
#           coverage at Close is dead weight. The Heater then wins on AR alone.
#   'close' the Buckler edits a DIFFERENT leg: when you Advance and they
#           Withdraw, the Measure closes by 1 anyway - you crowd them, shield
#           first. This aims at the sidearm's actual structural problem, which
#           is that Advance and Withdraw cancel: the chaser takes the Tempo and
#           gains no ground. Historically it is what a buckler is for.
BUCKLER_MODE = "tie"       # 'tie' | 'close'


class Fighter:
    def __init__(self, name, weapon, skill=3, armor="Mail Shirt", shield=None,
                 STR=3, DEX=2, wounds=3):
        self.name, self.weapon_name, self.shield = name, weapon, shield
        self.build = Build(
            name=name, STR=STR, DEX=DEX,
            weapon=profile(weapon, shield is not None), weapon_skill=skill,
            armor_ar=ARMORS[armor][0], armor_penalty=ARMORS[armor][1],
            max_wounds=wounds,
        )
        self.is_initiator = False
        self.reset()

    @property
    def bands(self):
        return WEAPON_BANDS[self.weapon_name]

    def reset(self):
        self.wounds = 0
        self.shield_used = False
        self.stepped = False
        self.last_decl = None
        self.ar = self.build.armor_ar
        self.reactions = reactions(self.build)

    @property
    def alive(self):
        return self.wounds < self.build.max_wounds

    @property
    def evasion(self):
        return max(0, 5 + self.build.DEX - self.build.armor_penalty)

    def shield_live(self, measure):
        """Is the off-hand tool able to parry at this Measure? See OFFHAND_BANDS."""
        if not self.shield:
            return False
        return OFFHAND_BANDS[self.shield](measure)

    def effective_ar(self, measure):
        return self.ar + (SHIELD_AR[self.shield] if self.shield_live(measure) else 0)

    def declare(self, measure):
        """Band-aware mixed strategy, asymmetric by role.

        The initiator spent a Major Action, so Holding wastes it - they want an
        aggressive step that still leaves them in Band. The responder pays
        nothing and can afford to wait. Never a pure strategy: a readable
        fighter is a dead one.

        THIS IS THE LARGEST CONFOUND IN THE TOOL. Sweeping BIAS moves the
        empty-Exchange rate from 10% to 43% and fight length from 2.1 rounds to
        2.7+. Every number the report prints is conditional on this model of how
        people actually play, which is the one thing a simulation cannot tell
        you."""
        hi = max(self.bands)
        good = [d for d in DECLS
                if max(0, min(MAX_MEASURE, measure + SHIFT[d])) in self.bands]
        if POLICY == "static":
            lo = min(self.bands)
            cls = "Sidearms" if lo == 0 else ("Arming" if lo == 1 else "Polearms")
            want = STATIC_WANT[cls]
        elif not good:
            want = ADVANCE if measure > hi else WITHDRAW
        elif self.is_initiator and not INITIATOR_MAY_HOLD:
            want = ADVANCE if ADVANCE in good else (HOLD if HOLD in good else good[0])
        else:
            want = HOLD if HOLD in good else good[0]
        if RESIDUE == "skewed":
            # A printed line splits the leftover unevenly - 9/2/1 on a d12 -
            # because a creature has a characteristic SECOND choice too.
            rest = [d for d in DECLS if d != want]
            w = {want: BIAS, rest[0]: (1 - BIAS) * 2 / 3, rest[1]: (1 - BIAS) / 3}
        else:
            w = {d: (BIAS if d == want else (1 - BIAS) / 2) for d in DECLS}
        if "norepeat" in TURN_FIX and self.last_decl is not None:
            w[self.last_decl] = 0.0        # no declaration twice in a row
            if want == self.last_decl:
                for d in DECLS:
                    if d != self.last_decl:
                        w[d] = 0.5
        elif "passivity" in TURN_FIX and self.last_decl == HOLD:
            w[HOLD] = 0.0          # no Hold twice in a row
            if want == HOLD:       # re-spread onto the legal options
                w[ADVANCE] = w[WITHDRAW] = 0.5
        d = random.choices(DECLS, weights=[w[x] for x in DECLS])[0]
        self.last_decl = d
        return d


def reach(f, measure):
    """0 = in Band, 1 = one Band off, 2+ = hopeless."""
    return 0 if measure in f.bands else min(abs(measure - b) for b in f.bands)


def slop(f, measure):
    """Is a one-Band mismatch survivable for free? Under GRAD_DIR='down' only
    when the fight is inside your Bands, never outside them."""
    if not GRADUATED:
        return False
    return GRAD_DIR == "both" or measure < min(f.bands)


def shorten_steps(f, measure):
    """Reactions this fighter would spend hafting down to reach `measure`.

    Minimum-spend policy: buy the ability to strike at all, never the removal
    of Disadvantage, and never a spend that still leaves you unable to strike.
    A more aggressive policy would trade harder into the Reaction pool - this
    one is the conservative read, since the same pool funds ripostes and OAs."""
    if SHORTEN == "off":
        return 0
    if measure >= min(f.bands):     # nothing to shorten toward
        return 0
    d = reach(f, measure)
    if d == 0:
        return 0
    if SHORTEN == "clean":          # pay only to un-Disadvantage a free step
        return 1 if (d == 1 and slop(f, measure) and f.reactions >= 1) else 0
    if d == 1 and slop(f, measure):
        return 0                    # already able to strike; don't pay
    # Shortening always lands us inside our own Bands, so the free Disadvantaged
    # step is available at the end of it under either GRAD_DIR.
    need = d - 1 if GRADUATED else d
    if SHORTEN == "flat":
        return need if f.reactions >= 1 else 0
    return need if need <= f.reactions else 0


# CANDIDATE, not adopted. "Inside the point": at Close nobody strikes with a
# weapon whose own reach starts further out - not even at Disadvantage. The
# draft already describes Close as "inside the point: wrestling, daggers,
# shield rims", so this makes the Band mean what its own flavour text says.
#
# Why it is a candidate at all: on a four-Band track with symmetric slop, the
# middle class is never more than ONE Band from anywhere, so an arming weapon
# holds a kill zone against sidearms (at Far) AND against polearms (at Close)
# while neither holds one against it. That is the whole of item 19's class
# imbalance. This removes the arming weapon's half of it.
CLOSE_FLOOR = False


def band_tier(f, measure, steps=0):
    """Where this Measure sits on the weapon's curve: 'adv', 'normal',
    'disadv', or None for "cannot attack at all". See REACH_CURVE."""
    if CLOSE_FLOOR and measure == 0 and min(f.bands) > 0:
        return None
    lo, hi = min(f.bands) - steps, max(f.bands) - steps
    if REACH_CURVE == "graded":
        if measure > hi:
            return None              # nothing lengthens a stick
        if measure == hi:
            return "adv"
        if measure == lo:
            return "normal"
        if measure == lo - 1:
            return "disadv"
        return None
    d = max(0, reach(f, measure) - steps)
    if d == 0:
        return "normal"
    if d == 1 and slop(f, measure):
        return "disadv"
    return None


def band_mod(f, measure, steps=0):
    """(may attack, flat roll modifier, 'adv'/'disadv'/None).

    The single place reach turns into a number. `classic` and `graded` express
    it as Advantage/Disadvantage and a wall; `flat` expresses it as a linear
    penalty and a lockout distance. Everything downstream reads this."""
    if REACH_CURVE != "flat":
        t = band_tier(f, measure, steps)
        return (t is not None), 0, t
    if CLOSE_FLOOR and measure == 0 and min(f.bands) > 0:
        return False, 0, None
    lo, hi = min(f.bands) - steps, max(f.bands) - steps
    if measure < lo:
        d, allow = lo - measure, REACH_SLOP_IN
    elif measure > hi:
        d, allow = measure - hi, REACH_SLOP_OUT
    else:
        return True, 0, None
    if d > allow:
        return False, 0, None
    return True, -REACH_PENALTY * d, None


def can_attack(f, measure):
    return band_mod(f, measure, shorten_steps(f, measure))[0]


def is_polearm(f):
    return max(f.bands) == max(max(v) for v in WEAPON_BANDS.values())


def cycle_winner(a, da, b, db, measure):
    """'a', 'b', or None for a tie - the Cycle alone, before any shield."""
    if da == db:
        return None
    if POLEARM_EDIT != "none":
        for pole, p_d, other, o_d, tag in ((a, da, b, db, "a"), (b, db, a, da, "b")):
            if is_polearm(pole) and not is_polearm(other) \
                    and p_d == WITHDRAW and o_d == ADVANCE:
                return None if POLEARM_EDIT == "tie" else tag
    return "a" if BEATS[da] == db else "b"


def shield_saves(a, da, b, db, measure, win, stats):
    """Does a shield rescue the fighter who just lost the read?

    The draft's own frequency law - an effect that fires on EVERY exchange
    inverts, one that fires on 13% nudges - was learned from lever 1 and then
    not applied to shields, which get a Cycle edit that fires every single time
    the bearer declares Advance into a Hold. Measurement says a hand is not a
    sufficient price: +19 to +25 points, against a reach ladder worth 17. These
    modes price or ration it. Returns True if the read becomes a tie."""
    if SHIELD_MODE == "off" or win is None:
        return False
    loser, l_d, w_d = (a, da, db) if win == "b" else (b, db, da)
    if not loser.shield_live(measure):
        return False
    if SHIELD_EFFECT.get(loser.shield) != "entry":
        return False        # a 'mirror' tool does not buy entry
    if SHIELD_MODE == "save":
        # Generalised: the shield forgives ONE lost read a round, whatever the
        # declarations were. Closer to "a shield forgives you for being wrong"
        # than an edit aimed only at entry, and rationed by construction.
        applies = True
    else:
        applies = (l_d == ADVANCE and w_d == HOLD)
    if not applies:
        return False
    mode = (SHIELD_MODE.get(loser.shield, "reaction")
            if isinstance(SHIELD_MODE, dict) else SHIELD_MODE)
    if mode in ("once", "save"):
        if loser.shield_used:
            return False
        loser.shield_used = True
    elif mode == "reaction":
        if loser.reactions <= 0:
            return False
        loser.reactions -= 1
    stats["shield_saves"] += 1
    return True


def attack(att, dfn, stats, measure, disadv=False, halve=False,
           preroll=None, bonus=0, extra=False):
    stats["attacks"] += 1
    stats[f"strike_{att.name}_b{measure}"] += 1
    steps = shorten_steps(att, measure)
    if steps:
        cost = 1 if SHORTEN == "flat" else steps
        att.reactions -= cost
        stats["shortens"] += 1
        stats["shorten_reactions"] += cost
    _ok, mod, tier = band_mod(att, measure, steps)
    if preroll is None:
        nat = roll_d12(disadvantage=(tier == "disadv" or disadv),
                       advantage=(tier == "adv"))
    else:
        nat = preroll          # the Tempo contest already rolled this die
        mod = 0                # ...and already carried the reach modifier
    if nat + att.build.weapon_skill + bonus + mod < dfn.evasion:
        stats["whiff_roll"] += 1
        return
    dmg = att.build.weapon.roll_damage()
    if steps and SHORTEN == "weak":     # no leverage on a shortened blow
        dmg = min(dmg, att.build.weapon.roll_damage())
    floor = att.build.weapon.crit_floor
    if MISMATCH_NO_CRIT and mod:
        floor = 12                     # no precision from the wrong distance
    if nat >= floor or extra:
        if nat >= floor:
            stats["crit_" + att.name] += 1
        dmg = max(dmg, att.build.weapon.roll_damage())
    dmg += att.build.attribute_value()
    if halve:                          # took it on the shield, not the body
        dmg = (dmg + 1) // 2
    after = dmg - dfn.effective_ar(measure)   # AR applies, THEN degrades
    dfn.ar = max(0, dfn.ar - 1)
    # The Wound Threshold is the DEFENDER's toughness - how much damage they
    # soak per Wound - not the attacker's. combat_engine passes defender.STR
    # here; this file passed att.build.STR until 2026-08-17, which inverted the
    # stat: raising your own STR raised your own thresholds and made your hits
    # produce fewer Wounds. Invisible in the weapon matrix, where both fighters
    # are STR 3 and the two readings coincide - and the sole reason every
    # cross-build comparison showed DEX as free win rate.
    w = wounds_from_damage(after, dfn.build.STR)
    dfn.wounds += w
    stats["hits_wounding" if w else "hits_absorbed"] += 1


def oa_count(threat, old, new):
    """Crossing into a threatened zone provokes. 'once' is the draft as written;
    'perband' charges one per Band of the zone you cross."""
    if OA_MODE == "off" or new >= old:
        return 0
    if OA_MODE == "once":
        return 1 if (old not in threat.bands and new in threat.bands) else 0
    return len([x for x in range(new, old) if x in threat.bands])


def _mirror_pay(f, stats):
    """Can this fighter swing in a Mirror? Spends the Reaction if one is owed.

    Nobody won the read, so this is not a riposte - but the initiator's Major
    Action bought their blow either way, which is the same split the riposte
    rule already uses. See MIRROR_COST.
    """
    if MIRROR_COST == "free":
        return True
    if MIRROR_COST == "responder" and f.is_initiator:
        return True
    if f.reactions <= 0:
        stats["mirror_unfunded"] += 1
        return False
    f.reactions -= 1
    stats["mirror_paid"] += 1
    return True


def mirror_cover(dfn, measure, stats):
    """Does the defender's off hand cover them in this Mirror? Once a round."""
    if SHIELD_EFFECT.get(dfn.shield) != "mirror":
        return False
    if not dfn.shield_live(measure):
        return False
    if MIRROR_COVER_LIMIT == "once":
        if dfn.shield_used:
            return False
        dfn.shield_used = True
    stats["mirror_cover"] += 1
    return True


def _mirror_blow(att, dfn, stats, m, is_advance):
    """One blow inside a Mirror, with the defender's off-hand cover applied.

    Returns True if a blow was actually resolved. `instead` is the only kind
    that costs the coverer something: they parry rather than trade, so their
    own swing does not happen either - handled by the caller via covered()."""
    cov = mirror_cover(dfn, m, stats)
    k = MIRROR_COVER_KIND
    if cov and (k == "negate" or k == "instead"
                or (k == "negadv" and is_advance)):
        return False
    attack(att, dfn, stats, m,
           disadv=cov and k == "disadv",
           halve=cov and k == "half")
    return True


def _margin_exchange(a, b, da, db, win, measure, new, stats):
    """One opposed roll; its margin says what happened. See TEMPO_MODE.

    Returns the Tempo holder (entitled to a follow-up), or None.

    Displacement has already happened, unconditionally, before this is called -
    that is the guardrail. Nothing here moves anybody.
    """
    stats["margin_exchanges"] += 1
    # Lever 3c keeps its home: on an Advance/Advance collapse the longer weapon
    # is striking from the Measure it HELD, so it contests from there too.
    m = {a: new, b: new}
    if REACH_ORDER and da == db == ADVANCE and max(a.bands) != max(b.bands):
        longer = a if max(a.bands) > max(b.bands) else b
        m[longer] = measure

    bid, armed = {}, {}
    for f in (a, b):
        armed[f] = can_attack(f, m[f])
        if not armed[f] and not CONTEST_OUT_OF_REACH:
            bid[f] = None                 # cannot reach: does not even contest
            continue
        steps = shorten_steps(f, m[f])
        _ok, mod, tier = band_mod(f, m[f], steps)
        nat = roll_d12(disadvantage=(tier == "disadv" or not armed[f]),
                       advantage=(tier == "adv"))
        bonus = mod + (CYCLE_BONUS if win == ("a" if f is a else "b") else 0)
        if (da if f is a else db) == WITHDRAW:
            bonus += WITHDRAW_BONUS      # gave ground with the point on line
        bid[f] = (nat, nat + f.build.weapon_skill + bonus, bonus)

    def strike(att, dfn, free=False, extra=False):
        """One blow, reusing the die already rolled for the Tempo contest.

        `free` marks the off-balance blow - a Bind, or the loser's answer in a
        Trade. It is NOT a Disadvantage: the die is already rolled, and the
        number that lost the contest is the same number that must meet the
        target's Passive Evasion, so a losing blow is weaker by construction and
        often fails outright. `free` says only that it costs no Reaction.

        (This parameter was called `disadv` until 2026-08-19, which was a lie -
        `attack()` ignores a Disadvantage flag whenever `preroll` is set, so it
        never applied one. Every figure was taken under the behaviour described
        above; the rename makes the code say what it does.)"""
        if not armed[att]:
            stats["tempo_no_strike"] += 1   # fended him off; could not hurt him
            return False
        if RIPOSTE_COSTS_REACTION and not att.is_initiator and not free:
            if att.reactions <= 0:
                stats["riposte_unfunded"] += 1
                return False
            att.reactions -= 1
            stats["riposte_paid"] += 1
        nat, _tot, bonus = bid[att]
        attack(att, dfn, stats, m[att], preroll=nat, bonus=bonus, extra=extra)
        return True

    if not (armed[a] or armed[b]):
        stats["neither"] += 1
        stats["empty_total"] += 1
        return None
    if bid[a] is None or bid[b] is None:      # only one weapon reaches
        att, dfn = (a, b) if bid[b] is None else (b, a)
        stats["margin_uncontested"] += 1
        if not strike(att, dfn):
            stats["empty_total"] += 1
        return att

    diff = bid[a][1] - bid[b][1]
    mg = abs(diff)
    if mg <= MARGIN_BIND:
        # Nobody dictated. Both blows land, simultaneously - neither fighter is
        # ahead of the other, so there is no basis for an ordering and the first
        # one landing does not stop the second. The double hit, kept.
        stats["margin_bind"] += 1
        acted = False
        for att, dfn in ((a, b), (b, a)):
            acted |= strike(att, dfn, free=True)     # a Bind is nobody's blow
        stats["empty_total"] += (not acted)
        return None

    att, dfn = (a, b) if diff > 0 else (b, a)
    if mg <= MARGIN_TRADE:
        stats["margin_trade"] += 1
        acted = strike(att, dfn)
        if dfn.alive and att.alive:
            acted |= strike(dfn, att, free=True)     # struck back, off balance
        stats["empty_total"] += (not acted)
    elif mg >= MARGIN_DOMINANT:
        stats["margin_dominant"] += 1
        if not strike(att, dfn, extra=(DOMINANT_EFFECT == "extra")):
            stats["empty_total"] += 1
    else:
        stats["margin_clean"] += 1
        if not strike(att, dfn):
            stats["empty_total"] += 1
    return att


def _mutual_pay(f, lost, stats):
    """Can this fighter swing under MUTUAL_SWING? Spends a Reaction if owed."""
    if MUTUAL_COST == "free":
        return True
    if MUTUAL_COST == "responder" and f.is_initiator:
        return True
    if MUTUAL_COST == "loser" and not lost:
        return True
    if f.reactions <= 0:
        stats["mutual_unfunded"] += 1
        return False
    f.reactions -= 1
    stats["mutual_paid"] += 1
    return True


def _mutual(a, b, da, db, win, measure, new, stats):
    """Resolve an Exchange where the read ORDERS the blows instead of gating
    them. Returns the fighter entitled to a follow-up, or None.

    Three properties inherited unchanged from the branches this replaces:
      - lever 3c: on an Advance/Advance collapse the longer weapon lands first,
        at the Measure it HELD, not the collapsed one;
      - a Hold/Hold Mirror is strictly simultaneous - neither fighter is moving,
        so there is no basis for an ordering and both blows land even if the
        first one kills;
      - the off-hand cover (`mirror_cover`) still applies in a true Mirror.
        MIRROR_COVER_KIND='instead' is NOT modelled on this path - it is not the
        adopted setting, and "you parried instead of swinging" has no meaning
        once every swing is unconditional.
    """
    stats["mutual_exchanges"] += 1
    double = (da == db == ADVANCE)
    simultaneous = (da == db == HOLD)
    if win is None:
        stats["mirror_" + (da.lower() if da == db else "tie_shield")] += 1
        pair = [(a, b), (b, a)]
        if REACH_ORDER:
            pair.sort(key=lambda p: max(p[0].bands), reverse=True)
        if "initiative" in TURN_FIX:
            pair.sort(key=lambda p: p[0].is_initiator, reverse=True)
        lead = None
    else:
        stats["reads_won"] += 1
        att, dfn = (a, b) if win == "a" else (b, a)
        pair = [(att, dfn), (dfn, att)]
        lead = att
    acted = False
    for i, (att, dfn) in enumerate(pair):
        if not simultaneous and not (att.alive and dfn.alive):
            stats["preempted"] += 1        # put down before they could swing
            continue
        m = new
        if double and REACH_ORDER and i == 0 and max(att.bands) > max(dfn.bands):
            m = measure                    # the pike lands on the way in
        if not can_attack(att, m):
            continue
        lost = lead is not None and att is not lead
        if not _mutual_pay(att, lost, stats):
            continue
        if lost:
            stats["loser_swings"] += 1
        if win is None:
            hit = _mirror_blow(att, dfn, stats, m, double)
        else:
            attack(att, dfn, stats, m,
                   disadv=(lost and MUTUAL_SWING == "disadv"))
            hit = True
        acted = acted or hit
    stats["empty_total"] += (not acted)
    return lead


def exchange(a, b, measure, stats):
    stats["exchanges"] += 1
    if not can_attack(a, measure) and not can_attack(b, measure):
        stats["neither"] += 1
        # Dead space outward ("we are 3 hexes apart with sidearms") is just the
        # approach and costs nothing narratively. Dead space inward ("we are
        # locked together and nobody's weapon works") is the real failure.
        inward = all(measure < min(f.bands) for f in (a, b))
        stats["neither_in" if inward else "neither_out"] += 1
    if DECL_ORDER == "defender" and a.is_initiator:
        db = b.declare(measure)          # the responder's guard is visible
        da = a.declare(measure)          # the initiator commits into it
    else:
        da = a.declare(measure)
        db = b.declare(measure)
    win = cycle_winner(a, da, b, db, measure)
    if shield_saves(a, da, b, db, measure, win, stats):
        win = None
    step = {}
    for f, d in ((a, da), (b, db)):
        # The initiator is acting on their own turn and always steps. A
        # responder gets one reactive step per round and is rooted after it.
        if f.is_initiator or REACTIVE_STEP == "unlimited" or not f.stepped:
            step[f] = SHIFT[d]
            if not f.is_initiator:
                f.stepped = True
        else:
            step[f] = 0
            stats["rooted"] += 1
    if BUCKLER_MODE == "close":
        # A Buckler catches the man who backs away: Advance into a Withdraw
        # closes a Band instead of cancelling. Priced like every other shield
        # edit - one Reaction, from the same pool as everything else.
        for f, d, od in ((a, da, db), (b, db, da)):
            if (f.shield == "Buckler" and d == ADVANCE and od == WITHDRAW
                    and f.shield_live(measure) and step[f] != 0
                    and f.reactions > 0):
                f.reactions -= 1
                step[f] -= 1
                stats["buckler_closes"] += 1
    net = step[a] + step[b]
    if ADVANCE_ALWAYS_CLOSES and any(
            d == ADVANCE and step[f] != 0 for f, d in ((a, da), (b, db))):
        net = min(net, -1)             # a committed approach cannot be cancelled
    new = max(0, min(MAX_MEASURE, measure + net))

    for mover, threat, decl in ((a, b, da), (b, a, db)):
        if decl != ADVANCE or step[mover] == 0:
            continue
        if da == db and not MIRROR_PROVOKES:   # log item 24
            continue
        for _ in range(oa_count(threat, measure, new)):
            if threat.reactions <= 0:      # OAs and follow-ups share the pool
                break
            threat.reactions -= 1
            stats["oas"] += 1
            attack(threat, mover, stats, new)
    if not (a.alive and b.alive):
        return new, None

    if TEMPO_MODE == "margin":
        return new, _margin_exchange(a, b, da, db, win, measure, new, stats)

    if MUTUAL_SWING != "off":
        return new, _mutual(a, b, da, db, win, measure, new, stats)

    if da == db == ADVANCE:                  # the double hit
        stats["mirror_close"] += 1
        pair = [(a, b), (b, a)]
        if REACH_ORDER:
            pair.sort(key=lambda p: max(p[0].bands), reverse=True)
        if "initiative" in TURN_FIX:       # commitment beats length
            pair.sort(key=lambda p: p[0].is_initiator, reverse=True)
        acted = False
        covering = {f: (MIRROR_COVER_KIND == "instead"
                        and SHIELD_EFFECT.get(f.shield) == "mirror"
                        and f.shield_live(new)) for f in (a, b)}
        for i, (att, dfn) in enumerate(pair):
            if not (att.alive and dfn.alive):
                stats["preempted"] += 1     # put down before they could swing
                continue
            # The longer weapon lands on the way in, at the measure it held.
            m = new
            if REACH_ORDER and i == 0 and max(att.bands) > max(dfn.bands):
                m = measure
            if MIRROR_COVER_KIND == "instead" and covering.get(att):
                continue                  # you parried; you did not also swing
            if can_attack(att, m) and _mirror_pay(att, stats):
                _mirror_blow(att, dfn, stats, m, True)
                acted = True
        stats["empty_total"] += (not acted)
        return new, None
    if da == db == HOLD and HOLD_MIRROR == "trade":
        # Two fighters both standing their ground at a measure where both can
        # reach are hitting each other, not staring. Makes Hold an attack rather
        # than a pass - which is what lets the initiator afford it.
        stats["mirror_hold"] += 1
        # SIMULTANEOUS: neither fighter is moving, so there is no basis for an
        # ordering, and resolving them in sequence quietly hands the win to
        # whoever is checked first. Both blows land even if the first one kills.
        acted = False
        covering = {f: (MIRROR_COVER_KIND == "instead"
                        and SHIELD_EFFECT.get(f.shield) == "mirror"
                        and f.shield_live(new)) for f in (a, b)}
        for att, dfn in ((a, b), (b, a)):
            if covering.get(att):
                continue                  # you parried; you did not also swing
            if can_attack(att, new) and _mirror_pay(att, stats):
                _mirror_blow(att, dfn, stats, new, False)
                acted = True
        stats["empty_total"] += (not acted)
        return new, None
    if da == db:                           # Hold/Hold standoff, Withdraw/Withdraw reset
        stats["mirror_" + da.lower()] += 1
        stats["empty_total"] += 1
        return new, None
    if win is None:                        # shield-forced tie
        stats["tie_shield"] += 1
        stats["empty_total"] += 1
        return new, None

    att, dfn = (a, b) if win == "a" else (b, a)
    # 'consolation': the initiator who loses the read gets a Reaction back - a
    # partial refund of the Major Action they just spent on nothing. Strictly
    # weaker than granting the Reaction unconditionally, which overshoots.
    if "consolation" in TURN_FIX and dfn.is_initiator:
        dfn.reactions += 1
        stats["consolation"] += 1
    stats["reads_won"] += 1
    if RIPOSTE_COSTS_REACTION and not att.is_initiator:
        if att.reactions <= 0:          # avoided the blow, cannot afford to answer it
            stats["riposte_unfunded"] += 1
            stats["empty_total"] += 1
            return new, att
        att.reactions -= 1
        stats["riposte_paid"] += 1
    if can_attack(att, new):
        stats["read_converted"] += 1
        attack(att, dfn, stats, new)
    else:
        stats["read_wasted"] += 1          # draft open item 4
        stats["empty_total"] += 1
    return new, att


def run_fight(a, b, start_measure, stats, max_rounds=30):
    a.reset(); b.reset()
    measure = start_measure
    order = [a, b] if a.build.DEX >= b.build.DEX else [b, a]
    for rnd in range(1, max_rounds + 1):
        for actor in order:
            if not (a.alive and b.alive):
                return rnd
            a.is_initiator, b.is_initiator = (a is actor), (b is actor)
            if "reaction" in TURN_FIX:
                actor.reactions += 1       # paid for by the Major Action
            measure, winner = exchange(a, b, measure, stats)
            while winner is not None and winner.reactions > 0 and a.alive and b.alive:
                winner.reactions -= 1
                stats["followups"] += 1
                if FOLLOWUP_INITIATOR == "thrower":
                    a.is_initiator, b.is_initiator = (a is winner), (b is winner)
                measure, winner = exchange(a, b, measure, stats)
        a.reactions = reactions(a.build)
        b.reactions = reactions(b.build)
        a.shield_used = b.shield_used = False
        a.stepped = b.stepped = False
    return max_rounds


def duel(wa, wb, sa=None, sb=None, trials=8000, start=None, kwb=None, **kw):
    """Returns (A win rate, draw rate, mean rounds, stats).

    `**kw` builds A, `kwb` builds B - so a non-baseline build can be put on
    either side, which is what symmetrising a build comparison needs."""
    stats, rounds, wins, draws = Counter(), [], 0, 0
    start = MAX_MEASURE - 1 if start is None else start
    a = Fighter("A", wa, shield=sa, **kw)
    b = Fighter("B", wb, shield=sb, **(kwb or {}))
    random.seed(11)
    for _ in range(trials):
        rounds.append(run_fight(a, b, start, stats))
        if a.alive and b.alive:
            draws += 1
        elif b.wounds >= b.build.max_wounds and a.alive:
            wins += 1
    return wins / trials, draws / trials, statistics.mean(rounds), stats


def sym_duel(x, y, sa=None, sb=None, trials=8000):
    """One matchup, averaged over both turn orders. See `matrix`."""
    wa, _, ra, _ = duel(x, y, sa=sa, sb=sb, trials=trials)
    wb, db, rb, _ = duel(y, x, sa=sb, sb=sa, trials=trials)
    return (wa + 1 - wb - db) / 2, (ra + rb) / 2


def matrix(weapons, label, trials=8000):
    """Cells are SYMMETRISED - each averages both turn orders.

    `run_fight` gives the row weapon the first turn of every round. That is not
    a neutral position: the initiator cannot afford to Hold, and Hold beats
    Advance, so acting first is a liability worth 13-23 points on average and up
    to 36 in a bad matchup. Reporting the raw 'row acts first' cell therefore
    conflates weapon strength with the first-mover penalty, unevenly by
    matchup. Every attribution claim this file produced before 2026-08-17 came
    off that raw view; four of them turned out to be backwards (see the draft's
    'Correcting the instrument').

    Both views are still printed. Spread-based verdicts held up fine under the
    correction - it is per-weapon attribution that the raw view gets wrong - and
    the turn-order gap is now its own statistic rather than something hiding
    inside the cells.
    """
    raw, draws = {}, {}
    for x in weapons:
        for y in weapons:
            if x != y:
                wr, dr, _, _ = duel(x, y, trials=trials)
                raw[(x, y)], draws[(x, y)] = wr, dr
    sym = {k: (raw[k] + 1 - raw[k[::-1]] - draws[k[::-1]]) / 2 for k in raw}
    gaps = [abs(raw[k] + raw[k[::-1]] - 1) for k in raw]

    print(f"\n--- {label} ---")
    print(f"{'':<12}" + "".join(f"{c[:9]:>9}" for c in weapons) + "     field   spread")
    for rn in weapons:
        row, vals = f"{rn:<12}", []
        for cn in weapons:
            if rn == cn:
                row += f"{'-':>9}"
                continue
            row += f"{sym[(rn, cn)]:>8.0%} "
            vals.append(sym[(rn, cn)])
        print(row + f"  {statistics.mean(vals):>6.0%}  {min(vals):>3.0%}-{max(vals):<4.0%}")
    sv, rv = list(sym.values()), list(raw.values())
    print(f"  SPREAD {min(sv):.0%}-{max(sv):.0%}   (balance would be 50-50)")
    print(f"    raw first-mover view {min(rv):.0%}-{max(rv):.0%}"
          f"    turn-order gap {statistics.mean(gaps):.0%} mean, {max(gaps):.0%} max")
    return min(sv), max(sv)


def main():
    global GRADUATED, OA_MODE, BIAS
    W = ["Dagger", "Broadsword", "Longsword", "Spear", "Pike"]

    print("=" * 74)
    print(" 1. DECLARATION POLICY - the confound that dominates everything else")
    print("=" * 74)
    print(f"{'bias to preferred':<22}{'empty':>9}{'wasted':>9}{'converted':>11}{'rounds':>8}")
    for b in (0.40, 0.60, 0.75, 0.90):
        BIAS = b
        _, _, r, s = duel("Broadsword", "Broadsword", trials=10000)
        ex = s["exchanges"]
        print(f"{b:<22.2f}{s['empty_total']/ex:>8.1%}{s['read_wasted']/ex:>9.1%}"
              f"{s['read_converted']/max(1,s['reads_won']):>11.1%}{r:>8.1f}")
    BIAS = 0.75

    print("\n" + "=" * 74)
    print(" 2. THE EMPTY EXCHANGE and DEAD SPACE - draft open item 4")
    print("    'neither' = exchanges where NO fighter could act at all")
    print("=" * 74)
    print(f"{'':<46}{'neither':>9}{'empty':>8}{'rounds':>8}")
    for grad, bset, lbl in ((False, "draft4", "binary in/out, edges own 1"),
                            (True, "draft4", "graduated, edges own 1"),
                            (True, "three", "graduated, three classes")):
        GRADUATED = grad
        use_bands(bset)
        for x, y in (("Broadsword", "Broadsword"), ("Broadsword", "Pike"),
                     ("Dagger", "Pike")):
            _, _, r, s = duel(x, y)
            ex = s["exchanges"]
            print(f"{lbl + ': ' + x + ' v ' + y:<46}{s['neither']/ex:>8.1%}"
                  f"{s['empty_total']/ex:>8.1%}{r:>8.1f}")
    GRADUATED = True

    print("\n" + "=" * 74)
    print(" 3. BAND LAYOUT - identical builds, no shields; Bands are the only")
    print("    variable. N Bands supports N-1 two-Band reach classes.")
    print("=" * 74)
    for bset, lbl in (("draft4", "4 Bands, extremes own 1 (as first drafted)"),
                      ("three", "4 Bands, three reach classes (recommended)"),
                      ("six", "6 Bands, five reach classes (the alternative)")):
        use_bands(bset)
        matrix(W, lbl)
    use_bands("three")

    print("\n" + "=" * 74)
    print(" 4. OPPORTUNITY ATTACKS - they favour SHORT weapons, not reach,")
    print("    and log item 24 measured WHY: the effect is the Advance Mirror.")
    print("    Exempt Mirrors (MIRROR_PROVOKES=False) and OAs go inert - on and")
    print("    off match within a point. That reading was ruled and reverted.")
    print("=" * 74)
    global MIRROR_PROVOKES
    for mprov in (False, True):
        MIRROR_PROVOKES = mprov
        for mode in ("off", "once", "perband"):
            OA_MODE = mode
            matrix(W, f"OA mode: {mode}, Mirror provokes: {mprov}", trials=6000)
    MIRROR_PROVOKES = True     # restore the adopted setting
    OA_MODE = "once"

    print("\n" + "=" * 74)
    print(" 5. SHIELDS - is one worth a hand? The bar is a two-hander.")
    print("    Which half earns its keep: the Cycle edit, or the AR?")
    print("=" * 74)
    global SHIELD_MODE
    print(f"{'Broadsword plus':<36}{'v Greatsword':>13}{'v Longsword':>13}"
          f"{'v Spear':>10}{'rounds':>9}")
    for edit, ar, sh, lbl in (
            ("off", 1, None, "bare"),
            ("off", 1, "Heater", "flat AR only, no edit"),
            ("once", 1, "Buckler", "edit once/round, no AR (Buckler)"),
            ("once", 1, "Heater", "edit once/round + AR 1 (Heater)  ADOPTED"),
            ("reaction", 2, "Heater", "edit costs a Reaction, AR 2 - rejected"),
            ("free", 2, "Heater", "edit unpriced, AR 2 - as first drafted"),
            ("save", 1, "Heater", "edit forgives ANY read - rejected")):
        SHIELD_MODE, SHIELD_AR["Heater"] = edit, ar
        out = [sym_duel("Broadsword", o, sa=sh, trials=8000)
               for o in ("Greatsword", "Longsword", "Spear")]
        print(f"{lbl:<36}" + "".join(f"{w:>12.0%} " if i < 2 else f"{w:>9.0%} "
              for i, (w, _) in enumerate(out))
              + f"{statistics.mean([r for _, r in out]):>8.1f}")
    SHIELD_AR["Heater"] = 0
    SHIELD_MODE = "once"           # restore the adopted setting
    print("\n  Buckler works at every Band; Heater adds AR but both die at Close.")
    for a_sh, b_sh in (("Buckler", "Heater"),):
        wr, r = sym_duel("Broadsword", "Broadsword", sa=a_sh, sb=b_sh, trials=8000)
        print(f"  Broadsword+{a_sh:<8} vs Broadsword+{b_sh:<8} {wr:>6.0%}   {r:.1f} rounds")

    global REACH_ORDER, POLEARM_EDIT
    print("\n" + "=" * 74)
    print(" 6. LEVERS TRIED ON THE REACH PROBLEM")
    print("=" * 74)
    for ro, pe, lbl in ((False, "none", "neither (simultaneous double hit)"),
                        (True, "none", "3c ADOPTED: longer weapon lands on the way in"),
                        (True, "tie", "3c + lever 1 'tie'  - REJECTED"),
                        (True, "flip", "3c + lever 1 'flip' - REJECTED")):
        REACH_ORDER, POLEARM_EDIT = ro, pe
        matrix(W, lbl, trials=6000)
    REACH_ORDER, POLEARM_EDIT = True, "none"

    global RIPOSTE_COSTS_REACTION, INITIATOR_MAY_HOLD
    print("\n" + "=" * 74)
    print(" 7. WHO PAYS FOR OFFENCE - and why acting first is a liability")
    print("=" * 74)
    for rip, hold, lbl in ((False, False, "riposte free, initiator must act (first draft)"),
                           (True, False, "riposte costs a Reaction (ADOPTED)"),
                           (False, True, "initiator may Hold freely (REJECTED)"),
                           (True, True, "both (REJECTED)")):
        RIPOSTE_COSTS_REACTION, INITIATOR_MAY_HOLD = rip, hold
        print(f"\n  {lbl}")
        print(f"    {'mirror':<14}{'first':>7}{'second':>8}{'empty':>8}{'rounds':>8}")
        for w in ("Broadsword", "Longsword", "Pike"):
            wr, dr, r, s = duel(w, w, trials=8000)
            print(f"    {w:<14}{wr:>6.0%}{1-wr-dr:>8.0%}"
                  f"{s['empty_total']/s['exchanges']:>8.0%}{r:>8.1f}")
        allv = [sym_duel(x, y, trials=4000)[0] for x in W for y in W if x != y]
        print(f"    weapon spread {min(allv):.0%}-{max(allv):.0%} (symmetrised)")
    RIPOSTE_COSTS_REACTION, INITIATOR_MAY_HOLD = True, False

    print("\n" + "=" * 74)
    print(" 8. POSITION ISOLATED - every weapon re-dealt identical dice, so")
    print("    Bands become the ONLY difference between these five.")
    print("    Separates 'this weapon is badly placed' from 'this weapon rolls")
    print("    badly' - the two the field average otherwise blends together.")
    print("=" * 74)
    global WEAPONS, VERSATILE
    real, real_vers = dict(WEAPONS), dict(VERSATILE)
    WEAPONS = {k: Weapon(k, "1d8", "STR", crit_floor=12) for k in real}
    # VERSATILE must be cleared too. profile() reads a Versatile weapon's dice
    # from VERSATILE rather than from WEAPONS, so swapping WEAPONS alone leaves
    # the Longsword, Quarterstaff and Spear on their REAL dice while every other
    # weapon gets the uniform one - which is not an isolation test at all.
    # Check: with this cleared, every weapon in a reach class must return the
    # same number (Spear and Pike are the same class and the same Bands, so any
    # gap between them is instrument error, not a finding).
    VERSATILE = {}
    matrix(W, "identical 1d8/STR/no crit expansion", trials=6000)
    WEAPONS, VERSATILE = real, real_vers
    RIPOSTE_COSTS_REACTION, INITIATOR_MAY_HOLD = True, False





if __name__ == "__main__":
    main()
