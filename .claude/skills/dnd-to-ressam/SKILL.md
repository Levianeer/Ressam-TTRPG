---
name: dnd-to-ressam
description: Convert a D&D 5e monster statblock into Ressam, grounded in this repo's actual formulas and data (core_rules.md, combat.md, data/weapons, data/armor, data/builds) rather than invented mechanics. Always outputs in the exact locked statblock template in this file. Use whenever the user pastes a 5e statblock and asks for a Ressam version, asks to "convert," "port," or "translate" a D&D monster, or asks to build a Ressam bestiary entry from a 5e source.
---

# D&D 5e -> Ressam monster conversion

This is a math-fidelity conversion skill, not a vibes conversion. Every derived
number must trace back to a formula that actually exists in this repo right
now - re-read the source files each run rather than trusting memorized values
from a past conversion, since `core_rules.md`/`combat.md`/`data/` can change.

Ressam has **no bestiary or monster schema** of its own yet - this is a
from-scratch statblock built out of player-facing mechanics (Evasion, AR,
Ward, HP, weapon skills). Nothing here writes into `core/` or `data/`; this
skill never touches the generated-content pipeline. Output goes directly in
the chat response unless the user explicitly asks to save it to a file, in
which case ask where (there is no existing bestiary location to default to).

## Required reading, every time

Do not skip this even on a second/third conversion in the same session -
grep for the current line numbers, don't reuse ones from memory:

- `core/core_rules.md` - HP, Wards, Skills, DC tiers, Exhaustion, Carrying Capacity
- `core/combat/combat.md` - Evasion, AR/damage, attack rolls, initiative, crits, conditions
- `scripts/formulas.py` - the same formulas as pure functions (`hp`, `evasion`,
  `attack_bonus`, `damage_bonus`, `ward_dc`, `initiative_bonus`,
  `carrying_capacity`). Prefer computing through these via
  `.venv/bin/python -c "from scripts.formulas import *; print(...)"` over hand
  arithmetic - it's the same source of truth `balance_report.py` uses, so
  numbers stay consistent with the rest of the toolchain.
- `data/weapons/*.yaml` and `data/armor/*.yaml` - **reuse an existing
  weapon/armor entry whenever the 5e monster's gear has a plausible Ressam
  equivalent** (matching dice size/damage type is a strong signal, e.g. 5e's
  "shortsword, 1d6 piercing" -> Ressam's actual `Shortsword` entry). Only
  invent new stats when nothing in the data files is close - and if you do,
  say so explicitly rather than silently presenting invented numbers as if
  they were pulled from the book.
- `data/builds/*.yaml` (Frontline Fighter, Battle Mage, Skirmisher) - use
  `Archetype.snapshot(level)`-equivalent reasoning (starting attributes/skills
  + level deltas) as the calibration ruler for "what does a level-N PC's
  Evasion/attack-bonus/HP look like." Never calibrate a monster in a vacuum -
  always check it against the archetype nearest the target encounter level.

## The six-step process

### 1. Parse the input statblock
Extract: name, size/type/alignment, AC, HP (+ hit dice if shown), Speed,
all six-ish ability scores, saves, skills, resistances/immunities/
vulnerabilities, senses, languages, CR/XP, and every trait/action/reaction/
legendary action verbatim.

### 2. Defensive conversion
- **HP**: Ressam has no CON-equivalent toughness stat separate from HP math.
  `Maximum HP = (END x 3) + 10` (`core_rules.md`, grep `Maximum HP`). Reverse-
  solve END from the 5e monster's average HP rather than porting the CON
  score directly - 5e CON mostly encodes hit-dice count, not toughness, and
  porting it literally produces wildly wrong HP totals. Round END to the
  nearest value that lands closest to the source HP; note the gap if it's
  more than a couple points.
- **AC -> Evasion**: `Evasion = 5 + Agility(skill) + DEX - Armor Penalty`
  (`combat.md`, grep `Evasion \=`). Pick Agility rank + DEX attribute + Armor
  Penalty to land Evasion in the right relative band versus the nearest
  archetype build's Evasion at the target level - not by porting the AC
  number literally (5e's bounded-accuracy math and Ressam's 1d12+bonus math
  are not on the same scale, see `core_rules.md`'s "Coming from D&D?" note).
- **AC's armor-like descriptor -> AR**: pick an existing `data/armor/*.yaml`
  entry if the flavor text names real armor; if it's vague ("natural armor,"
  "scraps"), assign a small flat AR with no Armor Penalty and note it degrades
  per the normal rule (`combat.md`, grep `Degradation`).
- Port resistances/immunities/vulnerabilities to their Ressam equivalents only
  where a matching mechanic actually exists (damage types, the Conditions
  table in `combat.md`, Exhaustion). Don't invent new immunity types.

### 3. Offensive conversion
- Map each 5e attack to a Ressam weapon skill category via the Skill
  Categories table (`core_rules.md`, grep `Skill Categories`) - melee usually
  STR, ranged usually REF, unless the weapon has Finesse (`weapons.md`, grep
  `Finesse`) which lets REF substitute on a STR-category weapon.
  `Attack bonus = weapon skill rank + attribute` (`combat.md`, grep
  `Attack Roll`).
- Calibrate weapon-skill rank + attribute (not the raw 5e to-hit bonus) so the
  resulting hit chance against the nearest archetype's Evasion sits in a
  sensible band for the source monster's CR - show the d12 threshold and
  resulting probability, don't just assert a number.
- `Damage = Weapon Damage (dice + any flat bonus already in the weapon entry)
  + attribute - target AR` (`combat.md`, grep `Damage Roll`). Use the reused
  weapon's actual dice string from `data/weapons/*.yaml`, don't reinvent dice.

### 4. Ability scores / skills / Wards
Build a mapping table (5e score+mod -> Ressam attribute 1-10) attribute by
attribute, with a one-line reason each - flag explicitly anywhere you
deviated from a literal proportional port (like the END/HP case in step 2).
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
Ressam has no CR or encounter-budget subsystem checked into this repo
(`data/progression.yaml` tracks player XP-to-level, a different currency
entirely). Do not invent one. Instead give one or two sentences of informal
DM guidance benchmarked against the nearest `data/builds/*.yaml` archetype at
the appropriate level (e.g. "fair 1-on-1 for a level 1 character, dangerous in
groups of 3+") and flag clearly that this is a judgment call, not an
authoritative Ressam mechanic.

### 6. Special features
Rewrite each remaining trait/action in Ressam terms, reusing exact
terminology from `combat.md`'s Conditions table and `core_rules.md` wherever
the 5e effect has a real equivalent (Bleeding, Frightened, Grappled, etc. -
grep the Conditions table before inventing new condition language). Flag any
judgment call explicitly - the canonical example is 5e's "monsters just die at
0 HP" convention vs. Ressam's PC-first Dying process in `core_rules.md`
(grep `Dying`): default mooks to **destroyed outright at 0 HP** and say so,
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
| **HP** | [value] |
| **Speed** | [value] ft. |
| **Initiative** | 1d12 + [bonus] |

| STR | REF | END | DEX | MIND | ARC | FAI | CHA |
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