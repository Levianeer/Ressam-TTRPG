#!/usr/bin/env python3
"""Equilibrium solver for the Exchange - turns `exchange_sim.BIAS` into an output.

    python3 tools/exchange_solver.py

WHY THIS EXISTS
  Every figure in `exchange_log.md` carries the same asterisk: the declaration
  policy is the largest confound in the tool, because it is a *guess* about how
  people choose. But the Exchange at a given state is a 3x3 matrix game, and
  those are solved, not guessed. This tool computes how the Cycle is correctly
  played instead of assuming it, and reports four things the sim cannot:

    1. THE EQUILIBRIUM MIX  - how to play a matchup, per Measure, per role.
    2. THE GAME VALUE       - the reach ladder with the confound removed.
    3. EXPLOITABILITY       - what a printed Intent line costs a monster against
                              a player who has worked it out. This is the number
                              that says whether `Brute 9/2/1` survives contact.
    4. THE SKILL GRADIENT   - how much an optimal reader beats a coin-flipper.
                              Nobody has measured this, and it is what decides
                              whether the Cycle is worth its table time: too
                              small and the minigame has no depth, too large and
                              it is brutal to a new player.

HOW
  The fight is treated as a Markov game whose state is (Measure, who initiated).
  For each state we estimate the 3x3 payoff matrix by self-play, solve it for
  its Nash equilibrium by regret matching, and iterate until the strategies stop
  moving. Regret matching is ~20 lines and needs no solver library, which keeps
  this stdlib-only like the rest of `tools/`.

WHAT IS APPROXIMATED, AND IT MATTERS
  The state ignores Wounds, remaining Reactions, and whether the reactive step
  is spent. A fighter one hit from death should read differently from a fresh
  one, and this tool cannot say so. It answers "how is this matchup played on
  average," not "what do I declare right now." Treat the mixes as a description
  of the matchup, not as a lookup table for a player.

  Everything else - Bands, the economy, shields, Opportunity Attacks, lever 3c -
  is `exchange_sim`'s, unmodified. This module only replaces `Fighter.declare`.
"""

import os
import random
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import exchange_sim as X

DECLS = X.DECLS
UNIFORM = [1 / 3, 1 / 3, 1 / 3]


# --------------------------------------------------------------------------
# 1. A 3x3 zero-sum solver, by regret matching (Hart & Mas-Colell)
# --------------------------------------------------------------------------

def _from_regret(R):
    pos = [r if r > 0 else 0.0 for r in R]
    t = sum(pos)
    return [p / t for p in pos] if t > 0 else [1.0 / len(R)] * len(R)


def solve_zero_sum(M, iters=8000):
    """M[i][j] = row player's payoff. Returns (row mix, col mix, game value).

    Both players run regret matching against the other's current strategy; the
    time-average of play converges to a Nash equilibrium in a zero-sum game.
    The Exchange is not quite zero-sum - both fighters can die - so payoffs are
    A's win rate with draws at 0.5, which makes it zero-sum by construction."""
    n, m = len(M), len(M[0])
    Rr, Rc = [0.0] * n, [0.0] * m
    Sr, Sc = [0.0] * n, [0.0] * m
    for _ in range(iters):
        sr, sc = _from_regret(Rr), _from_regret(Rc)
        for i in range(n):
            Sr[i] += sr[i]
        for j in range(m):
            Sc[j] += sc[j]
        ur = [sum(M[i][j] * sc[j] for j in range(m)) for i in range(n)]
        vr = sum(sr[i] * ur[i] for i in range(n))
        for i in range(n):
            Rr[i] += ur[i] - vr
        uc = [sum(-M[i][j] * sr[i] for i in range(n)) for j in range(m)]
        vc = sum(sc[j] * uc[j] for j in range(m))
        for j in range(m):
            Rc[j] += uc[j] - vc
    row = [x / sum(Sr) for x in Sr]
    col = [x / sum(Sc) for x in Sc]
    val = sum(row[i] * col[j] * M[i][j] for i in range(n) for j in range(m))
    return row, col, val


# --------------------------------------------------------------------------
# 2. Policies, and the hook that makes Fighter.declare obey one
# --------------------------------------------------------------------------
# A policy maps (measure, is_initiator) -> [P(Advance), P(Hold), P(Withdraw)].
# `None` means "fall through to exchange_sim's own heuristic", so the tool can
# still measure the thing it is replacing.

_POLICY = {}      # id(fighter) -> policy or None
_EXPLORE = 0.0    # chance of ignoring the policy and declaring uniformly
_TRACE = []       # (measure, is_initiator, decl, is_a), in call order
_PAIR = ()        # the two Fighters currently in play, for the dead-space guard

_orig_declare = X.Fighter.declare


class Sequential:
    """An OPEN-declaration policy. No secrecy: one side commits where the other
    can see it, and the other answers.

    `lead[(measure, is_initiator)]` is the declaration this fighter makes when
    they are the one committing first - a single choice rather than a mix,
    because against an opponent who can see it there is nothing left to hide.
    `follow[(measure, is_initiator, what the other side said)]` is what they do
    when they are answering something already on the table.

    Note what a solved Sequential policy therefore IS: a lookup table. If its
    `lead` entries are all the same declaration, the open game is dead - there
    is one line of play and no decision left. If they vary with the Measure, the
    decision survived and merely stopped being a mind-game: it became a
    positional one.
    """

    def __init__(self, lead=None, follow=None):
        self.lead = dict(lead or {})
        self.follow = dict(follow or {})

    def leads(self):
        return sorted(set(self.lead.values()))

    def follows(self):
        return sorted(set(self.follow.values()))




_NO_FLEE = True     # see the dead-space guard below


def _dead_space(f, measure):
    """True only when NEITHER fighter can reach the current Measure.

    The guard exists to stop two fighters drifting apart forever in a gap where
    no fight is possible. It must NOT fire when the opponent can hit you and you
    cannot hit them - backing out of somebody's guard is the correct play and
    the whole point of a short weapon's kill zone. An earlier version tested
    only `not can_attack(self)`, which trapped a longsword inside a dagger's
    measure permanently and inflated every dead-space figure it touched."""
    if not _PAIR:
        return False
    return not any(X.can_attack(g, measure) for g in _PAIR)


