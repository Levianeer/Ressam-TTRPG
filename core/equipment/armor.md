_Armor is your primary defense against physical attacks. In Ressam, armor absorbs damage but degrades with each hit \- protection is a finite resource that must be maintained and managed.

**Key Concepts:**

- **Dent Line / Rend Line:** The two numbers printed on your armor. A landing hit rolls weapon damage and compares the total against them - see Dent Line and Rend Line, below.
- **Penalty:** How much the armor restricts agility and Subterfuge  
- **Durability:** Your armor's current condition (starts equal to its Dent Line, decreases when hit \- both printed numbers fall together as it drops)
- **Carrying Armor:** worn or carried as a spare, every suit of actual armor (Flexible and Rigid, below) costs **1 Slot**, the same as any other spare gear (see [[Carrying Capacity|rest_and_survival]]; see [[Weapons|weapons]] for shields) - your equipped suit is free. Clothing costs 1 Slot too, cloth being cloth.

---

## Armor Types

### **Armor Table**

| Armor | Dent | Rend | Penalty | Price | Slots |
| :---- | :---: | :---: | :---: | :---: | :---: |
| **CLOTHING** |  |  |  |  |  |
| Common Clothes | \- | \- | \- | 10 Crown | 1 |
| Work Clothes | \- | \- | \- | 15 Crown | 1 |
| Travel Clothes | \- | \- | \- | 50 Crown | 1 |
| Fine Clothes | \- | \- | \- | 200 Crown | 1 |
| **FLEXIBLE ARMOR** |  |  |  |  |  |
| Gambeson | 3 | 7 | \-1 | 75 Crown | 1 |
| Buff Coat | 4 | 8 | \-1 | 120 Crown | 1 |
| Mail Shirt | 5 | 9 | \-1 | 150 Crown | 1 |
| Chain Mail | 6 | 10 | \-2 | 200 Crown | 1 |
| Brigandine | 7 | 11 | \-2 | 350 Crown | 1 |
| **RIGID ARMOR** |  |  |  |  |  |
| Breastplate | 7 | 11 | \-2 | 700 Crown | 1 |
| Half-Plate | 8 | 12 | \-2 | 1,000 Crown | 1 |
| Full Plate | 9 | 13 | \-3 | 2,000 Crown | 1 |

**Note:** Nothing in a fight reads Armor Penalty \- see [[The Exchange|exchange]]. **Once swords are out, your Dent and Rend Lines are the whole of what armor does**, and heavier is simply better. What holds plate in check is 2,000 Crown, Stealth, and the reasons people did not sleep in harness \- none of which is a combat rule, and all of which are real. A spare suit of Full Plate costs the same 1 Slot as a Gambeson - one more thing you can't afford, not one that physically won't fit.

**Breastplate against Brigandine** is the clearest read of the table: identical Dent/Rend Lines and identical Penalty, at twice the price and the same 1 Slot. What the extra 350 Crown buys is the Rigid label \- a cuirass shrugs off a blow it stops, and a coat of plates gets cut apart doing the same job (see Rigid Armor and Absorbed Blows, below).

### **Armor Descriptions**

**Clothing** provides no protection but carries no penalty. Some do provide benefits:

- **Work Clothes:** \+1 to checks with Artisan's Tools or Professional Equipment.  
- **Travel Clothes:** Consume rations every 2 days instead of daily.  
- **Fine Clothes:** \+1 to skills utilizing your Charisma.

**Gambeson** is a padded jacket of quilted linen or wool, worn alone or under heavier armor. Affordable, lightweight, and surprisingly effective against cuts. The most common armor among common soldiers and militia.

**Buff Coat** is a thick coat of buffalo or ox leather, popular among cavalry and officers. Offers slightly better protection than gambeson while remaining flexible.

**Mail Shirt** covers the torso with interlocking metal rings. Lighter than full chain mail but leaves the arms and legs exposed.

**Chain Mail** is a full hauberk of interlocking rings covering torso and arms, often with a coif. Excellent against slashing weapons, less effective against thrusts and crushing blows.

**Brigandine** consists of small steel plates riveted inside a cloth or leather covering. Popular among mercenaries and men-at-arms \- offers near-plate protection at lower cost.

**Breastplate** is a fitted steel chest and back plate, typically worn over mail or gambeson. Standard equipment for professional soldiers and knights. The polished surface can deflect glancing blows.

**Half-Plate** extends the breastplate with articulated plates protecting shoulders, arms, and thighs, while leaving joints covered by mail. Sometimes called "three-quarter armor."

