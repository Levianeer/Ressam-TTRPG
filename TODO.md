# TODO

Cross-session open items - what's actively in flight, why it matters, and what picking it up should look like. Only exists while something is outstanding; its absence means nothing's open, not that it was forgotten.

## Still-open draft audits

Two design drafts at the repo root (`magic_draft.md`, `spells_draft.md`) haven't been fully checked line-by-line against the chapters built from them. The audit method: read the draft's own sentence, not the general shape of the system, before trusting anything that looks plausible - this has caught real errors on every file it's been run against so far, including files already believed finished.

- **`magic_draft.md`, remaining territory.** Only the Push/Channel numbers have been checked line-by-line against the source. Not yet audited: the Casting/Resisting procedure end to end, the Ten Schools framing, Learning Workings' Feat-tier shape, Designing Workings (the Five Hard Limits, Held Will, area-working caps), and the Free Dice suggested-trait list. `magic_overview.md`, `laws_of_magic.md`, `minor_magic.md`, and `magic_feats.md` are the files in scope.
- **`spells_draft.md` - not audited at all yet.** Its fifteen example workings were the source for `magic_overview.md`'s mechanical *rules* (Casting, Magic Damage, Designing Workings), but nothing has specifically checked those rules against the worked examples the draft itself provides. Do this before or alongside the individual school spell-file conversion below, since the same worked examples are the natural template for the first few converted spells.

## Deliberately deferred - each needs its own dedicated pass, not a mechanical find-and-replace

- **The individual school spell files.** `core/magic/arcane/*.md` and `core/magic/divine/*.md` still describe every spell in an older Mana-Cost/flat-modifier/Spell-Attack-vs-Overcome shape. Converting each to the current Lesser/Common/Greater/Legendary tier shape is real per-spell design work (tier, dice, resist-shape), not a terminology swap - the same pass as "spell lists need a rebalance and expansion" below, not a second one. `DESIGN_GUIDE.md`'s Spell Design Guidelines and Magic Feat Guidelines sections should be rewritten in the same pass, once the draft audits above are done and there's a checked-against-source rule set to write guidelines for.
- **`core/feats/general_feats.md`, `martial_feats.md`, `skill_feats.md`.** All three are empty stub headers right now, cleared in preparation for a full rewrite against the current rules. `prestige_feats.md` and `racial_feats.md` have real content and are largely current; `feats_overview.md` is short and spot-checked clean of obvious stale terms, but hasn't had a full read-through.
- **`core/character/races/`.** All fifteen race files plus `races_overview.md` reflect current combat/equipment terminology (Reach/Tempo, Wound-framing, weapon Skill splits). **Not yet checked against `magic_draft.md`/`spells_draft.md`** - several races grant free casts of specific spells or have magic-adjacent Features (Tapio's Cultivation cast, Ash'shene's Pyromancy cast, and others) that should be re-examined once the magic audit above is done.
- **`core/bestiary/`.** `universal.md`, `mythical.md`, and `bestiary_overview.md` are current (Dent/Rend, Tempo Pool, Initiative, corrected weapon stats). The per-continent files (`aurkhan.md` and the rest) are still empty stubs - untouched, nothing to convert yet. `tools/` (below) should still be rebuilt before any *new* bestiary content leans on simulated numbers.
- **`templates/character/character_sheet.html` and `sheet_test.js`.** Still computes an older Tempo Pool (`DEX + 1`/STR-sized dice), Initiative off MIND, an older Mana formula, older Weapon Length/Edge fields, an older Bulky Capacity/Backpack Slots split, and an older rank-based Magic Feats table. This is a full rework of the sheet's derived-stat engine, not a formula patch. All 176 `sheet_test.js` assertions currently pass against the sheet as it stands today; they'll need rewriting alongside it, not just re-run.

## Bestiary and simulation tooling still model an older combat system

`tools/combat_engine.py`, `creature_rating.py`, `encounter_rating.py`, and `tempo_sim.py` model a deleted combat system and don't reflect current rules. **Rebuild the tooling first**, against the current rules, before leaning on simulated numbers for new bestiary content. `.claude/skills/bestiary-npc/`'s `SKILL.md` and `reference.md` have already been rewritten to hand-validate instead of calling the stale tools, and to stop advertising them - no further action needed there until the tools themselves are rebuilt, at which point the Validate stage should switch back to using them.

## Arcane and Divine spell lists need a rebalance and expansion pass

Folded together with "convert every spell to the current casting engine" above - do both in one pass, not two.

- **Expand every school to ~10 spells.** Most schools sit at 6 today (Shadowmancy is the outlier at 8).
- **Make the schools more restrictive and less trivial to spread across.** Nothing meaningfully discourages a caster from picking up spells in several schools at once right now.

## Character sheet: three incomplete pieces

- **No Knowledge UI** - no tier picker, no point tracking for the Freebie Pool or Race/Career grants.
- **Priority Allocation doesn't assign, only checks after the fact** - the five priority pickers drive the array/Skill budget/Feat count, but there's no slot-by-slot picker that stops you typing a number the array never handed out.
- **The whole sheet needs a rework to match the current rules** (see above) - Tempo Pool, Initiative, Mana->Will, Magic Feats, and carrying capacity all need updating.

## Systemic old-DC-scale numbers

Some hardcoded DCs across the book (traps, locks, Wards, monster and NPC abilities) still reflect an older DC scale. Rescale mapping used consistently everywhere it's been touched so far: Very Easy/Easy -> Easy (5); Medium -> Standard (7); Hard/Very Hard -> Hard (9); Grueling/Legendary -> Extreme (11). Already applied throughout `core/equipment/` (`supplies.md`, `alchemy.md`), `core/exploration/` (`traveling.md`, `leadership.md`), and every race/feat file touched by the combat/equipment passes. **Still needs checking** in `general_feats.md`/`martial_feats.md`/`skill_feats.md` once they're rewritten, the per-continent bestiary stubs once they gain content, and the individual spell files during their conversion pass - fold it into each file's own pass rather than running it as a separate global sweep.

## First-draft, unplaytested numeric ladders

Skills (18/15/12/9/6), Feats (4/3/2/1/0), and Career Crown deltas (+150/+75/0/-50/-100) have never had real table time. Also unplaytested: the four-tier DC ladder (5/7/9/11), Tempo Pool baseline+Attacks-modifier sizing, Trauma's 0-20 scale and its healing-costs-Trauma inflow, Wound boxes (4/5/6 by Size), Scar Line/Resolve-check DCs (7/9/11), Fear ratings (Terror 7/Dread 9), Revelry & Leisure's 10-Crown-per-night placeholder, and the armor Dent/Rend table (Gambeson 5/10 through Full Plate 11/16). All of it was tuned only against the standalone drafts' own playtest math, not against this repo's full character/Feat/race math stacked on top - flag anything that reads off in actual play.

## Small loose ends worth folding into other work when touched

- **`minor_magic.md` picks its DC by tier name off the current ladder** - confirm the Lesser/Common/Greater rungs it references still read right once the school spell files are converted and there's real content to check them against.
- **Alchemy's Vital Oil recipes heal real Wounds at a Trauma cost** - worth a balance read once spell-tier damage numbers are set in the deferred magic pass, since a potion and a working now compete on the same Wound-and-Trauma economy for the first time.
- **A recurring failure mode to keep watching for, not just in magic:** past audit passes have repeatedly found places where an older mainline behavior, or a plausible-sounding invented substitute, had quietly stood in for what a source draft actually states. Don't assume a file is finished because it reads consistently - check it against the draft sentence it's supposed to come from.