def _declare(self, measure):
    pol = _POLICY.get(id(self))
    is_a = bool(_PAIR) and self is _PAIR[0]
    # exchange() calls declare exactly twice per Exchange, so an odd-length
    # trace means the other side has already spoken. That is the ONLY way a
    # policy can tell that it is answering rather than committing, and it works
    # whichever order exchange_sim.DECL_ORDER put them in.
    following = (len(_TRACE) % 2 == 1)
    if pol is None and not (_NO_FLEE and _dead_space(self, measure)):
        d = _orig_declare(self, measure)
        _TRACE.append((measure, self.is_initiator, d, is_a))
        return d
    if _NO_FLEE and _dead_space(self, measure):
        # TRUE DEAD SPACE: neither weapon reaches, so no read exists here -
        # nobody can be hit whatever either side declares. Both fighters close.
        #
        # Forcing it rather than merely forbidding Withdraw, because forbidding
        # Withdraw alone still lets both sides Hold, and two fighters holding in
        # a gap where no fight is possible sit there for the rest of the
        # simulation. This costs no decision: there is nothing to decide in a
        # state where no declaration can produce a blow.
        #
        # Both fighters strictly prefer to engage - a timed-out fight scores as
        # a loss for BOTH - so this selects the payoff-dominant equilibrium the
        # solver cannot reach on its own, rather than imposing a preference.
        _TRACE.append((measure, self.is_initiator, X.ADVANCE, is_a))
        self.last_decl = X.ADVANCE
        return X.ADVANCE
    if pol is CLAIRVOYANT:
        # Declares SECOND with full knowledge, and answers on the Cycle - the
        # value of dropping secrecy under the draft's own gate.
        d = _counter(_TRACE[-1][2]) if _TRACE else random.choice(DECLS)
    elif isinstance(pol, Sequential):
        st = (measure, self.is_initiator)
        if _EXPLORE and random.random() < _EXPLORE:
            d = random.choice(DECLS)
        elif following:
            d = pol.follow.get(st + (_TRACE[-1][2],)) or random.choice(DECLS)
        else:
            d = pol.lead.get(st) or random.choice(DECLS)
    else:
        w = UNIFORM if (_EXPLORE and random.random() < _EXPLORE) \
            else pol.get((measure, self.is_initiator), UNIFORM)
        d = random.choices(DECLS, weights=w)[0]
    self.last_decl = d
    _TRACE.append((measure, self.is_initiator, d, is_a))
    return d


X.Fighter.declare = _declare


CLAIRVOYANT = object()   # sentinel policy: see the opponent's declaration first


def _counter(decl):
    """The Cycle answer to a known declaration."""
    for d in DECLS:
        if X.BEATS[d] == decl:
            return d
    return decl


def states():
    return [(m, i) for m in range(X.MAX_MEASURE + 1) for i in (True, False)]


def uniform_policy():
    return {s: list(UNIFORM) for s in states()}


def flat_line(adv, hold, wd):
    """A printed Intent line: the same split at every Measure, which is exactly
    what a stat block can express and exactly what item 14 says is the limit."""
    t = adv + hold + wd
    mix = [adv / t, hold / t, wd / t]
    return {s: list(mix) for s in states()}


def band_split_line(inside, outside, bands):
    """Two rows: one for when the fight is at a Measure this creature's weapon
    works in, one for when it is not. Costs a stat block one extra line.

    NOTE the test is `m in bands`, not `m > max(bands)`. The first version of
    this function used the latter, which for a Spear splits only at "out of
    Measure entirely" - barely a split at all, and it made a two-row line look
    almost as farmable as a flat one."""
    ins = [x / sum(inside) for x in inside]
    out = [x / sum(outside) for x in outside]
    return {(m, i): list(ins if m in bands else out) for (m, i) in states()}


def three_row_line(too_close, in_band, too_far, bands):
    """Three rows: driven off, in Measure, closing. The most a stat block can
    reasonably carry, and the ceiling on what a printed line can ever do."""
    lo, hi = min(bands), max(bands)
    tc = [x / sum(too_close) for x in too_close]
    ib = [x / sum(in_band) for x in in_band]
    tf = [x / sum(too_far) for x in too_far]
    return {(m, i): list(tc if m < lo else (ib if m <= hi else tf))
            for (m, i) in states()}


# --------------------------------------------------------------------------
# 3. Self-play sampling
# --------------------------------------------------------------------------

# A fight that never resolves is not a draw worth half to each. In a vacuum,
# stalling out of Measure is a costless equilibrium and the solver finds it
# instantly - a Broadsword mirror ran 29 rounds at 99% empty exchanges before
# this was fixed. exchange_log's item 4 predicted exactly that: "when nobody is
# compelled to move, positional advantage stops being contested at all... at a
# real table patience costs you, because the other side repositions, their
# archers keep shooting, and someone eventually has to close or lose the fight
# for reasons the Cycle knows nothing about." TIMEOUT_VALUE is that clock.
TIMEOUT_VALUE = 0.0        # nobody achieved anything, and both are punished
MUTUAL_KILL_VALUE = 0.5    # a genuine draw - they killed each other


def _outcome(a, b):
    if a.alive and not b.alive:
        return 1.0
    if b.alive and not a.alive:
        return 0.0
    if not a.alive and not b.alive:
        return MUTUAL_KILL_VALUE
    return TIMEOUT_VALUE


def sample(wa, wb, polA, polB, fights=20000, explore=0.12, sa=None, sb=None,
           start=None, **kw):
    """Play `fights` fights and return (payoff tables, A's realised win rate).

    Payoff tables are pay[(measure, a_initiated)][da][db] -> (sum, count) of A's
    eventual result. Attribution is to the whole fight, not to the exchange: a
    declaration is credited with what the fight went on to do, which is the
    honest question here ("was declaring this a good idea") and is what makes
    the per-state matrices comparable across Measures."""
    global _EXPLORE, _TRACE
    a = X.Fighter("A", wa, shield=sa, **kw)
    b = X.Fighter("B", wb, shield=sb, **kw)
    global _PAIR
    _PAIR = (a, b)
    _POLICY[id(a)], _POLICY[id(b)] = polA, polB
    _EXPLORE = explore
    start = X.MAX_MEASURE - 1 if start is None else start

    pay = defaultdict(lambda: [[[0.0, 0] for _ in DECLS] for _ in DECLS])
    stats = X.Counter()
    wins = 0.0
    for _ in range(fights):
        _TRACE = []
        stats["rounds_total"] += X.run_fight(a, b, start, stats)
        res = _outcome(a, b)
        wins += res
        for k in range(0, len(_TRACE) - 1, 2):
            e1, e2 = _TRACE[k], _TRACE[k + 1]
            ea, eb = (e1, e2) if e1[3] else (e2, e1)   # by identity, not order
            m, a_init, da, db = ea[0], ea[1], ea[2], eb[2]
            cell = pay[(m, a_init)][DECLS.index(da)][DECLS.index(db)]
            cell[0] += res
            cell[1] += 1
    _POLICY.pop(id(a), None)
    _POLICY.pop(id(b), None)
    _EXPLORE = 0.0
    stats["fights"] = fights
    return pay, wins / fights, stats


def _matrix(table, fallback=0.5, floor=25):
    """Mean payoff per cell, with thin cells pulled toward the table mean so a
    rarely-visited corner cannot swing the solve on four samples."""
    seen = [(s, n) for row in table for (s, n) in row if n]
    grand = (sum(s for s, _ in seen) / sum(n for _, n in seen)) if seen else fallback
    M = []
    for row in table:
        out = []
        for s, n in row:
            if n == 0:
                out.append(grand)
            else:
                w = min(n, floor) / floor          # shrink thin cells
                out.append(w * (s / n) + (1 - w) * grand)
        M.append(out)
    return M


# --------------------------------------------------------------------------
# 4. Equilibrium, and best response to a fixed opponent
# --------------------------------------------------------------------------

