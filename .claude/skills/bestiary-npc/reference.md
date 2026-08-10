# Ressam bestiary reference tables

Copied from `core/` so `bestiary-npc` doesn't have to re-grep the rulebook on every
invocation. If a number here ever looks wrong, trust the cited source file over this
copy and update this file to match.

## Skill Categories (core_rules.md) - which Attribute governs which Skill, and therefore
which Skill can drive that Attribute's Ward

| Attribute | Category | Skills |
|---|---|---|
| STR | Brawn & Melee | Blades, Hafted Weapons, Polearms, Brawling |
| PRE | Finesse & Ranged | Archery, Marksmanship, Thrown |
| END | Defense & Survival | Athletics, Armorer, Survival, Shields, Riding |
| DEX | Adroitness & Subterfuge | Acrobatics, Stealth, Lockpicking, Sleight of Hand, Crafting, Perception |
| MIND | Intellectual | Alchemy, Enchanting, Spell Crafting, Historic Lore, Medical Lore, Nature Lore, Identify |
| ARC | Arcane Schools | Arcane Lore, Aeromancy, Geomancy, Hydromancy, Pyromancy, Shadowmancy |
| FAI | Divine Schools | Religious Lore, Benediction, Invocation, Necration, Cultivation, Subjugation |
| CHA | Socialising & Interaction | Persuasion, Deception, Intimidation, Leadership, Animal Handling, Insight, Performance |

**Ward formula:** `Ward[Attr] = 5 + Attribute` - Skill no longer contributes to Ward at
all. Evasion is the same shape: `5 + DEX - Armor Penalty`.

**Skill cap:** a Skill's Rank can never exceed its own governing Attribute's current
score (core_rules.md) - there is no separate level-gated Skill cap table anymore. When
building an NPC, a Skill Rank higher than that Skill's governing Attribute is an
illegal build, not a strong one - check every trained Skill against its Attribute in
the table above.

**Agility was removed as a Skill (2026-08-08).** Dodge Style now rolls `1d12 + DEX -
Armor Penalty` directly - no Skill of any kind, just a `DEX >= 1` prerequisite (see
maneuvers.md). Don't add "Agility" to any NPC's Skills list; when giving a creature
Dodge, its bonus is derived purely from DEX (and Armor Penalty), nothing else.

## Points / Feats by Level (progression_&_rewards.md)

