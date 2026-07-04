## Foreword

### **Ressam is not Dungeons & Dragons.**

If you're coming from 5th Edition, you'll notice this system asks more of you. Armor degrades and needs repair. Exhaustion builds up over time. Magic is rarer, costlier, and comes with social baggage. Your choices \- tactical and strategic \- carry more weight than you might be used to. This is intentional but it's not meant to be a meat grinder.

Ressam sits somewhere between the relative safety of modern D\&D and the punishing lethality of dedicated survival games. You won't die to a single unlucky roll, but you also can't ignore your wounds and push through every encounter. Think of it as *consequential* rather than brutal \- a system where preparation matters, retreating is sometimes the smart play, and victory feels earned.

**Combat is the heart of this game.** Ressam is crunchy where it matters \- positioning, resource management, decisions with real trade-offs. The mechanics outside of combat exist primarily to support that loop: resting recovers what you'll spend in the next fight, equipment requires upkeep, and downtime prepares you for what's ahead. This isn't a game with elaborate subsystems for every pillar of play. Everything outside of combat is meant to be played loosely and with a ‘rulings not rules’ mentality.

**This system is built for Ressam's world.** Weapons, armor, magic, and social structures are balanced around a roughly early-mid 1500s baseline. Matchlock firearms sit alongside plate armor. Magic is feared and regulated. If you adapt this to another setting, some assumptions may need adjusting.

**Finally, this is a work in progress.** Mechanics will change. Spells will be rewritten. If something feels off, it might be \- feedback helps.

Welcome to Ressam.

---

## Dice and Standards

Ressam uses d4, d6, d8, d10, and d12 dice. The d12 is your primary resolution die.

**Rounding:** Always round down unless stated otherwise.

**Advantage:** Roll twice, use higher result.  
**Disadvantage:** Roll twice, use lower result.  
**Stacking:** Compare total sources of each; the side with more wins. If equal, roll normally.

**Note:** Advantage is typically worth the equivalent of a \+3 bonus, while disadvantage is worth \-3.

**Time Scale:** A round represents roughly 6 seconds of in-fiction time.

---

## Attributes

Attributes range from 1 (severely impaired) to 10 (peak mortal potential).

| Attribute | Abbr. | Governs |
| :---- | :---: | :---- |
| **Strength** | STR | Physical power, melee damage, carrying capacity |
| **Reflex** | REF | Reaction speed, ranged accuracy, initiative |
| **Endurance** | END | Toughness, hit points, resisting fatigue |
| **Dexterity** | DEX | Agility, fine motor control, dodging |
| **Mind** | MIND | Intelligence, reasoning, mana pool |
| **Arcane** | ARC | Arcane magical aptitude |
| **Faith** | FAI | Divine connection and conviction |
| **Charisma** | CHA | Social influence, force of personality |

---

## Literacy

Reading and writing are far from universal in Ressam \- most people never learn.

**Automatic Literacy:** A character with **MIND 6+** at character creation is literate, able to read and write every language they know.

**Below MIND 6:** Illiterate by default. Literacy determined this way is fixed at character creation \- raising MIND afterward (leveling, Keen Mind, etc.) does not retroactively grant it.

**Learning to Read Later:** An illiterate character can still choose to learn to read during play. This isn't automatic and has no fixed cost or timeline \- work it out with your DM.

**Note:** Spellcasting requires literacy (see Magic Overview) \- an illiterate character cannot invest in an Arcane or Divine school, regardless of ARC or FAI, until they learn to read.

---

## Skills

Skills range from 0 (untrained) to 10 (world-renowned master). Each is tied to one attribute.

### **Skill Check Formula**

**1d12 \+ Skill Ranks \+ Attribute** vs. **DC**  
**Note:** Only call for rolls when failure is reasonably possible.

**Trained:** The Attribute only applies once you have 1 or more Skill Ranks in that skill. An untrained skill (0 Ranks) rolls **1d12** alone \- no Skill Ranks, no Attribute. This applies anywhere a Skill adds an Attribute to a roll, including Weapon Skill on Attack Rolls (see Combat) and Magic School Skill on Spell Modifier (see Magic Overview).

### **Setting a Difficulty Class (DC)**

Ressam uses an eight-tier DC scale for Skill Checks, Ward Checks, Minor Magic, and Alchemy crafting alike. Pick a tier by how difficult the task is narratively; you rarely need to reach for a number outside this list.

| Tier | DC | Example |
| :---- | :---: | :---- |
| Very Easy | 5 | Recalling common knowledge, walking a plank |
| Easy | 8 | Climbing a knotted rope, haggling with a friendly merchant |
| Medium | 10 | Picking a simple lock, patching a minor wound |
| Tricky | 12 | Balancing on a narrow ledge, talking down a nervous guard |
| Hard | 15 | Persuading a skeptical noble, disarming a snare |
| Very Hard | 20 | Forging a noble's seal, scaling a sheer cliff in a storm |
| Incredibly Hard | 25 | Snapping manacles bare-handed, resisting a curse's full grip |
| Impossible | 30 | Outrunning a warhorse on foot, staring down a god without flinching |