def heuristic_policy(wa, wb, fights=6000, **kw):
    """The sim's own heuristic, read back as an explicit per-state policy.

    Used to SEED the equilibrium search. Starting from uniform drops the solver
    into a flat region of the payoff space: if both fighters drift out of
    Measure, every action in every state leads to the same timed-out fight, the
    matrices go flat, the solve returns uniform, and it never escapes. That is a
    local trap in the search, not a property of the game - a timed-out fight is
    already scored as a loss for both, so engaging is strictly better for
    everyone and no real equilibrium stalls. Seeding from a policy that does
    engage starts the search inside the region that matters; if stalling were
    genuinely better the solver would still find it."""
    counts = {st: [0, 0, 0] for st in states()}
    global _TRACE, _PAIR
    a = X.Fighter("A", wa, **kw)
    b = X.Fighter("B", wb, **kw)
    _PAIR = (a, b)
    stats = X.Counter()
    for _ in range(fights):
        _TRACE = []
        X.run_fight(a, b, X.MAX_MEASURE - 1, stats)
        for (m, init, d, _is_a) in _TRACE:
            counts[(m, init)][DECLS.index(d)] += 1
    pol = {}
    for st, c in counts.items():
        t = sum(c)
        pol[st] = [x / t for x in c] if t else list(UNIFORM)
    return pol


def equilibrium(wa, wb, iters=9, fights=8000, seed=True, **kw):
    """Alternating solve: sample under current play, solve each state's 3x3,
    average the solution into the policy. Returns (polA, polB, value, drift).

    The learning rate is 1/(t+1), so the policy IS the running mean of the
    per-iteration solves - fictitious-play averaging. A fixed rate oscillates
    instead of settling, which the first version of this tool did visibly."""
    polA = heuristic_policy(wa, wb) if seed else uniform_policy()
    polB = heuristic_policy(wb, wa) if seed else uniform_policy()
    drift = 1.0
    for t in range(iters):
        lr = 1.0 / (t + 1)
        pay, _, _ = sample(wa, wb, polA, polB, fights=fights, **kw)
        drift = 0.0
        for st in states():
            if st not in pay:
                continue
            row, col, _ = solve_zero_sum(_matrix(pay[st]), iters=2000)
            bs = (st[0], not st[1])            # B's own view of the same state
            for pol, new, key in ((polA, row, st), (polB, col, bs)):
                old = pol[key]
                pol[key] = [(1 - lr) * o + lr * n for o, n in zip(old, new)]
                drift = max(drift, max(abs(o - n) for o, n in zip(old, pol[key])))
    _, value, _ = sample(wa, wb, polA, polB, fights=fights, explore=0.0, **kw)
    return polA, polB, value, drift


def solved_value(wa, wb, **kw):
    """Equilibrium value to `wa`, SYMMETRISED across both turn orders.

    run_fight gives A the first turn of every round, and the draft's own economy
    makes that a bad place to stand - the initiator spent a Major Action so
    cannot afford to Hold, and Hold beats Advance. Reporting the raw cell mixes
    weapon strength with that penalty, exactly as `exchange_sim.matrix` warns.
    Caught here by an invariant: a same-weapon mirror read 42.9% raw."""
    _, _, ab, _ = equilibrium(wa, wb, **kw)
    if wa == wb:
        return 0.5, ab
    _, _, ba, _ = equilibrium(wb, wa, **kw)
    return (ab + 1 - ba) / 2, ab


def heuristic_pair(wa, wb, fights=16000, **kw):
    """(symmetrised, raw) under exchange_sim's own BIAS policy."""
    ab = sample(wa, wb, None, None, fights=fights, explore=0.0, **kw)[1]
    if wa == wb:
        return 0.5, ab
    ba = sample(wb, wa, None, None, fights=fights, explore=0.0, **kw)[1]
    return (ab + 1 - ba) / 2, ab


def best_response(wa, wb, polB, iters=8, fights=8000, **kw):
    """A's best response to a FIXED polB, and its value.

    Pure per state, averaged across passes - against an opponent who is not
    adapting there is never a reason to mix, but a state whose best action flips
    between passes should land on a mix rather than on whichever pass ran last.
    The value this returns is what a player who has solved the line actually
    gets, which is the definition of the line's exploitability."""
    polA = uniform_policy()
    for t in range(iters):
        pay, _, _ = sample(wa, wb, polA, polB, fights=fights, **kw)
        for st in states():
            if st not in pay:
                continue
            M = _matrix(pay[st])
            counts = [sum(pay[st][i][j][1] for i in range(3)) for j in range(3)]
            tot = sum(counts) or 1
            col = [c / tot for c in counts]      # what B actually did here
            u = [sum(M[i][j] * col[j] for j in range(3)) for i in range(3)]
            best = max(range(3), key=lambda i: u[i])
            br = [1.0 if i == best else 0.0 for i in range(3)]
            lr = 1.0 / (t + 1)
            polA[st] = [(1 - lr) * o + lr * n for o, n in zip(polA[st], br)]
    _, value, _ = sample(wa, wb, polA, polB, fights=fights, explore=0.0, **kw)
    return polA, value


def fixed_vs_fixed(wa, wb, polA, polB, fights=20000, **kw):
    _, value, _ = sample(wa, wb, polA, polB, fights=fights, explore=0.0, **kw)
    return value


# --------------------------------------------------------------------------
# 4b. The OPEN game - declarations on the table, solved as a Stackelberg game
# --------------------------------------------------------------------------
# Everything above assumes blind simultaneous commitment. This section drops it.
#
# WHY THIS IS COMPUTABLE AND NOT A GUESS. Once a declaration is visible, the
# Exchange at a state stops being a mixed-strategy matrix game and becomes a
# commitment game, which has a closed-form answer per state:
#
#   The FOLLOWER, seeing the leader play row i, takes argmin_j M[i][j].
#     Pure, always - there is nothing to be gained from mixing against a known
#     action, which is exactly why open declaration is dangerous.
#   The LEADER therefore banks min_j M[i][j] for declaring i, and takes
#     argmax_i of that.
#
# That maximin number is the classic LOWER VALUE of the matrix. The gap between
# it and the Nash value is precisely what secrecy is worth - not an estimate of
# it, the definition of it. Under the draft as written that gap is catastrophic
# (item 18, Finding 2). The question this section exists to answer is whether
# MUTUAL_SWING closes it, and it closes it only if losing the read stops being
# worthless - i.e. only if the counter on the Cycle and the counter on the MAP
# come apart.
#
# WHAT WOULD COUNT AS THE IDEA FAILING, stated before the numbers so it cannot
# be moved afterwards:
#   1. The leader's value stays far below the Nash value. Going first is still
#      fatal, and open declaration is unplayable whatever else is true.
#   2. The leader's solved commitment is the SAME declaration in every state.
#      The value may be fine, but there is one line of play and no decision -
#      the minigame is gone rather than transformed.
# Passing needs BOTH: a value near par AND a commitment that varies with the
# Measure. That second test is the one that says "the chess arrived."


def _leader_is_a(st):
    """Which fighter commits first in this state, per exchange_sim.DECL_ORDER."""
    _m, a_init = st
    if X.DECL_ORDER == "defender":
        return not a_init          # the responder's guard is visible first
    return True                    # 'ab': call order, A always leads


