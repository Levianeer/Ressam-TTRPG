# TODO

Findings from a full design review against `DESIGN_GUIDE.md`'s pillars (2026-08-05), covering `core/`, `ENCOUNTER_GUIDE.md`, and `DESIGN_GUIDE.md`/`laws_of_magic.md` themselves. Ordered by impact. Each entry states what's wrong, why it matters against the project's own stated goals, and what picking it up should look like.

## ENCOUNTER_GUIDE.md's Role ratios are validated at exactly one Threat Level

The "4 Easy / 2 Average / 1 Elite per player" ratio table is the primary tool a GM reaches for to build every fight in the game. It has only been Monte Carlo-tested (`tools/encounter_sim.py`) at Threat Level 1 - and at that level, the naive ratios it currently documents for every *other* level produced badly uneven fights before retuning (Easy 72% PCs win, Average 8%, Elite 64%, across thousands of trials). The Level 1 Example Roster was hand-retuned to land near 50/50, but that retuning was never generalized. Every Threat Level from 2 through 12 is still running on the same formula that just failed a validation check at the one level anyone bothered to check.

**Why this needs fixing:** This isn't a corner-case rule a GM might never touch - it's the tool used to build every single encounter, and it's demonstrated, with real numbers, that it's capable of an 8x swing in win rate before correction. A GM trusting this table at, say, Threat Level 6 has no way to know whether they've built a fair fight or a TPK, because the table's own methodology admits it hasn't checked. The file's core pitch ("NPC math never goes stale because it's just PC math") is undermined if the one genuinely new piece of content in the file - the Role ratios - is unvalidated everywhere it's actually used.

**Recommendation:** Extend `tools/encounter_sim.py` (or its successor) to at least 2-3 more benchmark levels spanning the Skill/Attribute cap breakpoints (e.g. 4, 8, 12), and either retune the ratios per-level to match, or confirm the existing ratios hold once Wounds pools are larger and the Level 1-specific pathology (tiny 2-4 Wound pools) no longer applies. If full validation isn't feasible immediately, at minimum move the "these ratios are unvalidated past Level 1" disclosure out of a mid-file footnote and onto the Role table itself, where a GM skimming for a quick build won't miss it. Confirm whether the validated numbers assume a specific party size - the "per player" scaling is itself unverified.

---

## Reactions-pool floor of 0 fully locks a build out of the Maneuver chapter, not just weakens it

Reactions/round = `(DEX + PRE) ÷ 3, rounded down`, with no floor. This was an intentional nerf to STR/END "Brute" builds. But the thing it gates isn't a minor bonus - it's the entire Maneuver system (Parry, Block, Dodge, and the Riposte free-counterattack Effect that's the game's sanctioned exception to "no Feat grants an extra attack"), plus Reactive Casting and Opportunity Attacks. A character with DEX 1, PRE 1 gets 0 Reactions and cannot Parry, Dodge, Block, cast reactively, or make an Opportunity Attack - ever, regardless of weapon skill. A high-STR/END armored-knight archetype, a normal and expected build for a 1500s-flavored game, is fully locked out of the game's most tactically rich chapter and can never earn the Riposte payoff that's supposed to be a Martial's signature reward.

**Why this needs fixing:** This is a hard cliff, not a curve, which sits against this project's usual instinct to cost-scale rather than hard-cap (see how Divine Healing, Blood-Rule, and other past rebalances were handled - scaled costs, not binary walls). "Worse at Maneuvering" is a legitimate build tax; "cannot Maneuver, cannot Riposte, cannot Reactive Cast, cannot Opportunity Attack, period" is a different thing - it removes access to a subsystem rather than pricing participation in it.

**Recommendation:** Decide explicitly whether full lockout is the intended cost of dumping DEX/PRE. If yes, state it plainly somewhere visible (Basic Moves or the Maneuvers intro) so it reads as a deliberate build consequence rather than an edge case nobody noticed. If not, add a narrow floor - a guaranteed minimum of 1 Reaction regardless of DEX/PRE, or a Feat/racial/career option that grants one - consistent with how this project usually reopens a cut mechanic (roll-gated or cost-gated, not free). Don't over-correct into broadly re-buffing Brutes; the goal is closing the "structurally cannot participate" cliff specifically, not undoing the nerf that put it there.

**Resolved (2026-08-05):** Added the narrow floor option - `combat.md`'s Reaction formula and its copy in `character_creation.md`'s stat table are now `(DEX + PRE) ÷ 3, rounded down, minimum 1`. A DEX/PRE dump still Reacts worse than an invested build (fewer Reactions per round, same as before), but is never fully locked out of Parry/Dodge/Block, Reactive Casting, or Opportunity Attacks. STR/END Brutes weren't otherwise re-buffed - this only changes the 0-Reaction edge case.

---

