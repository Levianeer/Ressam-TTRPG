# TODO

Cross-session open items - what's actively in flight, why it matters, and what picking it up should look like. Only exists while something is outstanding; its absence means nothing's open, not that it was forgotten.

**Reset 2026-08-29:** the Exchange merge and its immediate follow-up (DC scale recut, prerequisite pass, criticals deletion, Knowledge Phases 1-2) are done and committed. That history lived here in detail through the rework; it's been cleared now that the repo is moving from rework to polishing - the reasoning is preserved in `exchange_log.md` and `CLAUDE.md`, not repeated below. What's left is genuinely open work.

## Bestiary and simulation tooling still model a deleted combat system

`core/bestiary/universal.md`, `mythical.md`, per-continent files, and three of the four files in `tools/` (`combat_engine.py`, `creature_rating.py`, `encounter_rating.py`) all predate the Exchange - they implement Oppose, Evasion, the Margin table, and per-STR Wound Thresholds, none of which exist any more. `tools/tempo_sim.py` is the only tool that matches current rules. This blocks everything else that needs a number: there is no current weak-creature tier to calibrate a bestiary against, and no simulator with a notion of occupied squares to check the Far Band's intervening-square rule. **Rebuild the tooling first**, then convert the bestiary against it. `.claude/skills/bestiary-npc/` also wires the stale rating tools into its Validate stage and needs to follow once the tools are fixed.

## The Exchange is merged but unplaytested - open tuning questions

- **STR/DEX sits ~12.7 points to DEX under optimal play** (extra dice buy offense and defense; die size only buys quality). Shallow slope, no build below 42%/above 56%, accepted rather than fixed - revisit if real play disagrees.
- **An archer's win rate swings ~45 points on the GM's choice of opening distance** (42% at standoff 0, 82% at standoff 3). Worth a table-facing guideline once there's play data.
- **Armor has no in-fight counterweight** now that nothing reads Penalty - intended, but never explicitly decided as the reason. If plate needs holding back later, it has to be an AR or durability change.
- **Never measured:** the Shot DC table, the Mythic pool size, the Called Shot menu's rate, and the four new Tempo/Openings Feats (Cleave Through, Economy of Motion, Set Yourself, Practiced Loader).
- **Changed at merge, not re-simulated:** the Blinded ruling, the Size-to-Band remap, and the three rebuilt Feats that now move a weapon a Band (Adaptive Guard, Half-Swording, Shortened Grip).

## Character sheet: two incomplete UI pieces

- **No Knowledge UI** - no tier picker, no point tracking for the Freebie Pool or Race/Career grants.
- **Priority Allocation doesn't assign, only checks after the fact** - the five priority pickers drive the array/Skill budget/Feat count, but there's no slot-by-slot picker that stops you typing a number the array never handed out.

## Arcane and Divine spell lists need a rebalance and expansion pass

The Petition Roll rework changed how every Divine spell resolves, but damage dice/effect magnitudes/Mana Costs still carry pre-Petition-Roll numbers. Arcane has its own longstanding staleness independent of that. Needs real playtest data, not a desk pass - treat both lists as one rebalance, not two, since Distinction between the two paths is the point.

**Also scoped into this pass now that Spell Crafting is gone** (deleted outright 2026-08-29 as a system - see `CLAUDE.md`'s `core/magic/` bullet):

- **Expand every school to ~10 spells.** Most schools sit at 6 today (Shadowmancy is the outlier at 8) - custom spell-building was the pressure valve for a thin list, and without it the printed lists need to carry more of the weight themselves.
- **Make the schools more restrictive and less trivial to spread across.** Nothing meaningfully discourages a caster from picking up spells in several schools at once right now; tighten whatever gates that (Skill investment, a prerequisite, a slot/point cost) so specializing in one or two schools is a real choice rather than free breadth.

## First-draft, unplaytested numeric ladders

Skills (18/15/12/9/6), Feats (4/3/2/1/0), and Career Crown deltas (+150/+75/0/-50/-100) have never had real table time. Flagged specifically: the Feats ladder's gap doesn't shrink relative to the whole as level-ups add on top (an **A** ends Level 12 with exactly double an **E**'s total Feats, permanently), and Skills **A** (18 points) has to spread across 9+ Skills to spend against a per-Skill cap of 2, which may or may not have been the intent behind those numbers.

## Small loose ends worth folding into other work when touched

- **Mana Scar identification** (`laws_of_magic.md`) is still a flat MIND check, a stopgap from before Knowledge existed - now that Signature Lore is a real subject, it's a candidate to become tier-gated instead.
- **`minor_magic.md` picks its DC by tier name**, so it got quieter when the DC scale recut Hard/Very Hard down - probably correct, but was a side effect, not a decision. Worth a read once the tooling/bestiary work above gives a baseline to check it against.
