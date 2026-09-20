# Ressam bestiary reference tables

Copied from `core/` so `bestiary-npc` doesn't have to re-grep the rulebook on every
invocation. If a number here ever looks wrong, trust the cited source file over this
copy and update this file to match.

**2026-09-20: rewritten wholesale.** The previous version of this file predated the
2026-08-11/12 Attribute merge (it still listed PRE, END, ARC and FAI as live
Attributes), the 2026-08-23 Exchange merge (Evasion, Dodge Style, Reactions/round,
`maneuvers.md`), and the Reach/Tempo rework (Dent/Rend Lines, the four-tier DC ladder,
the current Tempo Pool and Initiative formulas) all at once. Every section below is
current as of the Reach/Tempo rework; see `CLAUDE.md` and `TODO.md` for the full
rework history if a number here ever needs re-deriving from scratch.

## Attributes and Skill Categories (core_rules.md, attributes_and_skills.md)

Four Attributes only: **STR, DEX, MIND, CHA** - ARC, FAI, PRE, and END are all deleted
(END merged into STR, PRE into DEX, ARC/FAI removed outright when magic schools became
Feats instead of Skills).

| Attribute | Category | Skills |
|---|---|---|
| STR | Brawn, Endurance & Melee | Two-Handed Blades, Cleaving Blades, Hafted Weapons, Polearms, Daggers & Wrestling, Athletics, Survival, Wayfaring |
| DEX | Finesse, Reflex & Subterfuge | Fencing Blades, Archery, Firearms, Thrown, Acrobatics, Subterfuge, Crafting, Perception, Chirurgery |
| MIND | Intellect, Education & Reasoning | Thaumaturgy |
| CHA | Socialising, Manipulation & Interaction | Influence, Manipulate, Intimidate, Leadership, Insight |

**Magic schools are Feats, not Skills** (Aeromancy, Geomancy, Hydromancy, Pyromancy,
Shadowmancy, Benediction, Cultivation, Invocation, Necration, Subjugation) - see
`magic_feats.md`. No Skill or Attribute is added to a casting roll at all; MIND only
sets the Will pool and the dice ceiling (see Casting, below).

**Ward formula:** `Ward[Attr] = 5 + Attribute`. There is no Evasion, Dodge Style, or
any other passive defense score - a melee attack is answered by a Parry (funded by
Tempo Dice) or it simply lands; a shot or a working is answered by a Shot DC or a
resist roll, never a flat defender-side number.

**Skill cap:** a Skill's Rank can never exceed its own governing Attribute's current
score (core_rules.md) - there is no separate level-gated Skill cap table. When
building an NPC, a Skill Rank higher than that Skill's governing Attribute is an
illegal build, not a strong one - check every trained Skill against its Attribute in
the table above.

## Points / Feats by Level (progression_&_rewards.md)

**Attributes are a standard array, not a point pool.** A PC's four Attributes come
from a fixed set of numbers picked by their Attributes priority letter (A: `3, 2, 1,
0` / B: `2, 2, 1, 0` / C: `2, 1, 1, 0` / D: `1, 1, 1, 0` / E: `1, 1, 0, 0`), plus
**\+1 to one Attribute at levels 4, 8 and 12** - that is the whole of Attribute
growth. Skills remain a real point budget (18/15/12/9/6 by priority, \+2/level
thereafter). Check an NPC's Attribute sum against the ATTR Total column below (the
largest total any PC of that Level could hold, i.e. A's array plus banked increases),
its Skill-rank sum against the SKILL Points column independently (shown here at **C**
priority), and the Attribute Cap ceiling on any single Attribute.

| Level | Total XP | ATTR Total | SKILL Points | ATTR Cap | Feats |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 30 | 6 | 12 | 3 | 2 |
| 2 | 120 | 6 | 14 | 5 | 2 |
| 3 | 270 | 6 | 16 | 5 | 2 |
| 4 | 480 | 7 | 18 | 5 | 3 |
| 5 | 750 | 7 | 20 | 5 | 3 |
| 6 | 1080 | 7 | 22 | 5 | 4 |
| 7 | 1470 | 7 | 24 | 5 | 4 |
| 8 | 1920 | 8 | 26 | 5 | 4 |
| 9 | 2430 | 8 | 28 | 5 | 5 |
| 10 | 3000 | 8 | 30 | 5 | 5 |
| 11 | 3630 | 8 | 32 | 5 | 5 |
| 12 | 4320 | 9 | 34 | 5 | 6 |

**ATTR Cap is a flat ceiling (5) from Level 2 on, not a stepped one** - `progression_&_rewards.md` states the cap this way because a racial modifier can push a score to 5 well before a character's own Level-4/8/12 increases would; it is not a claim that an ungifted Level 2 NPC can naturally reach 5 in an Attribute (its own array plus increases-so-far still governs that - see ATTR Total).

**An Attribute can sit below 0** (a racial modifier landing on an array 0), which is
legal. **Will floors at 0, Slots floor at 1** (`6 + STR`, minimum 1). **The Tempo Pool
no longer reads an Attribute at all** - see Tempo Pool, below.

A Prestige Feat (`prestige_feats.md`) forces Effective Level >= 5 regardless of Feat
count ("Can take a Prestige Feat" first appears at Level 5).

## Wounds (rest_and_survival.md)

