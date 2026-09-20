# Ressam - Mind & Magic (Playtest Draft)

*Playtest draft - these rules are still being tested and may change between sessions.*

A magic subsystem for Ressam, adapted from Middle-earth Strategy Battle Game's Magical Powers: individual named characters, spending a personal resource, in combat that plays like a wargame.

This file is mechanics only. The list of workings a caster can pick from is `spells_draft.md`. All distances are in squares.

**A scene** is a continuous stretch of fiction with its own clear start and end - a fight, a chase, a negotiation, a night's watch - not a fixed length of real time. It ends when the GM says it does. Sustained workings, Binding Chains' persistence, and every other "between scenes" reference in this file and `spells_draft.md` reads off this line.

## MIND

MIND rates a character's strength of will on the same 0-5 scale as every attribute. Most humans sit at 0-1. It does two separate jobs, and the split between them is the core of this adaptation.

**MIND is a hard ceiling on dice.** You may never commit more dice to a single cast or resist than your MIND rating. Dice granted free by traits sit outside this ceiling.

**MIND sets the daily pool.** Will points = MIND × 3, refreshed on a Long Rest.

| MIND | Who                                | Will/day |
|------|------------------------------------|----------|
| 0    | Most commoners                     | 0        |
| 1    | Hedge-witches, steady soldiers     | 3        |
| 2    | Trained adepts, named NPCs of note | 6        |
| 3    | Practised casters, player wizards  | 9        |
| 4    | Masters                            | 12       |
| 5    | Archmages, the legendary           | 15       |

Everyone has a MIND score, not just casters. It also pays for **resisting hostile magic and fear** (see Fear, `combat_draft.md`).

NPC casters run on the same MIND × 3 budget, commit dice under the same ceiling, and recover on the same Short/Field/Long Rest ladder as player casters.

## Trauma

Shared with `combat_draft.md` - one 0-20 track and bands (see there for the table and the full source list). Trauma carries no roll penalty of its own there, and none here either - it gates Scars and Automatic Death only. **The Wound Penalty (see `combat_draft.md`'s Wounds & Death's Door) never reaches casting or resisting** - neither is a Check.

Magic adds two sources beyond `combat_draft.md`'s list:

| Source                               | Trauma                                         |
|--------------------------------------|------------------------------------------------|
| Channelling                          | 1 (Lesser, Common), 2 (Greater), 3 (Legendary) |
| **Pushing** a casting or resist roll | 1 per `+1`, max `+2` per roll                  |

Will is a day's budget; Trauma is an expedition's - it only comes off via Revelry & Leisure, in town. Scars and their recovery also work as in `combat_draft.md`.

## Casting

