_Armor is your primary defense against physical attacks. In Ressam, armor absorbs damage but degrades with each hit \- protection is a finite resource that must be maintained and managed.

**Key Concepts:**

- **Armor Rating/AR:** How much damage your armor absorbs per hit  
- **Penalty:** How much the armor restricts agility, Stealth, and spellcasting  
- **Durability:** Your armor's current condition (starts equal to AR, decreases when hit)
- **Carrying Slots:** Worn armor and an equipped shield cost no Slots. The Slots column applies only to armor or a shield carried as a spare, not currently worn/equipped. A carried Pavise costs 2 Slots regardless of its bulk.

---

## Armor Types

### **Armor Table**

| Armor | AR | Penalty | Price | Slots |
| :---- | :---: | :---: | :---: | :---: |
| **CLOTHING** |  |  |  |  |
| Common Clothes | \- | \- | 10 Crown | 1 |
| Work Clothes | \- | \- | 15 Crown | 2 |
| Travel Clothes | \- | \- | 50 Crown | 2 |
| Fine Clothes | \- | \- | 200 Crown | 2 |
| **FLEXIBLE ARMOR** |  |  |  |  |
| Gambeson | 2 | \-1 | 75 Crown | 2 |
| Buff Coat | 3 | \-1 | 120 Crown | 2 |
| Mail Shirt | 4 | \-2 | 150 Crown | 3 |
| Chain Mail | 5 | \-2 | 200 Crown | 3 |
| Brigandine | 6 | \-3 | 350 Crown | 3 |
| **RIGID ARMOR** |  |  |  |  |
| Breastplate | 6 | \-6 | 700 Crown | 3 |
| Half-Plate | 7 | \-7 | 1,000 Crown | 5 |
| Full Plate | 8 | \-8 | 2,000 Crown | 6 |

###

**Note:** Rigid Armor uses the normal Evasion formula (5 \+ DEX − Armor Penalty) like anything else \- there's no special ban on Agility, DEX, or Dodging. Its Penalty (equal to its full AR, see Armor Penalty below) is what makes it costly, not a separate restriction on top.

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

### **Armor Rating (AR)**

Your AR determines how much damage your armor absorbs from each hit.

**When you're hit by an attack:**

1. Attacker rolls damage
2. Subtract your current AR from the damage
3. Remaining damage (if any) converts to Wounds via the Wound Thresholds (see [[Wounds and Survival|wounds_and_survival]])
4. Your armor loses 1 durability (reducing your AR by 1\)

**Example:** You're wearing brigandine (AR 6). An attacker hits you for 4 damage. Your armor absorbs all 4 damage, but your AR drops to 5\. Next hit, you'll only absorb 5 damage.

### **Armor Penalty**

Penalty represents how armor restricts movement. It applies to:

- **Acrobatics skill checks** (dodging, balance)
- **Stealth skill checks** (moving unseen and unheard)
- **Spellcasting rolls** (both attack rolls and Ward DCs)
- **Evasion and DEX-funded Oppose calculations**

Penalty is derived directly from an armor's AR, not tracked separately: **Rigid armor's Penalty equals its AR**, while **Flexible armor's Penalty is half its AR (rounded down)**. A Rigid piece always costs you something no matter how it's built - that's the tradeoff for wearing plate.

The **Armorer skill** reduces penalty: every rank in Armorer reduces your armor's penalty by 1 (minimum 0).

**Example:** Kira wears Full Plate (Penalty \-8) and has Armorer 5, the maximum. Her effective penalty is still \-3 \- Rigid armor never fully cancels, even at maxed Armorer.

### **Natural Armor**

Natural AR degrades like worn armor unless a creature's entry says otherwise, and regenerates during rests as noted in the creature's description.

---

## Armor Durability

Your armor's durability starts equal to its AR and decreases each time you're hit.

### **Degradation Rules**

- Every successful hit against you reduces your armor's durability by 1  
- Your *current* AR equals your *current* durability  
- Durability cannot drop below 0

### **Degradation Example**

Kira starts a fight wearing chain mail (AR 5, Durability 5).

| Event            |       Damage Taken        | AR After |
|:-----------------|:-------------------------:|:--------:|
| Start            |            \-             |    5     |
| Hit for 4 damage | 0 Wound Damage (absorbed) |    4     |
| Hit for 7 damage |      3 Wound Damage       |    3     |
| Hit for 3 damage | 0 Wound Damage (absorbed) |    2     |
| Hit for 6 damage |      4 Wound Damage       |    1     |

After four hits, her chain mail only provides AR 1\. She's taken 7 Wound Damage, but without armor she'd have taken 20\.

### **Destroyed Armor (0 AR)**

When armor reaches 0 durability, it provides no protection.

- **Flexible armor** can still be field-repaired using the Armorer skill (see Repairing Armor, below) - cloth, leather, and rings can be patched and re-riveted no matter how battered.
- **Rigid armor** cannot be field-repaired once broken. It must be taken to a blacksmith for reforging (see Professional Repair, below).

---

## Repairing Armor

### **Field Repair (Armorer Skill)**

Characters with the Armorer skill can repair armor during downtime, using **Armorer's Tools** (see [[Supplies|supplies]]). Repairing restores **durability equal to your Armorer rank, per hour spent working** (an untrained character, 0 Ranks, restores nothing).

This time can be spent during any Rest (Short, Field, or Long) without losing that Rest's other benefits, or as dedicated downtime outside of a Rest.

