A Maneuver is your reactive answer to an incoming attack - the moment where every turn spent setting up the exchange (see [[Basic Moves|core_rules]]) pays off. Instead of simply eating a hit or hoping your Passive Evasion holds, you answer it with a contested roll of your own. Everyone has access to this as long as they fulfil the prerequisites.

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

**Ties favor you, the defender** (Margin of exactly 0 falls under Stopped) - a deliberate exception to the normal [[Contested Check|core_rules]] convention, preserving how Parrying has always resolved. Reactive Casting (below) carries the same tie-favors-you principle, expressed through its Mana Value formula instead.

**Critical Hits:** A Natural 12 bypasses the Parry and Block Styles entirely - a blow that committed is too fast or too heavy to intercept, so reacting with either Style automatically Fails. Dodge is the exception: it works by not being where the blow lands rather than intercepting it, so it still resolves normally against a Crit.

Casters have a fourth option instead of a Style - **Reactive Casting** (below) - which doesn't intercept the attack at all, but lets a beaten roll buy you a spell instead of a parry.

### **Effects**

On a Dominant or Stopped result, you're not just surviving the exchange - your margin bought you the initiative in it. Effects resolve automatically off the Margin you already rolled; none of them need a further check. Every Style shares three Effects, and brings one signature Effect of its own that only makes sense for how that Style defends:

- **Riposte** *(any Style)* \- Make one weapon (or unarmed) attack against the attacker as part of this Reaction. Requires the attacker to be within your weapon's Reach - if their Reach put them farther away than yours reaches (a Long Pike against your Short dagger, say), you can't Riposte; pick a different Effect instead. Dodge's Reposition, or having already picked Close the Gap against this attacker, can close that gap first.
- **Exploit Opening** *(any Style)* \- You read their guard. Your next attack roll against the attacker before the start of your next turn has Advantage.
- **Close the Gap** *(any Style)* \- Only choosable if the attacker's weapon Reach Category is greater than yours ([[Reach Categories|weapons]]). You've fought your way inside their guard: until you Disengage, are forced back, or the fight ends, treat your Reach as equal to theirs against this specific attacker - no more Parry Disadvantage from the mismatch, no more Riposte lockout. This is how a short weapon answers a long one: not a bigger stick, better footwork.
- Plus your Style's signature Effect (Parry: **Guard Break** or **Bind Weapon**; Block: **Push Back** or **Stagger**; Dodge: **Reposition** or **Untouchable** - see below).

At Dominant, pick any 2 of the (up to) 5 Effects available to you - repeats aren't allowed, you're choosing 2 different ones. Nothing stops you from choosing both signature Effects if your Style offers two, or mixing a signature Effect with Riposte, Exploit Opening, or Close the Gap.

---

### **Style: Parry**

Deflect an incoming melee attack with your weapon.

**Prerequisites:** A melee weapon in your hand, and 1+ rank in that weapon's Skill.  
**Restrictions:** Melee attacks only. Does **not** work against AoE or unseen attacks.  
**Roll:** Your normal attack roll (Weapon Skill \+ Attribute). Disadvantage if the attacker's weapon Reach Category is strictly greater than yours (see [[Reach Categories|weapons]]).  
**Minimized:** Reduce damage by your weapon's damage die (roll it).

**Signature Effects:**

- **Guard Break** \- The attacker cannot use Parry or Block to answer the next attack against them, from any source, before the start of your next turn. Dodge is unaffected.
- **Bind Weapon** \- The attacker's next attack roll before your next turn has Disadvantage - their weapon is still fouled against yours.

---

### **Style: Block**

Use your shield, or a Two-Handed weapon, to absorb incoming attacks.

**Prerequisites:** A shield in your hand, or a melee weapon with the Two-Handed property, and 1+ rank in Shields. A Versatile weapon being wielded with both hands does not count as a Two-Handed Weapon for this purpose - only a melee weapon whose property list includes Two-Handed qualifies (a two-handed ranged weapon or firearm does not).  
**Restrictions:** Works against melee and ranged physical attacks if you're using a shield; a Two-Handed weapon only blocks melee. Does **not** work against AoE or unseen attacks.  
**Roll:** 1d12 \+ Shields Skill \+ END.  
**Minimized:** Reduce damage by your shield's AR Bonus ([[Shield Table|armor]]), or by Shields Skill ÷ 2 (rounded down) if you're blocking with a Two-Handed weapon instead of a shield. (A Buckler has no AR Bonus and reduces nothing here - see [[Shield Descriptions|armor]] for what it offers instead.)

