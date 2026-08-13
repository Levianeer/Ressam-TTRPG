Where creatures stand relative to each other - and how far a weapon reaches from there - shapes an exchange as much as the roll does. This chapter covers the grid, Measure Bands, movement, and the situational modifiers (Surprise, Cover) layered on top of them; see [[Combat|combat]] for turn structure and attack resolution, and [[Maneuvers|maneuvers]] for the reactive Oppose exchange these mechanics feed into.

---

## Battlemap & Positioning

Ressam is played on a grid of 5-foot squares, minis-and-battlemap style - every Speed, Reach, and Range value in this book is already denominated in that unit.

- **Size & Squares:** A creature occupies a number of squares matching its Space ([[Size|carrying_and_resting]]) - Small/Medium: 1 square, Large: 2x2, Huge: 3x3.
- **Measuring Distance:** Count outward square-by-square from your square to the nearest square of the target. Every square costs the same to enter, whether moved orthogonally or diagonally.
- **Areas of Effect:** Count outward from the origin square the same way; a radius reaches every square its count extends to, no partial-coverage rulings needed.

---

## Reach

Not every weapon threatens the same amount of ground. A dagger only menaces whoever's standing right next to you; a pike keeps anyone dangerous a good few paces back. Weapons carry a **Measure Band** - Short, Medium, Long, Far, or Very Far - that says how many squares out they can strike (see [[Measure Bands|weapons]] for the full table).

Unlike a static Reach comparison, Measure is a single shared value between two engaged combatants, and each side checks it against their *own* weapon independently - there's no "longer" and "shorter" combatant locked into fixed roles, just whoever's weapon currently matches the measure and whoever doesn't.

**How It Works:** Compare your own weapon's Measure Band to the current shared measure (see [[Measure Bands|weapons]]) - nothing stacks, nothing scales beyond the five bands.

| Your weapon vs. the current measure                                                       | What happens                                                                                                                                                                                                     |
|:------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Matches**                                                                               | Strike freely - no penalty.                                                                                                                                                                                      |
| **One or two bands off** (e.g. Short↔Long, Medium↔Far)                                    | Strike at Disadvantage.                                                                                                                                                                                          |
| **Three or four bands off** (e.g. Short↔Far, Short↔Very Far, the maximum possible spread) | **You cannot Strike at all** - no attack roll, no Strike Effect - and an Oppose roll funded by a Weapon Skill cannot be attempted this way at all (Oppose funded by a STR Ward or DEX Ward is unaffected). |

**Setting the measure:** An exchange begins at the longer weapon's Measure Band - the shorter weapon starts every fight with a problem to solve. Either side can change it: the **Shift Measure** Minor Action ([[Basic Moves|basic_moves]]) moves the shared measure one band, in or out, on your own turn; the **Shift** Effect (see [[Oppose|maneuvers]]) does the same for free as part of winning an Oppose Reaction, no provoke. **Closing through a band your opponent's weapon still matches provokes** - moving from outside your target's Measure Band into it triggers their Opportunity Attack, below, the same as closing to melee always has.

**Closing costs the long weapon too.** A pike is firewood once someone's dragged the measure down to Short - Very Far and Short are the maximum possible spread, so the same rule that stops a dagger from reaching a pike at Very Far stops the pike from Striking at all once the measure sits at Short. This is why anyone who fights with a Far or Very Far Band weapon carries a sidearm: the moment the measure collapses under them, their polearm becomes the wrong tool, and drawing something shorter is the actual answer, not just riding out the mismatch. Nothing needs to "break a lock" here the way the old Reach rules did - the symmetric comparison above already handles both sides at every measure, automatically.

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

**Closing the Distance:** If you're wielding a weapon with Measure Band Medium or higher, a creature moving from outside your reach to within it provokes the same way - the entry-side mirror of leaving reach (see [[Measure Bands|weapons]]); Short Band can't do this to you. It fires once, right as they cross into your threat range: continuing to close afterward, from your reach's outer edge down to fully adjacent, doesn't provoke it again (see "moving within reach you already occupy," below) - and running out of movement right at that edge, without reaching adjacent, still counts as having triggered it.

**Does NOT Provoke:**

- Moving within reach you already occupy
- Standing from prone  
- Forced movement (push, pull, teleport)
- Moving after taking the Disengage action
- Ranged attacks in melee (just disadvantage)

An Opportunity Attack is a normal attack roll like any other - if it beats the target's Passive Evasion, they may answer it with Oppose or Reactive Casting exactly like any other attack (see [[Maneuvers|maneuvers]]).

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