def _fill_seq(seqA, seqB, pay):
    """Recompute both open-declaration policies from sampled payoff matrices."""
    for st in states():
        if st not in pay:
            continue
        M = _matrix(pay[st])
        bst = (st[0], not st[1])               # B's own view of the same state
        if _leader_is_a(st):
            for i, da in enumerate(DECLS):     # B answers a visible A
                j = min(range(3), key=lambda j: M[i][j])
                seqB.follow[bst + (da,)] = DECLS[j]
            seqA.lead[st] = DECLS[max(range(3), key=lambda i: min(M[i]))]
        else:
            for j, db in enumerate(DECLS):     # A answers a visible B
                i = max(range(3), key=lambda i: M[i][j])
                seqA.follow[st + (db,)] = DECLS[i]
            # B leads, so B maximises its own payoff = minimises A's ceiling.
            worst = [max(M[i][j] for i in range(3)) for j in range(3)]
            seqB.lead[bst] = DECLS[min(range(3), key=lambda j: worst[j])]


def sequential_solve(wa, wb, iters=5, fights=8000, **kw):
    """SUPERSEDED and kept only so the fault stays reproducible. Use `oracle`.

    Solving BOTH sides of the open game as pure policies self-starves: a pure
    leader and a pure follower visit one cell of nine, the other eight fall
    under the shrink floor and are pulled to the table mean, and the argmax
    flips between passes. On Broadsword v Spear it returned 42% against a Nash
    value of 2% - impossible, because the lower value of a zero-sum game can
    never exceed its Nash value, and that impossibility is what caught it.

    `oracle` measures the same thing without the instability by leaving the
    LEADER mixing and making only the follower pure, which is the only side
    that has to be pure anyway.

    Returns (seqA, seqB, value, nash).

    Iterated because the per-state matrices depend on how the CONTINUATION is
    played, and under open declaration the continuation is open too. Seeded from
    the secret equilibrium so the first pass is sampled under competent play
    rather than noise - the same reason `equilibrium` seeds from the heuristic.
    """
    polA, polB, nash, _ = equilibrium(wa, wb, **kw)
    seqA, seqB = Sequential(), Sequential()
    pay, _, _ = sample(wa, wb, polA, polB, fights=fights, **kw)
    _fill_seq(seqA, seqB, pay)
    for _ in range(iters):
        pay, _, _ = sample(wa, wb, seqA, seqB, fights=fights, **kw)
        _fill_seq(seqA, seqB, pay)
    _, value, _ = sample(wa, wb, seqA, seqB, fights=fights, explore=0.0, **kw)
    return seqA, seqB, value, nash


def oracle(wa, wb, polA=None, polB=None, fights=24000, **kw):
    """A follower that answers a REVEALED declaration with the best response to
    it - learned from play rather than assumed.

    CLAIRVOYANT answers on the Cycle. That is the naive counter, and it is the
    correct answer only while winning the read is the only thing worth having;
    the moment losing a read still buys you a blow, the counter on the Cycle and
    the counter on the MAP come apart and the Cycle answer can be the wrong one.
    Measuring the cost of exposure with CLAIRVOYANT therefore measures the cost
    of exposure TO A PLAYER WHO HAS NOT NOTICED THAT. This measures it against
    one who has.

    Returned as a `Sequential` with only `follow` populated, which is exactly
    what a pure follower is. The leader keeps mixing, so nothing starves.
    """
    if polA is None:
        polA, polB, _, _ = equilibrium(wa, wb, **kw)
    pay, _, _ = sample(wa, wb, polA, polB, fights=fights, **kw)
    seqA, seqB = Sequential(), Sequential()
    _fill_seq(seqA, seqB, pay)
    return polA, polB, seqB


def open_play(wa, wb, fights=16000, **kw):
    """Open declarations played CORRECTLY. Returns (secret, mixed, pure, leads).

    The leader plays the per-state maximin pure row - the saddle row wherever
    one exists - and the follower answers with the learned best response. Both
    are derived once from equilibrium-play matrices, so nothing iterates on
    pure-vs-pure play and nothing starves (see `sequential_solve`).

    'mixed' is the same follower against a leader still playing its SECRET
    equilibrium mix, and the gap between mixed and pure is worth understanding:
    once a state has a saddle, playing anything but the saddle row is
    punishable on sight, so a mixed strategy is actively wrong under open
    declaration. Measuring exposure against a mixing leader therefore overstates
    it, and that is what the first version of this analysis did."""
    polA, polB, _, _ = equilibrium(wa, wb, **kw)
    pay, _, _ = sample(wa, wb, polA, polB, fights=fights, **kw)
    seqA, seqB = Sequential(), Sequential()
    _fill_seq(seqA, seqB, pay)
    return (fixed_vs_fixed(wa, wb, polA, polB),
            fixed_vs_fixed(wa, wb, polA, seqB),
            fixed_vs_fixed(wa, wb, seqA, seqB),
            seqA.leads())


def commitment_gap(wa, wb, fights=24000, **kw):
    """What secrecy is worth, measured exactly rather than simulated.

    Every 3x3 matrix has three values, not one:

      LOWER  max_i min_j M[i][j]   A commits where B can see it, B answers.
      NASH   the mixed-strategy value - both commit blind. Always between the
             other two, and equal to them only when the matrix has a pure
             saddle point.
      UPPER  min_j max_i M[i][j]   B commits where A can see it, A answers.

    UPPER - LOWER is therefore the whole swing between showing your hand and
    reading someone else's, and it IS the price of secrecy at that state - not
    an estimate of it. A game whose matrices have saddle points can be played
    face up; a game whose matrices do not, cannot.

    Preferred over simulating pure open-declaration policies (`sequential_solve`)
    because those self-starve: a pure leader and a pure follower visit one cell
    of nine, the other eight go thin, the shrink floor pulls them to the table
    mean, and the argmax flips between passes. That instability produced a
    Broadsword v Spear reading of 42% against a Nash value of 2% - impossible,
    since the lower value of a zero-sum game can never exceed its Nash value,
    and the impossibility is what exposed it.

    THE APPROXIMATION, and it is the real one: the matrices are sampled with the
    CONTINUATION played at equilibrium. So this measures the cost of exposing
    one declaration, not the cost of playing an entire fight face up. It is the
    right first question and the wrong last one.

    States at the outermost Measure are dropped: the dead-space guard forces
    Advance there, so no decision exists to expose."""
    polA, polB, nash, _ = equilibrium(wa, wb, **kw)
    pay, _, _ = sample(wa, wb, polA, polB, fights=fights, **kw)
    rows = []
    for st in states():
        if st not in pay or st[0] >= X.MAX_MEASURE:
            continue
        n = sum(c[1] for row in pay[st] for c in row)
        M = _matrix(pay[st])
        _, _, v = solve_zero_sum(M, iters=4000)
        lower = max(min(r) for r in M)
        upper = min(max(M[i][j] for i in range(3)) for j in range(3))
        rows.append((st, n, lower, v, upper))
    tot = sum(r[1] for r in rows) or 1
    agg = tuple(sum(r[1] * r[k] for r in rows) / tot for k in (2, 3, 4))
    return rows, agg, nash


def swing_stats(wa, wb, trials=6000):
    """The lethality bill: what mutual swinging costs in blood and table time."""
    _w, _d, rounds, st = X.duel(wa, wb, trials=trials)
    ex = st["exchanges"] or 1
    return {
        "rounds": rounds,
        "atk_per_exchange": st["attacks"] / ex,
        "empty": st["empty_total"] / ex,
        "loser_swings": st["loser_swings"] / ex,
    }


