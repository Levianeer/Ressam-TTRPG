## How an Exchange Works

This is the map of a melee or ranged exchange, start to finish, and where each piece of it lives in the rules. Read this first if Maneuvers are new to you - the Style-by-Style detail below assumes you already know the loop.

| Step | Ask Yourself | Then |
| :---- | :---- | :---- |
| **1. Get into range** | Am I already within my weapon's Reach of the target? | No: move or Dash to close - crossing into a Medium+ Reach opponent's threat range provokes their Opportunity Attack once, even if you stop short of adjacent. Yes: skip to Step 2. |
| **2. Make the attack** | Does my Attack Roll beat their Passive Evasion? | No: clean miss, exchange over, no Reaction spent. Yes: continue to Step 3. |
| **3. Defender reacts** | Do I have a Reaction left, and a Style (or spell) I qualify for? | Yes: choose Maneuver (pick Parry, Block, or Dodge) or Reactive Casting. No: the attack resolves as a normal hit. |
| **4. Resolve the Margin** | What's my roll minus their roll? | Check it against the Margin table below: Dominant, Stopped, Minimized, or Failed. |
| **5. Aftermath** | Did I hit Dominant or Stopped? In what order do I want my Effects? | Pick Effects in the order you want them to apply - order changes what they affect (see Order Matters, below). If Riposte connects, the original attacker can answer it exactly the same way, restarting from Step 3. |

**1. Get into range.** An attack needs the target within your weapon's Reach. If they already are when your turn starts, skip straight to Step 2. Otherwise you close the gap with a Move Action (a Dash, if you need more of it) - closing on a Medium+ Reach opponent provokes their Opportunity Attack once, the moment you cross into their threat range (see [[Opportunity Attacks|combat]] for the full trigger and its edge cases). If it hits, you answer it exactly like Step 3, below, before you've even closed the distance to swing back. A Feint or similar setup move can prime the attack you're closing in to make, but doesn't move you (see [[Basic Moves|core_rules]]).

**2. Make the attack.** The attacker rolls a normal Attack Roll against the defender's Passive Evasion (see [[Attack Roll|combat]]). If it doesn't beat Evasion, that's a clean miss - the exchange ends here, and no one spends a Reaction.

**3. The defender reacts, or doesn't.** An attack roll that beats Evasion would otherwise hit - now the defender may spend a Reaction from their shared pool (see [[Action Economy|combat]]) to answer it:

- **Maneuver** - pick a Style (Parry, Block, or Dodge, below) and roll a contested check against the attack roll.
- **Reactive Casting** - casters only; buy a spell off that same contested roll instead of intercepting the blow (below).
- **Nothing** - out of Reactions, no Style you qualify for, or you simply choose not to. The attack resolves as a normal hit.

**4. Resolve the Margin.** Compare whichever contested roll you made to the attacker's roll on the shared Margin table (below): Dominant, Stopped, Minimized, or Failed.

**5. Aftermath.** Dominant and Stopped let you pick Effects off that same roll, no further check needed. If you picked **Riposte**, you've just made a new attack roll against the original attacker - which means they can answer *your* Riposte exactly the same way, restarting this loop from Step 3, provided they still have a Reaction left in their pool. Nothing caps how many times an exchange can chain back and forth in a round beyond both sides running out of Reactions, or a Margin poor enough to end it (a Failed result spends the Reaction for nothing, but doesn't extend the exchange further).

**Example:** Toma (dagger, Short Reach) is attacked by a bandit wielding a shortsword (also Short Reach - equal, no mismatch). The bandit's attack roll beats Toma's Passive Evasion, so it would otherwise hit. Toma has 1+ rank in Daggers & Knives, so she reacts with Parry: the bandit rolled 14, and Toma's Parry roll comes out to 17 - Margin +3, Dominant. She picks two Effects, in this order: Exploit Opening, then Riposte. Exploit Opening resolves first and is already active by the time she resolves Riposte, so her Riposte attack roll (15, with Advantage) beats the bandit's Evasion (12) and hits, dealing damage and degrading his armor - had she picked the two in the other order, the Riposte would have rolled without Advantage, and the Advantage would instead sit banked for her next attack against him. The bandit still has a Reaction in his pool, so he could Parry Toma's Riposte the exact same way she just answered his own attack; if he can't or doesn't, it simply lands.

---

## Maneuver

Answer an incoming attack with your own contested roll, instead of simply eating the hit or hoping your Passive Evasion holds.

**Trigger:** An attack against you that you can see, and that beats your Passive Evasion (i.e. it would otherwise hit).  
**Action:** Reaction (shared pool, see [[Action Economy|combat]])  
**Choose a Style** below when you react - Parry, Block, or Dodge - each with its own prerequisites, restrictions, and roll. Then compare your result to the attack roll:

