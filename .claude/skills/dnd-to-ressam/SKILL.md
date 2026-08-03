---
name: dnd-to-ressam
description: Convert a D&D 5e monster statblock into Ressam, grounded in this repo's actual rules and reference tables (core_rules.md, combat.md, core/equipment/weapons.md, core/equipment/armor.md, ENCOUNTER_GUIDE.md) rather than invented mechanics. Always outputs in the exact locked statblock template in this file. Use whenever the user pastes a 5e statblock and asks for a Ressam version, asks to "convert," "port," or "translate" a D&D monster, or asks to build a Ressam bestiary entry from a 5e source.
---

# D&D 5e -> Ressam monster conversion

This is a math-fidelity conversion skill, not a vibes conversion. Every derived
number must trace back to a formula that actually exists in this repo right
now - re-read the source files each run rather than trusting memorized values
from a past conversion, since `core_rules.md`/`combat.md`/`core/equipment/`
can change.

Ressam has **no bestiary or monster schema** of its own yet - this is a
from-scratch statblock built out of player-facing mechanics (Evasion, AR,
Ward, Wounds, weapon skills). Nothing here writes into `core/`. Output goes
directly in the chat response unless the user explicitly asks to save it to a
file, in which case ask where (there is no existing bestiary location to
default to).

## Required reading, every time

Do not skip this even on a second/third conversion in the same session -
grep for the current line numbers, don't reuse ones from memory:

- `core/core_rules.md` - Wounds, Wards, Skills, DC tiers, Trauma, Slots
- `core/combat/combat.md` - Evasion, AR/damage, attack rolls, initiative, crits, conditions
- `core/equipment/weapons.md` and `core/equipment/armor.md` - **reuse an
  existing weapon/armor entry whenever the 5e monster's gear has a plausible
  Ressam equivalent** (matching dice size/damage type is a strong signal,
  e.g. 5e's "shortsword, 1d6 piercing" -> Ressam's actual `Shortsword`
  entry). Only invent new stats when nothing in these tables is close - and
  if you do, say so explicitly rather than silently presenting invented
  numbers as if they were pulled from the book.
- `ENCOUNTER_GUIDE.md` - use its "Stat Ranges by Tier" tables (HP/AR/
  Evasion/to-hit/damage per level range, Tiers 1-4 covering levels 1-12) as
  the calibration ruler for "what does a level-N monster's Evasion/attack-
  bonus/Wounds look like," and its four archetypes (Brute/Tank/Skirmisher/
  Caster) to pick the source monster's defensive identity. Never calibrate a
  monster in a vacuum - always check it against the tier nearest the target
  encounter level. **Note:** this guide's own tables are the source of truth
  for monster stats specifically (they're deliberately monster-scaled, not a
  player-character stand-in) - don't try to reverse-engineer a player build's
  stats as a substitute.

## The six-step process

### 1. Parse the input statblock
Extract: name, size/type/alignment, AC, HP (+ hit dice if shown), Speed,
all six-ish ability scores, saves, skills, resistances/immunities/
vulnerabilities, senses, languages, CR/XP, and every trait/action/reaction/
legendary action verbatim.

### 2. Defensive conversion
- **HP -> Wounds**: Ressam has no CON-equivalent toughness stat separate from
  Wounds math. `Maximum Wounds = END` (`core_rules.md`, grep `Maximum
  Wounds`) - a 1-5 range, nowhere near 5e's HP scale (10s to 100s), so do
  **not** attempt to reverse-solve END proportionally from the source
  monster's raw HP number. Instead, translate the source monster's
  *toughness role* (how many solid hits it should take to go down) into
  END directly, calibrated against `ENCOUNTER_GUIDE.md`'s Wounds range for
  the nearest tier/level - a monster meant to survive a couple of solid hits
  from an equal-level PC wants END near the top of that tier's range, a
  glass-cannon or mook wants END near the bottom. Then sanity-check the
  result against the Damage -> Wounds thresholds (`core_rules.md`'s Wounds
  and Survival: 1-9 dmg = 1 Wound, 10-15 = 2, 16+ = 3) using a typical hit at
  that tier - note explicitly how many hits-to-drop that implies, since
  that's the actual lever now, not a bigger END number. Flag this whole step
  as a judgment call, not a formula reversal.
