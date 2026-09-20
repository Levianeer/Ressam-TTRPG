# Ressam - Workings (Playtest Draft)

*Playtest draft - these rules are still being tested and may change between sessions.*

Fifteen workings, built against `magic_draft.md`'s Casting, Resisting, and Designing Workings rules. Read that file first - this one is only the content that plugs into it. Named and modeled on Middle-earth Strategy Battle Game's Magical Powers - the game `magic_draft.md` itself is adapted from - rather than generic fantasy-spell filler; where a working's shape diverges from its MESBG namesake, that's called out below.

**One universal list, no schools.** `magic_draft.md` already says school families carry no rules weight; this slice skips them entirely rather than inventing gates it can't playtest. Any caster with Will to spend may attempt any working here. **Feat-gating is also skipped** - `magic_draft.md`'s Novice/Adept/Expert/Master unlock ladder isn't exercised by this draft; a test character simply knows the whole list.

**Range is 12 squares** for every working unless its Target column says otherwise.

Every working follows the Five Hard Limits verbatim: the resist roll is never bypassed except by Blessing of the Valar's one-round total immunity (below - the one deliberate exception Limit 1 carves out), nothing generates Will or dice and nothing removes Trauma (Mending Touch *moves* it, which the limit allows and the ten-minute rule can't shortcut - see `magic_draft.md`), nothing grants an extra cast, nothing reaches past the MIND ceiling except a defensive free die (Ward of Aegis, and the MIND 0 free die on a Binding Chains break - both defensive, both inside the exception Limit 4 carves out), and every damage working rolls worse than a comparable weapon - lower dice, no STR added, no Shock, no Openings, and no damage type, so none of `equipment_draft.md`'s Blunt, Piercing or Armor-Piercing rules ever apply to one - though it does ignore armor outright, which none of that list can do (see Reading the tables, below).

**Denser in area workings than `magic_draft.md`'s own scarcity guideline recommends** (one area working per school, two at the outside) - four of the fifteen below are area effects. Deliberate for this slice: a single playtest session should exercise every area tier at least once, which a properly scarce list wouldn't guarantee. Treat the density itself as something to correct once this stops being a test list.

**One deliberate divergence from the source material.** MESBG's Immobilize/Transfix (a full lockdown) casts at its *cheapest* tier - the equivalent of our Lesser. `magic_draft.md`'s own Hard Limits table reserves "taking a turn away" for Greater and above, so The Long Root sits there instead.

---

## Lesser (5+)

One target, one round, one step of change. Never takes a turn away.

| Working             | Target                               | Effect                                                                                     | Resisted? |
|:--------------------|:-------------------------------------|:-------------------------------------------------------------------------------------------|:---------:|
| **Ember Lash**      | One creature                         | 1d4 damage.                                                                                |    Yes    |
| **Mending Touch**   | One other willing creature, Adjacent | Move 2 Trauma from them to you.                                                            |    No     |
| **Terrifying Aura** | One willing creature (self included) | Any enemy that attacks them in melee takes `-1` on that attack roll, until your next turn. |    No     |
| **Drain Courage**   | One creature                         | `-1` to their next roll before your next turn.                                             |    Yes    |

## Common (7+)

One target for a real duration, or several targets for a moment.

| Working             | Target                         | Effect                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Resisted? |
|:--------------------|:-------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------:|
| **Binding Chains**  | One creature                   | Restrained (see Conditions, `combat_draft.md`). Persists between scenes: while it holds, you **hold 2 Will** out of your pool (see Held Will, `magic_draft.md`) - not sustained, so you can cast freely meanwhile. Ends when you release it (free action), or when they break free by resisting again - **once on each of their turns in combat, or once per day outside it** - spending Will as normal; tie or beat the original casting's highest die. **A MIND 0 target gets 1 free die** (ignores their MIND ceiling, per Free Dice in `magic_draft.md`) on each break attempt. |    Yes    |
| **Ward of Aegis**   | One willing creature           | They gain 1 free die (ignores their MIND ceiling) on the next resist roll they make before your next turn - fear checks included.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |    No     |
| **Aura of Command** | Allies within 2 squares of you | `+2` Speed until your next turn. This is a Common-tier area working: origin is you, radius 2 squares, effect limited to position.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |    No     |
| **Chill Soul**      | One creature                   | 1d6 damage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |    Yes    |

