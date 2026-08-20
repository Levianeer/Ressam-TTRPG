# Your Tempo Pool

**STR sizes your Tempo Die. DEX counts your dice.** STR is melee damage for every weapon and every melee Skill, finesse blades included. Missiles take **DEX** for damage instead.

Your pool refills in full at the start of your turn. Unspent dice do not carry over.

| STR                |      0 or lower       |   1   |   2   |   3   |   4    | 5      |
|:-------------------|:---------------------:|:-----:|:-----:|:-----:|:------:|:-------|
| **Tempo Die Size** | `1d4 at Disadvantage` | `1d4` | `1d6` | `1d8` | `1d10` | `1d12` |

| DEX                  | 0 or lower |  1  |  2  |  3  |  4  | 5   |
|:---------------------|:----------:|:---:|:---:|:---:|:---:|:----|
| **Tempo Die Amount** |    `1`     | `2` | `3` | `4` | `5` | `6` |

Neither table runs negative: **STR 0 or lower is `1d4` at Disadvantage; DEX 0 or lower is 1 die.** Above 5: **STR 6+ is still `1d12`** (the die ladder has a ceiling); **DEX 6+ is `\+1` die per point** (the count does not).

| Spending a Tempo Die on | When |
| :---- | :---- |
| **Attacking** - every attack, including the first | Your turn |
| **Shooting** - every shot, including the first | Your turn |
| **Defending** - a Parry | Anyone's turn |
| An **Opportunity Attack** | Anyone's turn |
| **Reloading**, unless thrown | Your turn |
| Whatever a Feat says it costs | Varies |

**An empty pool cannot attack or Parry.** An attack against it simply lands - there is no static defense and no free guard. Your pool always refills before your own turn, so this only happens on someone else's.