- **AC -> Evasion**: `Evasion = 5 + Agility(skill) + DEX - Armor Penalty`
  (`combat.md`, grep `Evasion \=`). Pick Agility rank + DEX attribute + Armor
  Penalty to land Evasion in the right relative band versus
  `ENCOUNTER_GUIDE.md`'s Evasion range for the nearest tier - not by porting
  the AC number literally (5e's bounded-accuracy math and Ressam's
  1d12+bonus math are not on the same scale, see `core_rules.md`'s "Coming
  from D&D?" note).
- **AC's armor-like descriptor -> AR**: pick an existing
  `core/equipment/armor.md` entry if the flavor text names real armor; if
  it's vague ("natural armor," "scraps"), assign a small flat AR with no
  Armor Penalty and note it degrades per the normal rule (`combat.md`, grep
  `Degradation`).
- Port resistances/immunities/vulnerabilities to their Ressam equivalents only
  where a matching mechanic actually exists (damage types, the Conditions
  table in `combat.md`, Trauma). Don't invent new immunity types.

### 3. Offensive conversion
- Map each 5e attack to a Ressam weapon skill category via the Skill
  Categories table (`core_rules.md`, grep `Skill Categories`) - melee usually
  STR, ranged usually PRE, unless the weapon has Finesse (`weapons.md`, grep
  `Finesse`) which lets PRE substitute on a STR-category weapon.
  `Attack bonus = weapon skill rank + attribute` (`combat.md`, grep
  `Attack Roll`).
- Calibrate weapon-skill rank + attribute (not the raw 5e to-hit bonus) so the
  resulting hit chance sits in `ENCOUNTER_GUIDE.md`'s to-hit range for the
  nearest tier - show the d12 threshold and resulting probability, don't just
  assert a number.
- `Damage = Weapon Damage (dice + any flat bonus already in the weapon entry)
  + attribute - target AR` (`combat.md`, grep `Damage Roll`). Use the reused
  weapon's actual dice string from `core/equipment/weapons.md`, don't
  reinvent dice.

### 4. Ability scores / skills / Wards
Build a mapping table (5e score+mod -> Ressam attribute 1-5) attribute by
attribute, with a one-line reason each - flag explicitly anywhere you
deviated from a literal proportional port (like the END/Wounds case in step 2).
Assign minimal skill ranks only where the monster actually acts on them
(the weapon skills used, Agility if Evasion needs it, Perception if passive
Perception needs it) - don't pad out a full skill list nothing in the
statblock calls for.

Compute Wards for every attribute the monster has above floor value:
`Ward = 5 + Attribute + best-ranked skill governed by that attribute`
(`core_rules.md`, grep `Ward \\=`). Use 0 for "best governed skill" on
attributes with no assigned skill ranks.

Compute Initiative (`combat.md`, grep `Initiative \\=`) and Passive Perception
(`core_rules.md`, grep `Passive Perception \\=`) the same way.

### 5. Challenge / tier
Ressam has no CR or encounter-budget subsystem. Do not invent one. Instead
give one or two sentences of informal DM guidance benchmarked against
`ENCOUNTER_GUIDE.md`'s tier for the target level (e.g. "fair 1-on-1 for a
level 1 character, dangerous in groups of 3+") and flag clearly that this is
a judgment call, not an authoritative Ressam mechanic.

### 6. Special features
Rewrite each remaining trait/action in Ressam terms, reusing exact
terminology from `combat.md`'s Conditions table and `core_rules.md` wherever
the 5e effect has a real equivalent (Bleeding, Frightened, Grappled, etc. -
grep the Conditions table before inventing new condition language). Flag any
judgment call explicitly - the canonical example is 5e's "monsters just die at
0 HP" convention vs. Ressam's PC-first Dying process in `core_rules.md`
(grep `Dying`): default mooks to **destroyed outright at 0 Wounds** and say so,
rather than silently picking one.

Show your work for all of the above inline before the final statblock - name
the exact formula, the source line/file it came from, and the numbers you
plugged in. This is a rules document; a reader should be able to check your
math without re-deriving it themselves.

## Locked output format

The final statblock **must** follow this structure exactly - same section
order, same bold/italic conventions, same table shape. Fill in the bracketed
parts; do not add, remove, or reorder sections. Omit a line only if the
source monster genuinely has nothing for it (e.g. no ranged attack); never
add sections beyond this template.

```markdown
# [Name]
*[Size] [Type]*

| | |
|---|---|
| **Evasion** | [value] |
| **AR** | [value] ([armor source name]) |
| **Wounds** | [value] |
| **Speed** | [value] ft. |
| **Initiative** | 1d12 + [bonus] |

| STR | PRE | END | DEX | MIND | ARC | FAI | CHA |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [n] | [n] | [n] | [n] | [n] | [n] | [n] | [n] |

**Wards:** [Attribute] [value], [Attribute] [value], ...
**Skills:** [Skill] [rank], [Skill] [rank], ...
**Passive Perception:** [value]
**Senses:** [as ported from source]
**Languages:** [as ported from source]
**Damage Vulnerability:** [type(s), or omit line if none]
**Damage Resistance:** [type(s), or omit line if none]
**Immunities:** [damage types / conditions, or omit line if none]
**Special:** [any porting judgment calls or unique traits that don't fit an action, in plain prose]

**Actions**

*[Weapon/Attack Name].* [Melee/Ranged] Attack: **1d12 + [bonus]** vs. Evasion, [reach/range]. Hit: **[dice] + [attribute] - target's AR** [Damage Type] damage ([weapon properties], crit [range]).

*[Repeat one Actions line per attack/special action]*
```

Match every bolded formula string's shape exactly as shown (`1d12 + [bonus]
vs. Evasion`, `[dice] + [attribute] - target's AR`) - these aren't
placeholders to paraphrase, they're the literal syntax Ressam attack/damage
lines use.
