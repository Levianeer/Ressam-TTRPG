## Foreword

### **Ressam is not Dungeons & Dragons.**

If you're coming from other TTRPGs, you'll notice this system asks more of you. Armor degrades and needs repair. Trauma builds up over time. Magic is rarer, costlier, and comes with social baggage. Your choices \- tactical and strategic \- carry more weight than you might be used to. This is intentional but it's not meant to be a meat grinder.

Ressam sits somewhere between the relative safety of modern D\&D and the punishing lethality of dedicated survival games. You can't ignore your wounds and push through every encounter. Think of it as *consequential* rather than brutal \- a system where preparation matters, retreating is sometimes the smart play, and victory feels earned.

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

Attributes range from 0 (wholly absent) to 5 (peak mortal potential).

| Attribute | Abbr. | Governs |
| :---- | :---: | :---- |
| **Strength** | STR | Physical power, melee damage, carrying slots |
| **Precision** | PRE | Reaction speed, ranged accuracy, initiative |
| **Endurance** | END | Toughness, Wounds, resisting fatigue |
| **Dexterity** | DEX | Agility, fine motor control, dodging |
| **Mind** | MIND | Intelligence, reasoning, mana pool |
| **Arcane** | ARC | Arcane magical aptitude |
| **Faith** | FAI | Divine connection and conviction |
| **Charisma** | CHA | Social influence, force of personality |

**A 0 in an Attribute** is a complete absence of that capacity, not just poor - the same way an unranked Skill sits at 0 until trained. It's a legitimate choice at character creation (see Character Creation), not only a racial exception. **An Attribute can never go below 0** - if an effect would push one lower, the character dies.

---

## Literacy

Reading and writing are far from universal in Ressam \- most people never learn.

**Automatic Literacy:** A character with **MIND 3+** at character creation is literate, able to read and write every language they know. Certain Careers (see Careers) grant literacy as well, regardless of MIND.

**Below MIND 3:** Illiterate by default, unless literacy is granted by Career. Literacy determined this way is fixed at character creation \- raising MIND afterward (leveling, etc.) does not retroactively grant it.

**Learning to Read Later:** An illiterate character can still choose to learn to read during play. This isn't automatic and has no fixed cost or timeline \- work it out with your DM.

**Note:** Spellcasting requires literacy (see Magic Overview) \- an illiterate character cannot invest in an Arcane or Divine school, regardless of ARC or FAI, until they learn to read.

---

## Skills

Skills range from 0 (untrained) to 5 (world-renowned master). Each is tied to one attribute.

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
| Incredibly Hard | 22 | Snapping manacles bare-handed, resisting a curse's full grip |
| Impossible | 25 | Outrunning a warhorse on foot, staring down a god without flinching |

**Note:** Minor Magic and Alchemy crafting no longer keep their own copy of these numbers - both read Medium, Hard, and Very Hard directly off this table, so a spell or potion pegged "Hard" in those chapters always means DC 15 here, with nothing left to fall out of sync. The top two tiers are pinned to the actual ceiling of the d12 \+ Skill \+ Attribute system: a fully capped character (Skill 5, Attribute 5, both reached by level 8\) rolling a natural 12 hits 22 with no magical help at all \- that's Incredibly Hard. Magic items add at most \+3 on top of that, putting the true maximum possible roll anyone can ever produce at 25 \- that's Impossible, reachable only by a maxed, magically-equipped character on a natural 12\. Incredibly Hard shows up informally elsewhere (breaking Chains, Curse of the Beast, casting while Restrained) for feats meant to be exceptional even for a specialist; Impossible is there to mark tasks a DM shouldn't be calling for a roll on at all \- if the answer's really "no, unless something extraordinary happens," don't make the player roll for it.

