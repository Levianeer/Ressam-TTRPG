#!/usr/bin/env python3
"""
Ressam creature rating - "how does this thing stack up against a PC," as a
5-tier comparison instead of a raw number or a borrowed CR curve.

Ressam's PCs don't scale much over 12 levels (Level 1's Attribute-point
budget is 18, Level 12's is 21 - see power_score.LEVEL_TABLE), so a single
fixed reference build stays meaningful across the whole game as a yardstick,
unlike a D&D-style CR-vs-Level curve. combat_engine.BASELINE_PC is that
yardstick. This tool runs a Monte Carlo 1-on-1 duel (combat_engine.run_fight,
the full Oppose/Effect/Press loop) between a creature and BASELINE_PC many
times and buckets the creature's own win rate into a tier:

    < 20%  Much Worse       than a PC
    20-40% Worse            than a PC
    40-60% Equal            to a PC
    60-80% Better            than a PC
    >= 80% Much Better      than a PC

This is deliberately a 1-on-1 lens - see tools/encounter_rating.py for how a
creature performs fielded in numbers against a full party, which is a
different (and for most bestiary entries, more relevant) question.

Usage as a library:
    from creature_rating import rate_creature
    rate_creature(build, trials=2000) -> Rating

Usage as a script: rates a small library of example creatures adapted from
core/bestiary/universal.md's existing stat lines (reference only - this does
not read or write core/bestiary/*.md).
    python3 tools/creature_rating.py [trials]
"""

import sys
from dataclasses import dataclass

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from combat_engine import Build, WEAPONS, SHIELDS, ARMORS, BASELINE_PC, run_fight

TIER_THRESHOLDS = [
    (0.20, "Much Worse"),
    (0.40, "Worse"),
    (0.60, "Equal"),
    (0.80, "Better"),
    (1.01, "Much Better"),
]


def tier_for(win_rate):
    for threshold, label in TIER_THRESHOLDS:
        if win_rate < threshold:
            return label
    return TIER_THRESHOLDS[-1][1]


@dataclass
class Rating:
    name: str
    win_rate: float
    tier: str
    avg_rounds: float


def rate_creature(build_factory, trials=2000, name=None):
    """`build_factory` is a zero-arg callable returning a fresh Build (armor/
    Guard state mutates per-fight, so each trial needs its own instance)."""
    wins = 0
    total_rounds = 0
    for _ in range(trials):
        winner, rounds, _, _ = run_fight([build_factory()], [BASELINE_PC])
        total_rounds += rounds
        if winner == "a":
            wins += 1
    win_rate = wins / trials
    return Rating(name or build_factory().name, win_rate, tier_for(win_rate), total_rounds / trials)


# ---------------------------------------------------------------------------
# Example creatures, adapted from core/bestiary/universal.md (2026-08-09
# stat lines) into the new Build shape. Reference only.
# ---------------------------------------------------------------------------

def make_peasant():
    return Build(name="Peasant", STR=1, DEX=1, MIND=1, CHA=1,
                 weapon=WEAPONS["Club"], weapon_skill=0, max_wounds=3)


def make_skeleton():
    return Build(name="Skeleton", STR=2, DEX=1,
                 weapon=WEAPONS["Broadsword"], weapon_skill=1, max_wounds=3)


def make_zombie():
    return Build(name="Zombie", STR=2, DEX=0,
                 weapon=WEAPONS["Punch"], weapon_skill=1, max_wounds=3)


def make_bandit():
    return Build(name="Bandit", STR=2, DEX=2, MIND=1, CHA=1,
                 weapon=WEAPONS["Shortsword"], weapon_skill=2,
                 armor_ar=ARMORS["Buff Coat"][0], armor_penalty=ARMORS["Buff Coat"][1],
                 max_wounds=3)


def make_wolf():
    return Build(name="Wolf", STR=2, DEX=2, MIND=1, CHA=1,
                 weapon=WEAPONS["Bite"], weapon_skill=2, max_wounds=3)


def make_archer():
    return Build(name="Archer", STR=1, DEX=2, MIND=1, CHA=1,
                 weapon=WEAPONS["Longbow"], weapon_skill=2,
                 armor_ar=ARMORS["Gambeson"][0], armor_penalty=ARMORS["Gambeson"][1],
                 max_wounds=3)


def make_guard():
    # No block_skill field anymore - the STR Ward Oppose leg is flat and
    # untrained, funded automatically by STR=3 below.
    return Build(name="Guard", STR=3, DEX=1, MIND=1, CHA=1,
                 weapon=WEAPONS["Spear"], weapon_skill=2,
                 shield=SHIELDS["Heater Shield"],
                 armor_ar=ARMORS["Mail Shirt"][0], armor_penalty=ARMORS["Mail Shirt"][1],
                 max_wounds=3)


def make_bear():
    return Build(name="Bear", STR=4, DEX=1,
                 weapon=WEAPONS["Mace"], weapon_skill=3, max_wounds=4)  # Large (4)


def make_knight():
    return Build(name="Knight", STR=4, DEX=3, MIND=1, CHA=1, FAI=1,
                 weapon=WEAPONS["Longsword"], weapon_skill=4,
                 shield=SHIELDS["Heater Shield"],
                 armor_ar=ARMORS["Breastplate"][0], armor_penalty=ARMORS["Breastplate"][1],
                 max_wounds=4)  # Tough feat, +1


EXAMPLE_CREATURES = [
    make_peasant, make_skeleton, make_zombie, make_bandit,
    make_wolf, make_archer, make_guard, make_bear, make_knight,
]


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    print(f"Rated against BASELINE_PC (1-on-1), {trials} trials each:")
    print(f"{'Creature':<12} {'Win Rate':>9}   {'Tier':<12} {'Avg Rounds':>10}")
    print("-" * 48)
    for factory in EXAMPLE_CREATURES:
        r = rate_creature(factory, trials)
        print(f"{r.name:<12} {r.win_rate:>8.1%}   {r.tier:<12} {r.avg_rounds:>10.1f}")


if __name__ == "__main__":
    main()