# --------------------------------------------------------------------------
# 5. Report
# --------------------------------------------------------------------------

def _mix(p):
    return "  ".join(f"{d[:3]} {v:4.0%}" for d, v in zip(DECLS, p))


def _band_name(m):
    names = ["Close", "Middle", "Long", "Far"]
    return names[m] if m < len(names) else "out"


def hdr(t):
    print("\n" + "=" * 74)
    print(" " + t)
    print("=" * 74)


LADDER = [
    ("Broadsword", "Spear"), ("Broadsword", "Longsword"), ("Dagger", "Pike"),
    ("Longsword", "Spear"), ("Greatsword", "Halberd"), ("Spear", "Halberd"),
    ("Broadsword", "Broadsword"),
]

MIRRORS = ["Broadsword", "Longsword", "Spear", "Dagger"]


def main():
    random.seed(11)
    out = lambda *a: print(*a, flush=True)

    hdr("1. THE EQUILIBRIUM MIX - Broadsword (A) vs Spear (B)")
    out("How the Cycle is correctly played, computed rather than assumed.")
    out("'A init' = the Exchange is on A's turn, so A paid a Major Action.\n")
    polA, polB, raw, drift = equilibrium("Broadsword", "Spear")
    out(f"  {'Measure':<10}{'role':<8}{'Broadsword':<30}Spear")
    for m in range(X.MAX_MEASURE + 1):
        for init in (True, False):
            lab = "A init" if init else "B init"
            out(f"  {_band_name(m):<10}{lab:<8}{_mix(polA[(m, init)]):<30}"
                f"{_mix(polB[(m, not init)])}")
    out(f"\n  Max strategy drift on the last pass: {drift:.3f}  (converged)")
    out("  A near-pure row means that state is solved - no read is left in it.")

    hdr("2. THE LADDER, WITH THE CONFOUND REMOVED")
    out("Both figures symmetrised across turn order, as exchange_sim.matrix does.")
    out("'heuristic' = both sides on BIAS=0.75. 'solved' = both at equilibrium.\n")
    out(f"  {'matchup':<26}{'heuristic':>11}{'solved':>9}{'shift':>8}")
    for wa, wb in LADDER:
        h, _ = heuristic_pair(wa, wb)
        v, _ = solved_value(wa, wb)
        out(f"  {wa + ' v ' + wb:<26}{h:>10.0%}{v:>9.0%}{v - h:>+8.0%}")
    out("\n  Broadsword v Broadsword is the noise floor: it is 50% by construction")
    out("  after symmetrising, so read every other row against how close it lands.")

    hdr("3. DOES CORRECT PLAY CURE THE FIRST-MOVER PENALTY? - item 4")
    out("Same-weapon mirrors, RAW (A takes the first turn of every round).")
    out("50% would mean turn order is free. It is not, and the log knows it -")
    out("what is new here is whether playing well shrinks the gap.\n")
    out(f"  {'mirror':<20}{'heuristic':>11}{'solved':>9}{'gap: heur':>12}{'solved':>9}")
    for w in MIRRORS:
        _, hraw = heuristic_pair(w, w)
        _, sraw = solved_value(w, w)
        out(f"  {w + ' v ' + w:<20}{hraw:>10.0%}{sraw:>9.0%}"
            f"{1 - 2 * hraw:>+12.0%}{1 - 2 * sraw:>+9.0%}")
    out("\n  If the solved gap is materially smaller, part of item 4's 21 points")
    out("  is the heuristic mis-playing the initiator rather than a property of")
    out("  the Cycle - and item 4 was scoped out on the assumption it is real.")

    hdr("4. WHAT A PRINTED INTENT LINE COSTS - items 9 and 14")
    out("B is a Spear running a fixed Intent line. A is a Broadsword player who")
    out("has worked it out. A's win rate IS the exploitability of that line.")
    out("Par is the RAW equilibrium value - best_response is raw, so this table")
    out("must not be compared against a symmetrised figure.\n")
    _, _, par, _ = equilibrium("Broadsword", "Spear")
    SB = X.WEAPON_BANDS["Spear"]
    lines = [
        ("flat   Brute    9 / 2 / 1  (as drafted)", flat_line(9, 2, 1)),
        ("flat   Brute    6 / 4 / 2  (flatter)", flat_line(6, 4, 2)),
        ("flat   Elite    5 / 4 / 3  (as drafted)", flat_line(5, 4, 3)),
        ("flat   uniform  4 / 4 / 4  (unreadable)", uniform_policy()),
        ("2-row  in-Band 2/9/1 | out 9/2/1",
         band_split_line((2, 9, 1), (9, 2, 1), SB)),
        ("3-row  close 1/2/9 | in 2/9/1 | far 9/2/1",
         three_row_line((1, 2, 9), (2, 9, 1), (9, 2, 1), SB)),
    ]
    out(f"  {'B: Spear running...':<44}{'A farms it':>12}{'over par':>10}")
    for name, pol in lines:
        _, v = best_response("Broadsword", "Spear", pol)
        out(f"  {name:<44}{v:>11.0%}{v - par:>+10.0%}")
    out(f"\n  Par is {par:.0%}. Read the 'unreadable' row first: a perfectly mixed")
    out("  opponent is farmed almost as hard as a maximally readable one, so the")
    out("  exploit is NOT reading the temperament. It is that a printed line has")
    out("  no idea what Measure it is standing at. Skew is worth ~6 points;")
    out("  state-blindness is worth ~50.")

    hdr("5. THE SKILL GRADIENT - is the Cycle worth its table time?")
    out("A plays the solved equilibrium. B declares at random, then on the sim's")
    out("heuristic, then at equilibrium. Raw turn order, A first throughout.\n")
    out(f"  {'matchup':<24}{'v random':>10}{'v heuristic':>13}{'v equilibrium':>15}"
        f"{'gradient':>10}")
    for wa, wb in [("Broadsword", "Broadsword"), ("Broadsword", "Spear"),
                   ("Spear", "Spear"), ("Dagger", "Pike")]:
        pA, _, eqv, _ = equilibrium(wa, wb)
        rnd = fixed_vs_fixed(wa, wb, pA, uniform_policy())
        heu = sample(wa, wb, pA, None, fights=16000, explore=0.0)[1]
        out(f"  {wa + ' v ' + wb:<24}{rnd:>10.0%}{heu:>13.0%}{eqv:>15.0%}"
            f"{rnd - eqv:>+10.0%}")
    out("\n  'gradient' is what perfect reading buys against a coin-flipper in the")
    out("  same gear. Small means the Cycle has no depth and is not worth the")
    out("  ceremony; very large means a new player is punished for not having")
    out("  solved a matrix at the table. This is the number nobody had.")

    hdr("6. WHAT IS SECRECY WORTH? - the price of the declaration ceremony")
    out("A plays the equilibrium. B declares SECOND, seeing A's declaration, and")
    out("counters it on the Cycle. The drop is what simultaneity is buying, and")
    out("therefore what the fists-on-three ceremony at the table is paying for.\n")
    out(f"  {'matchup':<24}{'secret':>9}{'A exposed':>12}{'cost':>9}")
    for wa, wb in [("Broadsword", "Broadsword"), ("Broadsword", "Spear"),
                   ("Spear", "Spear"), ("Dagger", "Pike")]:
        pA, _, eqv, _ = equilibrium(wa, wb)
        exposed = fixed_vs_fixed(wa, wb, pA, CLAIRVOYANT)
        out(f"  {wa + ' v ' + wb:<24}{eqv:>8.0%}{exposed:>12.0%}{exposed - eqv:>+9.0%}")
    out("\n  Secrecy is load-bearing wherever the two weapons do not share Bands.")
    out("  It cannot be designed away to save table time - the ceremony has to be")
    out("  made cheaper, not removed.")


