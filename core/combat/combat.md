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
| **Major Action** | 1/round | Attack, cast spell, reload weapon, Dash, Disengage, Dodge      |
| **Minor Action** | 1/round | Sheathe weapon, drink potion, open door                        |
| **Object Interaction** | 1/round | Draw ammunition, pick up weapon, flip lever                    |
| **Reaction** | (DEX \+ PRE) ÷ 3, rounded down | Held Action, Maneuver (Parry/Block/Dodge), Reactive Casting, Opportunity Attack |
| **Free Action** | Unlimited | Drop item, speak briefly, stop channeling, etc                 |
| **Move Action** | Unlimited | Move up to your maximum speed, can be broken up into multiples |

- **Per Round:** Refreshes at the start of your *next* turn  
- **Reactions:** Usable on anyone's turn
- **Drawing multiple weapons:** As a single Object Interaction, you may draw any number of weapons at once, provided you have a free hand for each one.
- **Reactions/round \= (DEX \+ PRE) ÷ 3, rounded down.** Recalculate whenever DEX or PRE changes (leveling, injury, equipment). A low enough total rounds down to 0 \- a character who dumps both DEX and PRE cannot Parry, Dodge, Hold an Action, cast reactively, or make an Opportunity Attack at all.
- **Reactions are a single shared pool:** Maneuver (in any of its Parry, Block, or Dodge Styles), Reactive Casting, and Opportunity Attacks all draw from the same pool above \- and so does every other Reaction-based Feat or spell you have (Stress Inoculation, Ward of Faith, Dominating Stare, and the like). They compete for your Reactions, they do not stack. Only an effect that explicitly grants an additional Reaction (Combat Reflexes and the like) increases this pool.

---

## Making an Attack

### **Attack Roll**

**1d12 \+  Weapon Skill \+ Attribute vs. Target's Evasion**

**Trained:** As with all Skill-based rolls, the Attribute only applies once you have 1 or more ranks in the Weapon Skill used ([[Skill Check Formula|core_rules]]). An untrained attack rolls **1d12** alone.

### **Damage Roll**

**Weapon Damage \+ associated Attribute − Target's AR \= Wound Damage**

Damage ≤ AR deals 0 Wound damage but still degrades armor by 1\.

---

## Held Action

On your turn, you may spend your Major Action to ‘Hold’ an action. Declare a perceivable circumstance as the trigger, and choose a response: any Major Action (attack, spell, Dash, Disengage) or Move up to your speed.

When the trigger occurs before your next turn, use your Reaction to execute the response immediately after the trigger finishes \- or ignore it. If the trigger doesn't occur, the action is lost.

**Held Action with Spells**: You begin the casting process but must hold concentration, this counts as channelling. If concentration breaks, the spell dissipates (Mana is lost). Released on your specified trigger.

**Ready Volley:** Holding a ranged attack this way has its own name and a Called Shot option - see [[Ready Volley|maneuvers]].

---

## Critical Hits

Critical Hits occur on a **Natural 12** on attack rolls.

**Effects:**

- **Roll damage twice, take the higher result.**  
- Bypasses the Parry and Block Styles of Maneuver (Dodge is unaffected - see [[Maneuvers|maneuvers]])

Crits don't grant Trauma \- their pressure is indirect, since rolling twice raises the odds of landing in a higher Wound tier (see [[Wounds and Survival|core_rules]]).

**Expanded Crit Range:** Some weapons crit on 11-12, 10-12 or even 9-12.  
Features and Feats can expand this further.

**Spells:** Spell attack rolls can crit. Spell overcome rolls cannot.

---

## Agility

### **Evasion**

Evasion, or ‘Passive Evasion’ is your innate ability to stay out of harm's way. This requires no setup or actions, it happens automatically against attack rolls.

**Evasion \= 5 \+ Agility \+ DEX − Armor Penalty**

---

## Armor

Armor is just that, your worn armor, it protects a flat amount of damage passively, but degrades each time you are hit, successfully or not.

### **Armor Rating**

When hit:

1. Subtract AR from damage  
2. Armor loses 1 AR (degradation)  
3. Remaining damage converts to Wounds (see [[Wounds and Survival|core_rules]])

**Note:** A Critical Hit can still deal 0 Wound damage against fresh, heavy armor \- that's coherent with the armor fiction, not a bug.

### **Degradation**

Every hit (regardless of Wound damage) reduces armor by 1 AR.

| AR Status | Effect |
| :---- | :---- |
| AR 1+ | Functions normally |
| AR 0 | **Broken** \- no protection |

