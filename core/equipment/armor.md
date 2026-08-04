Armor is your primary defense against physical attacks. In Ressam, armor absorbs damage but degrades with each hit \- protection is a finite resource that must be maintained and managed.

**Key Concepts:**

- **Armor Rating/AR:** How much damage your armor absorbs per hit  
- **Penalty:** How much the armor restricts agility and spellcasting  
- **Stealth:** How much the armor restricts Stealth rolls and checks  
- **Durability:** Your armor's current condition (starts equal to AR, decreases when hit)
- **Carrying Slots:** Worn armor and an equipped shield cost no Slots. The Slots column applies only to armor or a shield carried as a spare, not currently worn/equipped. A carried Pavise costs 2 Slots regardless of its bulk.

---

## Armor Types

### **Armor Table**

| Armor | AR | Penalty | Stealth | Price | Slots |
| :---- | :---: | :---: | :---: | :---: | :---: |
| **CLOTHING** |  |  |  |  |  |
| Common Clothes | \- | \- | \- | 10 Crown | 1 |
| Work Clothes | \- | \- | \- | 15 Crown | 2 |
| Travel Clothes | \- | \- | \- | 50 Crown | 2 |
| Fine Clothes | \- | \- | \- | 200 Crown | 2 |
| **FLEXIBLE ARMOR** |  |  |  |  |  |
| Gambeson | 2 | \-1 | \- | 75 Crown | 2 |
| Buff Coat | 3 | \-1 | \- | 120 Crown | 2 |
| Mail Shirt | 4 | \-2 | \-2 | 150 Crown | 3 |
| Chain Mail | 5 | \-2 | \-3 | 200 Crown | 3 |
| Brigandine | 6 | \-3 | \-1 | 350 Crown | 3 |
| **RIGID ARMOR** |  |  |  |  |  |
| Breastplate | 6 | \-6 | \-2 | 700 Crown | 3 |
| Half-Plate | 7 | \-7 | \-3 | 1,000 Crown | 5 |
| Full Plate | 8 | \-8 | \-4 | 2,000 Crown | 6 |

###

**Note:** Rigid Armor uses the normal Evasion formula (5 \+ Agility \+ DEX − Armor Penalty) like anything else \- there's no special ban on Agility, DEX, or Dodging. Its Penalty (equal to its full AR, see Armor Penalty below) is what makes it costly, not a separate restriction on top.

### **Armor Descriptions**

**Clothing** provides no protection but carries no penalty. Some do provide benefits:

- **Work Clothes:** \+2 to checks with Artisan's Tools or Professional Equipment.  
- **Travel Clothes:** Consume rations every 2 days instead of daily.  
- **Fine Clothes:** \+2 to skills utilizing your Charisma.

**Gambeson** is a padded jacket of quilted linen or wool, worn alone or under heavier armor. Affordable, lightweight, and surprisingly effective against cuts. The most common armor among common soldiers and militia.

**Buff Coat** is a thick coat of buffalo or ox leather, popular among cavalry and officers. Offers slightly better protection than gambeson while remaining flexible.

**Mail Shirt** covers the torso with interlocking metal rings. Lighter than full chain mail but leaves the arms and legs exposed.

**Chain Mail** is a full hauberk of interlocking rings covering torso and arms, often with a coif. Excellent against slashing weapons, less effective against thrusts and crushing blows. The distinctive jingle makes stealth difficult.

**Brigandine** consists of small steel plates riveted inside a cloth or leather covering. Popular among mercenaries and men-at-arms \- offers near-plate protection at lower cost, and the fabric exterior makes less noise than exposed metal.

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
3. Remaining damage (if any) converts to Wounds via the Wound Thresholds (see [[Wounds and Survival|core_rules]])
4. Your armor loses 1 durability (reducing your AR by 1\)

**Example:** You're wearing brigandine (AR 6). An attacker hits you for 4 damage. Your armor absorbs all 4 damage, but your AR drops to 5\. Next hit, you'll only absorb 5 damage.

### **Armor Penalty**

Penalty represents how armor restricts movement. It applies to:

- **Agility skill checks** (dodging, acrobatics, balance)
- **Stealth skill checks** (if armor has a Stealth penalty)
- **Spellcasting rolls** (both attack rolls and Ward DCs)
- **Evasion and Dodge calculations**

Penalty is derived directly from an armor's AR, not tracked separately: **Rigid armor's Penalty equals its AR**, while **Flexible armor's Penalty is half its AR (rounded down)**. A Rigid piece always costs you something no matter how it's built - that's the tradeoff for wearing plate.

The **Armorer skill** reduces penalty: every rank in Armorer reduces your armor's penalty by 1 (minimum 0).

**Example:** Kira wears Full Plate (Penalty \-8) and has Armorer 5, the maximum. Her effective penalty is still \-3 \- Rigid armor never fully cancels, even at maxed Armorer.

### **Stealth Penalty**

Some armor imposes an *additional* penalty specifically to Stealth checks. This stacks with the normal penalty.

**Example:** Chain mail has Penalty \-2 and Stealth \-3. A character with no Armorer skill takes \-5 total to Stealth checks while wearing it.

