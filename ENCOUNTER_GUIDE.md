# Encounter Balance

Building encounters starts with knowing what numbers to target. This chapter gives you a practical reference for calibrating enemy stats against player characters at each level \- without reverse-engineering every value from scratch.

---

## The Core Principle: One Defence Per Enemy

Players layer their defences across a campaign because they need to survive hundreds of fights. An enemy exists for one encounter. Design each enemy around **one defensive identity**, with at most one reactive option on top. This keeps encounters fast, distinct, and tactically readable.

When players enter a room with a knight in plate, a cloaked duelist, and a robed caster at the back, they should immediately understand they face three different problems. If all three share equally layered defences, they feel the same \- and the encounter becomes a war of attrition rather than a set of decisions.

**The exception is bosses.** Named antagonists can combine a primary defence with one reactive option (Block or Parry) and one passive trait (regeneration, non-degrading armour, damage resistance, etc.). Aim for 2–2.5× the HP of a standard enemy at the same tier.

---

## The Four Archetypes

### **Brute**

No defensive tricks. High HP and damage output that creates urgency. Brutes don't use reactions for defence \- they use them for opportunity attacks or don't use them at all. Fast to run, easy to communicate, and scary because they just *hit hard*. Use expanded crit ranges (10–12 or 9–12) to stack Exhaustion on players rather than inflating raw damage.

**Primary defence:** HP pool  
**Reaction:** Opportunity attacks (not Block or Parry)  
**Weakness:** Sustained fire; abilities that bypass or ignore armour  
**Signature trait:** Expanded crit range, Reckless Charge, Sweeping Blow, or Regeneration

---

### **Tank**

Heavy armour plus the Block reaction. Hard to damage early, but the armour degrades under pressure \- a Tank gets progressively easier to damage as the fight goes on. Design encounters with this arc in mind: the first few rounds are rough, the last few aren't. A Tank with Armorer 5+ that can field-repair mid-fight is a fundamentally different and more dangerous threat.

**Primary defence:** Armour (high AR) \+ Block  
**Reaction:** Block (prioritise over opportunity attacks)  
**Weakness:** High-damage single strikes; sustained fire that degrades AR quickly  
**Signature trait:** Field repair, Shield Bash, Bulwark (protecting allies)

---

### **Skirmisher**

High Evasion, light or no armour. Hard to hit; very squishy when you do. Best used in pairs or with a meatshield, because a solo Skirmisher that gets flanked or targeted with advantage evaporates quickly. Their danger is forcing players to chase, reposition, and split focus. Add Pack Tactics or positioning-based abilities (Shadow Step, Nimble Escape) to reward the playstyle.

**Primary defence:** Evasion  
**Reaction:** Parry (once or twice) or one Dodge  
**Weakness:** Advantage attacks; area effects that bypass Evasion; being cornered  
**Signature trait:** Pack Tactics, Nimble Escape, Poison, expanded crit range

---

### **Caster**

Low physical defences, dangerous through conditions, Ward-targeting spells, and Exhaustion stacking. Casters should almost never be alone \- they're priority targets and will die in two rounds without support. Their danger is what they do *before* they die. Give them summons, a bodyguard, or terrain advantages, and make retreating part of their behaviour.

**Primary defence:** Ward saves \+ spell reactions (Phantom Aegis)  
**Reaction:** Spell aegis, or a single Dodge  
**Weakness:** Physical attacks; being engaged in melee; Silenced condition  
**Signature trait:** AoE Ward spells, condition-inflicting spells, Mana Siphon, Summon

---

## Stat Ranges by Tier

These ranges assume no racial or career bonuses and no magic items. A **typical** player at each tier sits roughly in the middle of the player baseline range \- fully optimised characters will be near the ceiling.

AR values shown are **starting** values. Armour degrades in combat exactly as it does for players.  
Natural armour on monsters (scales, thick hide, stone skin) should be noted as **non-degrading** when you want that enemy to feel consistently threatening across the whole fight.

---

### **Tier 1 \- Levels 1–3**

**Player baselines:** Max Evasion 15–17 · Max to-hit \+10 to \+12 · HP 25–35

| Archetype | HP | AR (armour type) | Evasion | To-hit | Avg damage | Primary defence |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Brute | 25–45 | 2–4 (hide/leather) | 7–9 | \+5 to \+8 | 1d8 \+ STR 4–5 | HP pool |
| Tank | 20–30 | 6–10 (chain) | 8–10 | \+6 to \+9 | 1d6 \+ STR 4–5 | Armour \+ Block |
| Skirmisher | 14–22 | 2–3 (leather) | 11–13 | \+6 to \+9 | 1d6 \+ REF 4–5 | Evasion |
| Caster | 14–22 | 0–2 (robes) | 10–12 | \+5 to \+8 ✦ | 1d8 \+ FAI/ARC 4–5 | Ward saves |