**Broken Armor:** Rigid armor cannot be field-repaired once broken and must be reforged by a blacksmith (1/2 of original price); Flexible armor can still be field-repaired. See [[Armor|armor]] for full repair rules.

### **Armor Penalty**

Reduces Evasion, your Dodge Style roll ([[Maneuver|maneuvers]]), and your Spell Modifier.

**Reducing Penalty:** Each rank in Armorer reduces Penalty by 1 (minimum 0).

---

## Battlemap & Positioning

Ressam is played on a grid of 5-foot squares, minis-and-battlemap style - every Speed, Reach, and Range value in this book is already denominated in that unit.

- **Size & Squares:** A creature occupies a number of squares matching its Space ([[Size|core_rules]]) - Small/Medium: 1 square, Large: 2x2, Huge: 3x3.
- **Measuring Distance:** Count outward square-by-square from your square to the nearest square of the target. Every square costs the same to enter, whether moved orthogonally or diagonally.
- **Areas of Effect:** Count outward from the origin square the same way; a radius reaches every square its count extends to, no partial-coverage rulings needed.

---

## Reach

Not every weapon threatens the same amount of ground. A dagger only menaces whoever's standing right next to you; a pike keeps anyone dangerous a good few paces back. Weapons carry a **Reach Category** - Touch, Short, Medium, Long, or Very Long - that says how many squares out they can strike (see [[Reach Categories|weapons]] for the full table).

That difference matters most the moment two weapons actually meet. Charging past the point of someone's spear to get in close is dangerous - they get a free swing at you for it (Closing the Distance, under Opportunity Attacks, below). And once you're trading blows, trying to parry a weapon much longer than yours is a losing proposition - your blade simply isn't there yet when theirs already is (see Parry, in [[Maneuvers|maneuvers]]).

| Reach Category |      Squares      | Who has it |
| :---- |:-----------------:| :---- |
| Touch |   Adjacent only   | Unarmed/Brawling attacks |
| Short |   Adjacent only   | One-handed sidearms - Dagger, Knife, Shortsword, Scimitar, Broadsword, Mace, Club, Battle Axe |
| Medium |   Adjacent only   | Two-handed swords and long thrusting blades (Longsword, Greatsaber, Greatsword, Warblade, Rapier, Estoc), plus other staff-length arms (Spear, Quarterstaff, Whip, Weighted Chain, Warhammer, Greatclub) |
| Long | 2 squares (10 ft) | Dedicated infantry polearms - Halberd, Glaive |
| Very Long | 3 squares (15 ft) | The pike, alone - built to out-reach everything else on the field |

Touch, Short and Medium cover identical ground - there's no such thing as "closer than adjacent" on a grid. The split still matters below: Touch (a bare fist) ranks below Short (an actual blade) even at the same distance.

**How They Interact:** Every rule Reach drives just compares your Category to theirs on the list above - nothing stacks, nothing scales with how many steps apart you are.

**Consequence:** When fighting an opponent whose weapon has a longer Reach Category than yours, you suffer disadvantage on rolls to Maneuver and to attack that target.