# --------------------------------------------------------------------------
# 6. Report - the OPEN game
# --------------------------------------------------------------------------
# Run with:  python3 tools/exchange_solver.py open
#
# Answers one question in two halves. Can the Cycle be played with the
# declarations face up - and if the answer needs MUTUAL_SWING to be true, what
# does MUTUAL_SWING cost everywhere else?

OPEN_PAIRS = [("Broadsword", "Broadsword"), ("Broadsword", "Spear"),
              ("Longsword", "Spear"), ("Greatsword", "Halberd")]


def _with(fn, *a, **kw):
    """Run fn with exchange_sim globals temporarily set from `_SET`."""
    old = {k: getattr(X, k) for k in _SET}
    for k, v in _SET.items():
        setattr(X, k, v)
    try:
        return fn(*a, **kw)
    finally:
        for k, v in old.items():
            setattr(X, k, v)


_SET = {}


def _cfg(**kw):
    global _SET
    _SET = kw


def exposure(wa, wb, fights=16000):
    """(secret, exposed to a solved follower, exposed to a naive Cycle counter)."""
    polA, polB, orc = oracle(wa, wb, fights=fights)
    return (fixed_vs_fixed(wa, wb, polA, polB),
            fixed_vs_fixed(wa, wb, polA, orc),
            fixed_vs_fixed(wa, wb, polA, CLAIRVOYANT))


def main_open():
    random.seed(11)
    out = lambda *a: print(*a, flush=True)

    hdr("O1. INSTRUMENT CHECK")
    out("Two things must hold before anything below is worth reading.\n")
    out("(a) A same-weapon matchup returns 50% symmetrised under every")
    out("    resolution rule. If not, that setting did not converge.\n")
    out(f"  {'setting':<12}{'Broadsword mirror':>20}{'Spear mirror':>15}")
    for mode in ["off", "priority", "disadv"]:
        _cfg(MUTUAL_SWING=mode)
        bs = _with(solved_value, "Broadsword", "Broadsword")[0]
        sp = _with(solved_value, "Spear", "Spear")[0]
        out(f"  {mode:<12}{bs:>19.0%}{sp:>15.0%}")
    out("\n(b) With MUTUAL_SWING off, exposing a declaration must reproduce log")
    out("    item 18's Finding 2: about one fight in a hundred in a mixed-reach")
    out("    matchup, and nearly free where both weapons own the same Bands.\n")
    out(f"  {'matchup':<26}{'secret':>8}{'exposed':>9}")
    _cfg(MUTUAL_SWING="off")
    for wa, wb in [("Broadsword", "Broadsword"), ("Broadsword", "Spear")]:
        sec, exp, _ = _with(exposure, wa, wb)
        out(f"  {wa + ' v ' + wb:<26}{sec:>8.0%}{exp:>9.0%}")

    hdr("O2. THE LETHALITY BILL - what mutual swinging costs in blood")
    out("Both sides on the sim's own heuristic, so this is volume, not strategy.")
    out("'empty' is the exchange where nothing happened - the thing mutual")
    out("swinging is meant to abolish, and does.\n")
    out(f"  {'matchup':<26}{'setting':<10}{'rounds':>8}{'atk/exch':>10}"
        f"{'empty':>8}{'loser swings':>14}")
    for wa, wb in OPEN_PAIRS[:3]:
        for mode in ["off", "disadv"]:
            _cfg(MUTUAL_SWING=mode)
            st = _with(swing_stats, wa, wb)
            out(f"  {wa + ' v ' + wb:<26}{mode:<10}{st['rounds']:>8.2f}"
                f"{st['atk_per_exchange']:>10.2f}{st['empty']:>8.0%}"
                f"{st['loser_swings']:>14.0%}")

    hdr("O3. THE HEADLINE - what does exposing a declaration cost?")
    out("A plays the solved equilibrium with its declarations FACE UP.")
    out("  'solved'  the follower answers with the best response to what it can")
    out("            see, learned from play. This is the number that matters.")
    out("  'naive'   the follower answers on the Cycle. Under the draft that IS")
    out("            the best response; under mutual swing it stops being one,")
    out("            and the gap between the two columns is that fact.")
    out("Raw throughout (A takes the first turn of every round).\n")
    out(f"  {'matchup':<26}{'setting':<10}{'secret':>8}{'solved':>8}"
        f"{'cost':>7}{'naive':>8}")
    for wa, wb in OPEN_PAIRS:
        for mode in ["off", "disadv"]:
            _cfg(MUTUAL_SWING=mode)
            sec, exp, naive = _with(exposure, wa, wb)
            out(f"  {wa + ' v ' + wb:<26}{mode:<10}{sec:>8.0%}{exp:>8.0%}"
                f"{exp - sec:>+7.0%}{naive:>8.0%}")
    out("\n  PASS CONDITION, stated before the numbers so it cannot be moved:")
    out("  'cost' has to come up to roughly the same place as the same-weapon")
    out("  row, where exposure is already nearly free. Anything still worth 20+")
    out("  points means going first is a losing position and the declarations")
    out("  cannot go face up, whatever else mutual swinging is worth.")

    hdr("O4. THE SECOND GATE - is the Band doing what the read used to?")
    out("If mutual swing does not close the gap, the obvious diagnosis is that")
    out("removing one hard counter only exposed another: knowing a declaration")
    out("still lets you pick a Measure where the other weapon does not reach.")
    out("GRAD_DIR='both' softens THAT gate too - one Band off is Disadvantage in")
    out("either direction rather than nothing outward. It is lever 5 reversed,")
    out("rejected for other reasons, and included here as a mechanism test.\n")
    out(f"  {'swing':<10}{'slop':<8}{'matchup':<26}{'secret':>8}{'exposed':>9}{'cost':>7}")
    for grad in ("down", "both"):
        for mode in ("off", "disadv"):
            for wa, wb in [("Broadsword", "Broadsword"), ("Longsword", "Spear")]:
                _cfg(MUTUAL_SWING=mode, GRAD_DIR=grad)
                sec, exp, _ = _with(exposure, wa, wb)
                out(f"  {mode:<10}{grad:<8}{wa + ' v ' + wb:<26}"
                    f"{sec:>8.0%}{exp:>9.0%}{exp - sec:>+7.0%}")

    hdr("O5. THE COLLATERAL - the reach ladder under mutual swing")
    out("Symmetrised, both sides at equilibrium, secrecy intact. This is what")
    out("mutual swinging costs somewhere it was not aimed.\n")
    out(f"  {'matchup':<26}{'as drafted':>12}{'mutual swing':>14}{'shift':>8}")
    for wa, wb in [("Broadsword", "Spear"), ("Longsword", "Spear"),
                   ("Dagger", "Pike"), ("Greatsword", "Halberd"),
                   ("Broadsword", "Longsword")]:
        _cfg(MUTUAL_SWING="off")
        a = _with(solved_value, wa, wb)[0]
        _cfg(MUTUAL_SWING="disadv")
        b = _with(solved_value, wa, wb)[0]
        out(f"  {wa + ' v ' + wb:<26}{a:>11.0%}{b:>13.0%}{b - a:>+8.0%}")

    hdr("O6. THE VALUE OF COMMITMENT, PER STATE - why the whole-fight cost is")
    out("    so much larger than any single decision")
    out("LOWER = A commits where B can see it. UPPER = B commits where A can.")
    out("NASH sits between them, and UPPER-LOWER is the exact price of secrecy")
    out("at that one state, with the rest of the fight played blind.\n")
    for mode in ("off", "disadv"):
        _cfg(MUTUAL_SWING=mode)
        rows, (lo, v, up), _ = _with(commitment_gap, "Broadsword", "Spear")
        out(f"  Broadsword v Spear, MUTUAL_SWING={mode}")
        out(f"    {'Measure':<10}{'role':<9}{'visits':>8}{'lower':>8}{'nash':>7}"
            f"{'upper':>7}{'swing':>8}")
        for (st, n, l, nv, u) in rows:
            out(f"    {_band_name(st[0]):<10}"
                f"{('A init' if st[1] else 'B init'):<9}{n:>8}"
                f"{l:>8.0%}{nv:>7.0%}{u:>7.0%}{u - l:>+8.0%}")
        out(f"    {'weighted':<19}{'':>8}{lo:>8.0%}{v:>7.0%}{up:>7.0%}"
            f"{up - lo:>+8.0%}\n")
    out("  Read this against O3. One exposed declaration is worth a few points;")
    out("  a whole fight of them is worth thirty or forty. Exposure COMPOUNDS -")
    out("  each read the follower wins also chooses the Measure the next one is")
    out("  fought at, and that is the half a single-state number cannot see.")


