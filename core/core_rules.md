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

**Note:** Advantage is typically worth the equivalent of a \+2 bonus, while disadvantage is worth \-2.

**Time Scale:** A round represents roughly 3 seconds of in-fiction time.

---

## Attributes

Attributes range from 0 (wholly absent) to 5 (peak mortal potential).

| Attribute | Abbr. | Governs |
| :---- | :---: | :---- |
| **Strength** | STR | Physical power, melee damage, the size of your Tempo Die, carrying slots, resisting fatigue |
| **Dexterity** | DEX | Agility, fine motor control, ranged accuracy and damage, the size of your Tempo Pool |
| **Mind** | MIND | Intelligence, reasoning, mana pool, initiative |
| **Arcane** | ARC | Arcane magical aptitude |
| **Faith** | FAI | Divine connection and conviction |
| **Charisma** | CHA | Social influence, force of personality |

**A 0 in an Attribute** is a complete absence of that capacity, not just poor - the same way an unranked Skill sits at 0 until trained. It's a legitimate choice at character creation (see [[Character Creation|character_creation]]), not only a racial exception.

**An Attribute can go below 0.** A racial modifier landing on an Attribute you assigned a 0 leaves you at \-1 or lower, and that is a legal character - a negative score simply subtracts wherever the Attribute is added. **Nothing in Ressam damages an Attribute**, so a negative score is always something you built, never something inflicted on you mid-campaign. Three derived stats floor rather than follow it down: a **Tempo Pool** is never fewer than 1 die, and **Mana** and **Slots** never fall below 0 (see [[Calculate Derived Stats|character_creation]]).

**Note:** For what each Attribute represents in play, see [[Attributes & Skills|attributes_and_skills]].

---

## Literacy

Reading and writing are far from universal in Ressam \- most people never learn.

**Automatic Literacy:** A character with **MIND 2+** at character creation is literate, able to read and write every language they know. Certain Careers (see [[Careers|careers]]) grant literacy as well, regardless of MIND.

**Below MIND 2:** Illiterate by default, unless literacy is granted by Career. Literacy determined this way is fixed at character creation \- raising MIND afterward (leveling, etc.) does not retroactively grant it.

**Learning to Read Later:** An illiterate character can still choose to learn to read during play. This isn't automatic and has no fixed cost or timeline \- work it out with your DM.

**Note:** Spellcasting requires literacy (see [[Magic Overview|magic_overview]]) \- an illiterate character cannot invest in an Arcane or Divine school, regardless of ARC or FAI, until they learn to read.

---

## Skills

Skills range from 0 (untrained) to 5 (world-renowned master). Each is tied to one attribute. **A Skill's Rank can never exceed its governing Attribute's current score** - this is the only cap a Skill has (see [[Character Creation|character_creation]] and [[Per Level Advancement|progression_&_rewards]]), no separate level-gated limit exists.

### **Skill Check Formula**

**1d12 \+ Skill Ranks** vs. **DC**  
**Note:** Only call for rolls when failure is reasonably possible. An untrained skill (0 Ranks) rolls **1d12** alone.

### **Setting a Difficulty Class (DC)**

Ressam uses a seven-tier DC scale for Skill Checks, Ward Checks, Minor Magic, and Alchemy crafting alike. Pick a tier by how difficult the task is narratively; you should not need a number outside this list.

| Tier | DC | Example |
| :---- | :---: | :---- |
| Very Easy | 4 | Recalling common knowledge, walking a plank |
| Easy | 6 | Climbing a knotted rope, haggling with a friendly merchant |
| Medium | 8 | Picking a simple lock, patching a minor wound |
| Hard | 10 | Balancing on a narrow ledge, talking down a nervous guard |
| Very Hard | 12 | Persuading a skeptical noble, disarming a snare |
| Grueling | 14 | Picking a masterwork lock under time pressure, holding a collapsing line |
| Legendary | 16 | Forging a noble's seal, scaling a sheer cliff in a storm |

**Every roll in this game is `1d12` plus a single number from 0 to 5** \- Skill Ranks on a Check, an Attribute on a Ward. Three consequences are worth knowing before you set a DC:

- **Two points of DC is exactly one step of one in six.** The d12 is flat, so there is no curve to reason about: each tier you climb costs the roller 16.7 percentage points, every time, at every modifier.
- **The highest total anyone can roll is 17** (a natural 12 at the mod-5 ceiling), so **16 is the hardest DC in the game** and 17 is the only number above it that is even theoretically live. A specific piece of gear may add to one particular check ([[Supplies|supplies]]); nothing lifts the general ceiling.
- **A DC more than 12 above the roller's modifier cannot be beaten at all.** There is no natural-12 escape hatch and no critical success anywhere in Ressam. If the fiction demands a number that high, **say no instead of calling for a roll** \- a die that cannot succeed is worse than a ruling, because it tells the player they had a chance.

### **Wards are not Skill Checks, and should not take the same DC**

A Skill Check is something a character **opted into** with training they chose to buy. A Ward Check is the opposite: the danger names the Attribute, and the roller has no say in which one. A standard array leaves most characters with **two Attributes at 0** ([[Assign Attributes|character_creation]]), so a randomly-aimed Ward is answered with a modifier of about 1, not the 2-5 a specialist brings to their own Skill.

**Set a Ward one tier lower than you would set the same fiction as a Skill Check**, and **do not put an unannounced hazard above Very Hard (12)**. Grueling and Legendary Wards are for named, telegraphed threats - a dragon drawing breath, a curse the party walked into knowingly - not for a trap in a corridor. At Legendary, a Ward is not a roll at all for anyone who did not build that Attribute; it is damage with a die attached.

