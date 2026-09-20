# Ressam - Combat (Playtest Draft)

*Playtest draft - these rules are still being tested and may change between sessions.*

You'll need a character card: Attributes (STR, DEX, MIND, CHA, each 0-5), Skills (0-5), weapon, armor, Speed, Wounds, and Tempo Pool size - gear stats are in `equipment_draft.md`. This is the whole combat loop - ask your GM about anything it doesn't cover.

Distances are measured in squares. One square is 5 feet.

---

## Building a Pregen

This slice has no leveling and no priority ladder - pregens are built once, to a fixed standard, and played as-is. Use the full ruleset's own array (`character_creation.md`) rather than inventing a new one, since it's already cut to this slice's four Attributes:

**Attributes.** Assign the **B** standard array - `2, 2, 1, 0` - one number to each of STR, DEX, MIND, CHA, in whatever order fits the concept. Every number is used; the 0 is a real choice, not a rounding error.

**Skills.** An **8-point budget**, spent one point per Rank, no Skill above **3** at creation. Spend it across the Weapon Skills and `equipment_draft.md`'s Reference list (Daggers & Wrestling, Fencing Blades, Two-Handed Blades, Cleaving Blades, Hafted Weapons, Polearms, Firearms, Archery, Chirurgery, Smithing) - whatever the concept and starting gear call for.

**Starting Crowns: 100**, spent on gear from `equipment_draft.md` before play begins - one weapon, armor, a shield if wanted, and whatever's left over on the Adventuring Gear list. Unspent Crowns don't carry forward; this isn't a wealth track.

**Two exceptions, so the slice actually tests itself.** At 100 Crowns nobody buys Mail (100) or Plate (300), which would leave the top half of Damage & Armor tested only from the GM's side of the screen. So: **one pregen is issued a suit of Mail, and another a suit of Plate**, as starting kit rather than buying it, and neither comes out of the purse. And **a caster pregen may take MIND 3** in place of the array's 2, matching the "player wizards" row in `magic_draft.md` and the MIND 3 worked examples in `spells_draft.md`. Everything else follows the array.

**Tempo Pool size** follows straight from the finished card: baseline 4, plus the equipped weapon's (and shield's) Attacks modifier - see The Tempo Pool, below.

*(Placeholder - the array, budget, and purse are a starting guess, not a tested baseline. Tune all three together: a bigger purse buys better armor, which changes how the Dent/Rend math in Damage & Armor actually plays.)*

---

## Starting a Fight

**Initiative = 5 + DEX**, static, never rolled. Highest goes first. **Ties go to the player characters**; tied players choose their own order.

**Awareness** is a GM call, not a roll or a subsystem: a target is **unaware of you** if nothing they've seen, heard, or otherwise noticed gives them reason to expect an attack. There is no surprise round and no change to Initiative - it's static (above), and an unaware creature still takes its turn in the usual order. What changes is the **first attack** made against them:

- **In melee, an unaware target cannot Parry it.** They decline, setting a DC of 0 (see The Exchange) - which is almost always an Opening for the attacker on top of the hit.
- **A shot at an unaware target** uses the Shot DC table's `-3` row instead.

Either way, the ambush is spent after that first attack - the target is aware from then on.

## Your Turn

| Action                                              |  Per round  |
|:----------------------------------------------------|:-----------:|
| Major Action (attack, cast, Dash, Disengage)        |      1      |
| Minor Action (reload, administer a draught, etc.)   |      1      |
| Lesser Action (draw, stow, or pick something up)    |      1      |
| Free Action (drop an item, speak, etc.)             |  Unlimited  |
| Move Action                                         | up to Speed |

**Base Speed is 6 squares**, before armor's and a shield's Speed modifier (`equipment_draft.md`). *(Placeholder - tune against pregens.)*

There are no Reactions - everything you do off your own turn is paid for out of your Tempo Pool.

---

## Checks & the Difficulty Ladder

A **check** is `1d12 + the relevant Skill` against a DC, minus your Wound Penalty (see Wounds & Death's Door, below). Checks are what you roll outside a fight's dice economy - forcing a door, Chirurgery, Nerve. Anything that spends Tempo Dice, shots included, is a Tempo roll and follows The Exchange's investment rules instead - the Wound Penalty never touches one.

**Attributes never add to a check roll - only Skill does.** STR pays for melee damage, DEX for Initiative and for how hard you are to shoot, MIND for magic, CHA for Nerve (see Morale, below); nothing else touches a bare Skill check. A STR 5 character forces a door no better than a STR 0 one with the same Skill - deliberate, not an oversight.

Every **base** DC in the game sits on one ladder - the same four numbers as the working difficulties in `magic_draft.md`:

| Difficulty | DC |
|:-----------|:--:|
| Easy       | 5  |
| Standard   | 7  |
| Hard       | 9  |
| Extreme    | 11 |

The ladder sets the **base** DC. Situation modifiers stack on top of it, so a shot at long range into heavy cover can go well past 11. **The Shot DC is the one place the base itself moves** - it reads `7 + the target's DEX` (see Ranged Attacks): the Standard rung, plus how hard that particular body is to hit.

---

## Named Characters

**Named** means player characters and any NPC the GM gives a name. Named characters go to Death's Door when their Wounds fill (see Wounds & Death's Door). **Named NPCs** also have MIND 1 minimum (see `magic_draft.md`). Everyone else has neither - rank and file simply die when their Wounds fill.

**Named status only ever touches Wounds, Death's Door, and what a failed Nerve check costs** (see Morale, below). Every other track - Trauma included - works identically for Named and Unnamed alike: Exerting costs Trauma, a failed fear check costs Trauma, and both apply to a rank-and-file mook exactly as they do to a PC.