**Note:** Medium, Hard, and Very Hard line up with the DC 10/15/20 used for Minor Magic and Alchemy crafting, so a spell or potion pegged "Moderate" in those chapters is a Hard check by this scale. Incredibly Hard shows up informally elsewhere (breaking Chains, Curse of the Beast, casting while Restrained) for feats meant to be exceptional even for a specialist; Impossible is there to mark tasks a DM shouldn't be calling for a roll on at all \- if the answer's really "no, unless something extraordinary happens," don't make the player roll for it.

**What to expect at the table:** A character actively trained in the relevant Skill clears Very Easy through Medium almost automatically at any level, and Tricky not long after. Hard is a real coin flip early on and becomes reliable by mid-game. Very Hard is a long shot for a level 1 character and doesn't become dependable until roughly level 10\+. Incredibly Hard and Impossible should stay hard even for a maxed-out specialist \- they're meant to represent genuinely exceptional feats, not routine business.

| Tier | DC | Level 1 (trained) | Level 6 (trained) | Level 12 (trained) |
| :---- | :---: | :---: | :---: | :---: |
| Very Easy | 5 | 100% | 100% | 100% |
| Easy | 8 | 100% | 100% | 100% |
| Medium | 10 | 100% | 100% | 100% |
| Tricky | 12 | \~92% | 100% | 100% |
| Hard | 15 | \~67% | 100% | 100% |
| Very Hard | 20 | \~25% | \~75% | 100% |
| Incredibly Hard | 25 | 0% | \~33% | \~67% |
| Impossible | 30 | 0% | 0% | \~25% |

*Success rates assume a character whose Skill Ranks and governing Attribute both scale from a level 1 specialist (Skill 3 \+ Attribute 7\) to a level 12 specialist (Skill 10 \+ Attribute 10\), the typical progression curve for a trained frontline build.*

**Coming from D\&D?** Don't reuse D\&D's DC numbers directly. D\&D's 1d20 \+ modifier rarely exceeds \+11, even at high level, so its DCs stay meaningful across the whole level range by design (bounded accuracy). Ressam's 1d12 \+ Skill \+ Attribute can climb to \+20 for a maxed specialist, so the same numeric DC means something very different in each system \- a DC that's brutally hard in D\&D can become close to automatic for a Ressam specialist, and vice versa for an untrained character. Set DCs by narrative difficulty using the tiers above, not by porting a number from another game.

### **Skill Categories**

**Combat Skills**

| Category                | Attr. | Skills |
|:------------------------| :---: | :---- |
| Brawn & Melee           | STR | One-Handed Blades, Two-Handed Blades, Axes & Hammers, Polearms, Brawling, Slings & Whips |
| Finesse & Ranged        | REF | Rapiers & Fencing, Daggers & Knives, Bows & Crossbows, Thrown Weapons, Pistols, Long Guns, Heavy Firearms |
| Defense & Survival      | END | Athletics, Armorer, Survival, Shields, Riding |
| Adroitness & Subterfuge | DEX | Agility, Acrobatics, Stealth, Lockpicking, Sleight of Hand, Crafting, Perception |

**Knowledge Skills**

| Category | Attr. | Skills |
| :---- | :---: | :---- |
| Intellectual | MIND | Alchemy, Enchanting, Spell Crafting, Historic Lore, Medical Lore, Nature Lore, Identify |
| Arcane Schools | ARC | Arcane Lore, Aeromancy, Geomancy, Hydromancy, Pyromancy, Shadowmancy |
| Divine Schools | FAI | Religious Lore, Benediction, Invocation, Necration, Cultivation, Subjugation |

**Social Skills**

| Category | Attr. | Skills |
| :---- | :---: | :---- |
| Socialising & Interaction | CHA | Persuasion, Deception, Intimidation, Leadership, Animal Handling, Insight, Performance |

**Note:** Identify covers recognizing what something actually is - appraising the value or authenticity of goods, art, and coin; spotting forgeries and fakes; and determining the nature of an unfamiliar substance, material, or object on sight.

---

## Checks vs. Ward

**Skill Checks:** Represent an active attempt at using your training. Roll 1d12 \+ Attribute \+ Skill ≥ DC

**Ward Check:** Wards represent a split-second reaction to danger. Roll 1d12 \+ Attribute \+ your highest-ranked Skill governed by that Attribute ≥ DC

**Note:** Your Ward also works as a passive, static defensive score \- **Ward \= 5 \+ Attribute \+ your highest-ranked Skill governed by that Attribute** \- representing the same resistance without requiring you to roll. Spells and other effects that target a Ward instead of Evasion roll against this score directly (see Magic Overview).

| Situation | Roll Type |
| :---- | :---- |
| Climbing a cliff | Athletics Check |
| Grabbing a ledge when pushed | STR Ward |
| Sneaking past guards | Stealth Check |
| Surprised by an assassin | REF Ward |

---

## Hit Points and Survival

**Maximum HP \= (END × 3\) \+ 10**

### **Dying**

At 0 HP:

1. You immediately fall Prone and become Unconscious. Dropping any equipment you were holding.  
2. You gain HP equal to your END. If your HP increases above this, you are no longer Dying or Unconscious.  
3. For every round you are Dying you gain 2 levels of Exhaustion. If this gets you to 10 levels of Exhaustion, you automatically die.

### **Coup De Grace:**

A dying creature can be executed by attacking them.

- Hitting a Dying creature and dealing damage over their END HP kills them instantly.  
- Enemies can also do this, and will use this to their advantage.

### **Stabilization**

- **Action:** Major Action while adjacent  
- **Check:** Medical Lore \+ MIND vs. DC (10 \+ target's Exhaustion)  
- **Healer's Kit:** Grants advantage

### **Falling**

Take 1d6 bludgeoning damage per 5 ft fallen, creature is forced prone unless damage is avoided. Deliberately jumping, reduces the number of dice rolled by 4d6 (minimum 0), Landing on soft surfaces may reduce damage by half (DM discretion).

### **Food and Water**

On average, a character can go three days without rations, each day after they gain a level of Exhaustion and cannot be healed until they have consumed a ration.

### **Suffocation**

You can hold your breath for END minutes. After that, you drop to 0 HP and begin to die.

### **Temporary Hit Points**

Temporary Hit Points, or tHP represents your temporary patching of a wound or injury. Keeping you in the fight until you can rest.

- **Maximum tHP:** Total HP − current HP  
- **Stacking:** Multiple sources add together  
- **Damage Order:** tHP lost before HP  
- **Duration:** Disappears after next Rest

---

## Carrying Capacity

**Carrying Capacity \= ((END \+ STR) × 10\) \+ 10 lbs**

**Encumbered (over capacity):** Speed drops to 5 ft; disadvantage on physical checks.

**Push/Drag/Lift:** Up to 2× carrying capacity, but speed drops to 5 ft.

| Size | Capacity Modifier | Space \& Reach |
| :---: | :---: | :---: |
| Small | × 0.5 | 5 ft |
| Medium | × 1 | 5 ft |
| Large | × 2 | 10 ft |
| Huge | × 4 | 15 ft |

**Space:** How much room a creature occupies.
**Reach:** How far its unarmed melee reach extends (see Combat for reach-based rules like Opportunity Attacks).

---

## Resting

### **Short Rest (1 Hour)**

- Regain HP equal to **END**  
- No Mana recovery  
- Exhaustion: Medical Lore DC 15 to remove 1 level  
- Can use: Armorer (rank 3+), Medical Lore, Scribing, Prayer etc  
- Interrupted by combat

### **Field Rest (6 Hours)**

- Regain HP equal to **END × 2**  
- Regain Mana equal to **MIND**  
- Exhaustion: Medical Lore DC 15 to remove 2 additional level  
- Can use: Armorer (rank 3+), Medical Lore, Scribing, Prayer etc  
- **Requires:** Shelter, watch rotation, defensible position, 1 ration per character

### **Long Rest (8 Hours)**

- Regain HP equal to **END × 4**, up to your Maximum HP  
- Regain Mana equal to **MIND × 3**, up to your Maximum Mana  
- Exhaustion: Remove 1 level automatically, Medical Lore DC 15 to remove 2 additional level  
- Can use: Armorer (rank 3+), Medical Lore, Scribing, Prayer etc  
- **Requires:** Permanent structure in civilization with security (inn, barracks, temple, etc.)

**Note:** Field Rests and Long Rests provide no benefits if their shelter requirements aren't met.

---

## Exhaustion

Exhaustion represents accumulated injuries, stresses and trauma beyond HP loss.

| Level | Effect |
| :---- | :---- |
| 1-2 | Manageable |
| 3-4 | Dangerous |
| 5-9 | Critical |
| 10 | **Automatic Death** |

**Note:** These labels describe how dangerous your condition is narratively \- the mechanical penalty scales continuously (subtract your current Exhaustion level from all rolls). No separate effect triggers at each band on its own.

**Penalties:** Subtract Exhaustion level from **all** d12 rolls, wards and checks.

---

## Stealth and Hiding

**Action:** Major Action  
**Check:** Stealth \+ DEX vs. observers' passive Perception

**Requirements (need one):** Heavily obscured, behind full cover, or special ability.

**Passive Perception \= 5 \+ Perception \+ DEX**

**Stealth breaks when you:** Attack, cast most spells, enter bright light without cover, make significant noise, or are found by active search.

---

## Light and Vision

| Level | Effect |
| :---- | :---- |
| **Bright Light** | Normal vision |
| **Dim Light** | Disadvantage on attacks and sight-based Perception, blurry and difficult to make out details |
| **Darkness** | Effectively blinded without darkvision, pitch-black with no discernable features |

| Source | Bright | Dim | Duration |
| :---- | :---- | :---- | :---- |
| Candle | 5 ft | \+5 ft | 1 hour |
| Torch | 20 ft | \+20 ft | 2 hours |
| Lantern | 30 ft | \+30 ft | 12 hours |

**Low-Light Vision:** Treat dim light as bright within range.  
**Darkvision:** See darkness as dim light within range (grayscale only).