✦ *Spell to-hit bonus.*

**Notes for this tier:** Players are fragile. A single bad round can drop a character. Brutes should feel immediately threatening. Casters at this tier have 2–3 spells maximum \- don't overcomplicate their stat block. Armour hasn't degraded far enough to matter much in short fights.

---

### **Tier 2 \- Levels 4–6**

**Player baselines:** Max Evasion 19–21 · Max to-hit \+14 to \+16 · HP 25–40

| Archetype | HP | AR (armour type) | Evasion | To-hit | Avg damage | Primary defence |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Brute | 38–55 | 3–6 (hide) | 7–9 | \+9 to \+12 | 2d6 \+ STR 6–7 | HP pool |
| Tank | 30–45 | 9–13 (brigandine) | 9–11 | \+10 to \+13 | 1d8 \+ STR 6–7 | Armour \+ Block |
| Skirmisher | 22–35 | 2–4 (leather) | 13–16 | \+10 to \+13 | 1d6 \+ REF 6–7 | Evasion |
| Caster | 22–35 | 0–3 (gambeson) | 11–13 | \+9 to \+12 ✦ | 1d10 \+ FAI/ARC 6–7 | Ward saves \+ Aegis |

✦ *Spell to-hit bonus.*

**Notes for this tier:** Players have Prestige Feat access at level 5 \- expect characters to feel more defined. Tanks can now plausibly have Armorer 3+ and repair armour during short rests. Add Pack Tactics or group dynamics to Skirmishers. Casters can begin using Phantom Aegis as their one reactive option.

---

### **Tier 3 \- Levels 7–9**

**Player baselines:** Max Evasion 22–24 · Max to-hit \+17 to \+19 · HP 28–40 · Skill cap reached at L8

| Archetype | HP | AR (armour type) | Evasion | To-hit | Avg damage | Primary defence |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Brute | 50–75 | 4–7 (monster hide) | 8–10 | \+12 to \+15 | 2d8 \+ STR 7–8 | HP pool \+ Regen |
| Tank | 40–58 | 12–15 (half/full plate) | 9–12 | \+12 to \+16 | 1d10 \+ STR 7–8 | Armour \+ Block |
| Skirmisher | 30–45 | 3–5 (leather) | 15–18 | \+12 to \+16 | 1d8 \+ REF 7–8 | Evasion \+ Parry |
| Caster | 30–48 | 0–4 (gambeson) | 11–14 | \+12 to \+15 ✦ | 2d6 \+ FAI/ARC 7–8 | Wards \+ Aegis \+ 1 Dodge |

✦ *Spell to-hit bonus.*

**Notes for this tier:** The L8 skill cap means the plateau has begun \- expect players to feel powerful between levels 9 and 11\. Skirmishers with Evasion 15–18 now force average players to roll 7+ to hit. Brutes with Regeneration create urgency (kill it before it heals). Tank field repair (Armorer 5+) is now viable \- a Tank restoring 2d6 AR in a 10-minute window is a meaningful pacing threat if the encounter is timed.

---

### **Tier 4 \- Levels 10–12**

**Player baselines:** Max Evasion 24–25 · Max to-hit \+19 to \+20 · HP 30–40 · Plateau L9–11, \+1 bump at L12

| Archetype | HP | AR (armour type) | Evasion | To-hit | Avg damage | Primary defence |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Brute | 65–95 | 5–8 (monster) | 8–11 | \+15 to \+18 | 2d10 \+ STR 9–10 | HP pool \+ Regen |
| Tank | 50–70 | 14–16 (full plate) | 10–13 | \+15 to \+19 | 2d6 \+ STR 9–10 | Armour \+ Block \+ combat repair |
| Skirmisher | 38–55 | 3–6 (leather) | 17–20 | \+15 to \+18 | 1d10 \+ REF 9–10 | Evasion \+ 2–3 Dodges |
| Caster | 38–58 | 0–5 (gambeson) | 12–15 | \+15 to \+18 ✦ | 3d6 \+ FAI/ARC 9–10 | Wards \+ Reflect \+ Aegis |

✦ *Spell to-hit bonus.*

**Notes for this tier:** Skirmisher Evasion 17–20 means players need to roll 7–11+ to hit \- these enemies feel nearly untouchable and should. Tank combat repair (Armorer 7+, Major \+ Minor action, 1/day) can restore 1d6 AR mid-fight; use it once, at a turning point. Caster Ward reflection on a missed spell punishes player casters hard \- reserve it for a boss-tier caster, not a standard enemy.

