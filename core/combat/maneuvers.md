> **Measure, in one sentence:** Compare your own weapon's Measure Band to the current shared measure - two bands off (Grip vs. Far) and you can't Strike at all, one band off and you Strike at Disadvantage. This is symmetric: shifting the measure to suit your own reach puts *their* weapon out of step with it in turn. Every other Measure mention in this chapter points back to this line; see [[Reach|combat]] for the full mechanic.

## How an Exchange Works

This is the map of a melee exchange, start to finish, and where each piece of it lives in the rules. Read this first if the Oppose Reaction is new to you - the roll-by-roll detail below assumes you already know the loop.

**The short version:** They swing. If it'd hit, you can answer. Roll off. Win big: two Effects. Win small: one. Lose small: half damage. Lose big: full damage. Either side can burn another Reaction to re-roll instead of accepting a result - that's the Press, below.

| Step                      | Ask Yourself | Then                                                                                                                                                                                                                                                                                 |
|:--------------------------| :---- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. Get into range**     | Is the current measure within my weapon's Strike range, and does theirs beat mine? | Not engaged yet: move or Dash to close - crossing into a Near+ Measure Band opponent's threat range provokes their Opportunity Attack once, even if you stop short of adjacent. Wrong band for your weapon: see the Measure box, above - a Minor Action Shift Measure or a won **Shift** Effect fixes it. Neither problem: skip to Step 2. |
| **2. Make the attack**    | Does my Attack Roll beat their Passive Evasion? | No: clean miss, exchange over, no Reaction spent. Yes: continue to Step 3.                                                                                                                                                                                                           |
| **3. Defender reacts**    | Do I have a Reaction left, and can I answer? | Yes: **Oppose** with a contested roll, or (casters) **Reactive Casting**. No: the attack resolves as a normal hit.                                                                                                                                                                   |
| **4. Resolve the Margin** | What's my roll minus their roll? | Check it against the Margin table, below.                                                                                                                                                                                                                                            |
| **5. Aftermath**          | Did I hit Dominant or Stopped? | Pick 2 (Dominant) or 1 (Stopped) Effects from the shared list - they resolve in a fixed default order, Strike always last (see Default order, below). Any result can instead be answered by spending another Reaction to Oppose it again - see the Press, below.                     |

**1. Get into range.** If you're already engaged at a workable band when your turn starts, skip straight to Step 2. Otherwise close with a Move Action (a Dash, if you need more of it) or a Minor Action Shift Measure - closing on a Near+ Band opponent provokes their Opportunity Attack once, the moment you cross into their threat range (see [[Opportunity Attacks|combat]] for the full trigger and its edge cases). If it hits, you answer it exactly like Step 3, below, before you've even finished closing. A Feint or similar setup move can prime the attack you're closing in to make, but doesn't move you (see [[Basic Moves|core_rules]]).

**2. Make the attack.** The attacker rolls a normal Attack Roll against the defender's Passive Evasion (see [[Attack Roll|combat]]).

**3. The defender reacts, or doesn't.** The defender may spend a Reaction from their shared pool (see [[Action Economy|combat]]) to answer it:

- **Oppose** - roll a contested check against the attack roll (below).
- **Reactive Casting** - casters only; buy a spell off that same contested roll instead of intercepting the blow (below).
- **Nothing** - out of Reactions, or you simply choose not to. The attack resolves as a normal hit.

**4. Resolve the Margin.** Compare your Oppose roll to the attacker's roll on the Margin table (below).

**5. Aftermath.** Dominant and Stopped let you pick Effects off that same roll, no further check needed, resolving in the fixed default order (Effects, below). Any result can instead be answered by spending another Reaction to Oppose it again - see the Press, below.

**Example:** Toma (dagger, Grip) is attacked by a bandit wielding a shortsword (also Grip - equal, no mismatch). The bandit's attack roll beats Toma's Passive Evasion, so it would otherwise hit. Toma reacts with Oppose, rolling her Brawling Skill: the bandit rolled 14, and Toma's roll comes out to 17 - Margin +3, Dominant. She picks two Effects: Control and Strike. Under the default order, Control resolves first and is already active by the time her Strike's attack roll happens, so her Strike (15, with the bandit at Disadvantage from Control) beats his Evasion and hits, dealing damage and degrading his armor. The bandit still has a Reaction in his pool, so instead of accepting the hit, he spends it to Oppose Toma's Strike - continuing the Press.

