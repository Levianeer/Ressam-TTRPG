#!/usr/bin/env python3
"""
Ressam encounter rating - "how does this encounter stack up against a party,"
the group-fight counterpart to tools/creature_rating.py's 1-on-1 lens. Same
5-tier idea (Much Worse/Worse/Equal/Better/Much Better), same Monte Carlo
win-rate bucketing, same fixed-baseline philosophy - just N monsters against
a party of BASELINE_PC clones instead of one creature against one PC.

    < 20%  Much Worse       than the party  (monsters win < 20% of fights)
    20-40% Worse            than the party
    40-60% Equal            to the party
    60-80% Better            than the party
    >= 80% Much Better      than the party  (monsters win >= 80% of fights)

Usage as a library:
    from encounter_rating import rate_encounter
    rate_encounter([make_bandit]*6, trials=1000) -> Rating

Usage as a script: headcount sweep for a few example creatures/monster
groups (imported from creature_rating.py, plus one Mythic example to
exercise Mythic Initiative), mirroring the old Fielding Guide validation.
    python3 tools/encounter_rating.py [trials]
"""

import sys
from dataclasses import dataclass

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from combat_engine import Build, WEAPONS, run_fight, make_baseline_pc
from creature_rating import (
    tier_for, make_peasant, make_bandit, make_guard, make_wolf, make_bear, make_knight,
)


@dataclass
class Rating:
    label: str
    win_rate: float
    tier: str
    avg_rounds: float
    avg_pc_losses: float
    avg_monster_losses: float


def rate_encounter(monster_factories, trials=1000, label=None):
    """`monster_factories`: list of zero-arg Build factories, one per
    monster fielded (a creature fielded x6 is [make_x]*6)."""
    wins = 0
    total_rounds = 0
    total_pc_losses = 0
    total_monster_losses = 0
    for _ in range(trials):
        party = [make_baseline_pc() for _ in range(4)]
        monsters = [f() for f in monster_factories]
        winner, rounds, pc_losses, monster_losses = run_fight(party, monsters)
        total_rounds += rounds
        total_pc_losses += pc_losses
        total_monster_losses += monster_losses
        if winner == "b":
            wins += 1
    win_rate = wins / trials
    return Rating(
        label or f"{len(monster_factories)}x monster", win_rate, tier_for(win_rate),
        total_rounds / trials, total_pc_losses / trials, total_monster_losses / trials,
    )


# ---------------------------------------------------------------------------
# One Mythic example (combat.md's Mythic Initiative), to exercise the
# multi-turn/escalating-penalty path - a solo Wyrm, mythic_turns=3.
# ---------------------------------------------------------------------------

def make_mythic_wyrm():
    return Build(name="Mythic Wyrm", STR=5, PRE=2, END=5, DEX=3, MIND=3, CHA=2,
                 weapon=WEAPONS["Bite"], weapon_skill=5, max_wounds=6, mythic_turns=3)


HEADCOUNT_SWEEPS = [
    ("Peasant", make_peasant, [8, 11, 14, 18]),
    ("Bandit", make_bandit, [3, 5, 7, 9]),
    ("Guard", make_guard, [3, 5, 7, 9]),
    ("Wolf", make_wolf, [3, 5, 7, 9]),
    ("Bear", make_bear, [1, 2, 3, 4]),
    ("Knight", make_knight, [1, 2, 3, 4]),
]


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    print(f"Rated against a 4x BASELINE_PC party, {trials} trials per row:")
    print(f"{'Encounter':<18} {'Win Rate':>9}   {'Tier':<12} {'AvgRounds':>9} "
          f"{'AvgPCsDown':>10} {'AvgMonstersDown':>15}")
    print("-" * 82)
    for name, factory, counts in HEADCOUNT_SWEEPS:
        for n in counts:
            r = rate_encounter([factory] * n, trials, label=f"{name} x{n}")
            print(f"{r.label:<18} {r.win_rate:>8.1%}   {r.tier:<12} {r.avg_rounds:>9.1f} "
                  f"{r.avg_pc_losses:>10.2f} {r.avg_monster_losses:>15.2f}")
        print()

    r = rate_encounter([make_mythic_wyrm], trials, label="Mythic Wyrm x1")
    print(f"{r.label:<18} {r.win_rate:>8.1%}   {r.tier:<12} {r.avg_rounds:>9.1f} "
          f"{r.avg_pc_losses:>10.2f} {r.avg_monster_losses:>15.2f}")


if __name__ == "__main__":
    main()