| Compared to your opponent's Reach | What happens |
| :---- | :---- |
| **Lower than yours** | If your Reach is Medium or higher, them closing from outside your Reach into it provokes an Opportunity Attack from you. |
| **Equal to yours** | No effect either way - a level exchange. |
| **Higher than yours** | Your Parry has Disadvantage against them, and Riposte is off the table - unless something (Dodge's Reposition, or landing the **Close the Gap** Effect against this attacker) closes the gap first. See [[Maneuver|maneuvers]]. |

---

## Flanking

You and an ally flank a target when your two squares are the **exact mirror of each other** across the target's space - not merely "somewhere on opposite sides." Picture the ring of squares touching the target: flanking requires you and your ally to occupy a directly-opposite pair in that ring (e.g. north and south, or northeast and southwest). There's no partial credit for a near-opposite position, and no drawing lines through corners to make a marginal angle count - if your square isn't the exact mirror of your ally's, you are not flanking.

**Effect:** Your melee attack rolls against a target you're flanking have Advantage.

**Larger Targets:** Against Large and Huge creatures, judge "directly opposite" the same way against the far side of their space, rather than a single mirrored square.

---

## Movement in Combat

- **Move:** Move up to your speed; can split before/after action  
- **Dash:** Major Action for additional movement equal to speed  
- **Disengage:** Major Action to avoid Opportunity Attacks this turn  
- **Difficult Terrain:** Costs double movement  
- **Standing from Prone:** Costs half your maximum movement

---

## Opportunity Attacks

When a creature **leaves your melee reach**, you may use your Reaction for one melee attack.

**Closing the Distance:** If you're wielding a weapon with Reach Medium or higher, a creature moving from outside your Reach to within it provokes the same way - the entry-side mirror of leaving reach (see [[Reach|weapons]]).

**Does NOT Provoke:**

- Moving within reach you already occupy
- Standing from prone  
- Forced movement (push, pull, teleport)
- Moving after taking the Disengage action
- Ranged attacks in melee (just disadvantage)

---

## Surprise

Ambushers gain a **Surprise Round**.

**Surprised creatures:**

- Cannot take actions or Reactions during Round 1  
- Roll initiative normally  
- Act normally from Round 2

---

## Cover

Cover in Ressam is a binary system \- you either have it or you don't. Your DM has final say on if your position is in cover or not.

**Cover:** Completely hidden behind solid obstruction. Cannot be targeted by attacks or most spells.

**No Partial Cover:** Any exposure \= targetable.

**Cover doesn't protect against:** AoE originating behind cover, spells without line of sight, attackers who reposition.

---

## Conditions

Conditions can be applied by numerous different sources and in a multitude of ways, magically or mundanely.

| Condition | Effects                                                                                                                                                                                                                                                                                |
| :---- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Bleeding** | At the start of each of its turns, the creature takes its Bleed value \- half the damage of the hit that applied Bleeding (rounded down, does not degrade AR). Ending it takes a Major Action and a Medical Lore check (DC \= Bleed value), made on itself or by an adjacent creature. |
| **Blinded** | Can't see. Automatically fails any check or Ward that relies on sight. Disadvantage on attack rolls; attack rolls against it have advantage.                                                                                                                                           |
| **Charmed** | Can't attack the charmer or target it with harmful effects. The charmer has advantage on Skill checks to interact with the creature socially.                                                                                                                                          |
| **Deafened** | Can't hear. Automatically fails any check or Ward that relies on hearing.                                                                                                                                                                                                              |
| **Flying** | Gains a flying Speed equal to the granting effect's value or its walking Speed, whichever is higher. If it loses this Speed or is knocked Prone while aloft, it falls (see [[Falling                                                                                                   |core_rules]]). |
| **Frightened** | While the source of its fear is within line of sight: disadvantage on attack rolls and Skill checks. It can't willingly move closer to the source.                                                                                                                                     |
| **Grappled** | Restrained, ends if the creature is moved beyond the reach of the grappler or grappling effect.                                                                                                                                                                                        |
| **Incapacitated** | Can't take actions or reactions (Major, Minor, Object Interaction, or Reaction). Movement is unaffected unless another effect says otherwise.                                                                                                                                          |
| **Invisible** | Attack rolls against it have disadvantage; its own attack rolls have advantage. Counts as heavily obscured for hiding and has advantage on Stealth checks.                                                                                                                             |
| **Paralyzed** | Incapacitated, Speed 0, and can't speak. Automatically fails STR and DEX Wards. Attack rolls against it have advantage, and any melee attack that hits it is a critical hit.                                                                                                           |
| **Petrified** | Incapacitated, Speed 0, and unaware of its surroundings. Becomes a nonmagical stone object: weight ×10, aging stops, resistance to all damage. All other conditions and ongoing effects are suspended until it's freed.                                                                |
| **Poisoned** | Disadvantage on attack rolls and Skill checks.                                                                                                                                                                                                                                         |
| **Prone** | Disadvantage on attack rolls. Melee attack rolls against it have advantage; ranged attack rolls against it have disadvantage. Can't move except to stand up, which costs half its maximum movement.                                                                                    |
| **Restrained** | Speed 0; disadvantage on attack rolls; \-3 to DEX Wards; casting requires a MIND Ward (DC 23\) or the spell fails.                                                                                                                                                                     |
| **Silenced** | Can't speak or cast spells.                                                                                                                                                                                                                                                            |
| **Stunned** | On its turn it can take only one action of any type \- a single Major, Minor, Object Interaction, or Move Action \- instead of its normal allotment.                                                                                                                                   |
| **Unconscious** | Incapacitated, Speed 0, can't speak, and unaware of its surroundings; it falls Prone and drops what it's holding. Automatically fails all checks and Wards. Attacks against it automatically hit, and any melee hit is a critical hit.                                                 |
