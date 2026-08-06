# Encounter Guide

This is a GM-facing tool, not a rulebook chapter - it lives outside `core/` on purpose and is **not** mirrored to the wiki. Its job is two things: give you a Challenge-Rating-style number for judging how dangerous an NPC is before the dice hit the table, and let you build that NPC's actual stat line in under a minute.

**The core idea: an NPC is a stripped-down PC, not a separate math system.** Every formula below - Wounds, Evasion, Attack Rolls, Damage Rolls - is the exact formula `core_rules.md`/`wounds_and_survival.md`/`combat.md` already defines for players, unchanged. Nothing here forks that math into a parallel monster-only version, because that's exactly what made the old version of this guide go stale: it hardcoded HP/AR ranges that drifted the moment the Wounds and Skills/Attributes rescales landed elsewhere in `core/`. The only genuinely new content in this file is **Role** (below) and **Mythic Initiative** (`combat.md`) - everything else is a pointer back at formulas and tables that already exist and are already kept current.

---

## Threat Level

**An NPC's Threat Level is simply the PC Level it's built to challenge (1-12).** Build it like a PC of that level: its Attributes and Skills are capped exactly where `progression_&_rewards.md`'s advancement table caps a real character at that level. A Threat Level 6 bandit captain feels like a fight against a level-6 PC because, mechanically, it more or less *is* one.

| Threat Level | Skill Cap | Attribute Cap |
| :---: | :---: | :---: |
| 1-2 | 2 | 4 |
| 3-4 | 3 | 4 |
| 5-6 | 4 | 4 |
| 7 | 5 | 4 |
| 8-12 | 5 | 5 |

**This table is a derived copy of `progression_&_rewards.md`'s Skill Cap / Attribute Cap columns, kept small for convenience at the table.** If that table's caps ever change, this one is stale until updated to match - `progression_&_rewards.md` is the source of truth, not this file.

---

## Role

Role measures an NPC against a single PC of the same Threat Level, and doubles as the answer to "how many of these make a fair, single-Role fight?" These ratios are the baseline for an *even* encounter - mixing Roles, or fielding more or fewer than the count below, is how you tune a fight easier or harder from there.

| Role | Against a lone PC | Field, for an even fight... | Fictional positioning |
| :---- | :---- | :---: | :---- |
| **Easy** | Badly outmatched | 4 per player | Woefully out of the party's league - petty criminals, animals, Skeggs, and the like. Only a threat in numbers. |
| **Average** | Worse in most regards, but can still threaten a 1v1 at poor odds | 2 per player | A soldier or rival who trained for this, just not at the party's tier. Biggest letdown is equipment, then stats. |
| **Elite** | Equal in every way that counts | 1 per player | Functionally a player made into a stat block. A single Elite with any backup is a genuine threat. |
| **Mythic** | Never loses a 1v1 | 1 per 2-4 players | A campaign boss - won't win alone against a full party, but is absolutely a threat. Elite's stat block plus Mythic Initiative, below. |

**Building each Role:** apply one offset to three numbers - the NPC's governing Attribute, its END, and its main Skill - all pulled down together from the Threat Level's caps above. Gear scales alongside them.

| Role | Governing Attribute, END & Skill | Gear |
| :---- | :---: | :---- |
| **Elite** | Threat Level's cap | The best gear its concept would plausibly carry at this Threat Level |
| **Average** | Cap − 1 | One tier down the Armor Table from Elite's pick |
| **Easy** | Cap − 3 (minimum 0) | Clothing, or nothing |
| **Mythic** | = Elite | = Elite, plus Mythic Initiative (below) |

**Wounds is always just END** - whatever value the offset above lands you on, same formula a PC uses. Role doesn't touch Wounds directly; the whole gap between an Easy mook and an Elite rival comes from the Attribute/Skill/Gear it was built with, same as it would between two differently-built PCs. This is also why Mythic doesn't get its own Wounds bump: Mythic Initiative already means every hit lands against a creature about to take 2-4× the turns (and Reactions) a PC gets in the same round - that's where its survivability actually comes from, and it's also exactly why a Mythic never loses a fair 1v1.