---

## Oppose

Answer an incoming attack with your own contested roll, instead of simply eating the hit or hoping your Passive Evasion holds.

**Trigger:** An attack against you that you can see, and that beats your Passive Evasion (i.e. it would otherwise hit). **Exception:** a Critical Hit (see [[Critical Hits|combat]]) bypasses an Oppose funded by Weapon Skill or Shields Skill entirely - it simply hits, no Reaction spent attempting it - though you can still Oppose it with bare DEX.
**Action:** Reaction (shared pool, see [[Action Economy|combat]])
**Roll:** 1d12 + whichever Skill funds it - pick whichever fits what you're defending with when you react, then compare your result to the attack roll:

| Funds the roll | Requires | Works Against | Notes |
| :---- | :---- | :---- | :---- |
| **Weapon Skill** | Melee weapon in hand, 1+ rank in that weapon's Skill | Melee only, not AoE | Disadvantage if the current measure is one band off your weapon's (see the Measure box, above) - can't Oppose this way at all two bands off. |
| **Shields Skill** | Shield in hand, or a melee weapon with the Two-Handed property (a Versatile weapon held two-handed counts) - blocking is a shield discipline whatever's in your hands, so 1+ rank in Shields is what trains it either way | Melee and ranged physical if using a shield; melee only with a Two-Handed weapon; not AoE | May Oppose for an adjacent ally instead of yourself - the attack retargets to you, and you take whatever damage gets through. |
| **DEX** | DEX 1+ - no Skill gate, this is raw reflex rather than trained technique | Melee, ranged, and AoE - against AoE you must be able to move the minimum distance necessary to clear the area (this movement doesn't consume your Move Action); can't clear it, Oppose simply fails and the Reaction isn't spent | Armor Penalty applies to this roll (see [[combat]]'s Armor Penalty entry) - a heavily armored character often qualifies on paper but finds the roll gutted in practice. |

**Margin \= Your roll − the attacker's attack roll**

| Margin | Result |
| :---- | :---- |
| \+3 or higher | **Dominant** \- Attack fully avoided. Choose 2 Effects from the list below. |
| 0 to \+2 | **Stopped** \- Attack fully avoided. Choose 1 Effect from the list below. |
| \-1 to \-2 | **Minimized** \- Attack connects, but damage is halved (round down), regardless of which Skill funded your roll. |
| \-3 or lower | **Failed** \- Full damage. Your Reaction is spent for nothing (unless you Press it - below). |

**Shield Guard:** If you have a shield equipped and your Margin comes out Minimized or Failed, add the shield's Guard to your Margin before checking the tier above - this applies no matter which Skill funded your roll, since the shield is physically there either way. A big loss can shrink to a small one; a small loss can shrink to nothing. See [[Shields|armor]] for Guard values and how Measure and Control interact with it.

**Measure defines fights:** see the Measure box at the top of this chapter for the one-line version, or [[Reach|combat]] for the full mechanic.

Casters have a second option instead of Oppose - **Reactive Casting** (below) - which doesn't intercept the attack at all, but lets a beaten roll buy you a spell instead.

### Effects

On a Dominant or Stopped result, you're not just surviving the exchange - your margin bought you the initiative in it. Effects resolve automatically off the Margin you already rolled; none of them need a further check.

- **Strike** \- Make one weapon (or unarmed) attack against the attacker as part of this Reaction. Subject to the Measure box, above: freely at your weapon's own band, at Disadvantage one band off, not selectable at all two bands off.
- **Shift** \- Move the shared measure one band, in or out, as part of this Reaction. This movement doesn't provoke - you already won the exchange to earn it.
- **Control** \- The opponent has Disadvantage on their next roll against you, or cannot select Strike against you, until they spend a win clearing it. If they're carrying a shield, this also zeroes its Guard against you for as long as it holds (see [[Shields|armor]]).
- **Recover** \- Regain one Reaction already spent this round, or exit the exchange safely - disengage from this specific opponent, ending the current measure engagement, without provoking.

At Dominant, pick any 2 Effects from the four above. Repeats aren't allowed, you're choosing 2 different ones.

