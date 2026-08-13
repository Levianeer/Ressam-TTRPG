Singular, campaign-defining threats - not fielded in numbers, not tied to one continent by default, and mechanically distinct from every other section in this bestiary: a Mythic creature carries Mythic Initiative ([[Mythic Initiative|bestiary_overview]]), rolling initiative multiple times and taking a full turn on each count, rather than one turn per round like everything else here.

**This section exists separately from a Very Rare tag elsewhere on purpose.** Frequency (see [[Bestiary Overview|bestiary_overview]]) describes how often a GM reaches for a creature - a Mythic entry is almost always Very Rare, but "rare" isn't what actually sets it apart from, say, a Bear. What sets it apart is Mythic Initiative itself, and that's a mechanical category, not a point on the Frequency scale.

**A note on Power Score:** `tools/power_score.py` cannot meaningfully price anything in this section. Power Score reads Attribute/Skill/Feat investment off the same table a PC advances through, and every character in Ressam shares the same Attribute 5 / Skill 5 ceiling - so a Mythic creature built at that ceiling scores identically to a non-Mythic creature built at the same ceiling, even though Mythic Initiative (extra turns, not bigger numbers) is what actually makes it dangerous. The Wyrm below and the hypothetical Blood-Rule Pyromancer stress-tested in `tools/danger_estimate.py` land on the exact same Effective Level and XP Reward despite one nearly wiping a 4-PC party solo and the other losing every simulated fight. Price a Mythic entry's reward by hand, or by comparison to the Wyrm below, not by running the calculator on it.

---

## Wyrm

*Ancient, serpentine, and legless - the closest thing to a true dragon that isn't one of the four God-Dragons themselves. Whatever it once was before the centuries made it this large is beside the point; what matters now is that it remembers every one of them, and it is very rarely in a hurry.*

**Frequency:** Very Rare

**Attributes:** STR 5, DEX 2, MIND 3, ARC 0, FAI 0, CHA 2

**Skills:** Daggers & Wrestling 5, Perception 3

**Feats:** Tough (\+1 Wounds), Second Wind (reroll a failed Ward once; \+3 to STR Ward below half Wounds)

| Wounds | Evasion | AR | Attack | Damage | Initiative |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 6 | 5 | 6 | \+5 | 2d8 \+ 5 | \+2 |

**Wound Threshold:** 1 Wound (1-11), 2 Wounds (12-17), 3 Wounds (18+).

**Wards:** STR 10, DEX 7, MIND 8

**Reactions:** 2/round (refreshed at the start of *each* of its turns, not once per round - see Mythic Initiative, below). No Maneuver - a Wyrm doesn't Parry, Block, or Dodge; scale and bulk are its only defense.

**Movement:** 40 ft - legless, but no less mobile for it; a serpentine glide rather than a walk.

**Natural Weapons:** Bite and Claw (2d8 Piercing/Slashing, Long Reach).

**Size:** Huge (6 Wounds \= baseline 5 \+ Tough; see [[Wounds and Survival|wounds_and_survival]] on scaling the baseline past Large for GM-statted creatures).

**Mythic Initiative (4):** Rolls initiative 4 times (normal, \-2, \-4, \-6); takes a full turn on each count. See [[Mythic Initiative|bestiary_overview]] - Reactions and end-of-turn effects (Bleed, Frightened saves, and the like) trigger on every one of its turns, not once per round.

**Dragonfire Breath (1/round, any one of its turns):** A 60 x 5 ft line of fire. Every creature in the line: DEX Ward (DC 16, Very Hard) or take 2d10 \+ STR Fire damage - a success halves the damage instead of negating it, matching Arcane's Resist convention ([[Magic Overview|magic_overview]]) rather than an all-or-nothing save. Once per round total, per Mythic Initiative's Repetition rule ([[Mythic Initiative|bestiary_overview]]) - not once per turn.

**Variant - Elemental Reskin:** Fire is the default here, but nothing about a Wyrm ties it to Infierno specifically - Cold, Lightning, or Acid breath (swap the damage type, nothing else) fits equally well, since a Wyrm is explicitly not one of the four God-Dragons and carries no allegiance to any single element.

**In Combat:** A Wyrm doesn't maneuver for advantage - it opens with Dragonfire Breath on whichever turn is most convenient, then spends its other three turns each round on Bite and Claw against whoever's closest, its AR 6 scales and 6 Wounds absorbing the return fire. Playtested solo at 50.7% monster-favored against a Level 1 Balanced 4-PC party (3,000 trials, avg 1.6 rounds) - a genuine coin flip, and it should feel that way at the table: dangerous, not unwinnable. The breath's damage was retuned down twice during testing (from Cataclysmic 6d8, a 98.7% near-instant party wipe) specifically because a guaranteed, no-roll-to-cast, whole-party hit is worth far more than the same dice on a single target - `spell_crafting.md`'s Magnitude/Area table prices that tradeoff via a DC-to-cast penalty a monster ability skips entirely, so the dice size has to do that job instead.