**Size.** Every creature is Small, Medium, or Large - it sets Wound boxes (see Wounds & Death's Door) and nothing else. Shove and Grapple (see Openings) assume a target your size or smaller; doing either to a larger creature is a GM ruling, not a rule here. A creature's Attributes, Skill, weapon, armor, and Tempo Pool size are built the same way a PC's are - there's no separate stat block format in this slice.

---

## Distance & Weapon Reach

Every weapon has a **Reach** - the farthest distance it can attack from - and can attack at any distance from Adjacent up to that Reach: **Normal** (Adjacent only), **Reach 1** (Adjacent or 1 square), or **Reach 2** (Adjacent through 2 squares). See `equipment_draft.md` for which weapons carry which Reach.

**Engaged** means you're within a living enemy's weapon Reach. Their remaining dice don't matter. Casting (see `magic_draft.md`) requires being unengaged. **A Downed creature isn't a living enemy for this purpose** - see Downed, below.

**Opportunity Attacks trigger on entering or leaving depending on the holder's Reach, never both:**

- **Normal Reach triggers on leaving.** Breaking Adjacent with a Normal-Reach foe draws their Opportunity Attack. Walking up to one is free - they get nothing as you close.
- **Reach 1 or Reach 2 triggers on entering.** Closing from outside their Reach into a square they threaten draws their Opportunity Attack. Walking away from one is free - they get nothing as you leave.
- **Reach 2 threatens two squares, and closing through each is its own trigger.** Entering the Reach 2 square draws an Opportunity Attack; continuing on into the Reach 1 square draws a second, separate one. Closing the last step into Adjacent draws nothing further - Adjacent is Normal Reach's square, not a Reach holder's.

**A landed Opportunity Attack from a Reach 1 or Reach 2 weapon stops the close outright** - your Move drops to 0 for the turn, wherever you are when it lands. Miss it, and a closing target keeps moving, which is how a Reach 2 holder can still get its second trigger at the Reach 1 square. **A Normal weapon's Opportunity Attack just lands as normal** - you're already leaving, so there's nothing left to stop.

**There's no cap beyond the Tempo Pool.** Each enemy whose trigger you cross gets its own Opportunity Attack, and a single winding Move can trigger more than one enemy, or the same Reach 2 holder twice - what stops the pile-up is running out of dice to pay for it, not a rule capping attacks per round.

**Being pushed never draws Opportunity Attacks.** Only choosing to move does.

**Dash** (Major Action): move up to double your Speed instead of the usual up-to-Speed Move. **Disengage** (Major Action): move up to your Speed without provoking any Opportunity Attack this turn, whether you're closing or leaving.

**Difficult terrain:** each square of it costs 2 squares of Move. Dash doubles your Move before any costs are counted.

**A Reach 2 attack reaches through an intervening square** - if a creature stands in the one square between the attacker and a target two squares off, the attack acts through it as though the square were empty.

---

## Weapons in Hand

**A Two-Handed weapon** (any weapon with `-1` Attacks) **can't be used with a shield.** The Shortbow, Longbow, Light Crossbow, Heavy Crossbow and Arquebus are also two-handed; the Pistolet is one-handed.

**Swapping:** drawing or stowing a weapon costs your Lesser Action. Dropping one is free.

**A ranged weapon in hand fights as Unarmed in every melee respect** - Reach (Normal), Skill (Daggers & Wrestling), Signature (Grapple, achievable at margin 3 same as any Unarmed fighter) - for Parrying, Opportunity Attacks, and any other melee attack it's pressed into. It's still an item you're holding, not empty hands: **you can be Disarmed while holding one** (Disarm only needs a Normal-Reach weapon in hand, same as a dagger) - only a target truly fighting bare-handed is immune. Sunder still doesn't apply; it needs a Reach 1 or 2 weapon, which a bow or gun in melee never is. **Unarmed is Blunt**, so a ranged weapon pressed into melee never finds the gaps in armor (see Damage & Armor).

**Attacks is the exception** - a ranged weapon in hand sets your Tempo Pool from its own Attacks modifier (see `equipment_draft.md`), never from Unarmed's `+1`. A Longbow in melee still fights as Unarmed, on the three dice a Longbow gives you.

**No dual-wielding in this slice.** A second weapon is a spare you can draw later; it adds nothing while carried.

---

## The Tempo Pool

Your Tempo Pool is your dice for the round, printed on your card - it pays for attacking, Parrying, and any off-turn act.

**Departure from the full ruleset:** every die here is a flat `1d12` (STR no longer sizes the Tempo Die), and pool size comes from your weapon's Attacks modifier, not `DEX \+ 1`. STR's whole role in a fight is melee damage; DEX's is Initiative and Shot DC (see Checks & the Difficulty Ladder, and Ranged Attacks, below).

**Pool size:** baseline 4, plus your weapon's Attacks modifier (see Weapons, below) - a shield counts too, where it has one. Pregens for this playtest are built at a fixed pool size; there's no leveling system in this kit to grow it over a campaign.

Every Tempo roll invests at least 1 die, and every invested die is `1d12`. Take the **highest** die you rolled, not the sum, and add your modifier once - `+ Weapon Skill` on an attack, `+ Weapon Skill + Guard` on a Parry - to that single result.

Your pool refills in full at the start of the round, not the start of your turn - one pool per character per round, shared by your own attack and every defense you make, whoever's turn it is - and starts full at the start of the fight, before anyone's first turn. Going early in Initiative means committing dice before you know what the round will ask of you; going late means defending on it first and swinging on what's left. **Pool size is recalculated only when it refills**: if you're disarmed or swap weapons mid-round, you keep the dice you have until the next round's refill. **No dice, no offense** - you can still Parry by Exerting (below), but you cannot attack, and that includes firing a shot.

---

## The Exchange

An attack, an answer - but the **defender rolls first**.

1. **Defend:** before the attack is rolled, the defender invests any number of Tempo Dice into a **Parry** and rolls them (`+ Weapon Skill + Guard` on the highest die), or declines and takes the hit outright. Either way, this sets a **DC** the attack must beat - 0 if they declined. **Declining almost always costs an Opening too** - a DC of 0 clears most margin-5 rolls. **Declining is a last resort, not a live choice** - it exists for when you're out of dice (see The Tempo Pool), not as a tactic to pick while you still have one to spend. An unaware target (see Awareness) has no choice: they decline.
2. **Attack:** now knowing the DC, the attacker invests Tempo Dice and rolls them (`+ Weapon Skill` on the highest die). **Once the defender has rolled, the attacker must invest at least 1 die** - declaring an attack is a commitment.
3. **Compare:** the attack must **strictly beat the DC** to land - a tie still goes to the defender. **Beat it by 5 or more and the attacker takes an Opening; fall short by 5 or more and the defender takes one instead** (3 or more for a Signature Opening - see Openings). Any hit that lands costs the target 1 Tempo Die (**Shock**), margin aside. A target with no dice left simply has none taken - Shock never goes negative, and it doesn't convert into Trauma or an extra Wound.

Both sides pay whatever they invested whether the attack lands or not.

One attack per Major Action. A Riposte or Opportunity Attack is a separate **plain attack** - same procedure (defender rolls first, attacker answers), but it never takes or gives an Opening, Signature or otherwise.

There are no critical hits - margin only ever buys an Opening, never bonus damage.

---

## Openings

Win a contest by 5 or more and take one - whether you're attacking or defending, on anyone's turn. It's free, and a win never grants more than one.

**Signature Opening.** Each weapon lists one Signature Opening (see `equipment_draft.md`). You can take it on a win by **3 or more** instead of 5. Any other Opening still needs 5. **It's always your own weapon's Signature** - what you're attacking or Parrying with, never the other side's - so a defender's margin-3 threshold can differ from the attacker's.

| Opening                                          | Effect                                                                                                                     |
|:-------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| **Riposte**                                      | A plain attack right now, first die free - invest more if you have dice left.                                              |
| **Disarm** (target wields a Normal-Reach weapon) | Their weapon drops in their square, picked up with a Lesser Action.                                                        |
| **Sunder** (target wields a Reach 1 or 2 weapon) | Their weapon breaks until repaired outside the fight, unless they spend 1 Tempo Die, if they have one, to drop it instead. |
| **Shove**                                        | Push them 1 square, or knock them Prone (see Conditions, below).                                                           |
| **Grapple**                                      | They're Restrained while you stay Adjacent and hold on (see Conditions, below).                                            |

A target fighting Unarmed can't be Disarmed or Sundered - pick another Opening.

---

## Conditions

**Prone.** Costs a whole Move to stand back up - no roll, no other cost. While Prone, you can invest **at most 1 die in each Parry**. Attacking is unaffected. See the Shot DC table under Ranged Attacks for how Prone changes incoming shots. **Prone is not pinned** - a Prone creature's armor still works normally (see Damage & Armor).

**Restrained.** Can't willingly move - Move is 0 while the hold lasts. While Restrained, you can invest **at most 1 die in each Parry**. Attacking and casting are unaffected (casting still requires being unengaged). Breaks for 1 Tempo Die, no roll. A Grapple ends for free the moment the grappler leaves the Reach that created it - Adjacent for a Normal-Reach hold, out to 1 square for the Halberd's; a working's hold ends however that working says. **A Restrained creature can be knifed through the gaps in its armor** - see Damage & Armor. **While you hold a Grapple, your own Tempo Pool drops by 1** - one hand is full.

**Downed.** See Wounds & Death's Door, below.

The 1-die cap counts every die, including an Exert die.

---

## Fear

Some creatures carry a **Fear rating**: **7** (Terror) or **9** (Dread). The first time you would move closer to one, resist its rating, spending Will as normal (see Resisting, `magic_draft.md`).

- **Pass,** and you act freely for the rest of the fight.
- **Fail,** and **you may not move closer to that creature this turn** - you can still move elsewhere, and still act - and you gain **1 Trauma** and lose **1 Tempo Die**, as if you'd taken a Shock. You test again the next time you try to close with it, on a later turn.

Only enemies test against a Fear rating. A creature already fighting you when it gains one isn't affected - the test only happens when someone closes.

**A MIND 0 creature tests with 1 free die** - it has no Will to spend, so the free die is the whole roll (free dice ignore the MIND ceiling; see Free Dice, `magic_draft.md`). That's 50% against Terror and 33% against Dread: long odds, never a lockout. It can't Push. Dice lent by an ally (Ward of Aegis, or similar) stack on top of it.

---

## Morale

Fear is about what a creature faces; **Nerve** is about what a creature can still stomach. It's **1d12 + CHA vs. Standard DC 7**, minus Wound Penalty. Nerve and the Resolve check (see Scars, below) are the two things CHA is for - one inside the fight, one after it.

**Every creature tests Nerve**, Named and Unnamed alike, **each time one of these happens to it**:

- It's reduced to its last Wound box.
- A Named creature leading it (its officer, its summoner) is Downed or killed.
- Its side has lost **half its number** - killed, Downed or Broken - counted at the moment that half falls. Past that point, Unnamed creatures keep testing it (see Past Half Strength, below).
- **Named creatures only:** a Named ally they can see is Downed or killed.

**Each trigger is tested at most once per fight, pass or fail - with one exception.** The half-strength trigger repeats for Unnamed creatures once their side crosses half (see Past Half Strength, below); every other trigger, and the half-strength trigger for Named creatures, still fires once and no more. A creature that has tested for one Named ally going down does not test again for the next. **Four triggers is the ceiling for Named creatures**, and a Named creature that never reaches one never rolls.

**Past half strength.** Once a side has lost half its number, every Unnamed creature still fighting on that side tests Nerve again at the end of each round, for as long as the side stays at or below half. A creature already Broken doesn't test - it's out of the fight. The repeat keeps firing every round whether or not more of the side falls, and switches off the moment healing or a rally pushes the count back above half, resuming if the count drops again. This is a **Scarcity** call, not a morale buff - a fight that's already decided should end there instead of grinding to the last body, and the repeat is what closes it out. It adds no Trauma: a failed Nerve check only costs Trauma for Named characters (see Trauma, below), and Named characters never repeat this trigger, so the inflow items 1, 6 and 14 track is unchanged.

**Pass,** and that trigger is spent - for an Unnamed creature testing the repeat, only until the next round's test. **Fail:**

- **Unnamed** creatures are **Broken** - they flee by the safest route they can see, attack no one, and can be ignored for the rest of the fight.
- **Named** creatures, PCs included, are never Broken - they decide for themselves whether to keep fighting. A failed test instead costs them **1 Trauma**, each time.

**Resolve a group that shares a trigger and a round with one roll for the lot, not one per creature** - the expected way to run the repeat, not just a GM's-call aside. Without it, a side past half strength is a fistful of d12s every round during mop-up, exactly what the Elegance pillar rejects.

**Steady the line.** A creature testing Nerve **within 3 squares of a Named ally it can see** may test on **that ally's CHA** instead of its own. Nothing is spent and no action is taken - this is simply what a steady officer is worth to the people around him. The lender must not be Downed or Broken. This governs the repeat too: a line past half strength keeps testing on its officer's CHA every round he's still up, and drops to its own CHA of 0 or 1 - already past half strength - the moment he's Downed or Broken.

That cuts both ways, and it is the point. **Killing the man giving orders trips the "leader is Downed" trigger and removes the aura in the same instant** - his line tests on its own CHA, which is usually 0 or 1, at the worst possible moment. Enemies work the same way the party does, so **give the party a way to see who it is**: the one shouting, the one with the horn, the only one in a good coat. A rout should be something someone chose to cause. The same logic runs the other way: the party's own Unnamed allies - hirelings, retainers, anything summoned or commanded - test the repeat on the same schedule once their side crosses half.

---

## Exerting

Out of dice but still need to Parry? Invest a `1d6` and take Trauma instead of spending a Tempo Die. Exerting only ever buys a Parry, never an attack - it feeds into the defender's roll in The Exchange, above. It cannot buy a shot; an archer out of dice is out of offense. Exert dice stay `1d6` even though every other invested Tempo Die is `1d12`; Exerting is a distinct fallback, not a draw from the pool.

**Cost is flat: 1 Trauma per Exert die**, no escalation. **At most 1 Exert die per Parry** - the same cap Prone and Restrained use. One weak die, once, when you've nothing left: that's the whole of it.

---

## Damage & Armor

A landed hit rolls the weapon's damage dice `+ STR` for melee. Missiles - bows and guns alike - roll damage dice alone, no Attribute added. Compare the total to the target's **Dent Line** / **Rend Line**:

- Below Dent: **Turned Aside** (0 Wounds).
- At or above Dent: **1 Wound**.
- At or above Rend: **2 Wounds**.

See `equipment_draft.md` for each armor's starting lines. **No armor counts as Dent 0 / Rend 5, and those lines never wear down** - every hit on an unarmored target is at least 1 Wound, and a total of 5 or more is 2. **Departure from the full ruleset:** the published rule is a flat 2 Wounds per hit on an unarmored target, no roll. This slice uses a real Dent/Rend pair instead, so a weak hit only deals 1 - see `magic_draft.md`'s Designing Workings for why that matters.

**Any landed hit reduces both lines of worn armor by 1, whether or not it deals a Wound** - a Turned Aside hit already costs the target Shock (see The Exchange), so it's landed too. **A Blunt hit reduces them by 2 instead** - a mace doesn't have to open harness to ruin it - **except an Unarmed one, which reduces them by 1**; a fist is not a mace. Lines stop at 0.

- **Broken** once Dent reaches 0. With Rend still at 5, it now behaves exactly like no armor.
- **Destroyed** once Rend reaches 0 too. Every hit is now 2 Wounds - *worse* than no armor.

Broken or Destroyed armor keeps its Speed penalty. Taking armor off costs a Major Action.

**There is no way past armor except through it - for a weapon.** A hit that cannot reach the Dent Line does nothing - no lucky opening, no lottery die. The two exceptions below are earned, not rolled for; a damage working bypasses armor a third way, unconditionally - see `magic_draft.md`'s Designing Workings.

**A Piercing weapon finds the gaps in a pinned foe.** Against a target who is **Restrained or Downed**, a melee attack made from **Adjacent** with a **Normal-Reach** Piercing weapon treats their armor as **None** (Dent 0 / Rend 5) for that hit. A man in harness knocked Prone is still in harness; one held still is not. This never applies to shots, to Reach 1 or Reach 2 weapons, or to any other damage type - it's the dagger through the visor, not the spear.

**Armor-Piercing** (crossbows and firearms, see `equipment_draft.md`) lowers worn armor's lines for a single hit. It never touches the None line.

**Every Opening but Riposte ignores armor entirely** - Disarm, Shove, Grapple and Sunder work the same against plate as against a shirt, and a Prone or Restrained target can barely Parry.

---

## Wounds & Death's Door

Every character has **5 Wound boxes** - 6 at size Large, 4 at size Small. Landed hits fill them.

**Wound Penalty.** Each Wound currently missing gives `-1` to Checks, cumulative - a character missing 3 of 5 Wounds checks at `-3`. **It never touches a Tempo roll** - attacks, Parries, shots, casts, and resists are unaffected, so there's no combat death spiral: a character on their last Wound still fights at full capability. The cost of injury lands on the strategic layer, not the fight you're bleeding in.

**A hit that deals 2 Wounds also deals 1 Trauma.**

**When your last Wound box fills:**

- **Unnamed** characters die.
- **Named** characters are **Downed** instead. Any Wounds beyond the last box are ignored.

**Downed.** You're Prone, can't stand, and can't take a Major Action. **Any further Wound kills you.** You can still Parry, at most 1 die (you're Prone). Armor still protects you against Blunt and Slashing - a hit that's Turned Aside deals no Wound - but **a Normal-Reach Piercing weapon finds the gaps** (see Damage & Armor), so the dagger standing over you is the thing to fear, harness or no harness.