---

## Attack and Evasion Scaling Reference

The formulas that drive everything:

Attack roll: 1d12 \+ Weapon Skill \+ Attribute vs. target Evasion

Evasion: 5 \+ Agility Skill \+ DEX − Armour Penalty

Both use **Skill \+ Attribute**, so they scale identically. The permanent gap between an optimised attacker and an optimised evader is exactly 5 \- meaning the attacker always needs a **5 or higher on the d12 to hit**, giving a flat **67% hit rate at every level**. This ratio never changes as levels increase.

| Level | Skill cap | Attr max | Max attack bonus | Avg roll | Max evasion | Min to hit max evasion |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 3 | 7 | \+10 | 16.5 | 15 | 5+ |
| 2 | 4 | 7 | \+11 | 17.5 | 16 | 5+ |
| 3 | 5 | 7 | \+12 | 18.5 | 17 | 5+ |
| 4 ★ | 6 | 8 | \+14 | 20.5 | 19 | 5+ |
| 5 | 7 | 8 | \+15 | 21.5 | 20 | 5+ |
| 6 | 8 | 8 | \+16 | 22.5 | 21 | 5+ |
| 7 | 9 | 8 | \+17 | 23.5 | 22 | 5+ |
| 8 ★ | 10 | 9 | \+19 | 25.5 | 24 | 5+ |
| 9 | 10 | 9 | \+19 | 25.5 | 24 | 5+ |
| 10 | 10 | 9 | \+19 | 25.5 | 24 | 5+ |
| 11 | 10 | 9 | \+19 | 25.5 | 24 | 5+ |
| 12 ★ | 10 | 10 | \+20 | 26.5 | 25 | 5+ |

★ *Breakpoints where skill cap and attribute ceiling increase simultaneously, causing a \+2 jump to both attack bonus and max Evasion.*

**Reading this table for encounter design:**

- To-hit bonus equals (player Evasion − 5\) → enemy hits 67% of the time. This is a standard threat.
- To-hit bonus equals (player Evasion − 7\) → enemy hits on 8+. About 42%. This is a nuisance enemy or minion.
- To-hit bonus equals (player Evasion − 3\) → enemy hits on 4+. About 75%. This is a terror encounter.
- Crits (natural 12\) bypass Evasion, Block, and Parry entirely. Expanded crit ranges (10–12, 9–12) make this happen more often.

**Note:** Most players will not be fully optimised. A typical player sits 2–4 points below the max Evasion column. Calibrate enemies to a realistic party, not the ceiling.

---

## Design Principles

### **Armour degrades \- account for the arc**

A heavily armoured enemy starts the fight hard to damage and gets progressively easier. A knight in Full Plate (AR 16\) can take roughly 16 hits before their armour breaks entirely. In a long fight, that Tank is nearly unprotected by the end. Use this arc intentionally: the fight should feel grinding at first and urgent at the end as armour fails. Natural armour that doesn't degrade (scales, stone hide) tells a completely different story \- consistent and relentless \- and should be used deliberately on monsters where that reliability matters.

### **Crits are your lethality dial**

Rather than inflating raw damage, widen the crit range on dangerous enemies. Crits deal maximum damage *and* stack 1 Exhaustion (if damage exceeds AR). Since Exhaustion subtracts from all d12 rolls, a character at Exhaustion 3 is attacking, dodging, and rolling wards at −3. This compounds \- a character accumulating Exhaustion mid-fight becomes exponentially more vulnerable, which creates escalating tension without requiring more HP. A Brute with a 9–12 crit range is far scarier than one with 30 extra HP.

### **The Reaction economy is a design lever**

Most enemies have one Reaction per round. A Tank burning Block cannot take Opportunity Attacks. A Skirmisher using Parry cannot use it again until the next round. Use positioning and multiple threats to force enemies into real Reaction dilemmas \- a Tank protecting a caster ally might Block to redirect an attack, but that leaves an adjacent opening. This creates tactical depth without you having to script anything. Always note in an enemy's stat block what their Reaction *priority* is.

### **Don't inflate HP to create difficulty**

A fight that drags because the enemy has too much HP is almost always less satisfying than one that ends faster but demanded real decisions. A Skirmisher dying in 2–3 well-placed hits is correct \- those hits were hard to land. Tune for drama and decision-making, not survival time. If a fight feels too short, add another enemy or a complication; don't just add HP.

### **Enemies threaten differently**