**Margin \= Your Style's roll − the attacker's attack roll**

| Margin | Result |
| :---- | :---- |
| \+3 or higher | **Dominant** \- Attack fully avoided. Choose 2 Effects from your Style's list below. |
| 0 to \+2 | **Stopped** \- Attack fully avoided. Choose 1 Effect from your Style's list below. |
| \-1 to \-2 | **Minimized** \- Attack connects, but reduce the damage (see your Style, below). |
| \-3 or lower | **Failed** \- Full damage. Your Reaction is spent for nothing. |

**Minimized, at a glance** - each Style reduces damage a different way; the full text lives with each Style below, but this is the version you want mid-exchange:

| Style | Minimized reduces damage by... |
| :---- | :---- |
| Parry | Your weapon's damage die (roll it) |
| Block | Your shield's AR Bonus, or Shields Skill ÷ 2 (rounded down) if blocking with a Two-Handed weapon |
| Dodge | Half (rounded down) |

**Ties favor you, the defender** (Margin of exactly 0 falls under Stopped) - a deliberate exception to the normal [[Contested Check|core_rules]] convention, preserving how Parrying has always resolved. Reactive Casting (below) carries the same tie-favors-you principle, expressed through its Mana Value formula instead.

**Critical Hits:** A Natural 12 bypasses the Parry and Block Styles entirely - a blow that committed is too fast or too heavy to intercept, so reacting with either Style automatically Fails. Dodge is the exception: it works by not being where the blow lands rather than intercepting it, so it still resolves normally against a Crit.

**Armor wear:** Parrying or Blocking still puts your gear between you and the blow, so your armor (and shield, if Blocking) degrades as normal - see [[Degradation Rules|armor]] - even on a Dominant or Stopped result. Dodge is the exception: see its Note, below.

**Reach defines fights:** see [[Reach|combat]] for how outreaching your opponent (or being outreached) affects your rolls to Maneuver and to attack.

Casters have a fourth option instead of a Style - **Reactive Casting** (below) - which doesn't intercept the attack at all, but lets a beaten roll buy you a spell instead of a parry.

### **Effects**

On a Dominant or Stopped result, you're not just surviving the exchange - your margin bought you the initiative in it. Effects resolve automatically off the Margin you already rolled; none of them need a further check. Every Style shares three Effects, and brings one signature Effect of its own that only makes sense for how that Style defends:

- **Riposte** *(any Style)* \- Make one weapon (or unarmed) attack against the attacker as part of this Reaction. Requires the attacker to be within your weapon's Reach - if their Reach put them farther away than yours reaches (a Long Pike against your Short dagger, say), you can't Riposte; pick a different Effect instead. Dodge's Reposition, or having already picked Close the Gap against this attacker, can close that gap first.
- **Exploit Opening** *(any Style)* \- You read their guard. Your next attack roll against the attacker before the start of your next turn has Advantage.
- **Close the Gap** *(any Style)* \- Only choosable if the attacker's weapon Reach Category is greater than yours ([[Reach Categories|weapons]]). You've fought your way inside their guard: until you Disengage, are forced back, or they leave your reach, treat your Reach as equal to theirs against this specific attacker - no more Parry Disadvantage from the mismatch, no more Riposte lockout. This is how a short weapon answers a long one: not a bigger stick, better footwork.
- Plus your Style's signature Effect (Parry: **Guard Break** or **Bind Weapon**; Block: **Push Back** or **Stagger**; Dodge: **Reposition** or **Untouchable** - see below).

At Dominant, pick any 2 of the (up to) 5 Effects available to you - repeats aren't allowed, you're choosing 2 different ones. Nothing stops you from choosing both signature Effects if your Style offers two, or mixing a signature Effect with Riposte, Exploit Opening, or Close the Gap.

**Order matters.** Your 2 Effects resolve one at a time, in the order you pick them - not simultaneously. An Effect only affects things that happen after it's already active, so picking Riposte before Exploit Opening means the Riposte's attack roll doesn't get Exploit Opening's Advantage (that Advantage is still banked for whatever your next attack against them ends up being); pick Exploit Opening first instead, and it's already active by the time you resolve Riposte, so the Riposte attack roll itself gets Advantage.