## Greater (9+)

Changes the shape of the engagement: area denial, mass fear, moving a body across the field.

| Working           | Target               | Effect                                                                                                                                                             |       Resisted?       |
|:------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------:|
| **Tremor**        | A point within range | Ground in a 4-square radius becomes difficult terrain until you cast something else (sustained). No lethal effect - pure denial, as Greater area workings require. |          No           |
| **Instill Fear**  | Self                 | You carry a Fear rating of **9** (Dread), sustained (see Fear, `combat_draft.md`).                                                                                 | Yes (as a fear check) |
| **Banishment**    | One creature         | 2d6 damage.                                                                                                                                                        |          Yes          |
| **The Long Root** | One creature         | Until your next turn, the target is **Restrained** and cannot take a Major Action. This hold can't be broken early.                                                |          Yes          |

## Legendary (11+)

Alters the scene. Named, story-visible consequences.

| Working                   | Target               | Effect                                                                                                                                         |    Resisted?     |
|:--------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:----------------:|
| **Nature's Wrath**        | A point within range | Each creature within a 6-square radius resists separately; on a failure, 2d10 damage. Legendary is the only tier area lethality is allowed at. | Yes (per target) |
| **Blessing of the Valar** | One willing creature | Total immunity to hostile workings, including fear checks, for one round.                                                                      |        No        |
| **The Long Hush**         | A point within range | Every creature within 6 squares resists separately; on a failure, that creature cannot cast, Push, or Channel until your next turn.            | Yes (per target) |

---

## Reading the tables

**Target** is who the effect lands on if it isn't resisted (or can't be). **Resisted?** marks whether it goes to a resist roll at all - a working aimed at an ally or the caster never does, per `magic_draft.md`'s Casting rules.

**Multi-target workings** (Nature's Wrath, The Long Hush) roll once against each target in range, each resisting separately with their own Will - never one roll for the whole group. Channelling one of these guarantees exactly one named target; every other target is still rolled normally.

**Instill Fear** is resisted differently: it doesn't target anyone. Each enemy who tries to close with the caster makes a fear check against its rating of 9, and only enemies ever test - so it spares allies without costing a tier. A creature that fails **can't close with the caster that turn** (see Fear, `combat_draft.md`) - it can still move elsewhere and still act - and tests again the next time it tries. **A MIND 0 mook isn't locked out**: it tests on its one free die, which clears a Dread 9 a third of the time, so a line of ordinary soldiers gets through eventually and the aura buys the caster turns rather than immunity. Enemies already fighting the caster when it goes up aren't affected; it keeps people away rather than breaking a fight already under way. Because it's sustained, it's a stance: while it holds, the caster casts nothing else.

**Aura of Command is position, not power.** `+2` Speed is what the Common-tier area row allows (see `magic_draft.md`'s area limits), and it is worth more than it looks in a game with entry-triggered Opportunity Attacks, a movement gate on shots, and a caster who has to stay unengaged. It does not touch any roll.

**Mending Touch moves Trauma, it doesn't remove it** - the party's total is unchanged. A caster at 18 Trauma who casts it reaches 20 and dies; the rules allow this. It never gets the ten-minute rule's free cast (`magic_draft.md`) - always a real Will point and a real roll.

**The Long Root** locks down fully for one round: no movement, no Major Action, at most 1 die per Parry (Restrained). Note what that hands your melee: a Restrained target's armor is no protection against a Normal-Reach Piercing weapon (see Damage & Armor, `combat_draft.md`), so The Long Root on a man in plate is an invitation to the party's knife.

**Blessing of the Valar's immunity covers fear checks too** - a fear check is a resist roll (`magic_draft.md`'s Resisting), so a protected target auto-passes one like any other hostile working. It isn't sustained; a second round costs a fresh Legendary cast.

**Damage numbers are flat regardless of who's casting** (see `magic_draft.md`'s Designing Workings), and **ignore armor entirely** - the total is compared to Dent 0 / Rend 5 no matter what the target is wearing, so a damage working is never Turned Aside once it lands, unlike a weapon that can bounce off plate outright. **Workings carry no damage type**, so none of the armor-defeating rules the weapons now have reach them - they don't need to, since armor was never in the way. In practice: Ember Lash always deals exactly 1 Wound once it lands (1d4 never reaches Rend 5); Chill Soul reaches 2 Wounds on a 5-6 (33%); Banishment and Nature's Wrath reach 2 Wounds on almost any roll. That's the whole of magic's edge over a blade here - a small, guaranteed Wound armor can't stop, paid for out of a pool that doesn't come back until a rest.