## Divine Prayer's Mana recovery may be less gated than Arcane's Rest recovery, breaking the intended parity of the Two Paths

Arcane's full Mana refill (`MIND × 3`) requires a Long Rest's Good Shelter + Good Food. Divine Mana recovers at a flat 1/hour of Prayer with no shelter or food requirement attached to the recovery itself - only a Rest's *other* benefits (Temp Wounds, Trauma) are shelter-gated, not Prayer's Mana income. In practice, a Divine caster stranded in the wilderness with no town nearby can pray for extra hours and reach full Mana on a bedroll; an Arcane caster in the same spot is capped at `MIND` (Field Rest tier) until they reach civilization. Outside dungeons specifically (where Turns and wandering-encounter checks at least tax extended Prayer), this reads as Divine having the easier path to full resources in exactly the scarcity-critical moments - mid-wilderness, no Good Shelter - the rest of the system works hard to protect.

**Why this needs fixing:** The "Two Paths of Magic" table sells Arcane vs. Divine as a symmetric trade (portability/shareability vs. spontaneity/personal-only), not as one path having an easier resource ceiling than the other. If Divine can reliably hit max Mana in conditions where Arcane structurally cannot, that's a quiet thumb on the scale in precisely the situations Scarcity is supposed to bind hardest, and it isn't one of the trade-offs the comparison table advertises.

**Recommendation:** Confirm whether this gap is deliberate compensation for Divine's other costs (no scroll economy, no stockpiling, personal-only casting) or an oversight from writing Prayer's mechanics independently of Rest's shelter gates. If it's a genuine gap, the cleanest fix is likely tying Prayer beyond a Rest's normal duration to some minimal safety/uninterrupted-time requirement, mirroring what Long Rest already asks of Arcane's full refill - not stripping Prayer's flexibility outright.

**Resolved, final shape (2026-08-05):** Landed on two changes, after a few discarded intermediate attempts (a shelter-tiered Prayer patch, then a smaller `FAI × 2` pool with ungated-anywhere Prayer - both superseded, not reflected in the final design below).

**Mana economy:** stayed simple. Divine shares Arcane's exact system - single `Maximum Mana = MIND × 2` pool, same Short/Field/Long Rest ladder, same amounts, same shelter/food requirements. The one real addition: **Devotion Required** (`magic_overview.md`, `core_rules.md`'s Resting section) - if you have any ranks in a Divine school, a Rest only grants its Mana if you genuinely perform your deity's devotional act sometime during it (`divine_overview.md`'s Prayer Requirements, no longer "purely thematic, no mechanical bonus"). Skip it and that Rest grants no Mana at all. This is what actually fixes the original parity concern and the separate in-fiction-atheist-cleric problem, without adding bookkeeping.

**Divine spellcasting:** got its own identity instead, via the **Petition Roll** - every Divine spell resolves on a flat `1d12 vs. DC 7` (a clean 50/50, no modifier from Skill/FAI/Armor Penalty), full effect on success, nothing on failure, Mana spent either way. This replaces Arcane-style Spell Attacks/Overcomes for Divine only; Arcane is untouched. Since the roll dropped its modifier, Divine School Skill got a new job to replace what it lost: **Rite Mastery** (`magic_overview.md`) - Skill Rank in a school = reroll charges per Long Rest, one reroll per cast, must take the new result. FAI keeps the job it already had outside the roll (the `+FAI` damage/effect bonus baked into most Divine spells). All 30 spells across the five Divine school files were rewritten to this pattern; `DESIGN_GUIDE.md`'s Overcomes guideline was restored forked (Arcane keeps "no save-or-suck," Divine's binary Petition Roll is an explicit carve-out); `general_feats.md`'s Stress Inoculation was removed outright (its trigger no longer applies to Divine).

---

## Spell Crafting's point-budget system is the one place that fails Elegance's own test