**A Downed creature doesn't threaten.** It isn't a living enemy for Engaged (see Distance & Weapon Reach) and can't make Opportunity Attacks, take Openings, or Riposte - it's fighting to survive a Parry, nothing more. Allies can walk past or away from it freely.

**Getting up.** Healing 1 Wound ends Downed. In a fight, an Adjacent ally can use their Major Action and a Healer's Kit to attempt a **Chirurgery check (DC 7)**; if it succeeds, you heal 1 Wound. An Adjacent ally can instead administer a Healing Draught with their Minor Action (see `equipment_draft.md`) - **a Downed character can't drink one themselves**, and nobody gets up alone.

**Every Wound healed costs 1 Trauma, however and whenever it happens** - a Chirurgery check, a draught, a working, or a Rest (see Trauma and Rest & Repair, below). A fight that draws blood leaves a mark even on a decisive win. **Standing back up mid-fight costs 1 further Trauma on top of that** - forcing yourself back into a fight you nearly died in hurts worse than mending in camp, and it stops Downed from being a free revolving door.

**Dragging.** An ally Adjacent to a Downed or Restrained creature can move it with them; every square they move counts double, as if it were difficult terrain. Dragging a Restrained creature this way doesn't end the Grapple.

**Environmental hazards** (falling, fire, drowning, poison, and the like) deal **1 Wound**, or **2** if the GM judges the hazard severe enough to reach the Rend line. No roll, no armor - a GM call on severity, not a subsystem.

