#!/usr/bin/env python3
"""Re-validate every ADOPTED lever under solved play instead of the heuristic.

    python3 tools/exchange_revalidate.py

WHY
  Every lever in `exchange_log.md` - adopted and rejected alike - was judged
  with `exchange_sim`'s BIAS heuristic standing in for how people declare.
  `exchange_solver.py` showed that heuristic is not a neutral stand-in: four
  open items turned out to be describing it rather than the system, and one
  closed conclusion (item 13) inverted outright.

  So each adopted lever is re-measured here with BOTH sides playing the solved
  equilibrium for that lever's own setting - the equilibrium is re-solved per
  configuration, because the right way to play changes when the rules do.

WHAT A ROW MEANS
  For each lever, ON is the adopted setting and OFF is the alternative it beat.
  The question is never "is ON better" - it is "does the REASON it was adopted
  still hold." Each lever's own justification metric is called out in the notes
  under its table.

COST
  Each configuration re-solves an equilibrium for every ordered pair in FIELD,
  so this is minutes, not seconds. That is the price of not guessing.
"""

import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import exchange_sim as X
import exchange_solver as S

# Two per class. Small enough to solve repeatedly, wide enough for a ladder.
FIELD = ["Dagger", "Broadsword", "Longsword", "Greatsword", "Spear", "Halberd"]
CLASS = {"Dagger": "Sidearm", "Broadsword": "Sidearm",
         "Longsword": "Arming", "Greatsword": "Arming",
         "Spear": "Polearm", "Halberd": "Polearm"}

ITERS, FIGHTS = 8, 7000


def field_report():
    """Solve every CROSS-CLASS ordered pair; return per-class field averages
    plus aggregate counters, under equilibrium play at the current settings.

    SAME-CLASS PAIRS ARE EXCLUDED, and that is not tidying. Under solved play
    two fighters whose weapons want the same Measure simply refuse to engage:
    a Broadsword mirror runs 27 rounds at 99% "neither can act" even with the
    timeout scored as a loss for both. Nothing in the Exchange compels anyone
    to close, which is exactly what exchange_log's item 4 says - the tool has
    no reason for anyone ever to be attacked, so patience is free in it. The
    heuristic could never find that equilibrium; the solver finds it at once.

    The ladder is a cross-class quantity anyway (Polearm minus Sidearm), so
    dropping same-class pairs removes contamination rather than signal. The
    stall guard below reports it if it ever leaks in regardless."""
    raw, agg = {}, Counter()
    for a in FIELD:
        for b in FIELD:
            if a == b or CLASS[a] == CLASS[b]:
                continue
            pa, pb, _, _ = S.equilibrium(a, b, iters=ITERS, fights=FIGHTS)
            _, v, st = S.sample(a, b, pa, pb, fights=FIGHTS, explore=0.0)
            raw[(a, b)] = v
            agg.update(st)
    sym = {k: (raw[k] + 1 - raw[k[::-1]]) / 2 for k in raw}
    per = {w: sum(sym[(w, o)] for o in FIELD if (w, o) in sym)
              / max(1, sum(1 for o in FIELD if (w, o) in sym))
           for w in FIELD}
    cls = {c: sum(per[w] for w in FIELD if CLASS[w] == c)
              / sum(1 for w in FIELD if CLASS[w] == c)
           for c in ("Sidearm", "Arming", "Polearm")}
    ex = agg["exchanges"] or 1
    return {
        "per": per,
        "cls": cls,
        "ladder": cls["Polearm"] - cls["Sidearm"],
        "spread": max(per.values()) - min(per.values()),
        "empty": agg["empty_total"] / ex,
        "stall": agg["neither"] / ex,          # guard: must stay near zero
        "rounds": agg["rounds_total"] / max(agg["fights"], 1),
        "unfunded": (agg["mirror_unfunded"] + agg["riposte_unfunded"]) / ex,
        "mirrors": (agg["mirror_close"] + agg["mirror_hold"]) / ex,
    }