**Nothing reduces a refill below 1 die**, except [Stunned](#conditions-and-your-pool) (halves it) and [Ambushed](#surprise) (zeroes all of Round 1). [Shock](#shock) empties a pool but never follows it into the next turn.

---

## The Exchange at a glance

An **Exchange** is one attack and its answer.

On your turn, declare your whole attack sequence at once - how many attacks, and a target for each - and pay all the dice up front. Then resolve each attack in order:

| Step | What happens |
| :---- | :---- |
| **1. Attack** | `1d(Tempo Die) \+ Weapon Skill`. If the target is outside the weapon's Length, this roll closes the gap - see [Fighting outside your Length](#fighting-outside-your-length). |
| **2. Answer** | The defender spends 1 Tempo Die on a **Parry**, or spends nothing and the blow lands. |
| **3. Compare** | Higher total wins; **ties go to the defender**. Winning by **5 or more** takes an **Opening**. |

| Outcome                    | What happens                                                                                   |
|:---------------------------|:-----------------------------------------------------------------------------------------------|
| **Nobody answered**        | The blow lands and counts as won at a margin of exactly 5 - the attacker takes an **Opening**. |
| **Attacker wins**          | The blow lands. Roll damage; **Shock takes a Tempo Die off the defender.**                     |
| **Defender wins, or ties** | The blow does not land.                                                                        |
| **Either wins by 5+**      | That fighter takes an **Opening.**                                                             |

There is no separate to-hit roll, no second contest, and no floor beneath declining to answer - not spending a die is a decision to be hit and taken apart.

---

## Distance

Ressam is played on a **square grid of five-foot squares** ([[Battlemap \& Positioning|positioning]] owns the grid); diagonals count as one square. **Adjacent** is 0 squares, **Reach** is 1 - 2 squares.

### Weapon Length

Every weapon carries a Length, 1-5, printed on it - the squares it can act across at all.

| Length |  Reaches  | Weapons                                                                                                                     |
|:-------|:---------:|:----------------------------------------------------------------------------------------------------------------------------|
| **1**  | Adjacent  | Unarmed, Dagger, Knife, Stiletto, Shield Bash, Throwing Axe, Dart                                                           |
| **2**  | Adjacent  | Shortsword, Scimitar, Broadsword, Battle Axe, Mace, Club, Chain Flail, Rapier                                               |
| **3**  | Adjacent  | Longsword, Greatsaber, Greatsword, Warblade, War Maul, Greatclub, Quarterstaff, Estoc, Spear, Javelin, Whip, Weighted Chain |
| **4**  | 1 square  | Halberd, Glaive, Lance                                                                                                      |
| **5**  | 2 squares | Pike                                                                                                                        |

**1-3 all fight Adjacent. 4 and 5 cannot act at Adjacent at all** - a polearm or pike that has been closed on has stopped working, not fighting at a discount.

A thrown weapon uses its held Length until thrown, then is a shot off the [Shot DC](#there-is-no-defense-against-a-ranged-attack) table. A **Sling** has no melee Length.

### The Edge

Whichever fighter is outside the other's ideal range holds nothing; the other holds **the Edge**, sized to the raw Length difference. Same Length holds nothing either way.

**The Edge adds only to reactionary rolls - a Parry, or an Opportunity Attack - never to an attack declared on your own turn.** Landing a hit flips the Edge outright to whoever landed it. Before anybody has landed anything, **the longer weapon holds it by default.**

### Fighting outside your Length

An attack can always be declared regardless of distance - it is what closes the gap. It carries no Edge, win or lose; win, and you are now inside your weapon's range (Edge included) of the target.

A **Length 4-5** weapon instead threatens the squares it can act in, and answers a crossing of that threat - entering or being forced past it - with its own **Opportunity Attack** (1 Tempo Die, an ordinary plain attack, carries the Edge if it holds one). It may be Parried; **beating it by enough takes Sunder, and Sunder only.**

**A pike's reach has no gap in it**: if a creature stands in the one square between a pike and a target two squares off, the pike acts through it as though the square were empty - attack, Parry, or Opportunity Attack alike. No other weapon has this.

---

## Attacking

Your Major Action is your whole attack sequence: declare every attack and target at once, pay for all of it, then resolve in order.

**Attack roll: `1d(Tempo Die) \+ Weapon Skill`.** No Length and no Edge on your own attack. The die is your Tempo Die's size regardless of how many you have left - the pool is a count, not a physical supply.

### Declaring the sequence

**Say how many attacks and a target for each, and pay that many Tempo Dice. Then they resolve in order.** No cap on how many attacks, and no per-swing penalty - the cost is that the sequence cannot change once declared.

**One exception:** if a declared target drops or leaves Distance before its attack comes up, that attack may be redirected to any other legal target. Nothing else moves.

### Plain attacks

A **Riposte**, an **Opportunity Attack**, and a held attack whose trigger fires are all **plain attacks** - they roll exactly like any other attack, but take no Opening and give none to whoever beats them, except the Sunder exception above. This is what stops a Riposte answered by a Riposte from chaining forever. You never choose to make one on your own turn.

---

## Defending

**A Tempo Die buys a defense. Without one you have nothing - an attack nobody pays to answer lands.**

| Defense | Costs | Requires | The number | Can take an Opening |
| :---- | :----: | :---- | :---- | :----: |
| **Parry** | 1 die | Something to parry with | `1d(Tempo Die) \+ Weapon Skill \+ Guard \+ Edge` | Every entry but **Called Shot** |
| **Nothing** | free | nothing at all | the blow lands | No |

**Higher total wins; ties go to the defender.** One die per attack, no stacking two defenses on one blow, no cap on how many attacks you may answer in a round.

**An unanswered attack counts as won at a margin of exactly 5**, for every purpose - Opening, damage, Shock - never more, whatever the roll was. This applies identically to a target that cannot act at all (unconscious, Incapacitated, Paralyzed, Restrained-and-helpless, Ambushed): the blow lands and the attacker takes an Opening.

**Weapon Skill** on a Parry is the Skill of whatever is actually parrying, not of your own weapon. **Guard** (`\+1` to `\+2` from a shield) adds to every Parry you make while it's equipped - only the highest counts with more than one, and it degrades by 1 whenever a Parry it added to is lost (repaired with armor). **Edge** is whatever [The Edge](#the-edge) gives the parrying implement against this attacker - there is no range lockout on a Parry.

**Bare hands Parry only Length 1** (Daggers \& Wrestling, no Guard). A caster's or unarmed fighter's pool against anything longer is pure defense that cannot connect - see [Casters](#casters).

---

## Openings

**Win a contest by 5 or more and you take an Opening** - attacker or defender, on anyone's turn. Nothing pays out twice; an Opening is free.

| Opening | Effect |
| :---- | :---- |
| **Riposte** | A plain attack now, and the next attack still to come in their declared sequence is cancelled (if none remain, you still get the swing). |
| **Called Shot** | Your blow also inflicts a minor extra effect - a stagger, a graze, a stumble. Requires a landing blow, so it's attacker-only. |
| **Disarm / Sunder** | Length 1-3: **Disarm** - drops into their square, picked up for an Object Interaction. Length 4-5: **Sunder** - breaks until repaired outside the fight, unless its wielder spends 1 Tempo Die to drop it instead. |
| **Shove** | Push them 1 square, or knock them **Prone**. |
| **Grapple** | See [Grappling](#grappling). |
| **Feats** | Many combat Feats add entries to this menu. |

**No Opening comes from a plain attack or from beating one**, except: beating a Length 4-5 weapon's Opportunity Attack by enough takes **Sunder, and Sunder only**. Openings do not chain.

### Grappling

**Grappling is an Opening and nothing else.** A Grappled creature is **Restrained** while the grappler stays Adjacent and keeps hold; it ends the moment they let go, move away, are knocked Prone, or the target takes an Opening against them. **Every weapon can Grapple**, two-handed included.

**Breaking free costs the Grappled creature 1 Tempo Die, no roll**, spent on their turn.

### There are no critical hits

**No margin pays double damage.** Damage is Weapon Damage \+ STR \- AR whether you won by 5 or by 15 - the whole reward for winning well is the Opening.

### Shock

**Every attack in an Exchange that lands takes 1 Tempo Die off the person it landed on** - no margin required, no Opening spent, whether the blow wounded them or their armor ate it. **Shock is melee only; a shot never causes it. Shock cannot follow you into your next turn** - your pool refills in full.

---

## Armor and Wounds

*Definitions live in [[Armor|armor]] and [[Wounds and Survival|wounds_and_survival]]. This is only what a fight reads.*

**Nothing in an Exchange reads Armor Penalty.** Once fighting starts, **AR is the whole of what armor does.**

Current AR equals current durability. **Every landing hit costs 1 durability** (a War Maul and every firearm cost 2). **A blow reduced to 0 damage after AR still costs Flexible armor 1 durability, and costs Rigid armor nothing.** Rigid armor at 0 cannot be field-repaired; Flexible armor can be patched from any state.

**Wound Thresholds** (same for every character): 0 Wounds on 0 or less damage, 1 on 1-9, 2 on 10-18, 3 on 19+. A blow that inflicts no Wound still degrades armor, and a melee one still Shocks.

---

## Initiative and turn order

**Initiative = 5 \+ MIND.** Static, never rolled, the same number for the whole fight; highest goes first. **Armor Penalty does not apply.**

**Ties:** tied fighters choose their order among themselves, once, when combat begins.

**Two PCs may swap Initiative scores once per combat**, by mutual agreement, permanently for that fight.

**Mythic Initiative (X):** the creature takes a full turn at its Initiative, and another at every `\-2` below it, X counts in all. **It refills its Tempo Pool in full on its first count, and regains 1 die on each count after that.** Shock reads every count as a full turn - the refill is the refill, and being emptied does not carry down the ladder. The stat-block side (Repetition, condition timing across counts) lives in [[Mythic Initiative|bestiary_overview]].

### Surprise

| | When it applies | What it costs you |
| :---- | :---- | :---- |
| **Caught Out** | You knew violence was coming, not from where or when | Lose your **Major Action** on your first turn only. Keep your Move, Minor Action, Object Interaction, and your **whole Tempo Pool**. |
| **Ambushed** | No reason to suspect anything | Round 1 is gone entirely - no actions, no Tempo Pool, **no defense roll at all**: every attack simply lands, with an Opening. Normal from Round 2. |

The test is fiction, not a roll: did they know a fight was starting?

---

## Situations

**Being outnumbered** is not a special rule - it is more Exchanges than you can afford to answer. A second enemy is worth more than any weapon, armor, or Feat.

**Who the enemy attacks** is the largest dial in the chapter. Concentrated fire against one target wins fights faster than any other lever, for either side of the screen.

### Holding an attack

**Declare an attack on your turn without resolving it.** Name the trigger, pay for it now. It resolves as a **plain attack** the instant the trigger occurs, any time before the start of your next turn. **If the trigger never comes, the die is gone.** Only one held attack at a time. A held shot's weapon stays loaded until the trigger actually fires it.

### Conditions and your pool

**A Condition that imposes Disadvantage on attack rolls does not touch your Parry unless it says so** (Poisoned, Frightened, Prone all read this way).

- **[[Blinded|wounds_and_survival]]** reaches your Parry - Disadvantage on it, same as your attacks.
- **Prone / Restrained:** attacks against you have Advantage, your own attacks have Disadvantage (Restrained also: DEX Ward at Disadvantage, Speed 0) - **you Parry at no penalty either way.**
- **Stunned:** your pool refills to **half as many dice, rounded down, never below 1.** Die size is unaffected.
- **Incapacitated, Paralyzed, Petrified, unconscious, or otherwise unable to act:** no Tempo Pool, no defense roll - attacks land automatically with an Opening.

### Leaving a fight

| Leaving by | Costs | Gets you |
| :---- | :---- | :---- |
| **Walking out** | every Opportunity Attack you provoke on the way | Move as normal - but a **landed Opportunity Attack cuts your Move short**, wherever it caught you. |
| **Disengage** | **1 Tempo Die** | Move as normal. Opportunity Attacks can still be made and can still land, but **landing one no longer cuts your Move short** - you still get where you were going. Any Edge held between you and whoever you were engaged with resets. |

**Disengage doesn't grant distance, it grants finishing the trip.** You still spend your own Move to cover the ground - 1 square clears a Length 4 weapon back into its own reach; a **Pike (Length 5) needs 2**. What the die buys is that getting hit along the way doesn't strand you short of it.

Stepping back in later provokes and risks exactly what approaching the first time did. **Break Away is gone** - Disengage is what covers a retreat now.

---

## Who fights an Exchange, and who does not

| | Attacks in Exchanges | Defends with a Tempo Die |
| :---- | :---- | :---- |
| **Melee fighter** | Yes | Yes - a Parry |
| **Ranged attacker** | No - see below | Yes, against melee, if something in hand can Parry. A bow, crossbow or firearm cannot. |
| **Caster** | No - see below | Only what bare hands can answer - a knife and nothing longer |
| **Cannot act** | No | No - attacks land automatically and take an Opening |

### There is no defense against a ranged attack

**No Tempo Die answers a shot: it cannot be Parried, takes no Opening, and there is no contest.**

**Shot: `1d(Tempo Die) \+ Ranged or Thrown Skill` vs. the Shot DC. 1 Tempo Die per shot**, declared and paid exactly like a melee sequence.

#### Loading

**Every missile weapon is loaded or empty, and firing empties it. Reloading costs your Minor Action *and* a number of Tempo Dice set by the weapon.** One Minor Action means a missile weapon fires **twice a turn at most.**

| Weapon | Reload | Two shots costs you |
| :---- | :---- | :----: |
| **Thrown** - Dart, Throwing Axe, Javelin, Knife, Spear | Object Interaction, no dice | **2 dice** |
| **Sling, and every bow** | Minor Action \+ 1 die | **3 dice** |
| **Crossbows** | Minor Action \+ 2 dice | **4 dice** |
| **Every firearm** | Minor Action \+ 3 dice | **5 dice** |
| **Hackbut** | 2 Major Actions - once a fight | \- |

**A brace of loaded weapons is two weapons, not one reloaded** - drawing the second is an Object Interaction, so it fires twice for 2 dice with no Minor Action spent. A shot always costs 1 die whatever it comes out of.

**Cover is binary** ([[Battlemap \& Positioning|positioning]]): wholly behind solid obstruction cannot be targeted at all; anything less is exposed.

| The shot | Shot DC |
| :---- | :----: |
| **Clear, inside the weapon's normal range** | 7 |
| Beyond normal range, out to maximum | \+2 |
| Target moved its full Speed since your last turn | \+2 |
| Target is Prone, and more than one square away | \+2 |
| Target is Prone, and adjacent | \-2 |
| Target is unaware of you, or helpless | \-4 |
| **Target is Adjacent to you** | \+2, and a Two-Handed missile weapon cannot shoot at all |

### Casters

**Spell Overcomes** resolve against **Ward** (`5 \+ Attribute`) as always. **Spell Attacks resolve against the Shot DC**: `1d12 \+ Spell Modifier` vs. the Shot DC table above.

**A Tempo Die never answers a spell of either kind.** A caster's pool is **pure defense** - bare hands Parry only Length 1, and a dagger in the off hand is the cheap fix for that.

---

## Hands and the off hand

| | May carry something in the off hand | Weapons |
| :---- | :---- | :---- |
| **Two-Handed** | Never | Greatsword, Warblade, War Maul, Greatclub, Estoc, Pike, Halberd, Glaive, and every bow, crossbow and long gun |
| **Versatile** | Yes - at the smaller die | Longsword, Greatsaber, Quarterstaff, Spear, Battle Axe |
| **One-handed** | Yes | Every Length 1-2 weapon, plus Whip, Weighted Chain, the Sling and both pistols |
| **Lance** | One-handed mounted; Two-Handed on foot, and loses its Charge | see [[Weapons|weapons]] |

**A Versatile weapon gripped two-handed drops 1 Length and gains its listed Two-Handed damage.** None of the off-hand tools carry AR.

| Off hand | What it does |
| :---- | :---- |
| **Shield** | `\+Guard` to every Parry, whatever you parry with. Also Parries itself with Daggers \& Wrestling, at any range. |
| **Buckler** | Same, at `\+1` Guard - the only shield light enough to keep on-hand while reloading or working a lock. |
| **Dagger or Knife** | Parries with Daggers \& Wrestling even with nothing else free. Still a weapon, still throwable. |
| **Another Light weapon** | Parries with its own Weapon Skill, alongside your main hand - whichever roll is better. No Guard. Throwable if it has a Thrown entry. |
| **Pavise** | Deployed, gives whoever is wholly behind it Cover (cannot be shot at all). Not a wielded shield - no Guard. |

---

## What everything costs

| | Costs |
| :---- | :---- |
| **Declaring your attack sequence** | Major Action |
| **Each attack in it** | 1 Tempo Die, all paid on declaration. No penalty and no cap |
| **Each shot in it** | 1 Tempo Die, same declaration. Two shots a turn at the most |
| **Reloading a missile weapon** | Minor Action \+ 1 to 3 Tempo Dice, by weapon. A thrown weapon takes an Object Interaction and no dice |
| **Holding an attack** | 1 Tempo Die, paid on declaration, lost if the trigger never comes |
| **Being hit in melee** | 1 Tempo Die - Shock, automatic. A shot causes no Shock |
| **A Parry** | 1 Tempo Die |
| **Declining to defend** | Free - and the blow lands, with an Opening |
| **An Opportunity Attack** | 1 Tempo Die |
| **Disengage** | 1 Tempo Die |
| **Taking an Opening** | Free - it is the reward |
| **A Riposte, Disarm/Sunder, Shove, Grapple, Called Shot** | Free, as the Opening |
| **Breaking out of a Grapple** | 1 Tempo Die, no roll, on your turn |
| **Your off hand** | Free - it costs a hand, not a die |

**An empty pool means you have stopped acting *and* stopped defending.** What is left is your armor, and nothing else.