The best encounters mix archetypes because each applies different pressure:

- **Brute** → urgency (kill it fast or die)
- **Tank** → attrition (the fight will cost you resources)
- **Skirmisher** → positioning (you can't stay still)
- **Caster** → conditions (you're weakening round by round)

A room with one of each archetype is one of the most tactically rich encounters you can run \- and it requires no special scripting.

---

# Mythic Initiative

Mythic creatures \- campaign-defining bosses and other singular threats \- do not act once per round. They are too fast, too vast, or too terrible for a single turn to contain them.

**Mythic Initiative (X):** A Mythic creature rolls initiative X times. The first roll is made normally. Each roll after the first takes a cumulative **−2 penalty** (second roll −2, third roll −4, fourth roll −6, and so on). The creature takes a **full turn** on each of its initiative counts.

All of a Mythic creature's initiative counts are public, rolled openly at the start of combat. The party always knows exactly when the beast will act \- surviving it is another matter.

**Repetition:** A Mythic creature's unique abilities (breath weapons, signature spells, lair-shaking special attacks) can each be used only **once per round**, no matter how many turns the creature takes. Basic attacks, movement, and mundane actions face no such limit.

---

## Turns & Effects

A Mythic creature's turns are real turns. Anything that references "a turn" applies to **each** of them:

- **Saves against conditions** that allow an attempt at the end of the creature's turn (Frightened, channelled spells, Creeping Rot, and similar) are attempted at the end of **every** Mythic turn. A Mythic (3) creature gets three chances per round to shake off an effect. Conditions land on Mythic creatures \- they just don't stay long.
- **Ongoing damage** such as Bleeding triggers at the start of **every** Mythic turn. A bleeding Mythic (3) creature takes its Bleed value three times per round.
- **Start-of-turn and end-of-turn traits** (regeneration, auras, recharging abilities) trigger on every turn unless the creature's statblock says otherwise.
- **Reactions:** A Mythic creature's Reaction refreshes at the start of **each** of its turns. A Mythic (3) creature can Parry, Block, or make an opportunity attack up to three times per round.

Mythic creatures do not need condition immunities or special resistances. Their many turns *are* their resistance \- and their many turns are also their weakness. Choose your poisons accordingly.

---

## Running Mythic Creatures

**Statblock math changes.** A trait that reads "regains 10 HP at the start of its turn" heals a Mythic (3) creature 30 HP per round. Write and read Mythic statblocks with the turn count in mind.

**Keep the party breathing.** The −2 stagger usually spreads a Mythic creature's turns across the round. If two of its initiative counts would ever resolve back-to-back with no player character between them, the GM may delay the later turn until at least one PC has acted. Bosses should be terrifying, not tedious.

**Bleed is boss-killer tech.** Parties will learn that stacking Bleeding punishes a creature for every turn it takes. This is intentional \- but watch the math on high-damage hits.

---

## Optional Rule: Mythic Pressure

Facing a creature that acts three or four times per round strains the party's defenses \- each character has only one Reaction per round to answer many attacks.

If your table finds Mythic fights shut down Parry, Block, and Dodge entirely, use this rule: **whenever a Mythic creature ends one of its turns, each player character regains their Reaction.** Mythic fights become the proving ground for defensive maneuvers rather than the place they stop mattering.

---

## Example: A Round Against a Mythic (3) Wyrm

The wyrm rolls initiative three times: **14**, then **11** (roll of 13, −2), then **6** (roll of 10, −4). The party rolled 13, 9, 8, and 5.

| Count | Actor | What Happens |
| :---: | :---- | :---- |
| 14 | **Wyrm (Turn 1)** | Bleeding ticks. It uses its once-per-round Fire Breath, then moves. At end of turn, it attempts a save against Grave Terror \- and fails. |
| 13 | Kaela | Lands a Trip; the wyrm is prone. |
| 11 | **Wyrm (Turn 2)** | Bleeding ticks. Its Reaction refreshes. It stands from prone, bites Kaela. End of turn: saves against Grave Terror again \- success. The fear ends. |
| 9 | Torvald | Attacks the wyrm; it spends its refreshed Reaction to Block. |
| 8 | Mirren | Casts Creeping Rot \- it lands. |
| 6 | **Wyrm (Turn 3)** | Bleeding and Creeping Rot both tick. It cannot use Fire Breath again this round, so it claws Mirren and repositions. End of turn: it attempts to fight off the Rot. |
| 5 | Osric | Acts with the wyrm's full round spent \- the safest moment to commit. |

The party knew every beat of this round before it began. The wyrm was never safe from conditions, and never helpless against them.