**Full Plate** is a complete harness of articulated steel covering the entire body. The pinnacle of the armorer's art. Extraordinarily expensive and requires professional fitting. Knights and wealthy nobles wear full plate; common soldiers do not.

---

## Understanding Armor Stats

### **Dent Line and Rend Line**

Your armor prints two numbers - **Dent Line** and **Rend Line** - and a landing hit is read straight off them.

**When you're hit by an attack:**

1. Attacker rolls their weapon's damage dice, summed, `\+ STR` (missiles: no Attribute added) \- see [[Damage Roll|combat]]
2. Compare the total to your current Dent Line and Rend Line \- or Dent 0 / Rend 5 if unarmored: below Dent, the blow is **Turned Aside** (no Wound); at or above Dent, **1 Wound**; at or above Rend, **2 Wounds**
3. If every die in the roll came up its maximum face, the blow **found a gap** \- see below
4. Your armor loses durability \- see Armor Durability, below

**Found a gap:** rolling maximum on every die is a fixed die-face outcome, not a reward for winning the Exchange by more (there are still no critical hits, see [[There are no critical hits|exchange]]). If the roll would have been Turned Aside, it lands for 1 Wound instead. If it already scored a Wound on its own, it instead applies **Bleeding** (see [[Conditions|rest_and_survival]]) on top of whatever it already dealt.

**Example:** You're wearing brigandine (Dent 7, Rend 11). An attacker's Longsword rolls `1d6 \+ 2 \+ STR 3` and comes up 9 \- at or above your Dent Line but below your Rend Line, so you take 1 Wound. Your armor loses 1 durability, dropping both lines to 6/10 for the next hit.

### **Armor Penalty**

Penalty represents how armor restricts movement. It applies to:

- **Acrobatics skill checks** (balance, tumbling, controlled falls)
- **Subterfuge skill checks** (moving unseen and unheard)

**2026-09-14: Penalty no longer touches spellcasting.** The new unified casting roll (see [[Magic Overview|magic_overview]]) carries no modifier - Skill, Attribute, or Armor Penalty - for it to reduce; a caster's only cost from armor is Slots and price, same as anyone else.

**It applies to nothing in a fight.** No attack roll, no Parry, no Tempo Die reads it (see [[The Exchange|exchange]]) \- Penalty is a cost you pay everywhere except the one place armor is doing its job.

Penalty is derived directly from an armor's Dent Line, not tracked separately, in bands of three:

| Dent Line | Penalty |
| :----: | :----: |
| 3-5 | \-1 |
| 6-8 | \-2 |
| 9-11 | \-3 |

**All armor carries some Penalty**, and the Rigid/Flexible split does not change it \- a cuirass and a coat of plates at the same Dent/Rend Lines restrict you the same amount, whatever else separates them.

**Nothing reduces Penalty.** No Skill and no Feat buys it back: a three-point axis has no room for a repeatable purchase, and Penalty no longer prices anything worth a Feat slot now that no combat rule consults it. If you want a smaller Penalty, wear lighter armor.

### **Natural Armor**

A natural Dent/Rend Line pair degrades like worn armor unless a creature's entry says otherwise, and regenerates during rests as noted in the creature's description.

---

## Armor Durability

Your armor's durability starts equal to its Dent Line and decreases each time you're hit. **Both printed lines fall together, 1 for 1, keeping the same 4-point gap between them** \- a Gambeson worn down 2 durability from 3/7 reads 1/5 for its next hit.

### **Degradation Rules**

- A hit that scores a Wound reduces your armor's durability by **1**
- A hit **Turned Aside** reduces Flexible armor's durability by **1** and Rigid armor's by **0** \- see Rigid Armor and Absorbed Blows, below
- A **Blunt** hit costs **2** instead of 1, whenever it would cost anything (**Unarmed** is the exception, at 1) \- see [[Damage Types|rest_and_survival]]
- Durability cannot drop below 0

### **Rigid Armor and Absorbed Blows**

> **A Turned Aside blow costs Flexible armor 1 durability and costs Rigid armor nothing.**

This is the whole of what the Rigid/Flexible label does while the fighting is on, and it is the other half of the bargain Destroyed Armor strikes below. **Rigid wears slowly and fails hard** \- a cuirass shrugs off what it stops, but once it is driven to 0 it wants a blacksmith and a forge. **Flexible wears fast and always comes back** \- it loses a point to every hit, and it can be patched up in the field even from Broken. One is for a man with a baggage train and one is for a man without.

A blow that scores a Wound degrades both kinds by the normal amount. The exemption is only for the blow armor turns aside entirely.

### **Degradation Example**

Kira starts a fight wearing chain mail (Dent 6, Rend 10, Durability 6).

