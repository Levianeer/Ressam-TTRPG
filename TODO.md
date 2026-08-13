# TODO

Cross-session open items - what's actively in flight, why it matters, and what picking it up should look like. Only exists while something is outstanding; its absence means nothing's open, not that it was forgotten.

## Skill consolidation (45 -> 24 skills): per-school magic Feats deferred (since 2026-08-11)

The Skill list was cut from 45 to 24 (see `CLAUDE.md`'s `core/character/` bullet for the full merge list - Blades/Hafted Weapons/Polearms/Brawling -> Melee, Archery/Marksmanship/Thrown -> Marksmanship, Shields -> Block, Armorer folded into Crafting, Lockpicking/Sleight of Hand -> Subterfuge, Historic/Medical/Nature Lore/Identify -> Lore, the 5 Arcane schools -> Arcanism, the 5 Divine schools -> Devotion). Landed in the same pass: every cross-reference across `core/` and `templates/character/character_sheet.html`, new **Weapon Focus** and **Scholar's Focus** Feats (flat `+1` to rolls/checks with one chosen weapon group or Lore subject, repeatable - `martial_feats.md` and `skill_feats.md`), and `tools/power_score.py`/`combat_engine.py`/`creature_rating.py`/`encounter_rating.py` updated and re-run clean against the new skill names.

**Still open:**

- **Per-school specialization Feats for Arcanism and Devotion, deferred on purpose.** The weapon/Lore groups got a simple repeatable `+1`-to-rolls Feat; magic didn't, because Devotion's Petition Roll is flat (`1d12 vs. DC 7`, no modifier at all per `magic_overview.md`) - a naive `+1` Feat does nothing there, and Arcanism's equivalent needs its own think rather than a copy-paste of the martial pattern. Until this lands, existing Feats that used to gate on a specific school's Skill rank (e.g. `arcane_feats.md`'s Shadowcraft entries, `divine_feats.md`'s Zealotry/Life's Balance/etc.) instead gate on the merged Skill rank *and* knowing at least one spell from that school - a workable interim, not the intended final shape.
- **All the new numbers are first-draft.** The Weapon Focus/Scholar's Focus `+1` value, and the decision to collapse Devotion's old per-school Rite Mastery charge pools into one shared Devotion-sized pool, weren't checked against `tools/creature_rating.py` or `tools/encounter_rating.py` for whether they shift any tier.
- **`core/bestiary/universal.md` and `mythical.md`** got their `**Skills:**` lines renamed (Blades/Brawling/etc. -> Melee, Shields -> Block) but their `**Reactions:**` lines still use the pre-08-09 Parry/Block/Dodge Maneuver wording - that's the pre-existing, separately-tracked issue below, untouched by this pass on purpose.

---

## Stance's Posture numbers are first-draft, unplaytested (since 2026-08-10)

`maneuvers.md`'s Stance section (a Funding + Posture pair declared for free at the end of your turn, replacing the old live "which Skill funds this Oppose" choice) landed as part of a cognitive-load pass on the reactive combat loop. The mechanic's shape is settled - Funding hard-locks which Skill answers an Oppose for the round, Posture (Ready/Aggressive/Guarded) gives even a single-Funding-option build a real independent choice - but its numbers weren't derived from anything beyond "feels roughly right next to the old Defensive Stance Basic Move it replaced":

- **Aggressive's trade** (Advantage on a chosen Strike's attack roll, Disadvantage on the Oppose roll that would unlock it) hasn't been checked against `tools/combat_engine.py` for whether the risk/reward actually nets out even, or whether it's a trap option / a dominant one at certain Skill-rank levels.
- **Guarded's -2 Strike damage penalty** was picked by halving the old Defensive Stance's -4, on the reasoning that Stance no longer costs a Minor Action to maintain - not derived from any damage-output model.

**Still open:** run `tools/creature_rating.py` (or a baseline-PC-vs-baseline-PC pass with `combat_engine.py`) with each Posture forced on, to see whether any of the three actually shifts win rate against `BASELINE_PC` before trusting the numbers. Low urgency - opt-in, PC-facing only, doesn't touch the bestiary.

---

## Character Creation: Priority Allocation rework (in progress, since 2026-08-08)

Character creation runs on a five-category priority ladder now (priorities **A** through **E**, one each to Attributes/Skills/Career/Feats/Race, no repeats) instead of flat point-buy - closes the old "master of nearly all" gap where Attributes and Skills were separate, uncoupled budgets with no trade-off for broad competence. Landed: the full `character_creation.md` restructure (new Step 2, reordered steps 3-6), Standard Array/Rolled removed, Career Status-tier Crown deltas baked directly into `careers.md`'s printed values, and a full Race power-tier rework (Mundane/Exotic/Extraordinary, 8 races got mechanical changes). Full detail in memory (`project_priority_allocation_chargen.md`), not repeated here.

**Still open:**

- **All the numeric ladders are first-draft, unplaytested.** Attributes (24/21/18/15/12), Skills (18/15/12/9/6), Feats (4/3/2/1/0), and the Career Crown deltas (+150/+75/0/-50/-100) all need real table time before they're trusted. The Feats ladder specifically is flagged as possibly too sharp: unlike Attributes/Skills, the gap doesn't shrink relative to the whole as level-up bonuses add on top - an **A** ends level 12 with exactly double an **E**'s total Feats, permanently, not just at creation.
- **`character_sheet.html`'s priority-letter input mechanism.** The sheet's layout was reorganized (2026-08-09: Attributes moved to the Skills tab, renamed "Attributes & Skills"; Currency moved to Equipment; Overview reordered to Combat Stats → Wounds & Survival → Wards), but its hardcoded per-level progression table still assumes flat 18/12/2 starting values. Needs a real input mechanism (five priority-letter pickers feeding the level-1 row). Don't start this until the ladders above are past first-draft, or it needs redoing twice.
- **Feat prerequisite reachability, deferred on purpose.** The literal text check (grepped for hardcoded old-baseline references) came back clean. Still unverified: whether individual prerequisites (e.g. "+4 ranks in a Skill," "MIND 3") stay reasonably reachable now that the lowest Skill/Attribute pool a priority letter can hand you is 6/12 instead of the old flat 12/18. User's explicit call - pinned, not urgent.

---

## Spell Crafting's point-budget system is the one place that fails Elegance's own test

`DESIGN_GUIDE.md` states plainly: "If a mechanic requires a calculator, or causes eyes to glaze over mid-explanation, it should be questioned." Spell Crafting's VERB + NOUN + MODIFIERS system (Range -12 to +2, Area -12 to 0, Duration and Magnitude tables, +2-per-school surcharges, then `Mana Cost = 4 - (Remaining Points ÷ 4)`) is real arithmetic load, out of step with everything else in the ruleset's texture. It's opt-in (Skill Rank 2+, learned outside combat) so the harm is contained, but it's also exactly the kind of subsystem that invites the system-mastery min-maxing the rest of the design actively resists elsewhere.

**Deferred:** not picked up per the user's explicit call - Spell Crafting is likely to be reworked or removed outright in an upcoming pass, so a lighter on-ramp fix here would probably be thrown away. `spell_crafting.md`'s intro is flagged as an "Optional Rule" ahead of that rework.

---

## Full spell-list rebalance pass needed for Arcane and Divine (post-Petition-Roll)

The Divine Petition Roll rework changed how every Divine spell resolves (flat `1d12 vs. DC 7`, Devotion's payoff moved to Rite Mastery reroll charges instead of the roll itself), but the spells' actual numbers (damage dice, effect magnitudes, Mana Costs) weren't rebalanced against the new resolution - carried over unchanged from the old Spell Attack/Overcome system. Arcane's spell list has its own longstanding staleness independent of this rework and was never in scope for it.

**Deferred:** this needs real playtest data, not a desk pass - a flat 50% base rate plus a Skill-gated reroll pool is a different risk shape than the old contested-roll curve. Treat both paths' spell lists as a single rebalance pass, not two separate ones, since Distinction between them is the entire point.

---

## Bestiary + simulation tooling still assume the old Parry/Block/Dodge Maneuver system (since 2026-08-09)

The combat exchange was reworked per `hema-combat-design.md`'s compression model: Maneuver's three named rolls (Parry/Block/Dodge) and the separate Counterattack Reaction collapsed into one **Oppose** Reaction (`1d12 + Weapon Skill, Shields Skill, or DEX - whichever funds it`), the old 6-item Effect menu collapsed into four (**Strike/Shift/Control/Recover**), a generalized reaction chain (**the Press**, renamed from "the Krieg" on 2026-08-09 to drop the borrowed German HEMA term per `DESIGN_GUIDE.md`'s new Realism note) now lets either side of a contest re-roll by spending another Reaction, and the 4-tier Reach Category system (Short/Medium/Long/Very Long) collapsed into 3 Measure Bands (Grip/Near/Far) with a symmetric per-combatant mismatch rule instead of a fixed longer/shorter comparison. Landed: `core/core_rules.md` (Basic Moves), `core/combat/maneuvers.md` (full rewrite), `core/combat/combat.md` (Reach → Measure Bands, Crit/Action-Economy cross-refs), `core/equipment/weapons.md` (Measure Band table, per-weapon remap, property renames), a terminology pass through `armor.md`, `attributes_and_skills.md`, `character_creation.md`, `carrying_and_resting.md`, `alchemy.md`, `martial_feats.md`, and `prestige_feats.md`, plus `CLAUDE.md`/`DESIGN_GUIDE.md`/`templates/Home.md` (2026-08-09). `templates/character/character_sheet.html` got its own relabeling pass the same day (Oppose Bonus DEX/Shields stat boxes, Shields table header, Weapons table Reach dropdown Grip/Near/Far) - it turned out to be pure terminology, no formula changes, so it didn't need to wait on the Priority Allocation input-mechanism work after all.

**Still open - not touched by that pass, on purpose (each needs real per-entry redesign, not a find-and-replace):**

- **`core/bestiary/universal.md` and `core/bestiary/mythical.md`.** Dozens of NPC stat blocks have individually-tuned `Reactions: Can Parry (1d12+X)/Block/Dodge` notes built around the *distinction* between the three old rolls (e.g. "Armor Penalty guts Dodge, Block is what this build is for" on the Knight; "no training needed" Dodge-only mobs like the Wolf and Wisp). Every one needs a real decision about which Skill funds its new Oppose roll, not a mechanical rename - re-run `tools/bestiary_sim.py`, `power_score.py`, and `danger_estimate.py` against each once updated. Compounded 2026-08-09: shields also dropped AR Bonus/Penalty/Evasion-Oppose Bonus entirely in favor of a single **Guard** stat (armor.md's Shield table collapsed from 6 shields to 3 - Buckler/Heater Shield/Pavise), so every shield-equipped NPC (the Guard and Knight both carry a Heater Shield "+2 AR while Blocking, Penalty -1" today) needs its Equipment line and combat notes redone against Guard too, not just the Reactions line.
- **`core/bestiary/bestiary_overview.md`'s "Reading a Stat Block" section.** One paragraph, describes the old Reactions-line format - update alongside the stat blocks above, not before (it should describe whatever the settled per-NPC format ends up being).
- ~~`tools/balance_sim.py`, `tools/encounter_sim.py`, `tools/bestiary_sim.py`, `tools/danger_estimate.py`, `tools/chain_sim.py`.`~~ **Done (2026-08-09).** Deleted, along with `tools/rest_pressure_sim.py` (a separate day-attrition question, dropped rather than ported - can be rebuilt from the new engine if actually needed again). Replaced by `tools/combat_engine.py` (a from-scratch Oppose/Effect/Press engine, standalone, no dependency on the deleted files) plus two new comparison tools built on it: `tools/creature_rating.py` and `tools/encounter_rating.py`. These also change what the tooling reports, at the user's request: instead of a raw danger ratio or a CR-style number, a creature or encounter is Monte Carlo-simulated against one fixed `BASELINE_PC` and bucketed into a 5-tier rating (Much Worse/Worse/Equal/Better/Much Better) - Ressam's PCs don't scale enough over 12 levels for a level-scaled or numeric baseline to be worth the complexity. `.claude/skills/bestiary-npc/SKILL.md`'s Validate stage now points at the new tools; `reference.md`'s own Reactions-line guidance (see the bullet above) was deliberately left untouched, so the skill will keep writing old-terminology Reactions lines into new entries until that bestiary content pass happens.