**Max Wounds = Size baseline + Feats** (Tough, etc.):

| Size | Wounds baseline | Space |
|:---:|:---:|:---:|
| Small | 4 | 5 ft (1x1) |
| Medium | 5 | 5 ft (1x1) |
| Large | 6 | 10 ft (2x2) |
| Huge | 7* | 15 ft (3x3) |

\*Huge extrapolates the \+1-per-step pattern - `rest_and_survival.md` only tables
Small/Medium/Large explicitly and says a GM is free to keep scaling past Large.
Bigger-than-Huge: keep extrapolating \+1/step unless a reason says otherwise.

**There is no separate Wound Threshold table any more.** A landing hit rolls weapon
dice \+ STR (missiles: no Attribute) and compares straight to the target's **Dent
Line and Rend Line** (see Armor, below, and `combat.md`'s Damage Roll) - below Dent is
Turned Aside, at or above Dent is 1 Wound, at or above Rend is 2. An Unarmored target
reads Dent 0 / Rend 5 instead of a bottomed-out pair of lines. **Stat block phrasing:**
give every entry a `Dent / Rend` column in its main stat table (or "Unarmored" /
"Natural hide (X / Y)" for a creature with no worn armor) instead of a separate
Wound Threshold line - there's nothing left to precompute per-defender.

## Tempo Pool, Parry, and Initiative (exchange.md)

**Tempo Pool = 4, plus the equipped weapon's (and shield's) Attacks modifier** -
`+1` for a Light weapon, `-1` for a Two-Handed one, `+0` for everything else. Every
die is a flat `1d12`; no Attribute sizes the pool or counts the dice. A natural
weapon (bite, claws, slam) defaults to `+1` Attacks, the same as Unarmed, unless the
creature's concept calls for something heavier or lighter.

**Parry:** `1d12 (per invested die) + Weapon Skill + Guard`, at 1 die invested for a
baseline stat block - note in the entry that more dice can be invested exactly like
a PC would. No Attribute, no Edge, no Evasion.

**Attack roll:** `1d12 (per invested die) + Weapon Skill`, same shape as a Parry. A
Skill Rank of 0 (untrained) rolls the bare die.

**Damage:** Weapon Damage \+ STR (missiles: no Attribute added).

**Initiative:** `5 + DEX`, static, never rolled.

**Shot DC (for a ranged NPC to present as a target):** `7 + DEX`, plus whatever
situational modifiers apply (see `exchange.md`'s Shot DC table). A ranged NPC's own
shot invests Tempo Dice exactly like a melee attack - see The Shot in `exchange.md`.

## Armor (armor.md)

| Armor | Dent | Rend | Penalty | Flexible/Rigid |
|---|:---:|:---:|:---:|---|
| Unarmored | 0 | 5 | - | - |
| Gambeson | 5 | 10 | -1 | Flexible |
| Buff Coat | 6 | 11 | -2 | Flexible |
| Mail Shirt | 6 | 11 | -2 | Flexible |
| Chain Mail | 6 | 11 | -2 | Flexible |
| Brigandine | 7 | 12 | -2 | Flexible |
| Breastplate | 7 | 12 | -2 | Rigid |
| Half-Plate | 9 | 14 | -3 | Rigid |
| Full Plate | 11 | 16 | -3 | Rigid |

A natural Dent/Rend pair (thick hide, scales, a shell) doesn't have to match a named
armor exactly - pick whichever row reads closest to the creature's fictional
toughness, or interpolate, and say so in one clause (see Movement's own note on
leaving a trail for judgment calls). **A Heater Shield-equivalent natural feature**
adds Guard to Parries and counts as Light cover against a shot; it does not touch
Dent/Rend. Nothing in a fight reads Armor Penalty - it restricts Acrobatics and
Subterfuge checks only.

## Movement (races_overview.md / individual race files)

Every entry in `core/bestiary/` carries a `**Movement:**` line - walking Speed in
feet, plus a secondary Speed (flying, climbing) if it has one. Armor Penalty does NOT
reduce this - it only hits Acrobatics/Subterfuge checks, never Speed and nothing in a
fight - so don't discount a heavily-armored humanoid's Movement for its gear.

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

Easy 5, Standard 7, Hard 9, Extreme 11 - the same ladder magic's Lesser/Common/
Greater/Legendary tiers use. Situational modifiers stack on top of the base tier;
don't invent a number outside this list for the base itself. Set a Ward (see Ward
formula, above) one tier below the same fiction as a Skill Check, and keep an
unannounced hazard at Hard (9) or below.

## Fear and Morale (exchange.md, rest_and_survival.md)

A creature may carry a **Fear rating** (Terror 7 or Dread 9) - enemies test a
Will-funded resist the first time they try to close with it. Separately, **Nerve**
(`1d12 + CHA` vs. Standard DC 7) governs Unnamed creatures Breaking under set triggers
(reduced to their last Wound box, their side crossing half strength, and so on - see
`exchange.md`'s Morale section for the full trigger list). Neither is required on
every entry; add a Fear rating only where the fiction calls for something genuinely
dreadful, and let ordinary Nerve triggers apply by default without restating them
per entry.

## Frequency scale (bestiary_overview.md)

Common (default filler) -> Uncommon (shows up with intent) -> Rare (party should
remark on it) -> Very Rare (closer to a plot beat than a random fight). Sort entries
within a section in that order.