`DESIGN_GUIDE.md` states plainly: "If a mechanic requires a calculator, or causes eyes to glaze over mid-explanation, it should be questioned." Spell Crafting's VERB + NOUN + MODIFIERS system (Range -12 to +2, Area -12 to 0, Duration and Magnitude tables, +2-per-school surcharges, then `Mana Cost = 4 - (Remaining Points ÷ 4)`) is real arithmetic load, out of step with everything else in the ruleset's texture. It's opt-in (Skill Rank 2+, learned outside combat) so the harm is contained, but it's also exactly the kind of subsystem that invites the system-mastery min-maxing the rest of the design actively resists elsewhere (e.g. Prestige Feats' ritual-gated, narrative-first unlocks).

**Why this needs fixing:** Not urgent since it's gated behind investment and used during downtime rather than at the table mid-combat, but it's currently the one subsystem that visibly contradicts a pillar this project otherwise enforces strictly against everything else, including its own crunchier corners (firearms lock types, Reach categories).

**Recommendation:** Consider a lighter on-ramp - e.g. 3-4 pre-costed "templates" (a fast damage spell, a fast control spell, a fast utility spell) a player can pick off instead of doing the full modifier arithmetic - as an additional easy mode alongside the full system, not a replacement for players who want genuine custom spell design.

**Deferred (2026-08-05):** Not picked up this pass, per user's explicit call - Spell Crafting is likely to be reworked or removed outright in an upcoming pass, so an on-ramp fix here would probably be thrown away. `spell_crafting.md`'s intro was re-flagged as an "Optional Rule" ahead of that rework (separately from this TODO item) - see the file itself, not this entry, for that in-progress framing change.

---

## General Feats is down to 4 entries after removing Stress Inoculation

The Divine Petition Roll rework (above) removed Stress Inoculation outright rather than reword it - its trigger ("a spell's Overcome roll targeting you") no longer means anything against Divine casters, who don't roll an Overcome at all anymore, and rather than patch the wording the call was to retire the Feat and replace it with something else later. General Feats now has 4 entries (Combat Awareness, Second Wind, Veteran's Instinct, Inspiring Leader), one below the 5-6 Lean Categories guideline (`DESIGN_GUIDE.md`).

**When picking this up:** design a new General Feat to fill the slot - real-world-grounded per the Feat Design Guidelines (not Arcane/Divine, which are exempt), no flat damage, no extra attacks. Doesn't need to cover the same "resist fear/panic" niche Stress Inoculation did, just needs to earn a slot the other 4 don't already cover.

---

## Full spell-list rebalance pass needed for Divine (post-Petition-Roll) and Arcane

The Divine Petition Roll rework (above) changed how every Divine spell resolves, but the spells' actual numbers (damage dice, effect magnitudes, Mana Costs) weren't rebalanced against the new resolution - they were carried over unchanged from the old Spell Attack/Spell Overcome system. The Petition Roll landed on a flat **1d12 vs. DC 7** (50%, identical for every caster regardless of investment - see the follow-up in the item above), with Divine School Skill's payoff moved to Rite Mastery (Skill-Rank rerolls per Long Rest) instead of the roll itself. Whether individual spells' effect sizes are still appropriately costed against that risk/reroll profile is unverified. Arcane's spell list has its own longstanding staleness independent of this rework and was never in scope for it.

**When picking this up:** this needs real playtest data, not a desk pass - a flat 50% base rate plus a Skill-gated reroll pool is a different risk shape than the old contested-roll curve, and individual spell balance (is a Mana Cost 5 Divine spell's effect worth a coin flip, softened only by however many Rite Mastery charges the caster has left that day? is Arcane's `Xd8 × Mana` cap still right relative to Divine's binary swing?) needs actual table time before touching numbers. Treat both paths' spell lists as a single rebalance pass, not two separate ones, since Distinction between them is the entire point.

---

## Minor / low priority

**Pyromancy's `Incinerate` can exceed its own damage cap in a narrow combo.** At Mana Cost 5, the Pyromancy cap (`Xd10 × Mana`) is `5d10`. Base Overcome damage is `4d10 + ARC` - within cap - but an already-burning target hit by the spread effect takes an additional `2d10`, totaling `6d10` on that specific target, one die over cap. Conditional and rare (requires a target already on fire from a prior instance), but worth a spot-fix or an explicit "this stacked total is an intended exception" note so it doesn't read as drift on the next Pyromancy audit.

**Resolved (2026-08-05):** the spread bonus was reduced from `2d10` to `1d10` in `pyromancy.md`, bringing the stacked total to exactly `5d10` - on cap, not over it - with an inline note explaining the number so it doesn't read as drift later.

**The DC tier success-rate table is still missing.** `core_rules.md` asserts specific claims about what's routine vs. a coin-flip vs. out of reach at each DC tier ("Hard is a real coin flip early on and becomes reliable by mid-game") with no derived math anywhere in the repo currently backing that up. Recompute against the current per-level Skill/Attribute cap columns in `progression_&_rewards.md` (capped at 5) once there's time; low urgency since it's a documentation gap, not a broken mechanic.

**Resolved (2026-08-05):** added a "Success Rate by Level (Specialist)" table to `core_rules.md` directly under the DC tier table, derived from `1d12 + Skill + Attribute` at each level's Skill/Attribute cap breakpoint (6/7/8/9/10 total, at levels 1-2/3-4/5-6/7/8-12). The derived numbers line up cleanly with the existing "What to expect at the table" prose without needing to change it: Very Hard is genuinely unreachable at level 1 even on a natural 12, Hard crosses exactly 50% at levels 5-6, and Incredibly Hard reduces to "natural 12 only" precisely at the level 8+ cap - confirming that prose was accurate, just previously unbacked by math.