**Picking X for Mythic Initiative** (`combat.md`): X is directly "how many players this Mythic is meant to threaten alone" - 2 for a boss meant to challenge a duo (or be a manageable set piece for a larger party), up to 4 for one meant to threaten a full four-person party on its own. The mechanic's own escalating \-2 penalty does the diminishing-returns work past X = 4 - a 5th roll sits at \-8, usually below any DC worth calling for.

**Note:** these ratios are design targets, not Monte Carlo-validated the way `tools/balance_sim.py` validates PC-vs-PC math - playtest and retune the offsets above if a Role over- or under-performs its intended count at the table. **Threat Level 1 is the exception:** `tools/encounter_sim.py` (a group-combat companion to `balance_sim.py`) Monte Carlo-tested the Level 1 Example Roster below against a generic 4-PC level-1 party and found the ratios above landed badly uneven at that level (Easy 72% PCs win, Average 8%, Elite 64%) - the counts and stat lines below have been retuned to land near 50/50 instead, and no longer match "4/2/1 per player" exactly. That retuning hasn't been generalized to other Threat Levels; treat the ratios above as the starting guess elsewhere until they get the same treatment.

---

## Fast Build (under a minute)

1. **Pick a Threat Level.** The PC level you want this fight to challenge.
2. **Pick a Role** (above), and with it, how many you're fielding.
3. **Pick ONE governing Attribute** for its combat math - STR for a melee brute, PRE for finesse/ranged, DEX for an agile skirmisher, MIND/ARC/FAI for a caster - and **ONE relevant Skill** - its weapon Skill, or a casting school. Set both, plus END, to the value Role's offset table gives you for this Threat Level. Everything else defaults to 0-2, a build choice the same way it would be for a PC.
4. **Gear:** pick armor and a weapon per Role's Gear column, off the Armor Table (`armor.md`) and Weapon Tables (`weapons.md`), or write up natural armor/weapons for a beast.
5. **Wounds \= END** (already set in step 3).
6. **Evasion \= 5 \+ Agility Skill \+ DEX − Armor Penalty.** 0 Agility is fine for most NPCs - they're not built to Dodge like a PC skirmisher unless that's the point of this one.
7. **Attack Roll \= 1d12 \+ Skill \+ governing Attribute vs. target's Evasion. Damage \= weapon/natural damage die \+ governing Attribute − target's AR.** Unchanged from `combat.md`.
8. **Optional: one signature trait.** A single Feat-sized rider - a condition on hit, a resistance, a terrain trick. Elite and Mythic almost always want one; Average sometimes does; Easy essentially never does - it's fodder, not a puzzle.
9. **Reactions**, if this NPC needs to Parry/Block/Dodge or make Opportunity Attacks, use the same `(DEX + PRE) ÷ 3, rounded down` pool as a PC. Skip building this out entirely for Easy fodder that isn't expected to survive long enough to use it.
10. **Mythic only:** add Mythic Initiative(X) per `combat.md`, using the X guidance above.

---

## Example Roster - Level 1, Party of Four

All four Roles at the same Threat Level, side by side, so the gap between them is easy to see directly - a bandit gang and their wolf, sized for a 4-player, level 1 party. Threat Level 1's caps are Skill 2 / Attribute 4.

**Counts and stat lines below are Monte Carlo-validated** (`tools/encounter_sim.py`), not just derived from the offset table above - Easy, Average, and Elite were each retuned until they landed close to a 50/50 fight against a generic 4-PC level-1 party (51-53% PCs win, across thousands of simulated trials each). At level 1's small Wounds pools (2-4), the naive "N per player" counts from the Role table above produced wildly uneven fights instead (Easy 72% PCs win at 16 fielded, Average only 8% at 8 fielded, Elite 64% at 4 fielded) - see `tools/encounter_sim.py`'s docstring for the full methodology. Mythic was deliberately left alone: it's expected to lean on allies and battlefield tactics rather than win a fair fight as a lone stat block, so "loses badly to a full party 1-on-4" is an acceptable outcome for it, not a bug to chase.

### Easy - Starving Bandit (field 8 for a 4-player party)