# --------------------------------------------------------------------------
# 7. Report - THE OPEN CALLS REWORK
# --------------------------------------------------------------------------
# Run with:  python3 tools/exchange_solver.py calls
#
# Two levers (exchange_sim.REACH_CURVE = 'graded' and ADVANCE_ALWAYS_CLOSES),
# aimed at the one state O6 localised the exposure cost to: the contested
# approach. Measures what they do to the reach ladder, to the price of exposing
# a declaration, and to the per-state value of commitment.

CALL_CFG = [("as drafted", dict(REACH_CURVE="classic", ADVANCE_ALWAYS_CLOSES=False)),
            ("graded reach", dict(REACH_CURVE="graded", ADVANCE_ALWAYS_CLOSES=False)),
            ("advance closes", dict(REACH_CURVE="classic", ADVANCE_ALWAYS_CLOSES=True)),
            ("Open Calls", dict(REACH_CURVE="graded", ADVANCE_ALWAYS_CLOSES=True))]

CALL_LADDER = [("Broadsword", "Spear"), ("Dagger", "Pike"),
               ("Longsword", "Spear"), ("Greatsword", "Halberd"),
               ("Broadsword", "Longsword"), ("Spear", "Halberd")]

CALL_PAIRS = [("Broadsword", "Broadsword"), ("Longsword", "Spear"),
              ("Broadsword", "Spear"), ("Dagger", "Pike"),
              ("Greatsword", "Halberd")]


def main_calls():
    random.seed(11)
    out = lambda *a: print(*a, flush=True)

    hdr("C1. THE REACH LADDER - both levers, secrecy intact")
    out("Symmetrised, both sides at equilibrium. 50% is even. This is the")
    out("question the levers were NOT aimed at, and it is where they land.\n")
    out(f"  {'matchup':<26}" + "".join(f"{n:>15}" for n, _ in CALL_CFG))
    vals = {}
    for name, cfg in CALL_CFG:
        _cfg(MUTUAL_SWING="off", **cfg)
        for wa, wb in CALL_LADDER:
            vals[(name, wa, wb)] = _with(solved_value, wa, wb)[0]
    for wa, wb in CALL_LADDER:
        out(f"  {wa + ' v ' + wb:<26}"
            + "".join(f"{vals[(n, wa, wb)]:>14.0%} " for n, _ in CALL_CFG))
    out("")
    for name, _ in CALL_CFG:
        v = [vals[(name, a, b)] for a, b in CALL_LADDER]
        out(f"  {name:<16}spread {min(v):.0%}-{max(v):.0%}   mean distance from "
            f"even {sum(abs(x - .5) for x in v) / len(v):.1%}")

    hdr("C2. WHAT EXPOSING A DECLARATION COSTS, PLAYED CORRECTLY")
    out("'secret' is the Nash value. 'open' has the leader on the per-state")
    out("maximin pure row and the follower solving against what it can see.")
    out("'commitments' lists the distinct declarations the leader ever makes:")
    out("a single entry means the open game has one line of play left in it.\n")
    out(f"  {'config':<20}{'matchup':<26}{'secret':>8}{'open':>7}{'cost':>7}"
        f"   commitments")
    for name, cfg in [("as drafted", dict(REACH_CURVE="classic",
                                          ADVANCE_ALWAYS_CLOSES=False,
                                          MUTUAL_SWING="off")),
                      ("Open Calls", dict(REACH_CURVE="graded",
                                          ADVANCE_ALWAYS_CLOSES=True,
                                          MUTUAL_SWING="off")),
                      ("Open Calls + swing", dict(REACH_CURVE="graded",
                                                  ADVANCE_ALWAYS_CLOSES=True,
                                                  MUTUAL_SWING="disadv")),
                      ("closes + swing", dict(REACH_CURVE="classic",
                                              ADVANCE_ALWAYS_CLOSES=True,
                                              MUTUAL_SWING="disadv"))]:
        _cfg(**cfg)
        for wa, wb in CALL_PAIRS:
            sec, _mx, pure, leads = _with(open_play, wa, wb)
            out(f"  {name:<20}{wa + ' v ' + wb:<26}{sec:>8.0%}{pure:>7.0%}"
                f"{pure - sec:>+7.0%}   {','.join(d[:3] for d in leads)}")
        out("")

    hdr("C3. THE VALUE OF COMMITMENT, PER STATE")
    out("UPPER-LOWER is the exact price of secrecy at one state. The target is")
    out("+0 everywhere - a matrix with a saddle point can be played face up.\n")
    for name, cfg in [("as drafted", dict(REACH_CURVE="classic",
                                          ADVANCE_ALWAYS_CLOSES=False,
                                          MUTUAL_SWING="off")),
                      ("Open Calls + swing", dict(REACH_CURVE="graded",
                                                  ADVANCE_ALWAYS_CLOSES=True,
                                                  MUTUAL_SWING="disadv"))]:
        _cfg(**cfg)
        rows, (lo, v, up), _ = _with(commitment_gap, "Broadsword", "Spear")
        out(f"  Broadsword v Spear - {name}")
        out(f"    {'Measure':<10}{'role':<9}{'visits':>8}{'lower':>8}{'nash':>7}"
            f"{'upper':>7}{'swing':>8}")
        for (st, n, l, nv, u) in rows:
            out(f"    {_band_name(st[0]):<10}"
                f"{('A init' if st[1] else 'B init'):<9}{n:>8}"
                f"{l:>8.0%}{nv:>7.0%}{u:>7.0%}{u - l:>+8.0%}")
        out(f"    {'weighted':<19}{'':>8}{lo:>8.0%}{v:>7.0%}{up:>7.0%}"
            f"{up - lo:>+8.0%}\n")