**Default order.** Whichever Effects you pick resolve one at a time, not simultaneously: Shift, Control, and Recover resolve first (in that relative order, whichever pair of those you picked), and Strike always resolves last, no matter which other Effect you paired it with. That means Control (or Shift, if it changes what Strike can reach) is already active by the time your Strike's attack roll happens, so a Strike paired with Control gets the opponent's Disadvantage automatically. You may instead declare your Strike unboosted, banking Control's effect for your next roll against the target instead of spending it now.

**Strike paired with Recover's disengage option:** if you choose Recover's "exit the exchange safely" option alongside Strike, resolve the Strike first, then Recover - you land your hit, then disengage from the opponent you just struck. This is the one pairing where Strike doesn't go last: Recover's disengage would otherwise remove you from the exchange before your Strike could resolve at all.

---

## The Press

An Oppose result doesn't have to be the end of the exchange. If you have a Reaction left, you may spend it to Oppose back instead of accepting the result that just came up - roll again, this time contesting whatever roll the other side just made. This works whether you won or lost: a defender who Minimized or Failed can burn another Reaction for a fresh shot at it, and an attacker who just ate a Strike can Oppose that Strike exactly like any other attack.

This can chain back and forth as long as either side keeps spending Reactions - there's no cap beyond both pools running dry, or someone choosing to let a result stand instead of paying to re-open it. Every link asks the same question the last one did: you have the advantage (or you don't) - do you cash it in, or spend another Reaction chasing a better one?

This is the contested middle of an exchange - momentum swinging between two combatants before anyone lands a telling blow. A three-Reaction exchange where Control and the measure trade hands twice before a Strike finally connects is the system working as intended, not a stall. It also makes overextension real: spend your Reactions early in a fight and you're defenseless in the one that matters.

---

## Reactive Casting

Answer an incoming attack by snapping off a spell before it lands, instead of intercepting the blow itself.

**Trigger:** Same as Oppose - an attack against you that you can see, and that beats your Passive Evasion (i.e. it would otherwise hit).
**Action:** Reaction (shared pool, see Action Economy - this competes with Oppose and Opportunity Attacks for the same Reaction.)
**Prerequisites:** 1+ rank in the relevant Casting Skill, and a spell you're able to cast.
**Roll:** Same shape as casting the spell normally (see [[Magic Overview|magic_overview]]) - it doesn't gain or lose anything for being reactive:

| Path | Roll |
| :---- | :---- |
| **Arcane** | 1d12 + Spell Modifier (Magic School Skill − Armor Penalty) |
| **Divine** | 1d12 alone, no modifier - the same flat shape as the Petition Roll |

**Rite Mastery doesn't apply here** - it only rerolls a failed Petition Roll, and this contested roll isn't one, even for a Divine caster.

**Margin \= Your spell roll − the attacker's attack roll.** Check it against the same Margin tiers Oppose uses (above) to find your **Mana Value** - the biggest Mana Cost you're allowed to spend this Reaction:

| Margin        | Result    |            Mana Value             |
|:--------------|:----------|:---------------------------------:|
| \+3 or higher | Dominant  |                 3                 |
| 0 to \+2      | Stopped   |                 2                 |
| \-1 to \-2    | Minimized | 0 - can't afford to cast anything |
| \-3 or lower  | Failed    | 0 - can't afford to cast anything |

You may cast any spell you're able to cast (and can pay for as normal from your own Mana pool) whose Mana Cost is no greater than your Mana Value - there's no surcharge for casting reactively, this only caps how big a spell your roll affords. At Minimized or Failed, you can't afford to cast anything, and your Reaction is spent for nothing.

**This does not avoid the attack on its own.** Reactive Casting doesn't intercept anything the way Oppose does, and there is no Strike tier here. The incoming attack still resolves normally (it already beat your Passive Evasion to trigger this) unless the spell you cast happens to reduce, negate, or otherwise answer it. Casting a Fireball in response to an incoming sword doesn't stop the sword.

**The Press doesn't apply here.** There's no Oppose result to re-open - Reactive Casting never intercepted the attack in the first place, so there's nothing to Press. A defender who wants another shot at avoiding the attack needs a Reaction-based option that actually contests it (Oppose).