---

## Trauma

Shared with `magic_draft.md` - one 0-20 track, not just a combat one. Wounds are what kill your body; Trauma is what breaks you. When Trauma reaches 20, the character dies.

| Trauma | Band                |
|:------:|:--------------------|
|  0-4   | Clear               |
|  5-9   | Manageable          |
| 10-14  | Dangerous           |
| 15-19  | Critical            |
|   20   | **Automatic Death** |

**Trauma carries no roll penalty of its own** - see Wound Penalty, above, for what a roll actually loses to injury. Trauma's own cost is longer-range: it gates Scars (see Scars, below - reaching a new band calls for a Resolve check) and kills outright at 20.

You gain Trauma from:

- **A hit that deals 2 Wounds:** 1.
- **Healing a Wound, by any means** (see Wounds & Death's Door, above): 1 per Wound - Rest included.
- **Standing back up from Downed mid-fight** (see Wounds & Death's Door, above): 1 further, on top of the Wound healed.
- **Exerting** (above): 1 per Exert die, flat, at most 1 die per Parry.
- **Failing a fear check** (above): 1.
- **Failing a Nerve check, Named characters only** (see Morale, above): 1 per failed check - a bad fight can ask two or three times.
- Channelling, Pushing a roll, and certain workings - see `magic_draft.md`.

**Trauma never comes down in the field.** Rest heals Wounds, not minds - the only way Trauma comes off is Revelry & Leisure, in a town. (Mending Touch can move it between characters, but never removes it - see `spells_draft.md`.)

---

## Revelry & Leisure

Downtime spent relaxing in a town is the only thing that clears Trauma.

**Each character chooses how many nights to spend, 1 to 7, and rolls `1d12` per night.** **Cost is 10 Crowns per character, per night** - a four-person party where everyone stays the full 7 nights runs up 280 Crowns, paid from the party's shared funds; a character who only stays 2 nights only adds 20 to the bill. *(Placeholder cost - tune it against what adventures actually pay out; see `equipment_draft.md`'s Reference for the rest of the price list this now sits against.)*

**Roll each die separately against DC 5, minus your Wound Penalty.** Each success removes **2 Trauma**; each failure removes **1**. Recompute your Wound Penalty before each night's roll - Wounds closing mid-stay (see below) lower the penalty on later nights.

Then count the dice:

- **More successes than failures:** gain a **boon** - a contact, a rumor, a favor owed.
- **More failures than successes:** a **Mishap** - a debt, a brawl, a loose tongue, lost gear.
- **Tied:** just the rest.

An odd number of nights can never tie, so a 1-, 3-, 5- or 7-night stay always ends in a boon or a Mishap. Only an even stay can come out quiet.

The GM describes both. Nights of revelry are still days in town for Rest & Repair.

| Wound Penalty  | Each die succeeds | Mishap, 3 nights | Mishap, 7 nights | Trauma removed, 7 nights (avg) |
|:---------------|:-----------------:|:----------------:|:----------------:|:------------------------------:|
| 0 (unhurt)     |        67%        |       26%        |       17%        |              ~12               |
| -3 (3 missing) |        42%        |       62%        |       68%        |              ~10               |

Chirurgery handles bodies and Scars. Revelry & Leisure handles minds.

---

## Scars

The number comes down. The marks do not.

**Your Scar Line is the highest Trauma band you have ever checked at** - Clear, Manageable, Dangerous or Critical. It starts at Clear and is one value on your character card.

**When a fight ends, compare your band to your Scar Line.** If your band is higher, make one **Resolve check** for each band you climbed, then set your Scar Line to your current band. If your band is equal or lower, nothing happens - no check, no matter how many fights you spend up there.

**Your Scar Line drops whenever your Trauma drops into a lower band**, however that happens - Revelry & Leisure, or occasionally Mending Touch. Climb back later and that band checks again.

**Resolve check:** `1d12 + CHA` against the band's rung, minus your Wound Penalty - the same ladder as every other DC in the game.

| Band reached    | DC |
|:----------------|:--:|
| Manageable (5)  | 7  |
| Dangerous (10)  | 9  |
| Critical (15)   | 11 |

**Pass, and the fight leaves no mark.** **Fail, and roll `1d6` on the table below**, or let the GM choose one that fits what happened.

**If you roll a Scar you already hold, or one that would have no effect on you** (Hollow at MIND 0, say), **you take Steeled instead** - or nothing at all, if you already hold Steeled. One roll, one outcome; never a reroll.

| `1d6` | Scar             | Effect                                                                             |
|:-----:|:-----------------|:-----------------------------------------------------------------------------------|
|   1   | **Flinching**    | You cannot Exert.                                                                  |
|   2   | **Haunted**      | Your first Parry each fight costs 1 extra Tempo Die.                               |
|   3   | **Hollow**       | Your Will pool is reduced by your MIND (see `magic_draft.md`).                     |
|   4   | **Wary**         | You cannot take Openings.                                                          |
|   5   | **Hair-Trigger** | On your first turn of any fight you must attack the nearest enemy if you are able. |
|   6   | **Palsied**      | `-1` to damage totals, minimum 1.                                                  |
|   -   | **Steeled**      | The first Trauma you would take in any fight is ignored.                           |

Scars are untouched by Revelry & Leisure. They come off only with treatment in a town: one week of downtime and a **Chirurgery check (DC 11)**, one Scar at a time. **Steeled is permanent and is never treated away.**

A character can hold more than one Scar, and they stack.

| Resolve check   | CHA 0 | CHA 1 | CHA 2 |
|:----------------|:-----:|:-----:|:-----:|
| Manageable (7)  |  50%  |  58%  |  67%  |
| Dangerous (9)   |  33%  |  42%  |  50%  |
| Critical (11)   |  17%  |  25%  |  33%  |

*(Placeholder - 7/9/11 is a starting guess. Scars are markedly rarer than under the old near-certain check. If that guts the attrition you wanted, raise the rungs to 9/11/13 before touching anything structural.)*

---

## Rest & Repair

Bodies and gear recover on the same schedule.

| Rest      | Length                                                              | Wounds healed                                                | Armor & shields repaired                                                      | Will (see `magic_draft.md`) |
|:----------|:--------------------------------------------------------------------|:-------------------------------------------------------------|:------------------------------------------------------------------------------|:----------------------------|
| Short     | A pause of minutes to an hour - catching your breath between fights | None                                                         | None                                                                          | 1                           |
| Field     | A night camped outside a town                                       | 1                                                            | 1 point to each line (Dent, Rend, Guard)                                      | MIND points, minimum 2      |
| Long Rest | A full day, in town                                                 | 1, or 2 if a medic passes a Chirurgery check (DC 9) that day | 1 point to each line, or 2 if a smith passes a Smithing check (DC 9) that day | Full                        |

**A character cannot take more than 2 Short Rests per day.** A Short rest only counts against this cap if something happened first - a fight, a scene, a stretch of travel. Ten in a row in the same corridor is one Short rest.

**A character benefits from at most one Field Rest per day.** Long Rest needs no such cap - a full day leaves no room for a second one.

Chirurgery checks need a Healer's Kit (see `equipment_draft.md`). A Sundered weapon is useless until it gets a day in town.

**Repair never exceeds an armor or shield's printed starting values** (see `equipment_draft.md`) - Dent, Rend, and Guard each cap where they began. A winter in town doesn't turn Plate into something better than Plate.

**Every rest, Short included, ends any Sustained working the character is maintaining** (see `magic_draft.md`) - that's Short Rest's other job, on top of the 1 Will above.

Trauma never comes down on this ladder - see Revelry & Leisure. Healing a Wound here still costs Trauma the same as it does anywhere else (see Trauma, above).

---

## Shields & Guard

A shield adds **Guard** to every Parry you make, whatever you're parrying with, and may cost Attacks or Speed to carry (see `equipment_draft.md` for which - the Buckler costs neither). Only the highest Guard counts if you have more than one. A Two-Handed weapon can't be used with a shield.

**Guard degrades by 1 whenever a Parry it aided is lost.** It stops at 0, where the shield adds nothing until repaired (see Rest & Repair).

**Reach 1 and Reach 2 weapons Ignore Guard** - a shield's bonus adds nothing to a Parry against one. A Parry Guard couldn't help doesn't degrade Guard when it's lost - nothing aided it, so nothing wears down.

**A Heater Shield counts as Light cover (+2 Shot DC) against shots at you.** Passive, no action. The Buckler doesn't count - it's a parrying tool, not a wall.

---

## Ranged Attacks

A shot cannot be Parried, takes no Opening, and causes no Shock. In every other
respect it is an attack like any other: **you invest Tempo Dice to make it.**

**Shot: invest any number of Tempo Dice and roll them, take the highest, and add
your Archery or Firearms Skill against the Shot DC below.** A shot is a Tempo
roll, so the Wound Penalty never touches it (see Wounds & Death's Door). Meet or
beat it and the shot lands. Firing costs a Major Action; one shot a turn, same
as melee. **No dice, no shot** - Exerting buys a Parry only.

Nothing is rolled against you. The Shot DC comes off the table, not off a
defender's Parry - a shot is a Tempo roll against a fixed number, not an Exchange.
**DEX gives the target the base number** - a harder target to hit, no roll on their
end - and every situational modifier below stacks on top of it.

| Situation                                                        |            Shot DC            |
|:-----------------------------------------------------------------|:-----------------------------:|
| Within the weapon's first range band                             |       7 + target's DEX        |
| Beyond it, out to the second                                     |             `+3`              |
| Beyond the second range band                                     | Out of range - cannot be shot |
| Light cover (a rail, a low wall, undergrowth, a body in the way) |             `+2`              |
| Target holds a Heater Shield                                     |      `+2` (Light cover)       |
| Heavy cover (a wall, a doorframe)                                |             `+4`              |
| Darkness (see `equipment_draft.md`)                              |      `+4` (Heavy cover)       |
| Total cover                                                      |        Cannot be shot         |
| Target Prone, anywhere but Adjacent                              |             `+2`              |
| Target Engaged in melee                                          |             `+2`              |
| Target Restrained, Prone and Adjacent, or unaware of you         |             `-3`              |
| You are Engaged when you fire (not the Pistolet)                 |             `+4`              |

**Cover never stacks with itself.** Light cover, a Heater Shield, Heavy cover, and Darkness read off the same bucket - take the single highest that applies, never add two together.

**A Shot DC more than 12 over your Skill is impossible** - the GM disallows the shot instead of rolling it, the same ceiling `core_rules.md` sets for every other roll in the game.

**Dice bought against the DC.** A hard shot is a price, not a wall - it costs more
of your round, and leaves less to defend with.

| Shot DC (Skill 3, target DEX 0) | 1 die | 2 dice | 3 dice |
|:--------------------------------|:-----:|:------:|:------:|
| 7 - close, in the clear         |  75%  |  94%   |  98%   |
| 10 - beyond first range band    |  50%  |  75%   |  88%   |
| 11 - close, heavy cover         |  42%  |  66%   |  80%   |
| 14 - long range, heavy cover    |  17%  |  31%   |  42%   |

A target's DEX pushes every row down: the same close shot against a DEX 2 body is
a DC 9, not a 7.

**Shooting into a melee.** If the target is Engaged and you miss by 3 or less, the
shot finds someone else in that fight instead - roll off between the other
combatants, friend or foe, and resolve the damage against them.

**Diving** (off-turn, 1 Tempo Die): when a shot is declared against you and
**before the shooter invests**, spend a die to add `+3` to its Shot DC and end up
Prone in your square (at most 1 die per Parry until you stand). No roll, no
contest. The shooter then invests knowing the higher number - the same
defender-first order as The Exchange. The dive's `+3` already covers the shot it
answers; a later shot against you while still Prone (this turn or next) uses the
normal Prone row instead.

**The movement gate:** spend up to half your Speed (**round down**) in Move and you
may still fire - Speed 5 (Mail) allows 2 squares, not 3. Spend more than that, or
climb, leap, or swim, and you cannot fire this turn. It counts Move *spent*, so
difficult terrain eats into it. Binary, no partial penalty - a couple of weapons
override it below.

**Loaded or Empty.** Track each ranged weapon as one or the other on your character
card. Firing empties it; reloading (below) fills it. No counters, no "ready next
turn" bookkeeping - just a flag. Damage and range for each weapon live in
`equipment_draft.md`.

| Weapon            | Movement to fire      | Reload                                                                    |
|:------------------|:----------------------|:--------------------------------------------------------------------------|
| Shortbow          | Half Move or less     | None - drawing the next arrow is part of firing                           |
| Longbow           | Half Move or less     | None - drawing the next arrow is part of firing                           |
| Light Crossbow    | No gate - move freely | Minor Action, no Move that turn - can't fire and reload the same round    |
| Heavy Crossbow    | No gate - move freely | Minor Action, no Move that turn - can't fire and reload the same round    |
| Pistolet          | No gate - move freely | Major Action, no Move that turn - can't fire and reload in the same round |
| Arquebus          | No gate - move freely | Major Action, no Move that turn - can't fire and reload in the same round |

The Crossbow can fire on the move but must reload standing still next turn; the
Pistolet must stand still just to reload.

**A Loaded weapon carries between scenes** - a fight that catches you already Loaded
needs no reload for your first shot.

**Misfire.** A Firearms weapon jams on **a natural 1 on any die invested in the
shot** - 8% on one die, 16% on two, 23% on three. A bow rewards committing dice; a
gun punishes it. A misfire still spends the Major Action you fired with; clearing
it costs a Major Action + a Minor Action, no earlier than your next turn, and it
can't be fired or reloaded until cleared.

---

## Weapons

**Attacks** sets your Tempo Pool size beyond the baseline (see Tempo Pool, above) - `+1` for a **Light** weapon (any weapon tagged `+1` Attacks in the table below - Unarmed, Dagger, Shortsword), `-1` for a **Two-Handed** one, `+0` for everything else. **Skill** is which Weapon Skill governs the Exchange roll. **Signature** is the Opening that weapon can take on a win by 3 (see Openings). **Damage type** now carries rules weight: Blunt grinds armor down twice as fast, and Normal-Reach Piercing finds the gaps in a pinned foe (see Damage & Armor). Ranged weapons carry an Attacks modifier like any other - every two-handed missile weapon is `-1`, the Pistolet `+0` (see `equipment_draft.md`). A shot spends from the same pool as everything else (see Ranged Attacks, above).

**Full weapon, armor, and shield stats live in `equipment_draft.md`.**

---

## Playtest watchlist

1. **Is Trauma climbing fast enough now that every healed Wound taxes it?** This is now the main inflow, not a rare spike - a decisive win that still drew blood should leave a real mark once the party patches up. If a full expedition still ends in Clear, the problem is upstream (not enough Wounds are landing), not this rule. If it instead blows straight to Critical after one ordinary fight, halve it to 1 Trauma per 2 Wounds healed rather than touching Exerting, which is tuned for its own, rarer trigger, or Nerve, whose own per-trigger inflow is a separate concern (see item 14).
2. **Does the Wound Penalty actually counter-pressure the healing tax?** It's the intended answer to hoarding Wounds to dodge Trauma - staying hurt now costs Checks (Nerve included), not nothing. But it never touches a Tempo roll, so a character who mostly cares about attacks/Parries/shots may still find riding low on Wounds nearly free. If parties still never top off between fights, that gap (Tempo rolls staying untouched) is the first thing to reconsider - not raising the healing tax again.
3. **Do Grapples break too easily?** If the 1-die break makes Grapple pointless, raise it to 2 dice - a number change, not a new rule. Watch this one closely now that Grapple is also the setup for gap-seeking.
4. **Is the Arquebus too reliable?** Misfires now scale with dice invested, so the player who rushes a gun shot is the one who jams it. If that still never bites, let it jam on 1-2 instead of 1.
5. **Does Revelry & Leisure spiral?** It's driven by the Wound Penalty now, not Trauma - so a character can be badly Trauma-shaken and still roll it at full odds, as long as they arrived healed up. The old spiral risk (high Trauma making Trauma harder to remove) is gone by construction; watch instead whether arriving at town still hurt (because healing the last few Wounds wasn't worth the Trauma) now unfairly tanks the whole party's stay.
6. **Is 0-20 still the right size for Trauma now that healing feeds it constantly?** Watch the other direction from before: if an ordinary expedition now blows past Critical on healing alone, before Exerting or a bad Nerve check ever enters into it, widen the track or halve the healing tax (see item 1) rather than touching the rarer sources.
7. **Does the round-refill actually balance Initiative?** Going first commits dice blind; going last means arriving at your attack already bled from defending. Watch for it swinging too far the other way - if acting first stops being an edge at all, that's a problem too.
8. **Is Nerve doing anything now that it tests per trigger?** This is the whole of CHA's combat job, so it has to fire. An ordinary fight should ask once or twice; a fight going badly, three or four times. If it still barely comes up, the half-strength trigger is the one to check first - it's the only one that fires without someone being nearly dead. If every fight ends in a rout before it gets interesting, raise the DC rather than restoring the once-per-fight cap; the cap is what made CHA invisible. **CHA also carries the Resolve check now (see Scars), so a CHA 0 pregen is a real liability on the strategic layer** - watch whether that reads as a meaningful build choice or as a trap the array pushes people into, since `2, 2, 1, 0` guarantees somebody dumps something.
8a. **Does Steady the line flatten CHA, and is that all right?** One CHA 2 character within 3 squares makes everyone else's CHA nearly irrelevant. That's intended - the party gets an ad hoc leader without anyone writing one on a sheet, and it's the reason investing in CHA is visible at the table. Watch that the 3-square leash actually bites: if the party never spreads out far enough to leave the aura, the range is too generous and should come down to 2.
8b. **Does killing the officer read as a tactic or as a surprise?** The rout is supposed to be something the party engineered. If enemy lines collapse and nobody at the table connects it to the man they just dropped, the GM isn't telegraphing him clearly enough - that's a table-practice fix, not a rules one.
8c. **Does the repeat end fights early enough to matter, or does it just formalize a rout that was already happening?** Watch whether it shortens fights the table can feel, or only adds rolls to a mop-up that was already decided. The failure runs both ways: if a side collapses the same round it crosses half strength, DC 7 is too low for a test that now fires every round - raise the repeating test (only) to **DC 9**, leaving the one-shot triggers at 7.
9. **Can a 3-die archer survive being charged?** Dumping every die into a first-round shot leaves nothing to Parry with. If archers open every fight all-in and die for it, raise the Shortbow and Longbow to `+0` Attacks rather than touching the core loop.
10. **Does gap-seeking end armored fights, or just decide them?** Grapple-then-knife should be the answer to a man in plate. If it's the answer to *everything* - if nobody bothers reaching a Dent Line honestly - narrow it further (Downed only) or make the Grapple harder to hold.
11. **Is being Downed now a death sentence?** Any Normal-Reach Piercing weapon reaches a Downed character's gaps, and any Wound kills. If Downed characters never get back up, the 2-Trauma stand-up cost (1 for the Wound, 1 for the danger premium) is moot and the rule needs softening.
12. **Is the Resolve check too forgiving?** Under the old rule a new band was very nearly a guaranteed Scar; now Manageable is a coin-flip at CHA 0 and better above it. If Scars stop appearing at all across a campaign, raise the rungs to 9/11/13 rather than reverting to a flat roll - the check is meant to be a character test, not a formality in either direction. Watch the opposite too: a CHA 0 character limping out of a fight at `-3` Wound Penalty faces a Critical check at 8%, which is close to the old automatic Scar. That's intended, but confirm it lands as consequence rather than as a punishment for one bad array slot.
13. **Does the end-of-fight timing get gamed?** The check reads your band **when the fight ends**, so Mending Touch can shed 2 Trauma in the last round to duck under a rung (see `spells_draft.md`'s watchlist). If that becomes routine, switch to checking against the highest band you reached at any point in the fight - it costs one more thing to remember, which is the only reason it isn't the default.
14. **Does per-trigger Nerve push Trauma too hard?** This adds inflow to a track items 1 and 6 already flag as possibly climbing too fast - a Named character in a bad fight can now fail two or three checks for 2-3 Trauma before any healing happens. Read those three items together, and if the track is blowing out, cut Nerve back to three triggers by dropping the half-strength one rather than halving the healing tax; healing is the deliberate main inflow, this is a side channel.