**Example:** Kira (Armorer 3) repairs her brigandine (AR 6), currently at 2 durability. At 3 durability per hour, she needs 2 hours - it just fits inside a 2-hour Short Rest, with plenty of room to spare in a Field or Long Rest. A rank 5 master would finish the same repair in under an hour; an untrained companion with the same tools restores nothing.

**Limitations:**

- Cannot restore durability above the armor's original AR  
- Rigid armor cannot be field-repaired once it reaches 0 durability (see Destroyed Armor, above) - only Flexible armor can be repaired from Broken  
- Requires Armorer's Tools and the character's full attention for that time (no other activity during those hours)

### **Professional Repair**

Any armor can instead be taken to a blacksmith for reforging - useful if nobody in the party has Armorer ranks, and mandatory for Rigid armor that's reached 0 durability, which cannot be field-repaired at all:

- **Cost:** Half the armor's original price  
- **Time:** Typically 1-3 days depending on armor complexity  
- **Result:** Fully restores durability to original AR

---

## Donning and Doffing Armor

| Armor Type     |    Don     |         Doff         | Rushed Don |
|:---------------|:----------:|:--------------------:|:----------:|
| Flexible Armor |  1 minute  |     Minor Action     |  5 rounds  |
| Rigid Armor    | 10 minutes | Major + Minor Action |  1 minute  |

**Doffing** is fast regardless of armor type \- shedding armor is a single Action on your turn, provokes no Reactions, and is one-way: you cannot re-don armor mid-combat, only take it off.

---

## Shields

Shields don't add protection the way armor does - instead, they make losing an exchange survivable rather than costly. A shield's whole identity is one number: **Guard**.

### **Shield Table**

| Shield | Guard | Properties | Price | Slots |
| :---- | :---: | :---- | :---: | :---: |
| Buckler | 1 | Keeps full Guard at Grip (see Guard and Measure, below) | 40 Crown | 1 |
| Heater Shield | 2 | \- | 80 Crown | 2 |
| Pavise | 3 | Deployable, \-5 ft speed | 120 Crown | 2 |

### **Shield Descriptions**

**Buckler** is a small fist-held shield used for parrying rather than blocking. Popular in civilian dueling and among those who value mobility. Its Guard is the lowest of the three, but it's the only shield light enough to still do its full work at wrestling range - see Guard and Measure, below.

**Heater Shield** is the iconic knightly shield, shaped like a clothing iron. Solid, dependable coverage for a soldier who still needs to move and swing a weapon. Often bears heraldic devices.

**Pavise** is a large rectangular shield originally designed to protect crossbowmen while reloading, offering the most Guard of any shield.  
**Major Action:** Can be Deployed as standing cover, providing Cover to one creature directly behind it. The user cannot move while the shield is Deployed, but is also counted as in Cover.

### **Using Shields**

Guard requires a shield equipped in one hand - since a shield occupies a hand, it's only ever paired with a one-handed weapon (or nothing) in the other, never a Two-Handed weapon.

Guard is passive: it applies whenever you have a shield equipped, regardless of which Skill funds your Oppose roll (see [[Oppose|maneuvers]]) - a shield strapped to your arm still catches a blow whether you're actively trained to use it or not.

**Guard and Measure:** A shield is an obstruction, not protection, once someone's inside it - Guard drops by 2 (minimum 0) whenever the current measure is Grip, except the Buckler, small enough to still do its full work that close in.

**Guard and Control:** While an opponent has Control on you (see [[Oppose|maneuvers]]), your Guard is 0 against them - your shield's been hooked, pinned, or pressed out of line, until you spend a win clearing it.

### **Shield Durability**

Shields share durability with your armor - they don't track separately. A shield's Guard degrades by 1 each time it actually reduces a losing Oppose margin (see [[Oppose|maneuvers]]) - a won exchange never touches the shield, so Guard only wears down at the moment it does its job. Guard cannot drop below 0, and is restored by the same Armorer repair rules as armor (see Repairing Armor, above) - when you repair your armor, you repair your equipped shield's Guard simultaneously.

---

## Armor Selection Guide

### **By Character Role**

| Role | Recommended Armor | Why |
| :---- | :---- | :---- |
| **Melee Fighter** | Brigandine or Breastplate | High AR; Breastplate's Rigid Penalty (equal to its full AR) is steep, but Evasion still scales normally |
| **Archer/Crossbowman** | Gambeson or Buff Coat | Low penalty for aiming |
| **Spellcaster** | None or Gambeson | Penalty hurts spellcasting |
| **Skirmisher/Scout** | Gambeson | Low penalty keeps Stealth usable |
| **Tank** | Full Plate \+ Pavise | Maximum AR, and the highest Guard to soften whatever gets through anyway |
| **Duelist** | Buff Coat \+ Buckler | Mobility, and a shield whose Guard still works at Grip range |

### 

### **The Protection vs. Penalty Tradeoff**

Higher AR means better damage absorption but worse:

- Evasion (harder to be missed)  
- Oppose funded by DEX (harder to actively evade)  
- Spellcasting (lower attack rolls and Ward DCs)  
- Stealth (harder to move unseen and unheard)

**Martial characters** generally favor higher AR \- they rely on armor to survive, not evasion.

**Spellcasters** favor low or no armor \- penalty directly reduces their effectiveness.

**Hybrid characters** often choose brigandine \- high AR (6) with only \-3 penalty.