**What to expect at the table:** A character actively trained in the relevant Skill clears Very Easy through Medium almost automatically at any level, and Tricky not long after. Hard is a real coin flip early on and becomes reliable by mid-game. Very Hard is out of reach at level 1 (even a maxed roll can't touch it) and stays a real risk even at the level cap without magical help. Incredibly Hard demands nothing short of a natural 12, even from a fully capped specialist \- and Impossible needs that same natural 12 stacked with the best magic gear money can buy. Neither is meant to be routine business.

### **Skill Categories**

**Combat Skills**

| Category                | Attr. | Skills |
|:------------------------| :---: | :---- |
| Brawn & Melee           | STR | One-Handed Blades, Two-Handed Blades, Axes & Hammers, Polearms, Brawling, Slings & Whips |
| Finesse & Ranged        | PRE | Rapiers & Fencing, Daggers & Knives, Bows & Crossbows, Thrown Weapons, Pistols, Long Guns, Heavy Firearms |
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

**Passive Ward \= 5 \+ Attribute \+ your highest-ranked Skill governed by that Attribute** \- a quick-reference defensive score standing in for a Ward Check without requiring you to roll.

**Contested Checks:** Whenever a Feat, Feature, Maneuver, or Spell Overcome pits one creature's Skill or Ward directly against another's (rather than a flat DC from the tier table above), only the instigator rolls: **1d12 \+ the named Attribute \+ the named Skill** (their Spell Modifier, for spells) against the defender's static score \- **5 \+ the defender's associated Attribute \+ their relevant Skill** (their highest-ranked Skill governed by that Attribute, for a **Contested Ward**; a specific named Skill instead, where the rule says so, such as Acrobatics defending a Grapple). The defender never rolls. Ties go to the instigator, same as a Skill Check meeting a DC exactly.

| Situation | Roll Type |
| :---- | :---- |
| Climbing a cliff | Athletics Check |
| Grabbing a ledge when pushed | STR Ward |
| Sneaking past guards | Stealth Check |
| Surprised by an assassin | PRE Ward |

---

## Wounds and Survival

**Maximum Wounds \= END**

Damage remaining after AR reduction converts to Wounds via thresholds, rather than subtracting 1-for-1:

| Damage (after AR) | Wounds inflicted |
|:---|:---:|
| 1-9 | 1 |
| 10-15 | 2 |
| 16+ | 3 |

**Design intent:** Big weapons genuinely threaten multi-wound hits; armor's job is dragging a 2-wound hit down into 1-wound territory; Reactions that shave even a few points of damage can drop a hit below a threshold and are therefore decisive, not marginal.

### **Wound Penalty**

Each Wound you're currently missing from your maximum imposes **\-1 to all non-combat rolls**, cumulative. There is deliberately **no combat death spiral** \- a character on their last Wound fights at full capability. The cost of injury is paid on the strategic layer afterward, not in the fight itself.

**Design philosophy:** Wound penalties are not punishment; they are the privilege of being alive. A tough character walking around at a steep penalty is doing so *because* anyone less tough would already be dead. END is not the stat that makes you good at surviving \- it's the stat that lets you afford to be hurt.

### **Dying**

At 0 Wounds:

1.  You immediately fall Prone and become Unconscious, dropping any equipment you were holding. Excess damage is ignored.
2.  Your **Death Clock** starts at your **END**. At the start of each of your turns, reduce it by 1. When it reaches 0, you die.
3.  **While Dying, you cannot regain Wounds.** Healing magic, potions, and similar effects instead *pause* your Death Clock until the start of your next turn \- they buy time, they don't save you. Only Stabilization ends Dying.

### **Coup de Grace**

A Dying creature can be executed by attacking it.

-   Attacks against a Dying creature automatically hit (it's Unconscious). Each instance of damage reduces its Death Clock by 2.
-   A creature that spends a Major Action adjacent to a Dying creature to deliberately execute it kills it outright, no roll required.
-   Enemies can and will do this.

### **Stabilization**

-   **Action:** Major Action while adjacent
-   **Check:** Medical Lore + MIND vs. DC (10 + target's Trauma)
-   **Healer's Kit:** Grants advantage
-   **Success:** The target is no longer Dying. They remain at 0 Wounds, Unconscious, and Prone until they regain at least 1 Wound \- at which point healing works on them normally again.
-   **Failure:** No progress; the clock keeps ticking. You may try again next round.

### **Falling**

Take 1d6 bludgeoning damage per 5 ft fallen, creature is forced prone unless damage is avoided. Deliberately jumping, reduces the number of dice rolled by 4d6 (minimum 0), Landing on soft surfaces may reduce damage by half (DM discretion).

### **Food and Water**

On average, a character can go three days without rations, each day after they gain a level of Trauma and cannot be healed until they have consumed a ration. A full day of hex travel also consumes 1 ration per character (see Traveling).

### **Suffocation**

You can hold your breath for END minutes. After that, you drop to 0 Wounds and begin to die.

### **Temporary Wounds**

Temporary Wounds, or Temp Wounds represents your temporary patching of a wound or injury. Keeping you in the fight until you can rest.

- **Maximum Temp Wounds:** Total Wounds − current Wounds  
- **Stacking:** Multiple sources add together  
- **Damage Order:** Temp Wounds lost before Wounds  
- **Duration:** Disappears after next Rest

### **Wound Recovery**

Wounds don't refill on the Short/Field/Long Rest cadence (see Resting, below, for Mana and Trauma recovery) \- they heal on their own, slower track:

-   **Attended:** Regain **1 Wound per 2 days** while actively attended by a medic or doctor (this may be a party member). The patient must rest and do nothing beyond light physical work; the medic is likewise occupied and cannot spend that time doing anything else productive.
-   **Unattended:** Regain **1 Wound per 2 weeks**. This is a deliberately punitive floor \- a medic-less party isn't stuck healing forever, but attended care is dramatically better.
-   A **Dying** character who has been Stabilized recovers their first Wound (ending Unconsciousness) on this same track \- Attended or Unattended, same rates as anyone else.

---

## Slots

Carrying capacity is tracked in **Slots**, not weight. Check your Slots when you decide what to carry \- not on every purchase or pickup.

**Slots \= STR \+ END**

Size modifies your Slot total, rounding down:

|  Size  | Slots Modifier | Space \& Reach |
|:------:|:--------------:|:--------------:|
| Small  |     × 0.5      |      5 ft      |
| Medium |      × 1       |      5 ft      |
| Large  |      × 2       |     10 ft      |
|  Huge  |      × 4       |     15 ft      |

**Space:** How much room a creature occupies.
**Reach:** How far its unarmed melee reach extends (see Combat for reach-based rules like Opportunity Attacks).

**Encumbered (items exceed Slots):** Speed drops to 5 ft; disadvantage on physical checks; cannot rest.

**Push/Drag/Lift:** Up to 2× your Slot capacity in equivalent bulk, but speed drops to 5 ft.

### **Slot Costs**

- **Tiny items** (trinkets, ammunition, small tools): 3 identical or similar items per Slot. A Belt Pouch holds 3 Tiny items for free.
- **Standard items** (most weapons, tools, clothing): 1 Slot.
- **Heavy items** (armor, larger tools): 2 Slots.
- **Bulky items** (tents, large furniture): 3 Slots.
- Anything larger: 1 Slot per 10 lb-equivalent of bulk, rounded up.
- **Coins:** 100 coins \= 1 Slot.
- **Bundles:** Torches, Candles, Rations, and Oil flasks are each sold and carried in bundles of 3 \= 1 Slot.

A **Backpack** costs no Slots itself, but is required to use your full Slot count \- without one, you can only carry STR Slots worth of gear. Worn armor and an equipped weapon or shield cost no Slots; the Slots value on an item only applies while it's carried as a spare.

---

## Resting

**Note:** Wounds do not heal on this ladder \- see Wound Recovery, above.

### **Short Rest (1 Hour)**

- No Mana recovery  
- Trauma: Medical Lore DC 15 to remove 1 level  
- Can use: Armorer (rank 3+), Medical Lore, Scribing, Prayer etc  
- Interrupted by combat

### **Field Rest (6 Hours)**

- Regain Mana equal to **MIND**  
- Trauma: Medical Lore DC 15 to remove 2 additional level  
- Can use: Armorer (rank 3+), Medical Lore, Scribing, Prayer etc  
- **Requires:** Shelter, watch rotation, defensible position, 1 ration per character

### **Long Rest (8 Hours)**

- Regain Mana equal to **MIND × 3**, up to your Maximum Mana  
- Trauma: Remove 1 level automatically, Medical Lore DC 15 to remove 2 additional level  
- Can use: Armorer (rank 3+), Medical Lore, Scribing, Prayer etc  
- **Requires:** Permanent structure in civilization with security (inn, barracks, temple, etc.)

**Note:** Field Rests and Long Rests provide no benefits if their shelter requirements aren't met.

---

## Trauma

Trauma represents accumulated stress and strain beyond Wound loss \- fatigue, privation, and the toll of pushing your body or mind past their limits. It is a separate track from Wounds and the Wound Penalty, above: those cover the physical cost of being hit, Trauma covers everything else that wears you down.

| Level | Effect              |
|:------|:--------------------|
| 1-2   | Manageable          |
| 3-4   | Dangerous           |
| 5-9   | Critical            |
| 10    | **Automatic Death** |

**Note:** These labels describe how dangerous your condition is narratively \- the mechanical penalty scales continuously (subtract your current Trauma level from all rolls). No separate effect triggers at each band on its own.

**Penalties:** Subtract Trauma level from **all** d12 rolls, wards and checks.

**Sources:** Trauma is not a byproduct of ordinary combat damage \- there is no automatic Trauma from taking a hit, dropping to 0 Wounds, or being Dying (that cost is paid through the Wound Penalty instead). Trauma accrues only from specific, named sources: privation (starvation, Forced March \- see Food and Water and Traveling), a handful of paid Feat and spell costs that explicitly grant it (Deadly Critical's crit rider, Stress Inoculation, Deep Devotion's fasting, Temporal Fortification's backlash, and similar), and anything else that explicitly says so. If a rule doesn't name Trauma, it doesn't grant it.

---

## Basic Moves

Basic Moves are the simple, universal actions everyone can take on their turn - proactively setting up an exchange, rather than the reactive Maneuver (see Combat) that answers one.

### **Dashing**

Sprint as fast as your body allows.

**Action:** Major  
**Effect:** Increase your movement this turn by an amount equal to your current speed (after all modifiers, difficult terrain, etc.).

---

### **Disengaging**

Move carefully and swiftly to avoid attacks.

**Action:** Major  
**Effect:** Until the end of your current turn, your movement does not provoke **Opportunity Attacks**.

---

### **Shoving**

Push an enemy back or knock them down.

**Action:** Major (replaces attack as a Martial Weapon Attack)  
**Check:** Athletics or Brawling vs. target's static Athletics or Acrobatics (Contested Check)  
**Success:** Push 5 ft OR knock prone

---

### **Disarming**

Force an enemy to drop their weapon or a held item.

**Action:** Major (replaces attack as a Martial Weapon Attack)  
**Check:** Weapon skill vs. target's static weapon skill (Contested Check)  
**Success:** Target drops one held item of your choice

---

### **Blind**

Throw dirt, sand, or grit into an opponent's eyes.

**Action:** Minor (one hand free)  
**Check:** **1d12 \+ your DEX \+ weapon skill** vs. target's DEX Ward (Contested Ward)  
**Success:** Target is Blinded until the end of their next turn.

---

### **Grappling**

Seize and restrain an opponent.

**Action:** Major (replaces attack as a Martial Weapon Attack)  
**Check:** Athletics or Brawling vs. target's static Athletics or Acrobatics (Contested Check)  
**Restriction:** Target at most one size larger  
**Prerequisites:** Must have one hand free

**Success:**

- Target is **Restrained**  
- You can drag and move target at half speed

**While Grappling:**

- Advantage on melee attacks against the target  
- Casting requires a MIND Ward check (DC 20\) or spell fails  
- Your melee attacks ignore half the target's AR

**Escape:** Major Action, repeat contested check.

---

### **Defensive Stance**

Adopt a protective stance that makes you difficult to hit.

**Action:** Minor  
**Effect:** Until the start of your next turn, attacks against you have Disadvantage and your Maneuver attempts have Advantage. Your damage rolls suffer \-4 until the start of your next turn.

---

### **Taunting**

Draw an enemy's focus entirely onto you, making it harder for them to threaten anyone else.

**Action:** Minor Action  
**Check:** Deception or Intimidation vs. target's MIND Ward  
**Restriction:** Target must be able to see and hear you. Target must be within 30 ft.

**Success:** Until the start of your next turn, the target has disadvantage on all attack rolls made against creatures other than you.

**Failure:** The target is unaffected and cannot be Taunted by you again until the start of your next turn.

**Limitations:**

- Does **not** work against creatures that cannot be frightened, charmed, or otherwise psychologically affected (e.g. constructs, undead without INT, etc.) \- GM's discretion.  
- Does **not** stack with itself. Taunting an already Taunted creature refreshes the duration rather than adding additional effects.

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

| Source  | Bright | Dim     | Duration             |
|:--------|:-------|:--------|:---------------------|
| Candle  | 5 ft   | \+5 ft  | 6 turns              |
| Torch   | 20 ft  | \+20 ft | 6 turns              |
| Lantern | 30 ft  | \+30 ft | 36 turns / oil flask |

**Turns:** A Turn is 10 minutes, the standard unit of dungeon/site exploration (see Dungeon Turns, Exploration). Light durations above are tracked on one shared party tracker, not per character. **Optional Rule:** groups who prefer real-time light tracking may instead treat these durations as 1 hour (Candle), 2 hours (Torch), and 12 hours per flask (Lantern) \- but this abandons the shared-tracker/wandering-encounter tie-in below.

**Low-Light Vision:** Treat dim light as bright within range.  
**Darkvision:** See darkness as dim light within range (grayscale only).
