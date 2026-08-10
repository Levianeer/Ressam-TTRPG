Combat in Ressam is lethal. Armor breaks, injuries accumulate, and death is always one bad decision away. This chapter covers everything from initiative to dying \- read it carefully.

Ressam is not a game where heroes fight to the last Wound. You won't fight worse for being hurt \- the Wound Penalty only bites outside combat \- but a small pool empties fast, and a big hit can take two or three Wounds at once. When you've lost half your Wounds, consider tactical withdrawal. Near 0, retreat should be your priority. There is no shame in living to fight another day.

---

## Initiative

**Initiative \= 1d12 \+ ((PRE \+ DEX) ÷ 2\)**

Actions resolve highest to lowest each round.

**Ties:** Higher DEX goes first. If still tied, roll 1d12.

**Changing Initiative:** Fixed for combat unless modified by ability, or you voluntarily swap with another PC (once per combat, both must agree).

---

## Action Economy

| Action Type | Quantity | Examples                                                       |
| :---- | :---- |:---------------------------------------------------------------|
| **Major Action** | 1/round | Attack, cast spell, reload weapon, Dash, Disengage              |
| **Minor Action** | 1/round | Sheathe weapon, drink potion, open door, Shift Measure          |
| **Object Interaction** | 1/round | Draw ammunition, pick up weapon, flip lever                    |
| **Reaction** | 1-3, scales with DEX (see below) | Held Action, Oppose, Reactive Casting, Opportunity Attack |
| **Free Action** | Unlimited | Drop item, speak briefly, stop channeling, etc                 |
| **Move Action** | Unlimited | Move up to your maximum speed, can be broken up into multiples |

- **Per Round:** Refreshes at the start of your *next* turn  
- **Reactions:** Usable on anyone's turn
- **Drawing multiple weapons:** As a single Object Interaction, you may draw any number of weapons at once, provided you have a free hand for each one.
- **Reactions/round scales with DEX:**

  | DEX | Reactions |
  | :---: | :---: |
  | 0-2 | 1 |
  | 3-4 | 2 |
  | 5 | 3 |

  Recalculate whenever DEX changes (leveling, injury, equipment). Even a character who dumps DEX keeps 1 Reaction \- worse at Opposing than someone who invested, but never locked out of Oppose, Reactive Casting, or Opportunity Attacks entirely. A 3rd Reaction requires DEX 5, unreachable before level 8+.
- **Reactions are a single shared pool:** Oppose, Reactive Casting, and Opportunity Attacks all draw from the same pool above \- and so does every other Reaction-based Feat or spell you have (Ward of Faith, Dominating Stare, and the like). They compete for your Reactions, they do not stack. Only an effect that explicitly grants an additional Reaction (Combat Reflexes and the like) increases this pool.

---

## Making an Attack

### **Attack Roll**

**1d12 \+ Weapon Skill vs. Target's Evasion**

An untrained attack rolls **1d12** alone.

### **Damage Roll**

**Weapon Damage \+ associated Attribute − Target's AR \= Wound Damage**

Damage ≤ AR deals 0 Wound damage but still degrades armor by 1\.

---

## Held Action

On your turn, you may spend your Major Action to ‘Hold’ an action. Declare a perceivable circumstance as the trigger, and choose a response: any Major Action (attack, spell, Dash, Disengage) or Move up to your speed.

When the trigger occurs before your next turn, use your Reaction to execute the response immediately after the trigger finishes \- or ignore it. If the trigger doesn't occur, the action is lost.

**Held Action with Spells**: You begin the casting process but must hold concentration, this counts as channelling. If concentration breaks, the spell dissipates (Mana is lost). Released on your specified trigger.

---

## Ready Volley

Hold a ranged shot on a chosen lane, ready to loose it the instant your trigger is met - the setup melee gets for free just by having a weapon in hand, ranged weapons pay for with a turn.

**Trigger:** Any perceivable circumstance you declare, same as a normal Held Action, above - an enemy entering your line of sight or your weapon's Range, closing to melee, breaking cover, attacking an ally, and so on.  
**Action:** Major Action to set (this is a Held Action), Reaction to release (shared pool, see Action Economy, above - this competes with Oppose and Opportunity Attacks for the same Reaction).  
**Prerequisites:** A loaded ranged weapon in hand. A firearm must already be loaded before you set the trigger - Ready Volley holds the shot, not the reload.  
**Roll:** Your normal attack roll (Weapon Skill), unless you're making a Called Shot below.

