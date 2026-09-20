Magic is the manipulation of energy - ten schools, each its own discipline, with no split between how they're learned or how they resolve. It is rare not just because people lack potential, but because they lack education and resources. With literacy rates below ~15%, magic remains confined to the wealthy, the religious, and the exceptionally lucky. Because talent is worthless if you have no way to learn.

**The Literacy Barrier:** The vast majority of people will never read a spell formula or a holy text. Even a caster with real talent cannot learn what they cannot read - see [[Literacy|core_rules]]: only a character with **MIND 2+** is literate by default, and only a literate character can invest in a magic school.

Learning any school requires access to teachers or texts, materials or offerings, and years of study or devotion, depending on the school's own flavor (see The Ten Schools, below). This is why hedge wizards are suspicious, wandering priests are valuable, and spellbooks are worth more than gold.

**For the deeper physics behind why magic behaves this way - and how to rule on an effect no spell list covers - see [[Laws of Magic|laws_of_magic]].**

---

## The Ten Schools

There is no Arcane/Divine split. Every school below works identically - same MIND, same Will pool, same roll, same Feat-tier system. Some schools keep a devotional, prayer-shaped flavor (Benediction, Cultivation, Invocation, Necration, Subjugation); others read as formulaic study (Aeromancy, Geomancy, Hydromancy, Pyromancy, Shadowmancy). That flavor is real for roleplay and for how a school's fiction reads - a Necromancer petitions a source the way a Pyromancer never has to - but it carries **no mechanical weight**. See [[Magic Feats|magic_feats]] for how a school is actually unlocked.

---

## MIND and the Will Pool

**2026-09-20 (the Reach/Tempo rework):** magic's whole resolution engine is replaced, adapted from Middle-earth Strategy Battle Game's Magical Powers. This section and Casting/Resisting/Channelling below supersede the old flat `1d12 + Feat bonus vs. DC` roll entirely.

MIND does two separate jobs, and the split between them is the core of this system.