| **Starving Bandit** | Threat Level 1 - Easy |
| :---- | :---- |
| **Attributes** | STR 4, PRE 1, END 3, DEX 1 |
| **Skill** | Brawling 0 (untrained) |
| **Wounds** | 3 |
| **Armor** | Gambeson - AR 2, Penalty 1 |
| **Evasion** | 5 |
| **Attack** | 1d12 alone vs. target's Evasion (untrained - no Skill or Attribute added) |
| **Damage** | 1d6 \+ 4 Bludgeoning (Punch) − target's AR |

Both STR and END stay within Threat Level 1's caps, but this is a heavier build than the cap − 3 offset would give you - untrained, unarmored fodder needs real STR/END to hold up once 8 of them are swinging at once, which is exactly the retuning finding above.

### Average - Bandit Cutthroat (field 6 for a 4-player party)

| **Bandit Cutthroat** | Threat Level 1 - Average |
| :---- | :---- |
| **Attributes** | STR 4, PRE 1, END 3, DEX 1 |
| **Skill** | One-Handed Blades 1 (trained) |
| **Wounds** | 3 |
| **Armor** | Gambeson - AR 2, Penalty 1 |
| **Evasion** | 5 |
| **Weapon** | Shortsword (1d6 \+ 1 Piercing, Light) |
| **Attack** | 1d12 \+ 1 \+ 4 \= 1d12 \+ 5 vs. target's Evasion |
| **Damage** | 1d6 \+ 1 (Shortsword) \+ 4 (STR) − target's AR |

STR sits at Threat Level 1's Attribute cap. Trained vs. Easy's untrained is now the load-bearing difference between these two Roles - their Attribute/END/gear ended up nearly identical once both were retuned to their own fielded counts.

### Elite - Bandit Captain (field 4 for a 4-player party)

| **Bandit Captain** | Threat Level 1 - Elite |
| :---- | :---- |
| **Attributes** | STR 4, PRE 1, END 4, DEX 2 |
| **Skill** | One-Handed Blades 2 |
| **Wounds** | 4 |
| **Armor** | Mail Shirt - AR 4, Penalty 2 |
| **Evasion** | 5 |
| **Weapon** | Broadsword (1d10 Slashing) |
| **Attack** | 1d12 \+ 2 \+ 4 \= 1d12 \+ 6 vs. target's Evasion |
| **Damage** | 1d10 \+ 4 − target's AR |
| **Signature trait** | Ambush Leader - Advantage on its first Attack Roll of the fight |

Sits right at Threat Level 1's cap. Armor upgraded from Buff Coat to Mail Shirt during retuning - still Flexible, still a bandit-plausible step up rather than a leap to Rigid plate.

### Mythic - The Timber Fang (1 for the whole 4-player party)

| **The Timber Fang** | Threat Level 1 - Mythic |
| :---- | :---- |
| **Attributes** | STR 4, PRE 1, END 4, DEX 3 |
| **Skill** | Brawling 2 (natural weapons) |
| **Wounds** | 4 |
| **Natural Armor** | Thick hide - AR 2, Penalty 1 (Flexible: AR ÷ 2, rounded down) |
| **Evasion** | 7 |
| **Weapon** | Bite (1d8 Piercing) |
| **Attack** | 1d12 \+ 2 \+ 4 \= 1d12 \+ 6 vs. target's Evasion |
| **Damage** | 1d8 \+ 4 − target's AR |
| **Mythic Initiative (3)** | Rolls initiative 3 times (normal, \-2, \-4); takes a full turn on each count |
| **Unique ability, 1/round - Howl** | Every creature within 20 ft: MIND Ward (DC 12, Tricky) or Frightened until the end of its next turn |

Builds exactly like Elite - no Wounds bump; its survivability is Mythic Initiative, not a bigger pool. X \= 3 for this 4-player party - a serious threat to most of the party at once without being guaranteed to overwhelm it.

---

## Encounter Budgeting

Once you've got a roster built, `progression_&_rewards.md`'s Rewards & Treasure section (Minor/Average/Grand Encounter XP tiers) is still the tool for pricing the fight as a whole and handing out its reward - Threat Level and Role tell you what a single NPC is worth in a fight, that section tells you what the fight is worth to the party once it's over.