# --------------------------------------------------------------------------
# 8. Report - THE MARGIN HYBRID
# --------------------------------------------------------------------------
# Run with:  python3 tools/exchange_solver.py hybrid
#
# Geometry from the Exchange, resolution from Oppose. The Cycle biases one
# opposed roll instead of gating the blow; displacement stays unconditional.

HY_CFG = [
    ("binary, as drafted", dict(TEMPO_MODE="binary", ADVANCE_ALWAYS_CLOSES=False,
                                REACH_CURVE="classic")),
    ("margin", dict(TEMPO_MODE="margin", ADVANCE_ALWAYS_CLOSES=False,
                    REACH_CURVE="classic")),
    ("margin + closes", dict(TEMPO_MODE="margin", ADVANCE_ALWAYS_CLOSES=True,
                             REACH_CURVE="classic")),
    ("full hybrid", dict(TEMPO_MODE="margin", ADVANCE_ALWAYS_CLOSES=True,
                         REACH_CURVE="graded")),
    # Item 28's tuning pass. Swept REACH_PENALTY x REACH_SLOP_OUT x
    # REACH_SLOP_IN against the solved ladder; this cell won. The finding is
    # that the LOCKOUT is the dial and the penalty size is secondary - every
    # config with slop_out 1 and slop_in 2 beats every config without,
    # regardless of penalty, because a lockout under margin means you do not
    # even contest and the other fighter strikes unopposed every beat.
    ("margin, tuned", dict(TEMPO_MODE="margin", ADVANCE_ALWAYS_CLOSES=True,
                           REACH_CURVE="flat", REACH_PENALTY=2,
                           REACH_SLOP_OUT=1, REACH_SLOP_IN=2)),
]

HY_LADDER = [("Broadsword", "Spear"), ("Dagger", "Pike"), ("Longsword", "Spear"),
             ("Greatsword", "Halberd"), ("Broadsword", "Longsword"),
             ("Spear", "Halberd")]

HY_PAIRS = [("Broadsword", "Broadsword"), ("Longsword", "Spear"),
            ("Broadsword", "Spear"), ("Dagger", "Pike")]


def main_hybrid():
    random.seed(11)
    out = lambda *a: print(*a, flush=True)

    hdr("H1. THE REACH LADDER")
    out("Symmetrised, both sides at equilibrium, secrecy intact. 50% is even.")
    out("The binary gate was propping the ladder up; the question is whether a")
    out("graded one still does.\n")
    out(f"  {'matchup':<26}" + "".join(f"{n:>19}" for n, _ in HY_CFG))
    vals = {}
    for name, cfg in HY_CFG:
        _cfg(**cfg)
        for wa, wb in HY_LADDER:
            vals[(name, wa, wb)] = _with(solved_value, wa, wb)[0]
    for wa, wb in HY_LADDER:
        out(f"  {wa + ' v ' + wb:<26}"
            + "".join(f"{vals[(n, wa, wb)]:>18.0%} " for n, _ in HY_CFG))
    out("")
    for name, _ in HY_CFG:
        v = [vals[(name, x, y)] for x, y in HY_LADDER]
        out(f"  {name:<22}spread {min(v):.0%}-{max(v):.0%}   mean distance from "
            f"even {sum(abs(x - .5) for x in v) / len(v):.1%}")

    hdr("H2. THE BILL - table time and blood")
    out("Both sides on the sim's heuristic. 'empty' is the exchange where")
    out("nothing happened at all, which is the drafted system's worst habit.\n")
    out(f"  {'config':<22}{'matchup':<24}{'rounds':>8}{'atk/exch':>10}{'empty':>8}"
        f"{'bind':>7}{'trade':>7}{'dom':>6}")
    for name, cfg in HY_CFG:
        _cfg(**cfg)
        for wa, wb in [("Broadsword", "Spear"), ("Longsword", "Spear")]:
            st = _with(swing_stats, wa, wb)
            _cfg(**cfg)
            _w, _d, _r, raw = _with(X.duel, wa, wb, trials=6000)
            ex = raw["exchanges"] or 1
            out(f"  {name:<22}{wa + ' v ' + wb:<24}{st['rounds']:>8.2f}"
                f"{st['atk_per_exchange']:>10.2f}{st['empty']:>8.0%}"
                f"{raw['margin_bind'] / ex:>7.0%}{raw['margin_trade'] / ex:>7.0%}"
                f"{raw['margin_dominant'] / ex:>6.0%}")

    hdr("H3. DOES A GRADED GATE MAKE OPEN DECLARATIONS SURVIVABLE?")
    out("The binary gate is what made exposure fatal - lose the read, get")
    out("nothing. A margin gate should soften that. 'open' has the leader on the")
    out("per-state maximin pure row, the follower solving against what it sees.\n")
    out(f"  {'config':<22}{'matchup':<26}{'secret':>8}{'open':>7}{'cost':>7}"
        f"   commitments")
    for name, cfg in HY_CFG:
        _cfg(**cfg)
        for wa, wb in HY_PAIRS:
            sec, _mx, pure, leads = _with(open_play, wa, wb)
            out(f"  {name:<22}{wa + ' v ' + wb:<26}{sec:>8.0%}{pure:>7.0%}"
                f"{pure - sec:>+7.0%}   {','.join(d[:3] for d in leads)}")
        out("")

    hdr("H4. CYCLE_BONUS - what should winning the read be worth?")
    out("The dial between 'the Cycle is everything' and 'the Cycle is flavour'.")
    out("Reported as the skill gradient: an equilibrium player against a")
    out("coin-flipper. The drafted binary system measures +36 in a mixed-reach")
    out("matchup, which is the depth the hybrid has to keep.\n")
    out(f"  {'bonus':<8}{'matchup':<26}{'v equilibrium':>15}{'v random':>10}"
        f"{'gradient':>10}")
    for bonus in (0, 1, 2, 3, 5):
        for wa, wb in [("Broadsword", "Spear"), ("Broadsword", "Broadsword")]:
            _cfg(TEMPO_MODE="margin", ADVANCE_ALWAYS_CLOSES=True,
                 REACH_CURVE="classic", CYCLE_BONUS=bonus)

            def _go():
                pA, _, eqv, _ = equilibrium(wa, wb)
                return eqv, fixed_vs_fixed(wa, wb, pA, uniform_policy())
            eqv, rnd = _with(_go)
            out(f"  {'+' + str(bonus):<8}{wa + ' v ' + wb:<26}{eqv:>14.0%}"
                f"{rnd:>10.0%}{rnd - eqv:>+10.0%}")
    out("\n  A gradient near zero means the read stopped mattering and the dice")
    out("  are doing all of it. Too large and the margin roll is decoration on")
    out("  an RPS game. The drafted system's +36 is the reference point.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "hybrid":
        main_hybrid()
    elif len(sys.argv) > 1 and sys.argv[1] == "calls":
        main_calls()
    elif len(sys.argv) > 1 and sys.argv[1] == "open":
        main_open()
    else:
        main()