**Held Will in practice.** Binding Chains is this list's one working priced on Held Will rather than a flat Trauma/Will cost - it's what lets a binding survive past the scene it was cast in. A caster holding it has a permanently smaller Will pool until they let go. In a fight, a bound MIND 1 prisoner resists once per turn and a MIND 0 one gets its free die, so the binding is real counterplay rather than a lockout. **Out of combat the attempt comes once a day, not once an hour** - that's what keeps the working worth its Held Will, since an hourly attempt at 33% means an ordinary prisoner is loose before nightfall and the price stops buying anything. Nothing stops holding several bindings at once - only Will pool room does: each one permanently reserves 2, so a MIND 3 caster (9 Will) tops out around four before there's no pool left to cast anything else, and a MIND 2 caster (6 Will) feels the first one immediately.

---

## Playtest watchlist

Same spirit as `magic_draft.md`'s own watchlist, narrowed for this specific list:

1. **Is any working obviously never picked?** If a table sits unused across a session, it's either overcosted for its tier or outclassed by something on the same or a cheaper tier. Two to watch first: **Drain Courage**, which costs a resist roll to impose the same `-1` that **Terrifying Aura** hands out unresisted, against every attacker, on the same tier; and **Instill Fear**, which costs the caster every other cast in the fight.
2. **Does armor-bypass make a caster the better answer to Plate, not just a different one?** A martial needs the target Restrained or Downed and a Normal-Reach Piercing weapon to skip armor at all; a caster just needs the working to land. If parties stop bothering with the Grapple-then-knife combo once there's a caster along, the bypass is undercutting the martial's own gap-seeking niche rather than sitting beside it - narrow it (Greater and up only, say) rather than reaching for Trauma damage instead.
3. **Is Held Will (Binding Chains) actually felt as a cost?** If a caster holds it and never notices their pool is smaller, the 2-point hold is too cheap for what it buys - a restraint that survives the scene.
4. **Does the free die make Binding Chains worth casting at all?** It should cost a MIND 0 target several turns, not none and not forever. If bound mooks are walking free in a round, raise the break to a full resist with no free die in combat and keep the free die only for the daily attempt.
5. **Is Mending Touch shuffling Trauma to dodge Resolve checks too easily?** The Scar Line reads your band when the fight ends, so 2 Trauma moved in the last round can drop someone under a rung and skip the check entirely - and moving it *back* afterwards doesn't re-trigger anything, since the Line only rises when a fight ends. If parties routinely park Trauma on whoever is lowest right before a fight ends, raise the cost (move 2 from them, take 3 yourself) or check against the highest band reached during the fight rather than the ending one.
6. **Is Aura of Command cast now that it's Speed?** It went from a general `+1` (over the Common-tier limit) through a morale-only version (near-useless) to this. If `+2` Speed for a radius-2 group still never comes up, the problem is the tier, not the effect - and it should move to Greater with a bigger radius rather than get its numbers back.
