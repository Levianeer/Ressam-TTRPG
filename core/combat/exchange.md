# Your Tempo Pool

**Pool size \= baseline 4, plus the Attacks modifier of your weapon and your shield** (see [[Weapons|weapons]]) \- `\+1` for a Light weapon, `\-1` for a Two-Handed one, `\+0` for everything else, a shield's own modifier stacking on top. **Every die is a flat `1d12`.** STR's whole role in a fight is melee damage (see [[Damage Roll|combat]]); DEX funds Initiative and the Shot DC a target presents instead \- see Initiative and The Shot, below.

Your pool refills in full **at the start of the round**, not the start of your own turn \- one pool per character per round, shared by your own attack and every defense you make no matter whose turn it is. It starts full before anyone's first turn. **Pool size is recalculated only when it refills**: disarmed or swapping weapons mid-round costs you nothing until the next refill, and it also means going early in Initiative commits dice blind, while going late means defending on what the round throws at you before you know what you'll have left to swing with.

Dice buy attacks, Parries, Opportunity Attacks, Disengages, breaking a Grapple, Exerting, and a shot - see [What everything costs](#what-everything-costs). **A shot invests Tempo Dice too**, the same as a melee attack, though nothing is ever rolled back against it - see [The shot](#the-shot).

**An empty pool means you have stopped acting *and* stopped defending**, unless you Exert (below). What is left is your armor, and nothing else.

---

## The Exchange

An **Exchange** is one attack and its answer \- but **the defender rolls first**.

| Step | What happens | |
| :---- | :---- | :---- |
| **1. Defend** | Before the attack is rolled, the defender invests any number of Tempo Dice into a **Parry** (each `1d12`, summed, `\+ Weapon Skill \+ Guard`) or declines outright. Either way this sets a **DC** the attack must beat \- 0 if they declined. | An unaware target has no choice: it declines \- see [Awareness](#awareness). |
| **2. Attack** | Now knowing the DC, the attacker invests any number of Tempo Dice (each `1d12`, summed, `\+ Weapon Skill`). Once the defender has rolled, the attacker must invest at least 1 die \- declaring an attack is a commitment. | Outside the weapon's Reach, this roll closes the gap \- see [Distance & Reach](#distance--reach). |
| **3. Compare** | The attack must **strictly beat the DC** to land \- a tie still goes to the defender. Beat it by **5 or more** and the attacker takes an Opening; fall short by **5 or more** and the defender takes one instead (**3 or more** for a Signature Opening \- see [Openings](#openings)). Any hit that lands costs the target **1 Tempo Die** (Shock), margin aside. | A target with no dice left simply has none taken \- Shock never goes negative, and never converts into anything else. |

**Declining is a last resort, not a live choice** \- it exists for when you're out of dice, not as a tactic to pick while you still have one to spend. Declining almost always costs an Opening too: a DC of 0 clears most margin-5 rolls.

Both sides pay whatever they invested whether the attack lands or not. **One attack per Major Action.** A Riposte or Opportunity Attack is a separate **plain attack**: same procedure, defender rolls first, but it never takes or gives an Opening.

**There are no critical hits.** Margin only ever buys an Opening, never bonus damage \- see [There are no critical hits](#there-are-no-critical-hits) in [[Combat|combat]].

---

## Attacking

Declare a target and your investment together, and pay at once \- no cap on dice, no per-die penalty, and the investment cannot change once declared. Each die is a flat `1d12` regardless of how many you have left; the pool is a count, not a physical supply.

One attack, however deep, is everything your Major Action buys. A **Riposte**, an **Opportunity Attack**, and a triggered held attack are the only ways to act again this round, each its own separate investment.

### Plain attacks

Riposte, Opportunity Attacks and a held attack's trigger are **plain attacks**. They roll and take invested dice like any attack, but **take no Opening and give none to whoever beats them**. **A Riposte's first die is free**; further dice cost normally. None are ever made on your own turn.

---

## Defending

**Tempo Dice buy a defense. Without one you have nothing but Exerting (below).**

| Defense | Requires | The number | Can take an Opening |
| :---- | :---- | :---- | :----: |
| **Parry** | Something to parry with | Every invested die (`1d12` each), summed, `\+ Weapon Skill \+ Guard` | Yes, any Opening |
| **Nothing** | Nothing at all | The blow lands | No |

No cap on how many dice you sink into a single Parry, no stacking two defenses on one blow, and no cap on how many attacks you may answer in a round \- each Parry is its own separate investment. **Weapon Skill** on a Parry is the Skill of whatever is actually parrying, not of your own weapon \- a ranged weapon in hand Parries as Unarmed (see [Weapons in Hand](#weapons-in-hand)). **Guard** (see [[Shields|weapons]]) adds to every Parry you make while a shield is equipped; only the highest counts with more than one, and it degrades by 1 whenever a Parry it aided is lost.

### Exerting

Out of dice but still need to Parry? **Invest a `1d6` and take 1 Trauma instead of spending a Tempo Die** (see [[Trauma|rest_and_survival]]). Exerting only ever buys a Parry, never an attack, and it cannot buy a shot \- an archer out of dice is out of offense. Exert dice stay `1d6` even though every other invested Tempo Die is `1d12`. **Cost is flat, no escalation, and at most 1 Exert die per Parry** \- the same cap [[Prone and Restrained|rest_and_survival]] use.

---

## Openings

**Win a contest by 5 or more and take one** \- attacker or defender, on anyone's turn. It's free, and a win never grants more than one. **Openings do not chain.**

**Signature Opening.** Each weapon lists one Signature Opening (see [[Weapons|weapons]]). Take it on a win by **3 or more** instead of 5 \- any other Opening still needs 5. It's always your own weapon's Signature, whether you're attacking or Parrying with it, never the other side's.

| Opening | Effect |
| :---- | :---- |
| **Riposte** | A plain attack right now, first die free \- invest more if you have dice left. |
| **Disarm** (target wields a Normal-Reach weapon) | Their weapon drops in their square, picked up with a Lesser Action. |
| **Sunder** (target wields a Reach 1 or 2 weapon) | Their weapon breaks until repaired outside the fight, unless they spend 1 Tempo Die to drop it instead. |
| **Shove** | Push them 1 square, or knock them Prone. |
| **Grapple** | They're Restrained while you stay Adjacent and keep hold \- see [[Conditions|rest_and_survival]]. |
| **Feats** | Many combat Feats add entries to this menu. |

A target fighting Unarmed can't be Disarmed or Sundered \- pick another Opening. Breaking a Grapple costs the Grappled creature 1 Tempo Die, no roll, on their turn; it also ends the moment the grappler lets go, moves away, or is knocked Prone.

**Every Opening but Riposte ignores armor entirely** \- Disarm, Shove, Grapple and Sunder work the same against plate as against a shirt.

### There are no critical hits

Margin does not multiply damage \- it only decides Openings, whether you invested 1 Tempo Die or all of them. **Finding a gap** (every die in a damage roll landing on its maximum face) upgrades a Turned Aside hit to a Wound \- see [[Dent Line and Rend Line|armor]]. This rides the dice, not the margin, so it fires just as often on a 1-die attack as an all-in one.

### Shock

**Every attack in an Exchange that lands takes 1 Tempo Die off the person it landed on** \- no margin required, no Opening spent, whether the blow wounded them or their armor turned it aside. **Shock is melee only.** It cannot follow you into your next round; your pool refills in full.

---

## Distance & Reach

Ressam is played on a **square grid of five-foot squares** ([[Battlemap \& Positioning|positioning]] owns the grid); diagonals count as one square. Every weapon carries a **Reach** \- the farthest distance it can attack from \- and can attack at any distance from Adjacent up to that Reach:

| Reach | Squares | Weapons (see [[Weapons|weapons]] for the full list) |
|:------|:-------:|:--|
| **Normal** | Adjacent only | Unarmed and every one-handed or Light melee weapon |
| **Reach 1** | Adjacent through 1 square | Halberd, Glaive |
| **Reach 2** | Adjacent through 2 squares | Pike |

**Engaged** means you're within a living enemy's weapon Reach. Their remaining dice don't matter. **A Downed creature isn't a living enemy for this purpose** \- see [[Downed|rest_and_survival]].

### Opportunity Attacks

**Opportunity Attacks trigger on entering or leaving depending on the holder's Reach, never both:**

- **Normal Reach triggers on leaving.** Breaking Adjacent with a Normal-Reach foe draws their Opportunity Attack. Walking up to one is free.
- **Reach 1 or Reach 2 triggers on entering.** Closing from outside their Reach into a square they threaten draws their Opportunity Attack. Walking away from one is free.
- **Reach 2 threatens two squares, and closing through each is its own trigger.** Entering the Reach 2 square draws one; continuing into the Reach 1 square draws a second, separate one. Closing the last step into Adjacent draws nothing further.

**A landed Opportunity Attack from a Reach 1 or Reach 2 weapon stops the close outright** \- Move drops to 0 for the turn, wherever the target is when it lands. Miss it, and the target keeps moving. **A Normal weapon's Opportunity Attack just lands as normal** \- the target is already leaving, so there's nothing left to stop.

**There's no cap beyond the Tempo Pool.** Each enemy whose trigger is crossed gets its own Opportunity Attack, and a single winding Move can trigger more than one enemy, or the same Reach 2 holder twice \- what stops the pile-up is running out of dice, not a per-round cap. **Being pushed never draws Opportunity Attacks.** Only choosing to move does.

**A Reach 2 attack reaches through an intervening square** \- if a creature stands in the one square between the attacker and a target two squares off, the attack acts through it as though the square were empty. No other Reach has this.

**Dash** (Major Action): move up to double your Speed instead of the usual up-to-Speed Move. **Disengage** (Major Action): move up to your Speed without provoking any Opportunity Attack this turn, whether closing or leaving. **Difficult terrain:** each square costs 2 squares of Move; Dash doubles your Move before costs are counted.

---

## Weapons in Hand

**A Two-Handed weapon** (any weapon with `\-1` Attacks) **can't be used with a shield.**

**A ranged weapon in hand fights as Unarmed in every melee respect** \- Reach (Normal), Skill (Daggers \& Wrestling), Signature (Grapple) \- for Parrying, Opportunity Attacks, and any other melee attack it's pressed into. It's still an item you're holding: **you can be Disarmed while holding one**, though Sunder still doesn't apply, since it needs a Reach 1 or 2 weapon a bow or gun in melee never is. **Unarmed is Blunt**, so a ranged weapon pressed into melee never finds the gaps in armor (see [[Dent Line and Rend Line|armor]]). **Attacks is the exception** \- a ranged weapon in hand still sets your Tempo Pool from its own Attacks modifier, never from Unarmed's `\+1`.

**Swapping:** drawing or stowing a weapon costs your Lesser Action. Dropping one is free.

**No dual-wielding.** A second weapon is a spare you can draw later; it adds nothing while carried, and a shield or a second implement in the off hand adds no second Parry of its own \- Guard from an equipped shield is the only off-hand bonus in the base rules (see [[Shields \& Guard|weapons]]). A Feat may grant an off-hand option; nothing does by default.

---

## Armor and Wounds

*Definitions live in [[Armor|armor]] and [[Wounds \& Death's Door|rest_and_survival]]. This is only what a fight reads.*

**Nothing in an Exchange reads Armor Penalty.** Once fighting starts, your armor's **Dent Line** and **Rend Line** are the whole of what it does. **Wound resolution:** roll the attack's weapon dice `\+ STR` (missiles: no Attribute added) and compare to the target's current Dent Line and Rend Line \- below Dent is **Turned Aside** (0 Wounds), at or above Dent is **1 Wound**, at or above Rend is **2 Wounds**. Every die at its maximum face **finds a gap** (see [[Dent Line and Rend Line|armor]]). **No armor counts as Dent 0 / Rend 5, and those lines never wear down** \- an unarmored target still takes at least 1 Wound on any landing hit, and 2 on a total of 5 or more.

**Any landed hit reduces both of worn armor's lines by 1**, whether or not it deals a Wound \- a Turned Aside hit already cost the target Shock, so it landed too. A **Blunt** hit reduces them by 2 instead (**Unarmed** is the exception, at 1). Lines stop at 0: **Broken** once Dent reaches 0 (behaves as no armor with Rend still at 5), **Destroyed** once Rend reaches 0 too (every hit is 2 Wounds \- worse than no armor).

**A Piercing weapon finds the gaps in a pinned foe.** Against a target who is Restrained or Downed, a melee attack from Adjacent with a Normal-Reach Piercing weapon treats their armor as None for that hit \- never against a shot, a Reach 1 or 2 weapon, or any other damage type.

---

## Initiative and turn order

**Initiative \= 5 \+ DEX.** Static, never rolled, the same number for the whole fight; highest goes first. **Ties go to the player characters**; tied players choose their own order, and tied NPCs choose theirs.

**Mythic Initiative (X):** the creature takes a full turn at its Initiative, and another at every `\-2` below it, X counts in all. It refills its Tempo Pool in full on its first count, and regains 1 die on each count after that. Shock reads every count as a full turn. The stat-block side lives in [[Mythic Initiative|bestiary_overview]].

---

## Awareness

**Awareness** is a GM call, not a roll or a subsystem: a target is **unaware of you** if nothing they've seen, heard, or otherwise noticed gives them reason to expect an attack. There is no surprise round and no change to Initiative \- an unaware creature still takes its turn in the usual order. What changes is the **first attack** made against them:

- **In melee, an unaware target cannot Parry it.** They decline, setting a DC of 0 \- almost always an Opening for the attacker on top of the hit.
- **A shot at an unaware target** uses the Shot DC table's `\-3` row instead \- see [The shot](#the-shot).

Either way, the ambush is spent after that first attack \- the target is aware from then on.

---

## Fear

Some creatures carry a **Fear rating**: **7** (Terror) or **9** (Dread). The first time you would move closer to one, resist its rating, spending Will as normal (see [[Resisting|magic_overview]]).

- **Pass,** and you act freely for the rest of the fight.
- **Fail,** and you may not move closer to that creature this turn \- you can still move elsewhere, and still act \- and you gain **1 Trauma** and lose **1 Tempo Die**, as if you'd taken Shock. You test again the next time you try to close with it, on a later turn.

Only enemies test against a Fear rating. A creature already fighting one when it gains the rating isn't affected \- the test only happens when someone closes.

**A MIND 0 creature tests with 1 free die** \- it has no Will to spend, so the free die is the whole roll (free dice ignore the MIND ceiling; see [[Free Dice|magic_overview]]). It can't Push.

---

## Morale

Fear is about what a creature faces; **Nerve** is about what a creature can still stomach. It's **1d12 \+ CHA vs. Standard DC 7**, minus Wound Penalty. Nerve and the Resolve check (see [[Scars|rest_and_survival]]) are the two things CHA is for \- one inside the fight, one after it.

**Every creature tests Nerve**, Named and Unnamed alike, each time one of these happens to it:

- It's reduced to its last Wound box.
- A Named creature leading it (its officer, its summoner) is Downed or killed.
- Its side has lost **half its number** \- killed, Downed or Broken \- counted at the moment that half falls. Past that point, Unnamed creatures keep testing it (see Past Half Strength, below).
- **Named creatures only:** a Named ally they can see is Downed or killed.

**Each trigger is tested at most once per fight, pass or fail** \- with one exception: the half-strength trigger repeats for Unnamed creatures once their side crosses half. **Four triggers is the ceiling for Named creatures.**

**Past half strength.** Once a side has lost half its number, every Unnamed creature still fighting on that side tests Nerve again at the end of each round, for as long as the side stays at or below half. A creature already Broken doesn't test. It switches off the moment the count rises back above half, resuming if it drops again. **Resolve a group that shares a trigger and a round with one roll for the lot**, not one per creature.

**Pass,** and that trigger is spent \- for the repeat, only until the next round's test. **Fail:**

- **Unnamed** creatures are **Broken** \- they flee by the safest route they can see, attack no one, and can be ignored for the rest of the fight.
- **Named** creatures, PCs included, are never Broken \- they decide for themselves whether to keep fighting. A failed test instead costs them **1 Trauma**, each time.

**Steady the line.** A creature testing Nerve **within 3 squares of a Named ally it can see** may test on **that ally's CHA** instead of its own, no action or cost. The lender must not be Downed or Broken. **Killing the man giving orders trips the "leader is Downed" trigger and removes the aura in the same instant** \- his line tests on its own CHA, usually 0 or 1, at the worst possible moment. This runs both ways: the party's own Unnamed allies test the same schedule.

---

## Situations

**Being outnumbered** is not a special rule \- it is more Exchanges than you can afford to answer. **Who the enemy attacks** is the largest dial in the chapter; concentrated fire against one target wins fights faster than any other lever.

### Holding an attack

Declare an attack on your turn without resolving it. Name the trigger; for a melee attack, also say how many Tempo Dice you are investing and pay them now. It resolves as a **plain attack** the instant the trigger occurs, any time before the start of your next turn. **If the trigger never comes, the Major Action \- and any dice paid on it \- is gone.** Only one held attack at a time. A held shot takes no dice, and its weapon stays loaded until the trigger fires it.

---

## Who fights an Exchange, and who does not

| | Attacks in Exchanges | Defends with a Tempo Die |
| :---- | :---- | :---- |
| **Melee fighter** | Yes | Yes \- a Parry |
| **Ranged attacker** | No \- see [The shot](#the-shot) | Yes, against melee, if something in hand can Parry (a bow, crossbow or firearm cannot) |
| **Caster** | No \- see [Casters](#casters) | Only what bare hands can answer \- Daggers \& Wrestling, no Guard |
| **Cannot act** | No | No \- attacks land automatically and take an Opening |

## The shot

**A shot cannot be Parried, takes no Opening, and causes no Shock.** In every other respect it is an attack like any other: **you invest Tempo Dice to make it.**

**Shot: invest any number of Tempo Dice and roll them (each `1d12`), take the highest, and add your Archery or Firearms Skill against the Shot DC below.** Meet or beat it and the shot lands. Firing costs a Major Action; one shot a turn. **No dice, no shot** \- Exerting buys a Parry only.

Nothing is rolled against you. The Shot DC comes off the table below, not off a defender's Parry. **DEX gives the target the base number** \- a harder target to hit, no roll on their end \- and every situational modifier stacks on top of it.

| Situation | Shot DC |
|:----------|:-------:|
| Within the weapon's first range band | `7 \+ target's DEX` |
| Beyond it, out to the second | `\+3` |
| Beyond the second range band | Out of range \- cannot be shot |
| Light cover (a rail, a low wall, undergrowth, a body in the way) | `\+2` |
| Target holds a Heater Shield | `\+2` (Light cover) |
| Heavy cover (a wall, a doorframe) | `\+4` |
| Darkness (see [[Light and Vision|stealth_and_light]]) | `\+4` (Heavy cover) |
| Total cover | Cannot be shot |
| Target Prone, anywhere but Adjacent | `\+2` |
| Target Engaged in melee | `\+2` |
| Target Restrained, Prone and Adjacent, or unaware of you | `\-3` |
| You are Engaged when you fire (not a one-handed missile weapon) | `\+4` |

**Cover never stacks with itself.** Light cover, a Heater Shield, Heavy cover, and Darkness read off the same bucket \- take the single highest that applies, never add two together.

**A Shot DC more than 12 over your Skill is impossible** \- the GM disallows the shot instead of rolling it, the same ceiling [[Setting a Difficulty Class \(DC\)|core_rules]] sets for every other roll in the game.

**Shooting into a melee.** If the target is Engaged and you miss by 3 or less, the shot finds someone else in that fight instead \- roll off between the other combatants, friend or foe, and resolve damage against them.

**Diving** (off-turn, 1 Tempo Die): when a shot is declared against you and before the shooter invests, spend a die to add `\+3` to its Shot DC and end up Prone in your square (at most 1 die per Parry until you stand). No roll, no contest. The shooter then invests knowing the higher number. A later shot against you while still Prone (this turn or next) uses the normal Prone row instead.

**The movement gate:** a Bow or Sling needs you to have spent no more than half your Speed (round down) in Move this turn to fire at all. Spend more than that, or climb, leap, or swim, and you cannot fire this turn. It counts Move *spent*, so difficult terrain eats into it. **Crossbows and firearms override it and are exempt** - see [[Weapons|weapons]] for which weapons carry which.

---

## Loading

**Every ranged weapon is loaded or empty, and firing empties it.** Reloading costs the action(s) set by the weapon, never a Tempo Die \- see [[Reloading|weapons]] for the full ladder (bows, crossbows, thrown weapons, and every firearm, including lock type and multi-barrel effects). **A Loaded weapon carries between scenes.**

**Misfire.** A Firearms weapon jams when any Tempo Die invested in the shot comes up at or below its Misfire score \- see [[Firearm Rules|weapons]]. No separate roll: it rides the same dice the shot itself invested, so a gun punishes committing dice while a bow rewards it. A misfire still spends the Major Action fired with; clearing it costs a Major Action \+ a Minor Action, no earlier than your next turn, and it can't be fired or reloaded until cleared.

---

## Casters

**Casting requires being unengaged** (see [Distance & Reach](#distance--reach)). A working aimed at an unwilling target resolves against the target committing their own Will and rolling to match or beat the caster's highest die \- never a Ward, never the Tempo Pool. See [[Casting|magic_overview]] for the full loop. **A Tempo Die never answers a working of either kind** \- a caster's pool is pure defense, and bare hands Parry only as Unarmed.

---

## What everything costs

| | Major Action | Tempo Dice |
| :---- | :----: | :---- |
| **Your attack (melee)** | Yes | 1+, however many you invest, paid on declaration |
| **A shot** | Yes | 1+, however many you invest |
| **Holding an attack** | Yes | Melee: 1+, paid on declaration, lost if the trigger never comes. Ranged: none |
| **Reloading a missile weapon** | By weapon \- see [Loading](#loading) | Never |
| **A Parry** | No | 1+, however many you invest |
| **Exerting a Parry** | No | 0 \- `1d6` and 1 Trauma instead |
| **An Opportunity Attack** | No | 1+, however many you invest |
| **Declining to defend** | No | None \- and the blow lands, with an Opening |
| **Being hit in melee** | No | 1 \- Shock, automatic. A shot causes no Shock |
| **Disengage** | Yes | None |
| **Breaking out of a Grapple** | No | 1, no roll, on your turn |
| **Dropping a weapon rather than have it Sundered** | No | 1 |
| **Taking an Opening** | No | None \- it is the reward |
| **A Riposte, Disarm/Sunder, Shove, Grapple** | No | None, as the Opening \- a Riposte's roll may still take further invested dice on top |
| **Diving to avoid a shot** | No | 1 |
| **Resisting a Fear check or a working** | No | Will, not Tempo Dice \- see [[Casting|magic_overview]] |
