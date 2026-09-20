# TODO

Cross-session open items - what's actively in flight, why it matters, and what picking it up should look like. Only exists while something is outstanding; its absence means nothing's open, not that it was forgotten.

**Reset 2026-09-20:** the Reach/Tempo/Magic rework (below) folded in and superseded everything the previous reset covered - the Exchange merge, the magic Stage 1/2 chassis, and their open tuning questions are all either done-and-then-replaced or absorbed into the items below. That history lived here in detail through both reworks; it's cleared now, same as last time - the reasoning is preserved in `exchange_log.md` and `CLAUDE.md`, not repeated below.

## The Reach/Tempo/Magic rework - core mechanics done, propagation is open

**2026-09-20:** a full combat/equipment/magic mechanical overhaul, adapted from four standalone playtest drafts at the repo root (`combat_draft.md`, `equipment_draft.md`, `magic_draft.md`, `spells_draft.md`) - MESBG-inspired resolution the drafts tested independently, adopted as the new mainline ruleset per the session's own decision, with what the drafts cut purely for their own one-shot playtest slice (leveling, Feat-gating, the full weapon/armor list, Arcane/Divine flavor split) reintegrated on top rather than dropped. See `CLAUDE.md`'s `core/core_rules.md`, `core/combat/`, `core/equipment/`, `core/magic/`, and `core/rest_and_survival.md` bullets for the itemized mechanical diff against the pre-rework rules - not repeated here.

**Done:** `core_rules.md` (DC ladder recut 7 tiers -> 4), `core/combat/` (`exchange.md`, `combat.md`, `positioning.md`), `core/rest_and_survival.md`, `core/equipment/` (`weapons.md`, `armor.md`, `supplies.md`, `alchemy.md`), `core/magic/` (`magic_overview.md`, `laws_of_magic.md`, `minor_magic.md`, `magic_feats.md`), and the mechanically load-bearing parts of `core/character/` (`character_creation.md`'s Step 8 derived stats, `attributes_and_skills.md`'s Attribute/Skill descriptions, `progression_&_rewards.md`'s stale array fix, `careers.md`'s Skill-name splits) and `core/exploration/` (`traveling.md`, `leadership.md` - stale Surprise/dying/DC references and mount/NPC stat blocks converted to the new schema).

**Open, deliberately deferred (explicit user call, not an oversight) - each needs its own dedicated pass, not a mechanical find-and-replace:**

- **The individual school spell files.** `core/magic/arcane/*.md` and `core/magic/divine/*.md` still describe every spell in the old Mana-Cost/flat-modifier/Spell-Attack-vs-Overcome shape. Converting each to the new Lesser/Common/Greater/Legendary tier shape is real per-spell design work (tier, dice, resist-shape), not a terminology swap - treat it as the same pass as the pre-existing "spell lists need a rebalance and expansion" item below, not a second one. `DESIGN_GUIDE.md`'s Spell Design Guidelines and Magic Feat Guidelines sections are flagged stale in-place and should be rewritten in the same pass.
- **`core/feats/`** (`general_feats.md`, `martial_feats.md`, `skill_feats.md`, `prestige_feats.md`, `racial_feats.md`, `feats_overview.md`). Only `magic_feats.md` was updated (mechanically load-bearing for casting). The rest still reference pre-rework mechanics in places - confirmed stale: `prestige_feats.md` cites the deleted Ambushed/Caught Out Surprise rungs. Expect old-DC-scale numbers and old Weapon Length/Edge/Tempo Pool language scattered through the rest; a full read-through is needed, not just a grep for known-bad terms.
- **`core/character/races/`** (all fifteen race files plus `races_overview.md`). Not touched by this rework at all.
- **`core/bestiary/`** (`universal.md`, `mythical.md`, `bestiary_overview.md`, per-continent stubs). Already flagged stale against the Exchange merge before this rework; now stale against this rework too, on top. Rebuilding `tools/` (below) should happen before or alongside this, not after - there's no current weak-creature tier to calibrate new stat blocks against otherwise.
- **`templates/character/character_sheet.html` and `sheet_test.js`.** Still computes the pre-rework Tempo Pool (`DEX + 1`/STR-sized dice), Initiative off MIND, the old Mana formula, and the old rank-based Magic Feats table. All 176 `sheet_test.js` assertions currently pass against the *old* sheet; they'll need rewriting alongside it, not just re-run.

