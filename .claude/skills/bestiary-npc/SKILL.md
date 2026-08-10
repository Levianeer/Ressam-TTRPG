---
name: bestiary-npc
description: Generate, power/danger-validate, and write generic Ressam bestiary NPCs (animals, undead mooks, mercenaries, vermin, and similar stock creatures that don't need the user's creative input) into core/bestiary/*.md, using tools/power_score.py, tools/creature_rating.py, and tools/encounter_rating.py to self-check balance before presenting anything. Use when asked to add NPCs/creatures/monsters to the bestiary, "generate some generic ones," or similar - NOT for a creature the user wants to design themselves or one central to a specific piece of Ressam lore (build those together, then still run the Validate step on the result).
---

# Bestiary NPC pipeline

Three stages, always in this order: **Design → Validate → Write**. Never skip Validate,
even for something that looks obviously fine - Peasant's attribute total looked fine by
eye too, and it still took a real calculator run to find the untrained-override edge
case (see Gotchas below). Load `reference.md` in this skill's directory before starting
Design - it has every lookup table this pipeline needs, copied from `core/` so you don't
have to re-grep the rulebook each time.

## 0. Scope check

This skill is for creatures that are mechanically simple and don't carry unique lore -
a Wolf, a Skeleton, a town Guard, a Giant Spider. If the user is describing something
that's meant to be a unique, named, story-relevant creature (a specific boss, a
race-specific monster tied to one continent's lore), design it together with them
first - then still run stages 1-2 on the finished build before writing it in, since
that part of the pipeline is universally useful regardless of how the creature was
conceived.

If the user names specific creatures, build those. If they just say "a few generic
ones," pick 2-4 that fill a real gap in the existing roster (check what's already in
`core/bestiary/universal.md` and the relevant continent file first - don't duplicate a
niche that's already covered) rather than picking arbitrarily.

## 1. Design

Build all eight Attributes (STR, PRE, END, DEX, MIND, CHA, ARC, FAI - 0 for anything
untrained/irrelevant), only the Skills actually relevant to the creature's kit, and any
Feats. Ground every number in something real:

- **Match an existing power tier unless there's a reason not to.** `core/bestiary/universal.md`'s
  existing entries are the working examples of each rough tier - Peasant (untrained
  fodder), Bandit/Guard/Wolf/Skeleton/Giant Rat/Archer (trained but unremarkable, sits
  at or under a Level 1 PC's budget), Bear (a real step up, Brawling 3 backed by STR 4),
  Knight (a maxed specialist, Skills sitting at or near their governing Attributes, both
  around 3-4). Building a new "trained but unremarkable" creature?
  Start from Bandit's shape (Attribute 2-3 range, one Skill at rank 1-2, no Feats) and
  reskin the weapon/flavor rather than inventing new numbers from nothing.
- **Weapon/armor come from `core/equipment/weapons.md` and `armor.md`**, or `reference.md`'s
  armor table for common picks. Don't invent a damage die or AR value.
- **Wards, Evasion, Attack, Damage, Initiative, Reactions, Wound Threshold** all follow
  fixed formulas - see `reference.md`. Compute these by hand once you've picked
  Attributes/Skills, but the Validate stage's tools are also a good cross-check since
  it's easy to use the wrong governing Skill for a Ward (see Gotchas).
- **Movement is the one field on the sheet that's a judgment call, not a formula** -
  see `reference.md`'s Movement section for the race Base Speed table and how to reason
  about an animal/monster with no race to borrow from.
- **Size** defaults to Medium (3 Wounds baseline) unless there's a real reason
  (Giant Rat is Small/2, Bear and Wyrm are Large/4 and Huge/5) - see `reference.md`'s
  Size table.
- **Mythic Initiative is a different category, not a bigger stat block** - see step 4.

## 2. Validate

For every creature, in order:

1. **Add a `Creature(...)` entry to `tools/power_score.py`** (attributes dict, skills
   dict, feats count, `has_prestige_feat` if it carries one) and add it to the tuple in
   `main()`. Run `python3 tools/power_score.py`. Read off Effective Level and XP Reward.
   - The untrained-override (Effective Level forced to 0) only fires when Skill
     investment AND Feats AND Prestige are all genuinely zero - don't expect it for
     anything with even one trained Skill.
   - A Prestige Feat forces a Level-5 floor on the Feat axis regardless of count.
2. **Add a matching `Build` factory to `tools/creature_rating.py`** (a module-level
   `combat_engine.Weapon(...)`/`Shield` if it's a new one - or reuse an entry already in
   `combat_engine.WEAPONS`/`SHIELDS`/`ARMORS` - plus a `make_x()` function added to
   `EXAMPLE_CREATURES`). The weapon's `dice` string is the WEAPON's own damage only
   (e.g. `"1d6+1"` for a quality shortsword) - the Attribute is added separately at
   resolution time by the engine, don't double-count it in the dice string.
   Immediately after, run `python3 -c "import sys; sys.path.insert(0,'tools');
   import creature_rating"` as a smoke test before moving on - an `Edit` call near an
   existing `Weapon`/`make_x()` definition can silently swallow or duplicate a
   neighboring line, and that only surfaces as a `NameError` the next time
   something imports that name, not at edit time.
3. **Run `python3 tools/creature_rating.py`.** Read off the creature's win rate and
   tier (Much Worse/Worse/Equal/Better/Much Better) against `combat_engine.BASELINE_PC`
   in a 1-on-1 duel - this is the direct successor to the old `danger_estimate.py`
   offense/durability numbers, just expressed as a tier against a fixed reference PC
   instead of a raw ratio.
4. **Sanity-check the tier against the creature's intended power tier, not just in
   isolation.** A creature with a much higher Power Score than its peers but a similar
   or worse rating tier is a real finding, not a bug to silently fix - say so plainly
   (see the Skeleton and Blood-Rule Pyromancer precedents, now expressed as rating
   tiers instead of danger ratios). A creature that can't land a hit on `BASELINE_PC`
   at all (tier reads Much Worse with a near-zero win rate) is fine ONLY if it's meant
   to be swarm/mob filler (Peasant, Giant Rat) - otherwise it's underpowered and needs
   a look.
5. **If the creature is meant to be fielded in numbers, or is Mythic-tier, run it
   through `tools/encounter_rating.py`'s actual Monte Carlo group fight**
   (`rate_encounter([make_x]*n, trials)` against the 4x `BASELINE_PC` party), not just
   the single-hit `creature_rating.py` number. A headcount sweep (1, 2, 3...) is the
   right validation for "how many is a fair fight," read the same way as
   `creature_rating.py`'s tier (Equal is the target for a fair fight at your intended
   headcount) - `creature_rating.py` alone will not catch an AoE-vs-whole-party ability
   being wildly over-tuned (see the Wyrm's breath weapon retuning in the Gotchas below),
   and it will not catch a solo creature's action-economy problem against 4 PCs at once
   (see the Blood-Rule Pyromancer). For a Mythic creature, set `mythic_turns` on the
   `Build` (combat_engine's Mythic Initiative support) rather than approximating it
   with a bigger stat block.

## 3. Write

1. Pick the right file: `core/bestiary/universal.md` for setting-agnostic creatures,
   `core/bestiary/<continent>.md` for something tied to one region's biome/culture,
   `core/bestiary/mythical.md` for anything carrying Mythic Initiative. Check
   `core/bestiary/bestiary_overview.md`'s Sections list if unsure which continent fits.
2. Pick a Frequency (Common/Uncommon/Rare/Very Rare per `reference.md`) and insert the
   entry in that order relative to what's already in the file (Common creatures first,
   Very Rare last).
3. Match the exact field order and formatting of the existing entries in that file:
   flavor italics, `**Frequency:**`, `**Attributes:**`, `**Skills:**`, `**Feats:**` (if
   any), the Wounds/Evasion/AR/Attack/Damage/Initiative table, `**Wound Threshold:**`
   (three bands, derived from this NPC's own END - see `reference.md`), `**Wards:**`,
   `**Reactions:**`, `**Movement:**` (walking Speed in feet, plus flying/climbing if
   any - see `reference.md`), `**Equipment:**` or `**Natural Weapons:**`, `**Size:**` (if
   non-Medium), `**Mythic Initiative**`/signature ability (Mythical entries only),
   `**In Combat:**`, and an optional `**Variant:**`. Every entry in `core/bestiary/` as
   of 2026-08-07 carries a Wound Threshold and Movement line - don't write a new one
   without both.
4. Follow `CLAUDE.md`'s content conventions: hyphens only (no em/en dashes), and
   backslash-escape literal `+`, `-`, `=` etc. in the Markdown source (e.g.
   `1d6 \+ 3`, `AR 6, Penalty \-6`) to match how the rest of the file is written.
5. **Report the validated numbers back to the user alongside the write** - Effective
   Level, XP Reward, danger ratio, and any flags from step 2.4 - the same way this
   pipeline's results have been reported all session. Don't just silently write the
   file and call it done.

## 4. Mythic creatures specifically

Only if the creature is meant to be a singular, campaign-defining threat. Read
`core/bestiary/mythical.md`'s own intro note first - Power Score cannot represent
Mythic Initiative at all (a Mythic creature at the Attribute/Skill ceiling scores
identically to a non-Mythic creature at the same ceiling), so don't lean on it here.
Give the creature Mythic Initiative(X) per `combat.md` (X = roughly how many PCs it's
meant to threaten alone, 2-4) via the `Build.mythic_turns` field, and if it has a
signature AoE ability, price its damage by running it through
`tools/encounter_rating.py`'s actual fight sim solo against the 4x `BASELINE_PC` party,
not by reading a spell-crafting magnitude table at face value - see the Gotchas below
for why that overshoots badly.

## Gotchas (found the hard way this session - don't repeat them)

- **Ward governing-Skill mistakes are easy.** Perception is DEX-governed, not MIND;
  Shields and Athletics are END-governed. Check `reference.md`'s Skill Categories table
  for every Skill on the sheet, not just the one that "feels" right.
- **A `Build` has no fixed "Style" field.** `combat_engine.py` picks the best legal
  Oppose funding (Weapon Skill/Shields Skill/DEX) fresh on every defended attack,
  per maneuvers.md's own "whichever fits what you're defending with when you react" -
  don't look for a `style="parry"`-style field to set, just give the creature the
  weapon/shield/Skills it actually has and the engine works out how it defends itself.
- **A completely untrained creature (0 Skills, 0 Feats) should score Effective Level 0,
  even if its Attributes are nonzero** - `power_score.py`'s untrained override exists
  because Attributes never touch Skill Check or Attack Roll dice at all, trained or not
  (only Skill does, per core_rules.md's Skill Check Formula) - a creature's raw
  Attributes alone buy it nothing offensively. This was found by running the calculator
  on Peasant and getting the wrong answer on the first pass - don't assume the naive
  three-axis max is right without checking it against a creature that's supposed to be
  harmless.
- **An AoE ability that hits the whole party with no attack roll and no cast risk needs
  to deal MUCH less damage than a single-target spell of the same dice size.**
  `spell_crafting.md`'s Magnitude/Area table prices wide coverage via a DC-to-cast
  penalty; a monster's innate ability that just always works skips that cost entirely,
  so the dice size has to absorb it instead. The Wyrm's breath went from Cataclysmic
  (6d8, a 98.7% solo party-wipe) down to Strong (2d10, a 66.1% "real fight") only after
  actually running it through the sim three times.
- **Power Score and simulated rating are different axes and will diverge, sometimes
  completely.** The Blood-Rule Pyromancer and the Wyrm land on the exact same Effective
  Level and XP Reward despite one losing nearly every simulated fight and the other
  nearly wiping a full party. This is expected, not a bug - report both numbers, don't
  average them into one.
- **`creature_rating.py`/`encounter_rating.py` don't model damage-type Resistance/
  Vulnerability/Immunity.** If a creature has one (Skeleton's Bludgeoning Vulnerability,
  Zombie's Piercing Resistance), say so explicitly in the write-up - the tools' numbers
  don't reflect it.