| Event                 |     Result      | Lines After |
|:----------------------|:----------------:|:-----------:|
| Start                 |         \-        |    6 / 10   |
| Hit totals 4          | Turned Aside     |    5 / 9    |
| Hit totals 11         | 2 Wounds         |    4 / 8    |
| Hit totals 3          | Turned Aside     |    3 / 7    |
| Hit totals 9          | 1 Wound          |    2 / 6    |

After four hits, her chain mail has fallen to 2/6\. She's taken 3 Wounds, but unarmored (Dent 0 / Rend 5) she'd have taken 6 against those same four totals \- every one of them is at least 1 Wound, and the 11 and 9 both clear Rend for 2.

**Had she been wearing a Breastplate instead**, the two Turned Aside hits would have cost her nothing at all \- Rigid armor doesn't wear when it wins \- and she'd have finished the same four hits at 5/9.

### **Destroyed Armor (0 Durability)**

When armor reaches 0 durability, it provides no protection \- the wearer resolves every landing hit as **Unarmored** (Dent 0 / Rend 5, see [[Damage Roll|combat]]) rather than reading a bottomed-out 0/4 pair of lines.

- **Flexible armor** can still be repaired from Broken \- cloth, leather, and rings can be patched and re-riveted no matter how battered.
- **Rigid armor** cannot be repaired in the field once broken. It must be taken to a blacksmith for reforging (see Professional Repair, below).

---

## Repairing Armor

**2026-09-20:** field repair is now purely a function of [[Rest \& Repair|rest_and_survival]] \- a Field Rest restores 1 point to each printed line (Dent, Rend, and an equipped shield's Guard), a Long Rest restores 1, or 2 if a smith passes a Smithing check (DC 7) that day. **Repair never exceeds the armor's original printed values.** The old hourly Crafting-rank repair system is gone; Crafting no longer funds armor repair on its own.

### **Professional Repair**

Any armor can instead be taken to a blacksmith for reforging \- faster than waiting out the Rest ladder, and mandatory for Rigid armor that's reached 0 durability, which cannot be repaired by resting at all:

- **Cost:** Half the armor's original price
- **Time:** Typically 1-3 days depending on armor complexity
- **Result:** Fully restores durability, and both printed lines, to their original values

---

## Donning and Doffing Armor

| Armor Type     |    Don     |         Doff         | Rushed Don |
|:---------------|:----------:|:--------------------:|:----------:|
| Flexible Armor |  1 minute  |     Minor Action     |  5 rounds  |
| Rigid Armor    | 10 minutes | Major + Minor Action |  1 minute  |

**Doffing** is fast either way \- the table above is the whole of it (a Minor Action for Flexible, a Major \+ Minor for Rigid). It provokes no Opportunity Attack, costs no Tempo Die, and is one-way: you cannot re-don armor mid-combat, only take it off.

---

## Armor Selection Guide

### **By Character Role**

| Role | Recommended Armor | Why |
| :---- | :---- | :---- |
| **Melee Fighter** | Brigandine or Breastplate | High Dent/Rend Lines at the same \-2 Penalty; the Breastplate costs twice as much and buys the Rigid absorb rule with it |
| **Archer/Crossbowman** | Gambeson or Buff Coat | Cheap, light, and \-1 Penalty; nothing you do with a bow reads armor's lines either way |
| **Spellcaster** | Whatever suits the rest of the build | Penalty no longer touches spellcasting - a caster picks armor the same way anyone else does, off Slots and price alone |
| **Skirmisher/Scout** | Gambeson | Low penalty keeps Subterfuge usable |
| **Tank** | Full Plate \+ Heater Shield | Highest Dent/Rend Lines in the book, and \+2 Guard on every Parry you make |
| **Duelist** | Buff Coat \+ Buckler | Mobility, and a fist-held shield you can keep on the hand while you reload or work a lock |

### 

### **The Protection vs. Penalty Tradeoff**

Higher Dent and Rend Lines mean a tougher blow to land at all but worse:

- Acrobatics (balance, tumbling, controlled falls)
- Subterfuge (harder to move unseen and unheard)

**And that is the entire list.** Nothing inside a fight is on it, and spellcasting is no longer on it either. **Martial characters** should wear the heaviest thing they can afford and carry, because in combat there is no counterweight at all \- armor is the only protection you don't have to spend a Tempo Die on.

**Spellcasters** have no mechanical reason to avoid armor anymore \- pick it the same way a Martial does, off Slots, price, and Acrobatics/Subterfuge if those matter to the build.

**Hybrid characters** often choose brigandine \- Dent 7 / Rend 11 at only \-2 penalty, the best ratio on the table.