**A systemic issue found but not fixed while doing the above:** hundreds of hardcoded DCs across the book (traps, locks, Wards, monster abilities - anywhere a number was written against the old 4/6/8/10/12/14/16 scale) still use pre-rework values. Per-file rescale mapping used so far, for consistency when the deferred files above get touched: Very Easy (4)/Easy (6) -> Easy (5); Medium (8) -> Standard (7); Hard (10)/Very Hard (12) -> Hard (9); Grueling (14)/Legendary (16) -> Extreme (11). **Fold this into each deferred file's own pass above rather than running it as a separate global sweep** - confirmed already needed in `core/feats/`, likely needed throughout `core/character/races/` and `core/bestiary/`.

## Bestiary and simulation tooling still model a deleted combat system

`core/bestiary/universal.md`, `mythical.md`, per-continent files, and three of the four files in `tools/` (`combat_engine.py`, `creature_rating.py`, `encounter_rating.py`) predate the Exchange merge and now *also* predate the Reach/Tempo rework on top - two reworks of staleness, not one. `tools/tempo_sim.py` was the one file that ever matched the rules, briefly, between the 2026-08-23 Exchange merge and the 2026-08-30 single-attack ruling; it's been stale since. **Rebuild the tooling first**, against the current Reach/Tempo/Magic rules, then convert the bestiary against it. `.claude/skills/bestiary-npc/` also wires the stale rating tools into its Validate stage and needs to follow once the tools are fixed.

## Arcane and Divine spell lists need a rebalance and expansion pass

Folded together with the "convert every spell to the new casting engine" item above - do both in one pass, not two. Also still scoped in from before this rework:

- **Expand every school to ~10 spells.** Most schools sit at 6 today (Shadowmancy is the outlier at 8).
- **Make the schools more restrictive and less trivial to spread across.** Nothing meaningfully discourages a caster from picking up spells in several schools at once right now.

## Character sheet: three incomplete pieces

- **No Knowledge UI** - no tier picker, no point tracking for the Freebie Pool or Race/Career grants.
- **Priority Allocation doesn't assign, only checks after the fact** - the five priority pickers drive the array/Skill budget/Feat count, but there's no slot-by-slot picker that stops you typing a number the array never handed out.
- **The whole sheet needs the Reach/Tempo rework applied** (see above) - Tempo Pool, Initiative, Mana->Will, and Magic Feats all changed shape.

## First-draft, unplaytested numeric ladders

Skills (18/15/12/9/6), Feats (4/3/2/1/0), and Career Crown deltas (+150/+75/0/-50/-100) have never had real table time - unchanged by this rework. **Also now in this category, freshly introduced by the Reach/Tempo rework and equally unplaytested:** the four-tier DC ladder (5/7/9/11) and its rescale mapping for old content (above), Tempo Pool baseline+Attacks-modifier sizing, Trauma's widened 0-20 scale and its healing-costs-Trauma inflow, Wound boxes (4/5/6 by Size, up from 3/4/5), Scar Line/Resolve-check DCs (7/9/11), Fear ratings (Terror 7/Dread 9), and Revelry & Leisure's 10-Crown-per-night placeholder. All of it was tuned only against the standalone drafts' own playtest math, not against this repo's full character/Feat/race math stacked on top - flag anything that reads off in actual play.

## Prose style pass across core/ is open work

**2026-09-14:** `DESIGN_GUIDE.md` gained a Prose Style section (table-reference density, cut rationale, tables over prose past two items, GM-ruling default on edge cases). **`exchange.md` had a first pass done pre-rework**; the file was then rewritten wholesale for the Reach/Tempo rework in a style that already leans terse/table-first, but hasn't been checked against the litmus test specifically. **Not yet applied to any other file.** Worth trying the two-pass shape (sentence-level trim against the litmus test, then a structural pass looking for facts stated in more than one place) on `weapons.md` and `rest_and_survival.md` next, both freshly rewritten and likely to have picked up incidental repetition during the rework.

## Small loose ends worth folding into other work when touched

- **`minor_magic.md` picks its DC by tier name off the new ladder** - confirm the Lesser/Common/Greater rungs it references still read right once the school spell files are converted and there's real content to check them against.
- **Alchemy's Vital Oil recipes now heal real Wounds at a Trauma cost** (converted from Patched Wounds during this rework) - worth a balance read once spell-tier damage numbers are set in the deferred magic pass, since a potion and a working now compete on the same Wound-and-Trauma economy for the first time.
