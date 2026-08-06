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

**A 0 in an Attribute** is a complete absence of that capacity, not just poor - the same way an unranked Skill sits at 0 until trained. It's a legitimate choice at character creation (see [[Character Creation|character_creation]]), not only a racial exception. **An Attribute can never go below 0** - if an effect would push one lower, the character dies.

---

## Literacy

Reading and writing are far from universal in Ressam \- most people never learn.

**Automatic Literacy:** A character with **MIND 3+** at character creation is literate, able to read and write every language they know. Certain Careers (see [[Careers|careers]]) grant literacy as well, regardless of MIND.

**Below MIND 3:** Illiterate by default, unless literacy is granted by Career. Literacy determined this way is fixed at character creation \- raising MIND afterward (leveling, etc.) does not retroactively grant it.

**Learning to Read Later:** An illiterate character can still choose to learn to read during play. This isn't automatic and has no fixed cost or timeline \- work it out with your DM.

**Note:** Spellcasting requires literacy (see [[Magic Overview|magic_overview]]) \- an illiterate character cannot invest in an Arcane or Divine school, regardless of ARC or FAI, until they learn to read.

---

## Skills

Skills range from 0 (untrained) to 5 (world-renowned master). Each is tied to one attribute.

### **Skill Check Formula**

**1d12 \+ Skill Ranks \+ Attribute** vs. **DC**  
**Note:** Only call for rolls when failure is reasonably possible.

**Trained:** The Attribute only applies once you have 1 or more Skill Ranks in that skill. An untrained skill (0 Ranks) rolls **1d12** alone \- no Skill Ranks, no Attribute. This applies anywhere a Skill adds an Attribute to a roll, including Weapon Skill on Attack Rolls (see [[Combat|combat]]) and Magic School Skill on Spell Modifier (see [[Magic Overview|magic_overview]]).

### **Setting a Difficulty Class (DC)**

Ressam uses a nine-tier DC scale for Skill Checks, Ward Checks, Minor Magic, and Alchemy crafting alike. Pick a tier by how difficult the task is narratively; you rarely need to reach for a number outside this list.

| Tier | DC | Example |
| :---- | :---: | :---- |
| Very Easy | 5 | Recalling common knowledge, walking a plank |
| Easy | 8 | Climbing a knotted rope, haggling with a friendly merchant |
| Medium | 10 | Picking a simple lock, patching a minor wound |
| Tricky | 12 | Balancing on a narrow ledge, talking down a nervous guard |
| Hard | 15 | Persuading a skeptical noble, disarming a snare |
| Grueling | 17 | Picking a masterwork lock under time pressure, holding a collapsing line |
| Very Hard | 20 | Forging a noble's seal, scaling a sheer cliff in a storm |
| Incredibly Hard | 22 | Snapping manacles bare-handed, resisting a curse's full grip |
| Impossible | 25 | Outrunning a warhorse on foot, staring down a god without flinching |

**Note:** Minor Magic and Alchemy crafting no longer keep their own copy of these numbers - both read Medium, Hard, and Very Hard directly off this table, so a spell or potion pegged "Hard" in those chapters always means DC 15 here, with nothing left to fall out of sync. The top two tiers are pinned to the actual ceiling of the d12 \+ Skill \+ Attribute system: a fully capped character (Skill 5, Attribute 5, both reached by level 8\) rolling a natural 12 hits 22 with no magical help at all \- that's Incredibly Hard. Magic items add at most \+3 on top of that, putting the true maximum possible roll anyone can ever produce at 25 \- that's Impossible, reachable only by a maxed, magically-equipped character on a natural 12\. Incredibly Hard shows up informally elsewhere (breaking Chains, Curse of the Beast, casting while Restrained) for feats meant to be exceptional even for a specialist; Impossible is there to mark tasks a DM shouldn't be calling for a roll on at all \- if the answer's really "no, unless something extraordinary happens," don't make the player roll for it.

**What to expect at the table:** A character actively trained in the relevant Skill clears Very Easy through Medium almost automatically at any level, and Tricky not long after. Hard is a real coin flip early on and becomes reliable by mid-game. Very Hard is out of reach at level 1 (even a maxed roll can't touch it) and stays a real risk even at the level cap without magical help. Incredibly Hard demands nothing short of a natural 12, even from a fully capped specialist \- and Impossible needs that same natural 12 stacked with the best magic gear money can buy. Neither is meant to be routine business.

### **Success Rate by Level (Specialist)**

Derived from **1d12 \+ Skill \+ Attribute** vs. each DC tier above, assuming a specialist: Skill Rank and that check's Attribute both maxed to the current level's cap ([[Per Level Advancement|progression_&_rewards]]). A generalist spreading points across multiple Skills or Attributes rolls worse than this at every level.

| Level | Skill \+ Attribute | Very Easy (5) | Easy (8) | Medium (10) | Tricky (12) | Hard (15) | Grueling (17) | Very Hard (20) | Incredibly Hard (22) | Impossible (25) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1-2 | 2 \+ 4 \= 6 | 100% | 92% | 75% | 58% | 33% | 17% | 0% | 0% | 0% |
| 3-4 | 3 \+ 4 \= 7 | 100% | 100% | 83% | 67% | 42% | 25% | 0% | 0% | 0% |
| 5-6 | 4 \+ 4 \= 8 | 100% | 100% | 92% | 75% | 50% | 33% | 8% | 0% | 0% |
| 7 | 5 \+ 4 \= 9 | 100% | 100% | 100% | 83% | 58% | 42% | 17% | 0% | 0% |
| 8-12 | 5 \+ 5 \= 10 | 100% | 100% | 100% | 92% | 67% | 50% | 25% | 8%\* | 0%\* |

\*Incredibly Hard only clears on a natural 12, even at the level 8+ cap; Impossible needs that same natural 12 plus the full \+3 a magic item can add, which this table doesn't include - see the Note above. Nothing here accounts for situational Advantage/Disadvantage either.

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

**Exception:** Divine spellcasting doesn't use a Contested Check at all - every Divine spell rolls against a flat DC instead of a target's Ward or Evasion, on purpose (see [[Magic Overview|magic_overview]]'s Petition Roll).

---

## Basic Moves

Basic Moves are the simple, universal actions everyone can take on their turn - proactively setting up an exchange, rather than the reactive Maneuver (see [[Combat|combat]]) that answers one.

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

### **Feint**

Use guile to open an opponent up to your strikes.

**Action:** Minor  
**Check:** Deception vs. target's static Insight (Contested Check)  
**Success:** You gain advantage on the next weapon attack you make this turn.

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

**Continued in:** [[Wounds & Survival|wounds_and_survival]] (Damage Types, Wounds and Survival, Trauma), [[Carrying & Resting|carrying_and_resting]] (Slots, Resting), and [[Stealth & Light|stealth_and_light]] (Stealth and Hiding, Light and Vision).