Attribute Points and Skill Points are two separate budgets, no conversion between them
(`character_creation.md`'s "Distribute Points") - check an NPC's Attribute sum against
the ATTR Points column, its Skill-rank sum against the SKILL Points column
independently, and the Attribute Cap ceiling on any single Attribute.

| Level | Total XP | ATTR Points | SKILL Points | ATTR Cap | Feats |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 30 | 18 | 12 | 4 | 2 |
| 2 | 120 | 18 | 14 | 4 | 2 |
| 3 | 270 | 18 | 16 | 4 | 2 |
| 4 | 480 | 19 | 18 | 4 | 3 |
| 5 | 750 | 19 | 20 | 4 | 3 |
| 6 | 1080 | 19 | 22 | 4 | 4 |
| 7 | 1470 | 19 | 24 | 4 | 4 |
| 8 | 1920 | 20 | 26 | 5 | 4 |
| 9 | 2430 | 20 | 28 | 5 | 5 |
| 10 | 3000 | 20 | 30 | 5 | 5 |
| 11 | 3630 | 20 | 32 | 5 | 5 |
| 12 | 4320 | 21 | 34 | 5 | 6 |

A Prestige Feat (prestige_feats.md) forces Effective Level >= 5 regardless of Feat
count ("Can take a Prestige Feat" first appears at Level 5).

## Wound Thresholds (wounds_and_survival.md) - keyed to the DEFENDER's own END

At END `e`: 1 Wound on damage-after-AR of 1 to `6+e`; 2 Wounds on `7+e` to `12+e`;
3 Wounds on `13+e` or more.

**Stat block phrasing:** every entry in `core/bestiary/` carries a `**Wound Threshold:**`
line, right after the Wounds/Evasion/AR/Attack/Damage/Initiative table, spelled out as
three bands so a GM never has to re-derive it from raw END mid-fight - e.g. END 2 reads
`**Wound Threshold:** 1 Wound (1-8), 2 Wounds (9-14), 3 Wounds (15+).` Compute it from
the defender's own END using the formula above, don't copy another entry's band by eye.

**Max Wounds = Size baseline + Feats** (Tough, etc.) - NOT tied to END.

| Size | Wounds baseline | Space | Reach |
|:---:|:---:|:---:|:---:|
| Small | 2 | 5 ft (1x1) | Short |
| Medium | 3 | 5 ft (1x1) | Short |
| Large | 4 | 10 ft (2x2) | Medium |
| Huge | 5* | 15 ft (3x3) | Long |

\*Huge's Wounds baseline (5) extrapolates the +1-per-step pattern - `wounds_and_survival.md`
only tables Small/Medium/Large explicitly and says a GM is free to keep scaling past
Large. Bigger-than-Huge: keep extrapolating +1/step unless a reason says otherwise.

## Armor (armor.md)

| Armor | AR | Penalty | Notes |
|---|:---:|:---:|---|
| Gambeson | 2 | -1 | Flexible |
| Buff Coat | 3 | -1 | Flexible |
| Mail Shirt | 4 | -2 | Flexible |
| Chain Mail | 5 | -2 | Flexible |
| Brigandine | 6 | -3 | Flexible |
| Breastplate | 6 | -6 | Rigid |
| Half-Plate | 7 | -7 | Rigid |
| Full Plate | 8 | -8 | Rigid |

Flexible Penalty = floor(AR / 2). Rigid Penalty = AR. A Heater Shield adds +2 AR while
Blocking specifically (not to passive AR) and -1 Penalty always.

## Movement (races_overview.md / individual race files)

Every entry in `core/bestiary/` carries a `**Movement:**` line - walking Speed in feet,
plus a secondary Speed (flying, climbing) if it has one. Armor Penalty does NOT reduce
this - it only hits Acrobatics/Stealth/spellcasting/Evasion (see Armor table above), so
don't discount a heavily-armored humanoid's Movement for its gear.

For a human-equivalent NPC (Peasant, Bandit, Guard, Archer, Knight, and similar), match
Human's own Base Speed unless the flavor calls for a deliberate outlier:

| Race | Base Speed |
|---|:---:|
| Humans, Orkhs, Dzinari, Tapio | 30 ft |
| Dwergaz, Tembels | 25 ft |
| Aelves, Feliids, Strygs | 35 ft |

For an animal or monster with no race to borrow from, ground the number in the
creature's own flavor rather than defaulting to 30 ft - a pack predator or something
built to close distance fast (Wolf, Bear) reads faster (35-40 ft), a deliberately slow
or shambling threat (Zombie) reads slower (10-20 ft), and a flier gets both a low
walking Speed and a separate, higher flying Speed (Giant Vulture: `10 ft, flying speed
40 ft`). Say so in one clause if the number isn't self-evidently 30 ft, the way Zombie's
and Bear's entries do - a bare number with no justification is the one field on this
checklist that's pure judgment call, not a formula, so leave a trail for why it landed
where it did.

## DC Tiers (core_rules.md)

Very Easy 5, Easy 7, Medium 9, Tricky 10, Hard 12, Grueling 14, Very Hard 16,
Incredibly Hard 17, Impossible 20.

## Initiative and Reactions

`Initiative bonus = (PRE + DEX) // 2` (integer division). `Reactions/round` is a pure
DEX threshold: DEX 0-2 -> 1, DEX 3-4 -> 2, DEX 5 -> 3.

## Frequency scale (bestiary_overview.md)

Common (default filler) -> Uncommon (shows up with intent) -> Rare (party should
remark on it) -> Very Rare (closer to a plot beat than a random fight). Sort entries
within a section in that order.