One working per character per round, costing your Major Action (see `combat_draft.md`'s Your Turn table). The caster must be unengaged - see `combat_draft.md`'s Distance & Weapon Reach for what Engaged means. **Every working has a range of 12 squares unless its entry says otherwise.** **A working needs line of sight to its target, exactly like a shot** - Total cover blocks it the same way it blocks an arrow, and darkness hinders it the same way (see `combat_draft.md`'s Shot DC table and Darkness in `equipment_draft.md`). A working aimed at a point rather than a creature needs line of sight to that point instead.

1. Declare the working and a legal target in range.
2. Commit Will - 1 point per d12, up to your MIND. **Pay before rolling.** You cannot buy a die, see the result, and buy another.
3. Roll. Take the **highest** die, not the sum.
4. You may **Push**: spend Trauma, 1 per +1 to the highest die, up to `+2` per roll, declared immediately so your opponent knows the final number.
5. Meet or beat the difficulty and it goes off. Miss and every Will point committed is gone.

**No purchased result may exceed 11 - only a natural, unmodified 12 ever reaches 12.** Channelling and Pushing are both purchases; rolling isn't. A Channelled die, a Pushed die, or a Channelled die pushed further all cap at 11, however they combine.

| Tier      | Target | One die | What lives here                            |
|-----------|--------|---------|--------------------------------------------|
| Lesser    | 5+     | 67%     | Utility, small buffs, single-target nudges |
| Common    | 7+     | 50%     | Workhorse control and damage               |
| Greater   | 9+     | 33%     | Battle-turning effects                     |
| Legendary | 11+    | 17%     | Once-a-day, story-altering workings        |

This is also the game's whole difficulty ladder - every **base** DC in `combat_draft.md` sits on the same 5/7/9/11. The one place the base itself moves is the Shot DC, which reads `7 + the target's DEX`: the Standard rung plus the target's own evasiveness. Situational modifiers stack on top of every base, so real numbers in play run well past 11.

Workings that target an ally or the caster cannot be resisted and simply take effect. Only workings aimed at an unwilling target go to a resist roll.

**A working with several targets is resolved one target at a time.** Commit the pool once, roll it fresh against each target, and each resists separately with their own Will. Extra targets cost no extra Will, only reliability - never one roll for the whole group.

**Channelling a multi-target working guarantees exactly one of those rolls.** Name the target when you declare Channelling; every other target in the same casting is rolled normally.

**Will lost on a miss is committed once, not per target** - never returned regardless of how many targets the working affects.

**Unresisted multi-target workings (allies, self) roll once, not per target.** Aura of Command rolls once against the difficulty; success applies it to every target in range.

**Pushing a multi-target casting applies once, to every rolled target alike.** It's declared when you commit the cast, not target by target, and costs Trauma once, not per target.

**"Until your next turn" outside combat** lasts about a minute - long enough to use a buff, too short to prepare one before walking into a fight.

## Resisting

Resisting is casting, mirrored. The target commits their own Will - 1 point per d12, up to their MIND, paid before rolling - and needs to **tie or beat** the caster's highest die to negate the working entirely. A defender may Push the resist roll the same way, spending Trauma instead.

A fear check (see `combat_draft.md`) is a resist against a fixed number - the creature's Fear rating stands in for the caster's highest die.

**The refund.** A natural 11 or 12 on a resist die that came from the defender's own Will pool returns that point immediately. "Natural" means rolled and unmodified - a Pushed die's new value never refunds. A resist die can never be Channelled in the first place (see Channelling, below), so that case doesn't arise. Dice granted free by traits never refund.

**Free dice** are the defensive tech of the system, and the main thing to hand out as a trait or blessing. Suggested sources:

- *Steadfast* - one free die whenever you are targeted
- *Bulwark* - two free dice while the bearer has a Will point left
- *Rally* - one free die to every ally within a short distance, for a round
- *Sanctuary* - total immunity to hostile workings for one target, one round

**Free dice ignore the MIND ceiling. Will never does.** This is the only way a MIND 0 character ever passes a fear check, and it is also the standing escape hatch the rules themselves use wherever a MIND 0 creature would otherwise be locked out with no roll at all: a fear check (`combat_draft.md`) and a Binding Chains break attempt (`spells_draft.md`) each hand a MIND 0 creature **one free die**. The principle is worth holding to if you write more lasting effects - *a MIND 0 creature always gets a die, never a certainty.*

**Be sparing with these traits** - free dice cost nothing, never refund, and stack; a party with three sources effectively opts out of hostile magic.

## Channelling

**Declare Channelling at the end of your turn,** naming the working and paying its cost. **On your next turn, casting it must be your first action.** One die of your casting pool is set to **the working's difficulty number exactly** - a channelled 9+ gives you a 9. That die is guaranteed to meet the difficulty - the defender still gets a normal resist roll against it.

**Channelling and Pushing stack, capped at 11 total (see Casting, above).** The channelled die can still be Pushed afterward at the usual cost (1 Trauma per `+1`, max `+2`) - a Legendary working, already channelled to 11, can't be Pushed further.

Against a working with several targets, Channelling only ever guarantees one of them - see Casting, above.

**Cost.** Channelling costs 1 Will, committed as normal - it just isn't rolled - and Trauma **scaled to the working's tier**: 1 for Lesser and Common, 2 for Greater, 3 for Legendary. Both are paid when you declare. **Channelling commits exactly that one die, for exactly that one Will - you cannot commit further dice alongside it in the same cast, even if your MIND allows more.** The channelled die is the whole of the casting pool that turn.

**What that means for the bottom of the ladder.** Because the channelled die presents the difficulty number and nothing higher, it also presents the *easiest possible number to resist*. A channelled Lesser working shows a 5, which one die ties or beats 67% of the time; cast the same working normally on two dice and your high is usually 9 or better. **So Channelling a low-tier working at a resisting target actively makes it easier to shrug off.** Channelling is for two things: **unresisted** workings, where guaranteeing the cast is the entire point and there is no resist roll to hand anyone, and **Greater and Legendary** workings, where a guaranteed 9 or 11 is a number a defender genuinely struggles with. Channelling a Common working at an enemy is usually a mistake, and that's intended.

**Risk.** **You must be unengaged when the cast happens, and Channelling doesn't change that.** A Move Action taken purely to become unengaged doesn't break "first action" - you may Move, then cast as your next act, but nothing else (no other Major Action, no Lesser or Minor Action) may come before the cast. Disengage doesn't help, because Disengage and casting both cost the Major Action. **If you're still Engaged when you would cast - because you couldn't break away with your Move, or chose not to - you can't cast, and the cost is lost.** Charging the caster is still the counterplay; it just now forces a bad Move rather than an automatic loss.

**Channelling only ever applies to your own cast.** A resist roll happens off-turn, on someone else's, and can never be Channelled.

## Recovery and casting outside combat

**Will recovers on the same Short/Field/Long Rest ladder as Wounds and gear**, including its per-day caps - see `combat_draft.md`'s Rest & Repair table. **Trauma does not sit on this ladder** - only Revelry & Leisure removes it (see `combat_draft.md`).

**Outside pressure, taking ten uninterrupted minutes counts as having rolled a 7.** No Will spent, no roll made. **Workings that move Trauma (Mending Touch) never get this shortcut** - they always cost a real Will point and a real roll, even outside combat.

A working attempted under any pressure at all - a watch approaching, a rope fraying, anything with a clock - is a normal cast.

## MIND 0 and ordinary people

Most humans are MIND 0-1: domination, terror, and compulsion would auto-succeed against nearly any NPC without limits. Four guard rails:

- **Named-NPC floor.** Any Named NPC (see `combat_draft.md`) has MIND 1 minimum. Player characters aren't covered - a MIND 0 PC has chosen to stand defenceless against magic.
- **Tier gating.** Anything that takes control of a target - taking a turn away, compulsion, domination - lives only at 9+ and 11+, so it always costs real dice and real Will.
- **Contested duration** where a working lasts. Binding Chains, for one, can be shaken off by resisting again each turn (see `spells_draft.md`).
- **The MIND 0 free die.** Where a MIND 0 creature would otherwise face a roll it cannot make at all - a fear check, a Binding Chains break - it gets one free die (see Free Dice, above). Long odds, never a lockout. This matters at the table as well as in the fiction: the `2, 2, 1, 0` pregen array (see Building a Pregen, `combat_draft.md`) makes MIND 0 a legal player character, and a MIND 0 PC must never be permanently unable to act.

Target caps aren't needed: rolling separately per target already blunts area workings against crowds.

**GM note.** Have enemies charge the party's caster - it's the counterplay the whole system assumes.

## Progression

Raising MIND directly is the wrong lever for progression - it moves the ceiling, pool, and resist floor at once. Treat it as a rare, story-weight advancement, not a per-level increase.

Grow casters sideways instead:

- **More workings known.** Still one cast per round, so the choice gets harder rather than the caster getting stronger.
- **Free resist dice.** A Steadfast-style trait, not more Will.
- **Better refunds.** Borrow the Stormcaller trick: a natural 11-12 returns the *entire* casting pool, not one point.
- **A signature working.** Lower the difficulty by one tier on exactly one named working, not across the board.
- **Access to Channelling**, and later a Trauma discount on it - a signature working that channels for free, or a flat reduction elsewhere. (Not "more uses per day": Channelling was never day-gated, only Trauma-gated, so there's nothing to raise. A second Channel in the same round would mean a second cast, which breaks the one-per-round pacing spine below.)
- **Attunement.** One free Will point per scene, refunded before any spending. This is the "Unlimited Mage" tier and should feel like a genuine milestone.

Reliability, flexibility, and staying power grow; raw ceiling barely moves.

### Learning workings

Workings are gated by Feats, taken at character creation and on levelling. Each Feat tier unlocks the difficulty tier beside it:

| Feat   | Unlocks            | Difficulty |
|--------|--------------------|------------|
| Novice | Lesser workings    | 5+         |
| Adept  | Common workings    | 7+         |
| Expert | Greater workings   | 9+         |
| Master | Legendary workings | 11+        |

Holding the Feat is permission, not possession. Learning an individual working costs downtime and money, and usually a trainer - or luck, where the table turns up a grimoire. Character creation grants a token number of workings based on the character's highest Feat.

**`spells_draft.md` skips this ladder entirely** - a test caster simply knows its whole list, so the loop under test is Casting/Resisting/Trauma, not the Feat economy around them.

**Feat and MIND are separate axes.** Feat sets what tier of magic you could ever perform; MIND sets how reliably you perform it.

## Designing workings

**Effects are flat. MIND buys reliability only.** No working scales its effect with the caster's MIND - no damage equal to MIND, no MIND dice of anything. MIND already decides how often you succeed; letting it decide magnitude too double-dips and makes the gap between tiers of caster vicious. A Greater working does the same thing in a novice's hands as a master's. The master just gets it off.

**Tiers buy scope and duration, not numbers.**

| Tier            | What it may do                                                                               |
|-----------------|----------------------------------------------------------------------------------------------|
| Lesser (5+)     | One target, one round, one step of change. Never takes away a turn.                          |
| Common (7+)     | One target for a real duration, or several targets for a moment.                             |
| Greater (9+)    | Changes the shape of the engagement: area denial, mass fear, moving a body across the field. |
| Legendary (11+) | Alters the scene. Named, story-visible consequences.                                         |

At 17% on one die, nobody casts Legendary without Channelling, and Channelling a Legendary working costs 3 Trauma that only comes off in a town. So every Legendary working costs a piece of the caster's expedition. Price them accordingly. "Heavy damage" is not worth that. "The flood comes and the pursuit ends" is.

**Five hard limits.** Breaking any of these breaks something else in this document.

1. Nothing bypasses the resist roll. The resist is how non-casters participate. **Blessing of the Valar's one-round total immunity (Legendary, `spells_draft.md`) is the one deliberate exception** - matched in scope to the Sanctuary trait above, and costed at the top of the ladder for it.
2. No working generates Will or dice, and no working removes Trauma. Trauma can be moved, never removed. The economy stays closed.
3. No working grants an extra cast. One per round is the pacing spine.
4. Nothing reaches past the MIND ceiling. Free resist dice are the one deliberate exception, and they are defensive only.
5. Damage workings are worse at damage than weapons. A caster's value is doing what a sword cannot.

**A damage working ignores armor entirely.** Compare the total to Dent 0 / Rend 5 - the None line - no matter what the target is wearing, the same treatment a Piercing weapon earns against a foe it's already pinned (see `combat_draft.md`'s Damage & Armor), except a working needs no setup to earn it. This is the one edge Hard Limit 5 promises a caster over a blade: a sword has to get through the harness, a working never has to. It stays worse than a weapon in every other way - the dice are small, a miss (the cast or the target's resist) spends the Will for nothing, and the Will pool that pays for it doesn't refill mid-fight the way a Tempo Pool does. **Workings carry no damage type**, so none of the type rules reach them either way: a working is never Blunt, never Piercing, never Armor-Piercing - it doesn't need to be, since it's already past the armor before any of those would matter.

**Held Will is the third cost lever.** Difficulty says how hard a working is to land. Will says what one casting costs today. Some workings need a price that persists past the scene, and the soul fragment is that price: while the effect exists in the world, a set number of Will points are held out of the caster's pool. Not spent - held. They return when the effect ends and the fragment is reabsorbed.

This is reversible, which is what makes it playable where Trauma is not. A caster with two fragments out has a smaller day, every day, until they take them back.

**A working that holds Will is not sustained** - you can cast freely while it lasts. Sustained workings cost your attention; held ones cost your pool.

Reach for it on any working whose effect should persist between scenes - a fragment given form, a ward left standing on a door, something bound into an object. Dial it by holding more points, or by making the hold permanent at Legendary: a piece lent versus a piece given away. Note this is the only sanctioned way for a working to touch the Will pool, and it only ever subtracts (limit 2 above).

**Duration comes free.** A sustained working lasts while you cast nothing else. No new subsystem, no tracking, and it stops casters from stacking buffs. Most Common and Greater workings should either end on your next turn or be sustained this way; very few should be fire-and-forget. **A sustained working also ends at the end of the scene, or the moment the caster takes any rest, whichever comes first** - it never survives a scene break. Anything meant to outlast a scene belongs on Held Will instead. **A Downed or killed caster instantly ends every Sustained working they're maintaining** - maintaining one takes an active turn, which a Downed or dead caster no longer has.

**Held Will doesn't need the caster conscious, but it does need them alive.** The effect persists on its own once cast - a bound prisoner is still bound if their captor is Downed. **If the caster dies, the fragment is never reabsorbed and the Will it held never returns** - the effect itself is left masterless, not undone: Binding Chains stays shut with nobody left to release it early, though the target can still resist it off on schedule as normal. The GM adjudicates anything stranger than that.

**Two hazards to design around.** Rolling separately per target already blunts the MIND 0 problem - a Greater working thrown at six soldiers simply fails on a third of them, resist or no resist - but a cap on the largest area workings is still worth writing, and group-scale effects that rout and scatter age better than ones that remove bodies. And the ten-minute rule makes every Lesser and Common working free outside combat, so nothing that answers a question or solves an investigation belongs below 9+ - and nothing below 9+ may remove anything from a track (see limit 2).

**On capping area workings.** MESBG never caps by number. It bounds them four other ways instead, and all four port cleanly:

- **Scarcity.** Only five of its thirty-five powers are area effects at all, and few models own them. The cap lives on the spell list, not inside the spell.
- **Geometry.** Effects are bounded by a radius around the caster, a straight line drawn from them, or a piece of terrain - one power only functions near rock, and only becomes an area effect when channelled. Positioning is the limit, and it drags the caster forward into danger.
- **Soft effects.** Its area powers knock models prone, panic mounts and deal weak hits. Every genuinely lethal power in the game is single-target.
- **Friendly fire.** Some spare allies and some do not, and the ones that don't are markedly harder to use well.

Recommended default here: no numeric cap. Bound area workings by a radius measured from the caster, keep their effects to position and morale, and hold genuinely lethal area effects at Legendary. Per-target rolling already blunts the MIND 0 problem, and a radius drawn from the caster does the rest by putting them in reach of a charge.

**Hard limits for area workings.** What a tier is allowed to buy:

| Tier            | Area allowed | Origin                          | Max radius           | Effects permitted                                      |
|-----------------|--------------|---------------------------------|----------------------|--------------------------------------------------------|
| Lesser (5+)     | No           | -                               | -                    | Single target only                                     |
| Common (7+)     | Yes          | The caster                      | 2 squares            | Position and morale; ends on your next turn            |
| Greater (9+)    | Yes          | The caster, or a point in range | 4 squares            | Denial, terrain, sustained effects, taking a turn away |
| Legendary (11+) | Yes          | Any point in range              | 6 squares, or a line | Lethal effects, scene-altering change                  |

"Position and morale" at Common means exactly that, and it's narrower than it sounds: **moving bodies around** (Speed, forced movement, a shove) and **Nerve or fear** are in; a general bonus to attacks, Parries or casts is not, because that's a numbers buff wearing a positional coat.

And six rules that hold regardless of tier:

1. Always roll per target. No area working resolves on a single roll for everyone.
2. **Sparing allies costs a tier.** A working that harms only enemies is written one tier above the same working that catches everything in the radius. This is the cleanest dial you have - use it before reaching for anything else. (A working built on the Fear rule spares allies for free - only enemies ever test against a Fear rating.)
3. No lethal area damage below Legendary. Beneath that, area workings move, frighten, blind, hinder or knock down.
4. Radius is fixed per working, never chosen at cast time. No variable-size areas.
5. One sustained area working at a time, which falls out of the sustain rule for free.
6. Budget roughly one area working per school, two at the outside. Scarcity does more work here than any cap.

**School families are fiction, not mechanics.** Arcane and Divine describe how magic is understood and performed in the setting - who petitions, who commands, who is trusted with what - and carry no rules weight. Nothing about access, difficulty or cost keys off a school's family. Where schools do gate each other, set that school by school.

## At the table

The whole loop, for reading mid-session.

**To cast:** one working per round, costs your Major Action, unengaged, range 12 squares unless stated. Name the working and target. Spend Will, 1 per d12, never more dice than your MIND. Roll. Highest die meets the difficulty or the working fails and the Will is gone. You may Push: spend Trauma, 1 per `+1` to the highest die, max `+2`. No purchased result (Pushed, Channelled, or both) ever exceeds 11 - only a natural, untouched 12 reaches 12.

**Difficulties:** Lesser 5+ · Common 7+ · Greater 9+ · Legendary 11+ (the same ladder as every base DC in the game)

**To resist:** only against workings aimed at you, and fear. Spend your own Will, 1 per d12, up to your MIND, committed before rolling. Tie or beat the caster's highest die (or the Fear rating) and nothing happens. A natural 11 or 12 on a die you paid for comes straight back. Free dice from traits never refund and ignore the MIND ceiling. A MIND 0 creature gets 1 free die against a fear check or a Binding Chains break, and nothing else. You may Push a resist the same way Casting does.

**Friendly targets never resist.** Buffs simply land.

**Several targets:** commit the pool once, roll it fresh for each target, each resists separately.

**Channelling:** declare at the **end** of your turn, paying 1 Will and Trauma by tier (1 Lesser/Common, 2 Greater, 3 Legendary). Cast it as your first action next turn - a Move to become unengaged first is fine, nothing else is. **One die, and only one**, is set to the working's difficulty exactly; you may not add dice alongside it. The defender still resists normally, and against a low-tier working that set die is an *easy* number to beat - Channel unresisted workings and the top of the ladder, not Common attacks. Can be Pushed further on top, capped at 11 same as any purchase. If you're still Engaged when you would cast, you can't, and the cost is spent anyway.

**Held Will** workings aren't sustained - cast freely while they last, and they outlast the caster being Downed (though not the caster dying, which strands the effect for good - see Held Will, above). **Sustained** workings end when you cast anything else, at the end of the scene, at your next rest (Short included), or the moment you're Downed or killed, whichever comes first.

**Out of combat:** ten uninterrupted minutes counts as a rolled 7. No Will, no roll. Under any clock at all, cast normally. "Until your next turn" lasts about a minute.

**Recovery:** Short returns 1 Will. Field returns Will equal to MIND, minimum 2 (one Field rest a day). Long Rest returns all your Will. Trauma comes off only through Revelry & Leisure in town. Scars need a week of downtime and a DC 11 Chirurgery check, one at a time.

**Will pool:** MIND × 3.

## Reference tables

**Casting - chance at least one die meets the difficulty.** Rows capped by MIND.

| Dice | 5+   | 7+  | 9+  | 11+ |
|------|------|-----|-----|-----|
| 1    | 67%  | 50% | 33% | 17% |
| 2    | 89%  | 75% | 56% | 31% |
| 3    | 96%  | 88% | 70% | 42% |
| 4    | 99%  | 94% | 80% | 52% |
| 5    | >99% | 97% | 87% | 60% |

**Resisting - chance to tie or beat the caster's highest die.**

| Caster's high | 1 die | 2 dice | 3 dice | 4 dice | 5 dice |
|---------------|-------|--------|--------|--------|--------|
| 5             | 67%   | 89%    | 96%    | 99%    | >99%   |
| 7             | 50%   | 75%    | 88%    | 94%    | 97%    |
| 9             | 33%   | 56%    | 70%    | 80%    | 87%    |
| 11            | 17%   | 31%    | 42%    | 52%    | 60%    |
| 12            | 8%    | 16%    | 23%    | 29%    | 35%    |

The 7 and 9 rows double as the odds of passing a Terror or Dread fear check - read the **1 die** column for a MIND 0 creature on its free die. The 5 row is what a channelled Lesser working presents to a defender, and it is the reason not to Channel one.

**Trauma - band and what it takes to get there.** Carries no roll penalty (see Trauma, above) - it gates Scars and Automatic Death only.

| Trauma | Band                | Reached by                                                                                         |
|--------|---------------------|----------------------------------------------------------------------------------------------------|
| 0-4    | Clear               | A few Exerts, a Push or a Channel                                                                  |
| 5-9    | Manageable          | Patching up after a fight or two: every healed Wound taxes it, Rend-line hits worse                |
| 10-14  | Dangerous           | An expedition without a town, healing up after several fights, or a Legendary Channel on a bad one |
| 15-19  | Critical            | Stacking every source across a long trip - **and a Resolve check at DC 11 if a fight ends here**   |
| 20     | **Automatic Death** | -                                                                                                  |

**Nothing reduces the casting and resisting tables above.** The Wound Penalty (see `combat_draft.md`'s Wounds & Death's Door) only ever reduces a Check, and casting and resisting are both Tempo-style rolls, not Checks - the numbers on this page are the real ones, unmodified.

## Playtest watchlist

Six signals tell you whether the numbers are wrong.

1. **Are casters ending the day with unspent Will?** If yes, the pool is too generous - drop to MIND × 2. If they are dry before the second fight, raise to × 4. Watch the MIND 2 pregen especially: a single Binding Chains locks a third of their day.
2. **Does resisting feel like a decision at MIND 1?** One die against a 9-high is a 33% shot. If players stop bothering, either hand out free dice more freely or lower Greater-tier workings to 8+.
3. **Does anyone ever cast at 11+?** If the Legendary tier goes untouched across several sessions it is a trap option. Drop it to 10+, or make Channelling the ordinary route to reaching it.
4. **Is Channelling a decision or a reflex?** Now that it commits exactly one die, it should be near-worthless on Common attack workings and near-mandatory on Legendary ones. If players still Channel everything, the tier Trauma costs are too flat; if they never Channel at all, the end-of-turn declaration is too exposed.
5. **Where is Trauma sitting when an expedition ends?** Consistently in Clear means the track is doing nothing and needs more sources (see `combat_draft.md`'s watchlist). Consistently Critical means Scars will pile up faster than town downtime can clear them, and the party will spiral.
6. **Are casters reaching the Critical band without being hit?** Pushing and Channelling are supposed to be able to walk a caster to a Scar on their own. If that never happens, the magic-side Trauma costs are decorative.