**MIND is a hard ceiling on dice.** You may never commit more dice to a single cast or resist than your MIND rating. Dice granted free by traits sit outside this ceiling (see [Free Dice](#free-dice), below).

**MIND sets the daily pool.** **Will points = MIND x 3**, minimum 0, refreshed on the [[Rest \& Repair|rest_and_survival]] ladder - Short returns 1, Field returns MIND (minimum 2), Long Rest returns all of it.

Everyone has a MIND score, not just casters. It also pays for **resisting hostile magic and fear** (see [[Fear|exchange]]). NPC casters run on the same MIND x 3 budget, commit dice under the same ceiling, and recover on the same Rest ladder as player casters.

**Named-NPC floor.** Any Named NPC (see [[Named Characters|rest_and_survival]]) has MIND 1 minimum. Player characters aren't covered - a MIND 0 PC has chosen to stand defenceless against magic.

---

## Casting

One working per character per round, costing your Major Action (see [[Action Economy|combat]]). The caster must be unengaged (see [[Distance \& Reach|exchange]]). **Every working has a range of 12 squares unless its entry says otherwise**, and needs line of sight to its target exactly like a shot - Total cover blocks it the same way it blocks an arrow, and darkness hinders it the same way (see [[Shot DC|exchange]] and [[Light and Vision|stealth_and_light]]). A working aimed at a point rather than a creature needs line of sight to that point instead.

1. Declare the working and a legal target in range.
2. Commit Will - 1 point per `1d12`, up to your MIND. **Pay before rolling.** You cannot buy a die, see the result, and buy another.
3. Roll. Take the **highest** die, not the sum.
4. You may **Push**: spend Trauma, 1 per `\+1` to the highest die, up to `\+2` per roll, declared immediately so the target knows the final number.
5. Meet or beat the difficulty and it goes off. Miss and every Will point committed is gone.

**No purchased result may exceed 11 - only a natural, unmodified 12 ever reaches 12.** Channelling and Pushing are both purchases; rolling isn't. A Channelled die, a Pushed die, or a Channelled die pushed further all cap at 11, however they combine.

### **The Difficulty Ladder**

The same four-tier ladder every other DC in the game uses (see [[Setting a Difficulty Class \(DC\)|core_rules]]):

| Tier | DC | One die | What lives here |
|-----------|--------|---------|--------------------------------------------|
| Lesser | 5+ | 67% | Utility, small buffs, single-target nudges |
| Common | 7+ | 50% | Workhorse control and damage |
| Greater | 9+ | 33% | Battle-turning effects |
| Legendary | 11+ | 17% | Once-a-day, story-altering workings |

Workings that target an ally or the caster cannot be resisted and simply take effect. Only workings aimed at an unwilling target go to a resist roll (see [Resisting](#resisting), below).

**A working with several targets is resolved one target at a time.** Commit the pool once, roll it fresh against each target, and each resists separately with their own Will. Extra targets cost no extra Will, only reliability - never one roll for the whole group. **Channelling a multi-target working guarantees exactly one of those rolls** - name the target when you declare Channelling; every other target in the same casting is rolled normally. **Will lost on a miss is committed once, not per target.** **Unresisted multi-target workings (allies, self) roll once, not per target.** **Pushing a multi-target casting applies once, to every rolled target alike** - declared when you commit the cast, costing Trauma once, not per target.

**"Until your next turn" outside combat** lasts about a minute.

### **Magic Damage**

Roll the working's damage dice and compare the total to Dent 0 / Rend 5 - **a damage working ignores armor entirely**, no matter what the target is wearing (see [[Damage Types|rest_and_survival]]). **Workings carry no damage type**, so none of Blunt/Piercing/Slashing's rules ever reach one - it doesn't need them, since it's already past the armor before any would matter. This is the one edge a caster holds over a blade: a sword has to get through the harness, a working never has to. It stays worse than a weapon in every other way (see [Designing Workings](#designing-workings), below).

---

## Resisting

Resisting is casting, mirrored. The target commits their own Will - 1 point per `1d12`, up to their MIND, paid before rolling - and needs to **tie or beat the caster's highest die** to negate the working entirely. A defender may Push the resist roll the same way, spending Trauma instead.

A Fear check (see [[Fear|exchange]]) is a resist against a fixed number - the creature's Fear rating stands in for the caster's highest die.

**The refund.** A natural 11 or 12 on a resist die that came from the defender's own Will pool returns that point immediately. "Natural" means rolled and unmodified - a Pushed die's new value never refunds. A resist die can never be Channelled (see Channelling, below), so that case doesn't arise. Dice granted free by traits never refund.

### Free Dice

Free dice are the defensive tech of this system, and the main thing to hand out as a trait, blessing, or Feat benefit. **Free dice ignore the MIND ceiling. Will never does.** This is the only way a MIND 0 character ever passes a Fear check, and it is also the standing escape hatch the rules use wherever a MIND 0 creature would otherwise be locked out with no roll at all - a Fear check and a Binding Chains-style break attempt each hand a MIND 0 creature **one free die**. *A MIND 0 creature always gets a die, never a certainty.*

**Be sparing with these traits** - free dice cost nothing, never refund, and stack; a party with three sources effectively opts out of hostile magic.

---

## Channelling

**Declare Channelling at the end of your turn,** naming the working and paying its cost. **On your next turn, casting it must be your first action** - a Move taken purely to become unengaged doesn't break this, but nothing else may come before the cast. **One die of your casting pool is set to the working's difficulty number exactly** - a channelled 9+ gives you a 9. That die is guaranteed to meet the difficulty - the defender still gets a normal resist roll against it. **Channelling commits exactly that one die, for exactly that one Will - no further dice alongside it, even if your MIND allows more.**

**Cost.** 1 Will, committed as normal (it just isn't rolled), and Trauma scaled to the working's tier: **1 for Lesser and Common, 2 for Greater, 3 for Legendary.** Both are paid when you declare.

**Channelling and Pushing stack, capped at 11 total.** The channelled die can still be Pushed afterward at the usual cost - a Legendary working, already channelled to 11, can't be Pushed further.

**Because the channelled die presents the difficulty number and nothing higher, it also presents the easiest possible number to resist.** A channelled Lesser working shows a 5, which one die ties or beats 67% of the time. **Channelling is for unresisted workings**, where guaranteeing the cast is the entire point, **and for Greater and Legendary workings**, where a guaranteed 9 or 11 is a number a defender genuinely struggles with. Channelling a Common working at a resisting enemy is usually a mistake.

**Risk.** You must be unengaged when the cast happens. If you're still Engaged when you would cast - because you couldn't break away, or chose not to - you can't cast, and the cost is lost. Charging the caster is the counterplay. **Channelling only ever applies to your own cast** - a resist roll happens off-turn, on someone else's, and can never be Channelled.

---

## Recovery and casting outside combat

**Will recovers on the same [[Rest \& Repair|rest_and_survival]] ladder as Wounds and gear.** **Trauma does not sit on this ladder** - only [[Revelry \& Leisure|rest_and_survival]] removes it.

**Outside pressure, taking ten uninterrupted minutes counts as having rolled a 7.** No Will spent, no roll made. **Workings that move Trauma never get this shortcut** - they always cost a real Will point and a real roll. A working attempted under any pressure at all - a watch approaching, a rope fraying, anything with a clock - is a normal cast.

---

## MIND 0 and ordinary people

Most humans are MIND 0-1: domination, terror, and compulsion would auto-succeed against nearly any NPC without limits. Four guard rails:

- **Named-NPC floor** (above).
- **Tier gating.** Anything that takes control of a target - taking a turn away, compulsion, domination - lives only at 9+ and 11+, so it always costs real dice and real Will.
- **Contested duration** where a working lasts, rather than an outright lock (see a school's own list for workings of this shape).
- **The MIND 0 free die** (see Free Dice, above). Long odds, never a lockout. A MIND 0 PC must never be permanently unable to act.

Target caps aren't needed: rolling separately per target already blunts area workings against crowds.

**GM note.** Have enemies charge the party's caster - it's the counterplay the whole system assumes.

---

## Designing Workings

**Effects are flat. MIND buys reliability only.** No working scales its effect with the caster's MIND - no damage equal to MIND, no MIND dice of anything. A Greater working does the same thing in a novice's hands as a master's. The master just gets it off.

**Tiers buy scope and duration, not numbers.**

| Tier | What it may do |
|-----------------|-----------------------------------------------------------------------------------------------|
| Lesser (5+) | One target, one round, one step of change. Never takes away a turn. |
| Common (7+) | One target for a real duration, or several targets for a moment. |
| Greater (9+) | Changes the shape of the engagement: area denial, mass fear, moving a body across the field. |
| Legendary (11+) | Alters the scene. Named, story-visible consequences. |

At 17% on one die, nobody casts Legendary without Channelling, and Channelling a Legendary working costs 3 Trauma that only comes off in a town. Price a Legendary working accordingly - "heavy damage" is not worth that; "the flood comes and the pursuit ends" is.

**Five hard limits.** Breaking any of these breaks something else in this system.

1. Nothing bypasses the resist roll. The resist is how non-casters participate. A single, deliberate Legendary working may grant total immunity for one round as its whole effect - matched in scope to a Sanctuary-style free-die trait, and costed at the top of the ladder for it - but that's the one sanctioned exception.
2. No working generates Will or dice, and no working removes Trauma. Trauma can be moved, never removed. The economy stays closed.
3. No working grants an extra cast. One per round is the pacing spine.
4. Nothing reaches past the MIND ceiling. Free resist dice are the one deliberate exception, and they are defensive only.
5. Damage workings are worse at damage than weapons. A caster's value is doing what a sword cannot (see [Magic Damage](#magic-damage), above).

**Held Will is the third cost lever**, alongside Will spent and Trauma. Difficulty says how hard a working is to land. Will says what one casting costs today. Some workings need a price that persists past the scene: while the effect exists in the world, a set number of Will points are **held** out of the caster's pool - not spent, held - and return when the effect ends and is reabsorbed. This is reversible, which is what makes it playable where Trauma is not. **A working that holds Will is not sustained** - cast freely while it lasts. Reach for it on any working whose effect should persist between scenes - a fragment given form, a ward left standing on a door, something bound into an object. Dial it by holding more points, or make the hold permanent at Legendary tier.

**Held Will doesn't need the caster conscious, but it does need them alive.** The effect persists on its own once cast. **If the caster dies, the fragment is never reabsorbed and the Will it held never returns** - the effect itself is left masterless, not undone.

**Duration comes free.** A **sustained** working lasts while you cast nothing else - no new subsystem, no tracking, and it stops casters from stacking buffs. Most Common and Greater workings should either end on your next turn or be sustained this way; very few should be fire-and-forget. **A sustained working also ends at the end of the scene, or the moment the caster takes any rest, whichever comes first** - it never survives a scene break. **A Downed or killed caster instantly ends every Sustained working they're maintaining.**

**Two hazards to design around.** Rolling separately per target already blunts the MIND 0 problem, but a cap on the largest area workings is still worth writing, and group-scale effects that rout and scatter age better than ones that remove bodies. The ten-minute rule makes every Lesser and Common working free outside combat, so nothing that answers a question or solves an investigation belongs below 9+, and nothing below 9+ may remove anything from a track.

**On capping area workings**, bound by four levers rather than a number cap:

- **Scarcity.** Keep area effects rare on any given spell list, and few characters holding them.
- **Geometry.** Bound by a radius around the caster, a straight line drawn from them, or a piece of terrain. Positioning is the limit, and it drags the caster forward into danger.
- **Soft effects.** Knock Prone, panic, deal weak hits. Save the genuinely lethal effects for single-target workings.
- **Friendly fire.** Some workings spare allies and some do not, and the ones that don't are markedly harder to use well.

**Hard limits for area workings.** What a tier is allowed to buy:

| Tier | Area allowed | Origin | Max radius | Effects permitted |
|-----------------|--------------|----------------------------------|-----------------------|----------------------------------------------------------|
| Lesser (5+) | No | \- | \- | Single target only |
| Common (7+) | Yes | The caster | 2 squares | Position and morale; ends on your next turn |
| Greater (9+) | Yes | The caster, or a point in range | 4 squares | Denial, terrain, sustained effects, taking a turn away |
| Legendary (11+) | Yes | Any point in range | 6 squares, or a line | Lethal effects, scene-altering change |

"Position and morale" at Common means exactly that: **moving bodies around** (Speed, forced movement, a shove) and **Nerve or fear** are in; a general bonus to attacks, Parries or casts is not, because that's a numbers buff wearing a positional coat.

And six rules that hold regardless of tier:

1. Always roll per target. No area working resolves on a single roll for everyone.
2. **Sparing allies costs a tier.** A working that harms only enemies is written one tier above the same working that catches everything in the radius. (A working built on the Fear rule spares allies for free - only enemies ever test against a Fear rating.)
3. No lethal area damage below Legendary. Beneath that, area workings move, frighten, blind, hinder or knock down.
4. Radius is fixed per working, never chosen at cast time.
5. One sustained area working at a time, which falls out of the sustain rule for free.
6. Budget roughly one area working per school, two at the outside.

**School families are fiction, not mechanics.** Arcane and Divine describe how magic is understood and performed in the setting - who petitions, who commands, who is trusted with what - and carry no rules weight. Nothing about access, difficulty or cost keys off a school's family. Where schools do gate each other, set that school by school.

---

## At the table

The whole loop, for reading mid-session.

**To cast:** one working per round, costs your Major Action, unengaged, range 12 squares unless stated. Name the working and target. Spend Will, 1 per `1d12`, never more dice than your MIND. Roll. Highest die meets the difficulty or the working fails and the Will is gone. You may Push: spend Trauma, 1 per `\+1` to the highest die, max `\+2`. No purchased result (Pushed, Channelled, or both) ever exceeds 11 - only a natural, untouched 12 reaches 12.

**Difficulties:** Lesser 5+ - Common 7+ - Greater 9+ - Legendary 11+ (the same ladder as every base DC in the game).

**To resist:** only against workings aimed at you, and Fear. Spend your own Will, 1 per `1d12`, up to your MIND, committed before rolling. Tie or beat the caster's highest die (or the Fear rating) and nothing happens. A natural 11 or 12 on a die you paid for comes straight back. Free dice from traits never refund and ignore the MIND ceiling. A MIND 0 creature gets 1 free die against a Fear check or a similar break attempt, and nothing else. You may Push a resist the same way Casting does.

**Friendly targets never resist.** Buffs simply land.

**Several targets:** commit the pool once, roll it fresh for each target, each resists separately.

**Channelling:** declare at the **end** of your turn, paying 1 Will and Trauma by tier (1 Lesser/Common, 2 Greater, 3 Legendary). Cast it as your first action next turn. **One die, and only one**, is set to the working's difficulty exactly; no further dice alongside it. The defender still resists normally. Can be Pushed further on top, capped at 11.

**Held Will** workings aren't sustained - cast freely while they last, and they outlast the caster being Downed (though not the caster dying, which strands the effect for good). **Sustained** workings end when you cast anything else, at the end of the scene, at your next rest (Short included), or the moment you're Downed or killed, whichever comes first.

**Out of combat:** ten uninterrupted minutes counts as a rolled 7. No Will, no roll. Under any clock at all, cast normally. "Until your next turn" lasts about a minute.

**Recovery:** Short returns 1 Will. Field returns Will equal to MIND, minimum 2. Long Rest returns all your Will. Trauma comes off only through Revelry \& Leisure in town.

**Will pool:** `MIND x 3`.

## Reference tables

**Casting - chance at least one die meets the difficulty.** Rows capped by MIND.

| Dice | 5+ | 7+ | 9+ | 11+ |
|------|------|-----|-----|-----|
| 1 | 67% | 50% | 33% | 17% |
| 2 | 89% | 75% | 56% | 31% |
| 3 | 96% | 88% | 70% | 42% |
| 4 | 99% | 94% | 80% | 52% |
| 5 | \>99% | 97% | 87% | 60% |

**Resisting - chance to tie or beat the caster's highest die.**

| Caster's high | 1 die | 2 dice | 3 dice | 4 dice | 5 dice |
|---------------|-------|--------|--------|--------|--------|
| 5 | 67% | 89% | 96% | 99% | \>99% |
| 7 | 50% | 75% | 88% | 94% | 97% |
| 9 | 33% | 56% | 70% | 80% | 87% |
| 11 | 17% | 31% | 42% | 52% | 60% |
| 12 | 8% | 16% | 23% | 29% | 35% |

The 7 and 9 rows double as the odds of passing a Terror or Dread Fear check (see [[Fear|exchange]]) - read the **1 die** column for a MIND 0 creature on its free die.

---

## Learning Workings

**Workings are gated by Feats**, taken at character creation and on levelling - see [[Magic Feats|magic_feats]]. Holding the Feat is permission, not possession: learning an individual working still costs downtime and money, and usually a trainer.

| Feat | Unlocks | Difficulty |
|--------|--------------------|------------|
| Novice | Lesser workings | 5+ |
| Adept | Common workings | 7+ |
| Expert | Greater workings | 9+ |
| Master | Legendary workings | 11+ |

**Learning New Workings:** requires time, money, and practice. At character creation you may spend 50 Crown per tier (Lesser 50, Common 100, Greater 150, Legendary 200) to "buy" your starting workings. Otherwise: 1 day studying per tier, and the same Crown cost, in whatever materials, offerings, or tuition the school's flavor calls for, from a teacher, a text, a mentor, or - where the fiction wants it - a vision or a master's demonstration.

**Feat and MIND are separate axes.** The Feat sets what tier of magic you could ever perform; MIND sets how reliably you perform it.

---

## Progression

Raising MIND directly is the wrong lever for progression - it moves the ceiling, pool, and resist floor at once. Treat it as a rare, story-weight advancement (see [[Per Level Advancement|progression_&_rewards]]), not a routine per-level increase.

Grow casters sideways instead - see [[Magic Feats|magic_feats]] for how Focus Feats spend this menu:

- **More workings known.** Still one cast per round, so the choice gets harder rather than the caster getting stronger.
- **Free resist dice.** A trait or Feat benefit, not more Will.
- **Better refunds.** A natural 11-12 that returns the *entire* casting pool, not one point.
- **A signature working.** Discount its Will cost, or let it Channel for free - not a difficulty change across the board.
- **Access to Channelling, and later a Trauma discount on it.** Not "more uses per day": Channelling was never day-gated, only Trauma-gated.
- **Attunement.** One free Will point per scene, refunded before any spending - a late-game milestone.

Reliability, flexibility, and staying power grow; raw ceiling barely moves.

---

**For small, instinctive Will effects that fall outside a normal working, see [[Minor Magic|minor_magic]].**