A banked Effect doesn't expire just because a Riposte chain loops back to you - it still applies to whichever qualifying roll comes next, per that Effect's own wording (Exploit Opening watches your next attack roll against the target, Bind Weapon watches the attacker's next attack roll), whether that roll happens two exchanges later in the same chain or on an ordinary turn, as long as it lands before that Effect's stated deadline.

---

### **Style: Parry**

Deflect an incoming melee attack with your weapon.

**Prerequisites:** A melee weapon in your hand, and 1+ rank in that weapon's Skill.  
**Restrictions:** Melee attacks only. Does **not** work against AoE.  
**Roll:** 1d12 \+ Weapon Skill \+ Attribute (your normal attack roll). Disadvantage if the attacker's weapon Reach Category is strictly greater than yours (see [[Reach Categories|weapons]]).  
**Minimized:** Reduce damage by your weapon's damage die (roll it).

**Signature Effects:**

- **Guard Break** \- The attacker cannot use Parry or Block to answer the next attack against them, from any source, before the start of your next turn. Dodge is unaffected.
- **Bind Weapon** \- The attacker's next attack roll before your next turn has Disadvantage - their weapon is still fouled against yours.

---

### **Style: Block**

Use your shield, or a Two-Handed weapon, to absorb incoming attacks.

**Prerequisites:** A shield in your hand, or a melee weapon with the Two-Handed property, and 1+ rank in Shields - blocking is a shield discipline whatever you're holding, so the weapon in your hands doesn't change which Skill trains it. A Versatile weapon being wielded with both hands does count as a Two-Handed Weapon for this purpose (a two-handed ranged weapon or firearm does not work).  
**Restrictions:** Works against melee and ranged physical attacks if you're using a shield; a Two-Handed weapon only blocks melee. Does **not** work against AoE.  
**Roll:** 1d12 \+ Shields Skill \+ END.  
**Minimized:** Reduce damage by your shield's AR Bonus ([[Shield Table|armor]]), or by Shields Skill ÷ 2 (rounded down) if you're blocking with a Two-Handed weapon instead of a shield. (A Buckler has no AR Bonus and reduces nothing here - see [[Shield Descriptions|armor]] for what it offers instead.)

**Protecting Allies:** You may Block for an adjacent ally; the attack targets you instead, your armor degrades as normal, and you take any damage that gets through.

**Signature Effects:**

- **Push Back** \- Shove the attacker 5-10 ft directly away from you.
- **Stagger** \- The attacker's Speed becomes 0 until the start of your next turn - the force of your Block leaves them unable to reposition.

---

### **Style: Dodge**

Use your adroit agility to escape danger.

**Prerequisites:** 1+ rank in Agility.  
**Restrictions:** Unlike Parry and Block, Dodge isn't flatly locked out of AoE attacks - but you must be able to move the minimum distance necessary to clear the attack's area (this movement does not consume your Move Action) to answer one at all. If you can't clear it, Dodge simply fails and your Reaction is not spent.  
**Roll:** 1d12 \+ Agility \+ DEX.  
**Minimized:** Halve the damage (round down) instead of a flat reduction - you couldn't fully clear the blow, but you weren't square in its path either.  
**Note:** Unlike Parry and Block, a Dominant or Stopped result here means the attack never touched you at all - your armor does not degrade.

**Signature Effects:**

- **Reposition** \- Move up to half your speed as part of this Reaction. This movement CAN provoke Opportunity Attacks.
- **Untouchable** \- The next attack against you, from any source, before the start of your next turn has Disadvantage.

---

## Reactive Casting

Answer an incoming attack by snapping off a spell before it lands, instead of intercepting the blow itself.

**Trigger:** Same as Maneuver - an attack against you that you can see, and that beats your Passive Evasion (i.e. it would otherwise hit).  
**Action:** Reaction (shared pool, see Action Economy - this competes with Maneuver and Opportunity Attacks for the same Reaction).  
**Prerequisites:** 1+ rank in the relevant Casting Skill, and a spell you're able to cast.  
**Roll:** Your normal spell roll (Casting Skill \+ Attribute) vs. the attacker's attack roll.

**Margin \= Your spell roll − the attacker's attack roll.** Unlike the Style Margin above, this Margin is read as a raw number rather than checked against the tier table - it feeds directly into the Mana Value formula below.

**Mana Value \= Margin \+ 1.** You may cast any spell you're able to cast (and can pay for as normal from your own Mana pool) whose Mana Cost is no greater than your Mana Value - there's no surcharge for casting reactively, this only caps how big a spell your roll affords. A Margin of 0 (a tie, favoring you the same way it favors a Style's defender, above) gives a Mana Value of 1, enough for the cheapest spell. If your Margin is **\-1 or lower**, your Mana Value is 0 or less - you can't afford to cast anything, and your Reaction is spent for nothing.

**This does not avoid the attack on its own.** Reactive Casting isn't a Style - it doesn't intercept anything, and there is no Riposte tier here. The incoming attack still resolves normally (it already beat your Passive Evasion to trigger this) unless the spell you cast happens to reduce, negate, or otherwise answer it. Casting a Fireball in response to an incoming sword doesn't stop the sword.