LEVERS = [
    ("lever 3c - longer weapon lands on the way in",
     "REACH_ORDER", True, False,
     "Adopted to make reach LEGIBLE, not to rescue it: it turned a one-point\n"
     "  gradient into a nine-point gap at no cost to the spread. Watch the\n"
     "  ladder and the spread together."),
    ("pricing the riposte",
     "RIPOSTE_COSTS_REACTION", True, False,
     "Adopted to narrow the spread (23-77 -> 27-73) and lengthen fights.\n"
     "  Watch spread first; the claim about WHICH weapons it helps was already\n"
     "  withdrawn once."),
    ("Hold/Hold trades blows",
     "HOLD_MIRROR", "trade", "standoff",
     "Adopted purely to cut empty exchanges, 30% -> 17%. It also quietly\n"
     "  flattened the ladder by ~4 points, which is why P2 exists. Watch empty."),
    ("P2 - a Mirror blow costs the responder",
     "MIRROR_COST", "responder", "free",
     "Adopted on the ladder: 16 points was 'reach that does not read', 29-30\n"
     "  was the fix. If the ladder is not what the heuristic said, this is the\n"
     "  adopted lever with the most to lose."),
    ("P6 - one reactive step per round",
     "REACTIVE_STEP", "once", "unlimited",
     "Adopted for the multi-opponent case, which this tool cannot see. It was\n"
     "  accepted because it costs nothing in the duel. Only that claim is\n"
     "  testable here, and it is the only one being tested."),
    ("item 17 - the follow-up thrower is the initiator",
     "FOLLOWUP_INITIATOR", "thrower", "turn",
     "Worth ~4 points and provably unreachable at 1 Reaction. Expect no move\n"
     "  at the default pool; a null result here CONFIRMS the item."),
    ("graduated mismatch",
     "GRADUATED", True, False,
     "The cure for dead space. Not really in question - included because it is\n"
     "  the largest single assumption under every other row."),
]


def show(tag, r):
    c = r["cls"]
    print(f"    {tag:<10}"
          f"side {c['Sidearm']:>5.1%}  arm {c['Arming']:>5.1%}  "
          f"pole {c['Polearm']:>5.1%}   ladder {r['ladder']:>+5.1%}   "
          f"spread {r['spread']:>5.1%}   empty {r['empty']:>5.1%}   "
          f"rounds {r['rounds']:>4.1f}   stall {r['stall']:>4.1%}", flush=True)


def main():
    t0 = time.time()
    print("=" * 86)
    print(" ADOPTED LEVERS, RE-VALIDATED UNDER SOLVED PLAY")
    print("=" * 86)
    print(f" field: {', '.join(FIELD)}")
    print(f" every configuration re-solves {len(FIELD) * (len(FIELD) - 1)} "
          f"equilibria; ON = the adopted setting\n")

    base = field_report()
    print(" BASELINE - all levers at their adopted settings")
    show("adopted", base)
    print(f"    {'':<10}per weapon: "
          + "  ".join(f"{w[:4]} {base['per'][w]:.0%}" for w in FIELD))

    for name, attr, on, off, note in LEVERS:
        print("\n" + "-" * 86)
        print(f" {name}   [{attr}]")
        print("-" * 86)
        setattr(X, attr, off)
        r_off = field_report()
        setattr(X, attr, on)
        show("ON", base)
        show("OFF", r_off)
        d_lad = base["ladder"] - r_off["ladder"]
        d_spr = base["spread"] - r_off["spread"]
        d_emp = base["empty"] - r_off["empty"]
        print(f"    {'delta':<10}ladder {d_lad:>+5.1%}   spread {d_spr:>+5.1%}"
              f"   empty {d_emp:>+5.1%}")
        print(f"  {note}")

    print("\n" + "=" * 86)
    print(f" done in {time.time() - t0:.0f}s")
    print("=" * 86)


if __name__ == "__main__":
    main()