If your trigger doesn't occur before your next turn, the action is lost, same as any Held Action.

### **Called Shot**

When your Ready Volley fires, you may aim for more than center mass instead of a normal hit. Declare your zone before you roll - this option only exists because you took the time to aim; a snapped-off attack on your own turn doesn't give you that choice.

| Zone              | Penalty | On Hit                                                                                                                                   |
|:------------------|:-------:|:------------------------------------------------------------------------------------------------------------------------------------------|
| Torso *(default)* |   \-    | Normal damage, no additional effect.                                                                                                     |
| Legs              |   \-2   | Speed becomes half until the end of their next turn. Aim Margin \+3 or higher: they are knocked Prone instead.                           |
| Arms              |   \-2   | Their next attack roll before your next turn has Disadvantage. Aim Margin \+3 or higher: they drop one held item of your choice instead. |
| Head              |   \-4   | This attack ignores the target's AR entirely.                                                                                            |

**Aim Margin \= Your attack roll − the target's Evasion** - the same numbers you already rolled to resolve the hit, no extra roll needed. This is a different quantity from an Oppose's Margin (see [[Oppose|maneuvers]]): there's no tier table here, only the \+3 threshold above.

---

## Critical Hits

Critical Hits occur on a **Natural 12** on attack rolls.

**Effects:**

- **Roll damage twice, take the higher result.**  
- Bypasses an Oppose roll funded by Weapon Skill or Shields Skill entirely - the attack simply hits, and no Reaction is spent attempting it (an Oppose roll funded by Evasion Skill is unaffected - see [[Oppose|maneuvers]])

Crits don't grant Trauma \- their pressure is indirect, since rolling twice raises the odds of landing in a higher Wound tier (see [[Wounds and Survival|wounds_and_survival]]).

**Expanded Crit Range:** Some weapons crit on 11-12, 10-12 or even 9-12.  
Features and Feats can expand this further.

**Spells:** Arcane Spell Attack rolls can crit; Arcane Spell Overcome rolls cannot. Divine's Petition Roll never crits - it's binary by design (see [[Magic Overview|magic_overview]]'s Petition Roll).

---

## Evasion

Evasion, or ‘Passive Evasion’ is your trained ability to stay out of harm's way. This requires no setup or actions, it happens automatically against attack rolls.

**Evasion \= 5 \+ Evasion Skill Ranks − Armor Penalty**

---

## Armor

Armor is just that, your worn armor, it protects a flat amount of damage passively, but degrades each time you are hit, successfully or not.

### **Armor Rating**

When hit:

1. Subtract AR from damage  
2. Armor loses 1 AR (degradation)  
3. Remaining damage converts to Wounds (see [[Wounds and Survival|wounds_and_survival]])

**Note:** A Critical Hit can still deal 0 Wound damage against fresh, heavy armor \- that's coherent with the armor fiction, not a bug.

### **Degradation**

Every hit (regardless of Wound damage) reduces armor by 1 AR.

| AR Status | Effect |
| :---- | :---- |
| AR 1+ | Functions normally |
| AR 0 | **Broken** \- no protection |

**Broken Armor:** Rigid armor cannot be field-repaired once broken and must be reforged by a blacksmith (1/2 of original price); Flexible armor can still be field-repaired. See [[Armor|armor]] for full repair rules.

### **Armor Penalty**

Reduces Evasion, your Evasion Skill-funded Oppose roll ([[Oppose|maneuvers]]), and your Spell Modifier.

**Reducing Penalty:** Each rank in Armorer reduces Penalty by 1 (minimum 0).

---

## Continued In

[[Positioning|positioning]] covers Battlemap & Positioning, Reach, Movement in Combat, Opportunity Attacks, Surprise, and Cover. [[Wounds & Survival|wounds_and_survival]]'s Conditions section covers Bleeding, Blinded, Prone, and the rest of the status-effect list. [[Bestiary Overview|bestiary_overview]]'s Mythic Initiative section covers campaign-boss creatures that take multiple turns per round.
