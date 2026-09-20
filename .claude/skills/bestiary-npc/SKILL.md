---
name: bestiary-npc
description: Generate, hand-validate, and write generic Ressam bestiary NPCs (animals, undead mooks, mercenaries, vermin, and similar stock creatures that don't need the user's creative input) into core/bestiary/*.md. tools/power_score.py, tools/creature_rating.py, and tools/encounter_rating.py are currently stale (they model a deleted combat system) and are not used - validation is done by hand against reference.md's formulas until those tools are rebuilt. Use when asked to add NPCs/creatures/monsters to the bestiary, "generate some generic ones," or similar - NOT for a creature the user wants to design themselves or one central to a specific piece of Ressam lore (build those together, then still run the Validate step on the result).
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

Build all four Attributes (STR, DEX, MIND, CHA - 0 for anything untrained/irrelevant),
only the Skills actually relevant to the creature's kit, and any Feats. Ground every
number in something real:

- **Match an existing power tier unless there's a reason not to.** `core/bestiary/universal.md`'s
  existing entries are the working examples of each rough tier - Peasant (untrained
  fodder), Bandit/Guard/Wolf/Skeleton/Giant Rat/Archer (trained but unremarkable, sits
  at or under a Level 1 PC's budget), Bear (a real step up, Daggers & Wrestling 3
  backed by STR 4), Knight (a maxed specialist, Skills sitting at or near their
  governing Attributes, both around 3-4). Building a new "trained but unremarkable"
  creature? Start from Bandit's shape (Attribute 2-3 range, one Skill at rank 1-2, no
  Feats) and reskin the weapon/flavor rather than inventing new numbers from nothing.
- **Weapon/armor come from `core/equipment/weapons.md` and `armor.md`**, or `reference.md`'s
  armor table for common picks. Don't invent a damage die or a Dent/Rend pair - and
  don't forget a weapon's **Attacks** modifier, which now directly sets the creature's
  Tempo Pool size.
- **Tempo Pool, Parry, Attack, Damage, Initiative, Wards** all follow fixed formulas -
  see `reference.md`. Compute these by hand once you've picked Attributes/Skills/gear;
  cross-checking against `tools/` isn't available right now (see the Validate section's
  own caveat below).
- **Movement is the one field on the sheet that's a judgment call, not a formula** -
  see `reference.md`'s Movement section for the race Base Speed table and how to reason
  about an animal/monster with no race to borrow from.
- **Size** defaults to Medium (5 Wounds baseline) unless there's a real reason
  (Giant Rat is Small/4, Bear and the Wyrm are Large/6 and Huge/7) - see `reference.md`'s
  Wounds table.
- **Mythic Initiative is a different category, not a bigger stat block** - see step 4.

## 2. Validate

**Every tool this stage used to call is currently stale.** `tools/power_score.py`,
`tools/creature_rating.py`, and `tools/encounter_rating.py` all sit on top of
`tools/combat_engine.py`, which models the Oppose/Reaction combat system deleted at
the 2026-08-23 Exchange merge - and the whole bestiary has since fallen behind a
second time, at the 2026-09-20 Reach/Tempo rework, on top of that. **Do not run these
tools and do not quote a number from them** - see `CLAUDE.md`'s `tools/` bullet and
`TODO.md`'s bestiary/tooling item for the full state. Rebuilding this stage against
the current rules is tracked, cross-session work, not something to patch ad hoc while
writing one creature.

Until that rebuild happens, validate by hand and by comparison instead:

1. **Compute the creature's Tempo Pool, Parry, Attack, Damage, and Initiative directly**
   from `reference.md`'s formulas and sanity-check them against the nearest existing
   entry in `core/bestiary/universal.md` of a similar concept and power tier (a new
   "trained but unremarkable" human should read close to Bandit/Guard, not wildly
   above or below).
2. **Check every Skill against its governing Attribute** (Rank <= Attribute, per
   `core_rules.md`) and every Ward against `5 + Attribute` - see the Gotchas below for
   specific Skill-governance mistakes made here before.
3. **Sanity-check Wounds, Dent/Rend, and damage dice against the target's rough
   intended survivability** - does a party at the level this creature is meant to
   threaten land Wounds on it at a reasonable clip, and does it land Wounds back? This
   is judgment, not a formula, until the simulation tools exist again.
4. **Flag anything that reads like a real outlier** (a much higher Attribute/Skill
   total than its peers, an ability that hits an entire party with no roll and no
   cost) explicitly in the write-up rather than silently shipping it - the Wyrm's
   breath weapon and the Skeleton's Vulnerability are both precedents for calling this
   out even without a simulator backing the call.

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
   any), a `Wounds / Dent / Rend / Tempo Pool / Initiative` table, `**Wards:**`,
   `**Parry:**` (the formula and what's funding it - weapon, shield, bare hands),
   `**Movement:**` (walking Speed in feet, plus flying/climbing if any - see
   `reference.md`), `**Equipment:**` or `**Natural Weapons:**`, `**Damage:**` (spelled
   out as weapon dice \+ Attribute, since the table above doesn't have room for it),
   `**Size:**` (if non-Medium), **Damage Types** (if the creature has a Resistance/
   Vulnerability/Immunity), `**Mythic Initiative**`/signature ability (Mythical entries
   only), `**In Combat:**`, and an optional `**Variant:**`/`**Fielding Guide:**`. Match
   `core/bestiary/universal.md`'s current entries field-for-field rather than an older
   example - the shape changed with the Reach/Tempo rework.
4. Follow `CLAUDE.md`'s content conventions: hyphens only (no em/en dashes), and
   backslash-escape literal `+`, `-`, `=` etc. in the Markdown source (e.g.
   `1d6 \+ 3`, `Dent 7 / Rend 12, Penalty \-2`) to match how the rest of the file is
   written.
5. **Report the computed numbers back to the user alongside the write** - Wounds,
   Dent/Rend, Tempo Pool, and any flags from step 2.4 - the same way this pipeline's
   results have been reported all session. Don't just silently write the file and call
   it done.

## 4. Mythic creatures specifically

Only if the creature is meant to be a singular, campaign-defining threat. Read
`core/bestiary/mythical.md`'s own intro note first. Give the creature Mythic
Initiative(X) per `bestiary_overview.md`'s Mythic Initiative section (X = roughly how
many PCs it's meant to threaten alone, 2-4) - its Tempo Pool refills in full on its
first count and regains 1 die on each count after. If it has a signature AoE ability,
price its damage by comparison to the Wyrm's Dragonfire Breath (below) rather than by
eyeballing a comparable working's damage dice at face value - an ability that hits an
entire party with no roll and no cast cost needs to deal much less damage than a
single-target working of the same dice size, precisely because it skips the cost a
working pays for that reach. There is no simulator to run this through right now (see
the Validate section's caveat) - state your reasoning for the number in the write-up
instead of a bare figure.

## Gotchas (found the hard way - don't repeat them)

- **Ward governing-Skill mistakes are easy.** Perception is DEX-governed, not MIND.
  Check `reference.md`'s Skill Categories table for every Skill on the sheet, not just
  the one that "feels" right.
- **A creature's Tempo Pool comes from its weapon's (and shield's) Attacks modifier,
  never from an Attribute.** `+1` for a Light weapon or a natural weapon (bites, claws,
  and slams default to Light-equivalent), `-1` for Two-Handed, `+0` otherwise, on top
  of the baseline 4. Don't reach for DEX when sizing a creature's pool - that formula
  was deleted in the Reach/Tempo rework.
- **A completely untrained creature (0 Skills, 0 Feats) is still weak even with high
  Attributes** - Attributes never touch a Skill Check or an attack/Parry roll at all
  (only Skill does, per `core_rules.md`'s Skill Check Formula), so a creature's raw
  Attributes alone buy it nothing offensively. Peasant (STR 1, no Skills) is the
  working example: its Parry and Attack are both a bare `1d12`, no modifier at all.
- **An AoE ability that hits the whole party with no attack roll and no cast risk needs
  to deal much less damage than a single-target working of the same dice size** - see
  the Wyrm's Dragonfire Breath entry and its in-line note on why its damage was tuned
  down twice.
- **A creature's Power Score-style "how strong is this on paper" read and how it
  actually plays in a simulated fight are different axes and can diverge completely** -
  don't assume a creature with a high Attribute/Skill investment automatically performs
  well in a straight fight, or vice versa. Flag a mismatch explicitly rather than
  silently smoothing it over, the way the Wyrm and a hypothetical high-investment,
  action-economy-starved solo caster would diverge if either were actually simulated.
- **Damage-type Resistance/Vulnerability/Immunity has to be called out explicitly in
  the write-up** (Skeleton's Blunt Vulnerability, Zombie's Piercing Resistance) since
  there's no tool right now to catch a creature that should have one and doesn't.