### **Success Rate by Skill Rank / Attribute**

Derived from **1d12 \+ Skill** (Skill Checks) or **1d12 \+ Attribute** (Wards, all of which are Attribute-funded) vs. each DC tier above - the same six rows serve every case, since each roll only ever adds a single 0-5 stat. Level does not determine this directly: only reaching a Skill's governing Attribute does, and that is a build choice. **Modifier 5 requires Attribute 5**, which needs all three of the increases granted at Levels 4, 8 and 12 poured into one Attribute, and so cannot exist before Level 12 for any character who did not start with a 3 ([[Per Level Advancement|progression_&_rewards]]).

| Skill Rank / Attribute | Very Easy (4) | Easy (6) | Medium (8) | Hard (10) | Very Hard (12) | Grueling (14) | Legendary (16) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 (untrained) | 75% | 58% | 42% | 25% | 8% | 0% | 0% |
| 1 | 83% | 67% | 50% | 33% | 17% | 0% | 0% |
| 2 | 92% | 75% | 58% | 42% | 25% | 8% | 0% |
| 3 | 100% | 83% | 67% | 50% | 33% | 17% | 0% |
| 4 | 100% | 92% | 75% | 58% | 42% | 25% | 8% |
| 5 | 100% | 100% | 83% | 67% | 50% | 33% | 17% |

Nothing here accounts for situational Advantage or Disadvantage.

**What to expect at the table:** a character trained in the relevant Skill clears Very Easy and Easy almost automatically, and Medium comfortably. **Hard is the honest middle** - a coin flip for an expert, a quarter for someone who never trained it. **Very Hard stays a real risk for an entire career**: it tops out at 50% even for a fully capped specialist and never becomes routine. **Grueling locks out the untrained completely** and asks a specialist to accept 1-in-3. **Legendary is for one character at the table, in the one thing they built** - it does not exist for anybody else, and setting one for a whole party is setting an auto-fail for most of them.

**Note:** For the full list of Skills grouped by category, and what each one actually covers, see [[Attributes & Skills|attributes_and_skills]].

---

## Checks vs. Ward

**Skill Checks** are an *active attempt* at applying your training against the world - climbing a cliff, picking a lock, forging a seal. Roll **1d12 \+ Skill Ranks** ≥ DC. An untrained skill (0 Ranks) rolls **1d12** alone.

**Ward Checks** are the opposite: a *reactive attempt* to avoid or mitigate something happening to you - not a conscious choice so much as your body's trained or instinctive response to danger. Every Ward is funded by the relevant **Attribute** - STR Ward, DEX Ward, and so on - a raw defensive capacity every creature has whether or not they've trained for it, with no trained Skill standing between raw Attribute and the danger. Roll **1d12 \+ the relevant Attribute** ≥ DC.

**A Ward is not a combat defense.** Answering a weapon is a **Parry**, paid for with a Tempo Die and rolled off your Weapon Skill (see [[Defending|exchange]]); Wards answer everything that isn't a blade in front of you - a spell's Overcome, a poison, a fall, a shove from a Feat. There is no passive score standing between you and an attack.

**Passive Ward \= 5 \+ the relevant Attribute** \- a quick-reference defensive score standing in for a Ward Check without requiring you to roll.

| Situation | Roll Type       |
| :---- |:----------------|
| Climbing a cliff | Athletics Check (Skill) |
| Grabbing a ledge when pushed | STR Ward (Attribute)        |
| Sneaking past guards | Stealth Check (Skill)   |
| Resisting a spell's Overcome | The Ward the spell names (Attribute) |

**Contested Checks:** Whenever a Feat, Feature, or Spell pits one creature's active roll directly against another's static defense (rather than a flat DC from the tier table above), only the instigator rolls - the defender's score simply stands, whatever it is. This always plays out as one of two shapes, the same two tags you'll see inline throughout the rest of this book:

- **Contested Check** (one character's training set directly against another's - out-forging a rival smith's work, shouting down a herald, matching a scholar's recall): a battle of training against training. The instigator rolls **1d12 \+ their Skill** (their Spell Modifier, for spells); the defender's static score is **5 \+ their relevant Skill** - a Passive Skill, the same shape as a Passive Ward but built from a Skill instead of an Attribute. **No published rule currently calls for one** - the combat maneuvers that used to (Grapple, Disarm, Taunting) are all Openings under [[The Exchange|exchange]] now. It is kept as a shape for a DM to adjudicate against, not a mechanic anything reaches for.
- **Contested Ward** (a Spell Overcome against a Ward, resisting a Petrifying Glare, and the like): a battle of skill - or raw instinct - against reactive ability. The instigator rolls **1d12 \+ whatever Skill, Spell Modifier, or Attribute the ability calls for**; the defender's static score is their **Passive Ward**.

The defender never rolls. Ties go to the instigator, same as a Skill Check meeting a DC exactly.

**Exception:** Divine spellcasting doesn't use a Contested Check at all - every Divine spell rolls against a flat DC instead of a target's Ward, on purpose (see [[Magic Overview|magic_overview]]'s Petition Roll).

---

**Continued in:** [[The Exchange|exchange]] (melee combat entire - the Tempo Pool, Distance, Attacking, Defending, Openings, Shock, Initiative and Surprise), [[Combat|combat]] (action economy, the damage roll, armor), [[Wounds & Survival|wounds_and_survival]] (Damage Types, Wounds and Survival, Conditions, Trauma), [[Carrying & Resting|carrying_and_resting]] (Slots, Resting), and [[Stealth & Light|stealth_and_light]] (Stealth and Hiding, Light and Vision).