Brigandine notably has no Stealth penalty despite its protection \- the fabric exterior muffles the metal plates within.

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

| Event | Damage Taken | AR After |
| :---- | :---: | :---: |
| Start |  \-  | 5 |
| Hit for 4 damage | 0 Wound Damage (absorbed) | 4 |
| Hit for 7 damage | 3 Wound Damage | 3 |
| Hit for 3 damage | 0 Wound Damage (absorbed) | 2 |
| Hit for 6 damage | 4 Wound Damage | 1 |

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

| Armor Type | Don | Doff | Rushed Don |
| :---- | :---: | :---: | :---: |
| Gambeson/Buff Coat | 1 minute | 1 Action | 5 rounds |
| Mail Shirt/Chain Mail/Brigandine | 5 minutes | 1 Action | 1 minute |
| Rigid Armor | 10 minutes | 1 Action | 3 minutes |

**Doffing** is fast regardless of armor type \- shedding armor is a single Action on your turn, provokes no Reactions, and is one-way: you cannot re-don armor mid-combat, only take it off.

**Help:** Another character can reduce don time by half if they have Armorer 1+.

---

## Shields

Shields provide active and passive defenses.

### **Shield Table**

| Shield | AR Bonus | Penalty | Properties | Price | Slots |
| :---- | :---: | :---: | :---: | :---: | :---: |
| Buckler | \- | \- | \+1 Agility | 40 Crown | 1 |
| Targe | \+1 | \- | \- | 60 Crown | 2 |
| Rotella | \+2 | \-1 | \- | 90 Crown | 2 |
| Heater Shield | \+2 | \-1 | \- | 80 Crown | 2 |
| Kite Shield | \+3 | \-2 | \- | 100 Crown | 2 |
| Pavise | \+4 | \-3 | Deployable, \-5 ft speed | 120 Crown | 2 |

### 

### **Shield Descriptions**

**Buckler** is a small fist-held shield used for parrying rather than blocking. Popular in civilian dueling and among those who value mobility. Grants \+1 to Agility skill (affecting Evasion and your Dodge Style roll) but has no AR Bonus, so it reduces nothing on a Block Style Minimized result.

**Targe** is a small round shield gripped or strapped to the forearm. Common among skirmishers and those who need a free hand. Offers modest protection without hindering movement.

**Rotella** is the classic round shield, popular among infantry and duelists. Good balance of protection and mobility.

**Heater Shield** is the iconic knightly shield, shaped like a clothing iron. Provides solid coverage while remaining maneuverable. Often bears heraldic devices.

**Kite Shield** is a large teardrop-shaped shield offering excellent coverage, especially for mounted combat. The extended lower portion protects the legs.

**Pavise** is a large rectangular shield originally designed to protect crossbowmen while reloading.  
**Major Action:** Can be Deployed as standing cover, providing Cover to one creature directly behind it. The user cannot move while the shield is Deployed, but is also counted as in Cover.

### **Using Shields**

**Blocking** requires:

- A shield equipped in one hand  
- Your Reaction for the round

Block is one Style of the Maneuver Reaction (see [[Combat|combat]]) - on a Minimized result, your shield's AR Bonus reduces the incoming damage. Whether the attack is Dominant, Stopped, Minimized, or Failed, your armor and shield degrade as normal.

**Buckler Exception:** The buckler grants no AR Bonus, so it reduces nothing on a Block Style Minimized result. Its benefit is the passive \+1 to Agility, which improves your Evasion and Dodge Style roll instead.

### **Shield Durability**

Shields share durability with your armor \- they don't track separately.

**Reasoning:** The shield's AR bonus temporarily increases your total AR. When an attack hits despite your block, the impact damages whatever absorbed the blow \- armor and shield together take the wear.

When repairing armor, you repair the shield simultaneously.

---

## Armor Selection Guide

### **By Character Role**

| Role | Recommended Armor | Why |
| :---- | :---- | :---- |
| **Melee Fighter** | Brigandine or Breastplate | High AR; Breastplate's Rigid Penalty (equal to its full AR) is steep, but Evasion still scales normally |
| **Archer/Crossbowman** | Gambeson or Buff Coat | Low penalty for aiming |
| **Spellcaster** | None or Gambeson | Penalty hurts spellcasting |
| **Skirmisher/Scout** | Gambeson | Stealth-compatible |
| **Tank** | Full Plate \+ Shield | Maximum protection |
| **Duelist** | Buff Coat \+ Buckler | Mobility \+ Agility bonus |

### 

### **The Protection vs. Penalty Tradeoff**

Higher AR means better damage absorption but worse:

- Evasion (harder to be missed)  
- Dodge (harder to actively evade)  
- Spellcasting (lower attack rolls and Ward DCs)  
- Stealth (some armor only)

**Martial characters** generally favor higher AR \- they rely on armor to survive, not evasion.

**Spellcasters** favor low or no armor \- penalty directly reduces their effectiveness.

**Hybrid characters** often choose brigandine \- high AR (6) with only \-3 penalty and no Stealth penalty.