**Protecting Allies:** You may Block for an adjacent ally; the attack targets you instead, your armor degrades as normal, and you take any damage that gets through.

**Signature Effects:**

- **Push Back** \- Shove the attacker 5-10 ft directly away from you.
- **Stagger** \- The attacker's Speed becomes 0 until the start of your next turn - the force of your Block leaves them unable to reposition.

---

### **Style: Dodge**

Use your adroit agility to escape danger.

**Prerequisites:** 1+ rank in Agility. You must also be able to move the minimum distance necessary to clear the attack's range (this movement does not consume your Move Action) - if you can't (such as against an Area of Effect attack), Dodge simply fails and your Reaction is not spent.  
**Roll:** 1d12 \+ Agility \+ DEX.  
**Minimized:** Halve the damage (round down) instead of a flat reduction - you couldn't fully clear the blow, but you weren't square in its path either.  
**Note:** Unlike Parry and Block, a Dominant or Stopped result here means the attack never touched you at all - your armor does not degrade.

**Signature Effects:**

- **Reposition** \- Move up to your speed as part of this Reaction. This movement does not provoke Opportunity Attacks.
- **Untouchable** \- The next attack against you, from any source, before the start of your next turn has Disadvantage.

---

## Reactive Casting

Answer an incoming attack by snapping off a spell before it lands, instead of intercepting the blow itself.

**Trigger:** Same as Maneuver - an attack against you that you can see, and that beats your Passive Evasion (i.e. it would otherwise hit).  
**Action:** Reaction (shared pool, see Action Economy - this competes with Maneuver and Opportunity Attacks for the same Reaction).  
**Prerequisites:** 1+ rank in the relevant Casting Skill, and a spell you're able to cast.  
**Roll:** Your normal spell roll (Casting Skill \+ Attribute) vs. the attacker's attack roll.

**Margin \= Your spell roll − the attacker's attack roll**

**Mana Value \= Margin \+ 1.** You may cast any spell you're able to cast (and can pay for as normal from your own Mana pool) whose Mana Cost is no greater than your Mana Value - there's no surcharge for casting reactively, this only caps how big a spell your roll affords. A Margin of 0 (a tie, favoring you the same way it favors a Style's defender, above) gives a Mana Value of 1, enough for the cheapest spell. If your Margin is **\-1 or lower**, your Mana Value is 0 or less - you can't afford to cast anything, and your Reaction is spent for nothing.

**This does not avoid the attack on its own.** Reactive Casting isn't a Style - it doesn't intercept anything, and there is no Riposte tier here. The incoming attack still resolves normally (it already beat your Passive Evasion to trigger this) unless the spell you cast happens to reduce, negate, or otherwise answer it. Casting a Fireball in response to an incoming sword doesn't stop the sword.

---

## Ready Volley

Hold a ranged shot on a chosen lane, ready to loose it the instant your trigger is met - the setup melee gets for free just by having a weapon in hand, ranged weapons pay for with a turn.

**Trigger:** Any perceivable circumstance you declare, same as a normal Held Action (see [[Held Action|combat]]) - an enemy entering your line of sight or your weapon's Range, closing to melee, breaking cover, attacking an ally, and so on.  
**Action:** Major Action to set (this is a Held Action), Reaction to release (shared pool, see [[Action Economy|combat]]).  
**Prerequisites:** A loaded ranged weapon in hand. A firearm must already be loaded before you set the trigger - Ready Volley holds the shot, not the reload.  
**Roll:** Your normal attack roll (Weapon Skill \+ Attribute), unless you're making a Called Shot below.

If your trigger doesn't occur before your next turn, the action is lost, same as any Held Action.

### **Called Shot**

When your Ready Volley fires, you may aim for more than center mass instead of a normal hit. Declare your zone before you roll - this option only exists because you took the time to aim; a snapped-off attack on your own turn doesn't give you that choice.

| Zone              | Penalty | On Hit                                                                                                                               |
|:------------------|:-------:|:-------------------------------------------------------------------------------------------------------------------------------------|
| Torso *(default)* |   \-    | Normal damage, no additional effect.                                                                                                 |
| Legs              |   \-2   | Speed becomes half until the end of their next turn. Margin \+3 or higher: they are knocked Prone instead.                           |
| Arms              |   \-2   | Their next attack roll before your next turn has Disadvantage. Margin \+3 or higher: they drop one held item of your choice instead. |
| Head              |   \-4   | This attack ignores the target's AR entirely.                                                                                        |

**Margin \= Your attack roll − the target's Evasion** - the same numbers you already rolled to resolve the hit, no extra roll needed.
