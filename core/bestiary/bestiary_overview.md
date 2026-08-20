NPCs in Ressam are not built to keep pace with the party. There is no Threat Level to look up, no ratio of Easy/Average/Elite per player, no formula that reads the party's current level and hands back a bigger number. A stat block here is written once, at a fixed set of Attributes and Skills, and it stays that way for the life of the campaign - a Bandit a level 1 party meets is the exact same Bandit a level 10 party meets later. What changes over time is the party, not the world around them.

This works because Attributes and Skills share one cap across every character in the game, PC or NPC alike - Attribute 5, Skill 5, the same ceiling [[Character Creation|character_creation]] and [[Progression & Rewards|progression_&_rewards]] describe for players. A veteran built at or near that ceiling doesn't need to scale up to stay dangerous; the math was already sitting at the top of the game's range the day they were written. That's also why a **Knight** is a fundamentally different kind of threat than a **Peasant** - not a bigger number pasted onto the same template, but a career's worth of training expressed in the same Attribute/Skill/gear math a player would use to build their own character.

---

## Reading a Stat Block

Every entry lists exactly what a GM needs at the table and nothing else - Slots, Mana Points, and other bookkeeping that only matters for a character sheet are left out on purpose.

- **Frequency:** How likely a GM is to actually field this creature in its home region - see Frequency, below.
- **Attributes / Skills:** Only Skills relevant to this NPC's kit are listed; anything unlisted is 0 (untrained).
- **Wounds:** Size baseline (Medium \= 3 for every entry here) plus any Feat that adds to it.
- **Wound Threshold:** How much damage-after-AR it takes to inflict 1/2/3 Wounds in one hit, keyed to this NPC's own STR - see [[Wounds and Survival|wounds_and_survival]]. Given as three bands (e.g. `1 Wound (1-7), 2 Wounds (8-13), 3 Wounds (14+)`) so a GM doesn't have to cross-reference that table's STR row mid-fight.
- **Tempo Pool:** `DEX + 1` dice, never fewer than 1, sized by STR - see [[Your Tempo Pool|exchange]]. This is the whole of an NPC's off-turn economy: it pays for every Parry and Opportunity Attack the same way it does for a PC.
- **AR:** Current Armor Rating from worn or natural armor - see [[Armor|armor]]. A shield's Guard is not AR; it adds to the Parry roll instead (below).
- **Parry:** `1d(Tempo Die) + Weapon Skill + Guard + Edge`, the same formula a PC rolls - see [[Defending|exchange]]. Costs 1 Tempo Die, same as everything else in an Exchange.
- **Attack:** The Skill Rank added to `1d(Tempo Die) + Weapon Skill` on an attack roll ([[Attacking|exchange]]) - `-` means the attack rolls the die alone (untrained: 0 Skill Ranks add nothing).
- **Damage:** Weapon Damage \+ STR (or \+ DEX for a missile weapon), before the target's AR is subtracted.
- **Wards:** Passive Ward scores (`5 + Attribute`) for the Attributes this NPC's kit actually calls on - STR, DEX, MIND.
- **Movement:** Walking Speed in feet, plus any secondary Speed (flying, climbing) it has. Armor Penalty never reduces this - it restricts Acrobatics, Subterfuge, and spellcasting, but not raw Speed and nothing in an Exchange (see [[Armor|armor]]).
- **Initiative:** `5 + MIND`, static and never rolled - see [[Initiative and turn order|exchange]].
- **Mythic Initiative / signature abilities:** [[Mythical|mythical]] entries only - see that page's own note before pricing one.
- **Fielding Guide:** Where present, a rough per-Level headcount ceiling for a 4-PC party - simulated with `tools/bestiary_sim.py`/`tools/rest_pressure_sim.py`, not eyeballed. Read these as a floor, not literal odds: the simulation can't see retreat, positioning, mid-fight healing, or spellcasting, and all of those favor the party in real play. "Past this count, treat it as a genuine threat" is the intended read, not "this many equals this percent chance of winning." Only a handful of entries have one so far - its absence elsewhere isn't a claim that headcount doesn't matter, just that the count hasn't been run yet.

> **This guide is written for the Tempo Pool/Exchange combat system, current as of the 2026-08-23 Exchange merge. The stat blocks in [[Universal|universal]] and [[Mythical|mythical]] are not yet converted** - they still show `Evasion`, a flat `Attack` bonus, and a `Reactions`/`Maneuver`/`Block` line from the combat system the merge deleted, matching neither this guide nor `core/combat/exchange.md`. Until they're rewritten, read past those lines: the Attributes and Skills each entry lists are enough to derive its actual Tempo Pool, Parry, and Attack roll under the current rules. This mirrors how `tools/combat_engine.py` and its dependents are deliberately left stale post-merge - see `CLAUDE.md`.

---

## Frequency

Every entry's Frequency tag says how likely a GM is to actually put it in front of the party in its home section, and sets the reading order within that section (Common first, Very Rare last) - it's an organizational aid, not a formal random-encounter table. Wandering Encounters ([[Dungeon Turns|dungeon_turns]]) stay GM-discretion ("roll a check per your usual frequency") - nothing here plugs into a dice-driven roll table.

- **Common:** The default filler of that section; a GM reaches for this first.
- **Uncommon:** A real but less frequent sight; shows up with intent, not by default.
- **Rare:** A notable encounter in its own right; the party should remark on seeing one.
- **Very Rare:** Borders on a set-piece; encountering one is closer to a plot beat than a random fight.

---

## Sections

Eleven sections, each its own page: [[Universal|universal]] first, then the nine continents of [[Geography|geography]] in the order that chapter presents them, then [[Mythical|mythical]] last.

### Universal

Creatures with no race or continent tied to them - built once, reused anywhere in Ressam without reskinning. Peasant, Bandit, Guard, Wolf, and Knight all live here, among others.

### Aurkhan

Dense jungle and wetlands, thick with divine-charged growth. Aelf and Tapio territory.

### Lustralis

Desert, savannah, and coastal rainforest. Human and Alsahli lands; Varulf haunt the misted inland woods.

### Inggaz

Molten plains in the north, frozen wastes in the south. Orkh warbands and Khoridae citadels.

### Terrevault

Mountain ranges and terraced valleys. Dwergaz halls, with Tierratuar roaming the higher peaks.

### Gelidia

Tundra, glaciers, and icy fjords. Dzinari sanctuaries and Feliid snow-forests.

### The Gran Mar

The Central Sea and its trade islands. Maritime encounters, rogue storms, and the ports between the other eight.

### The Southlands

A cursed, undead-infested wasteland - almost uninhabited, and what wildlife remains is twisted and aggressive.

### Halig

Temperate highland plains, currently a warzone between the Halig and the invading Orkhaden Horde.

### Trere

A north-to-south gradient from desert to rainforest. Home to Mafsoleios and the Gilded Hwispian Maw.

### Mythical

Singular, campaign-defining threats carrying Mythic Initiative - not tied to a continent by default, and mechanically distinct from a merely Very Rare entry elsewhere in this bestiary. See that page's own note on why Power Score can't price what lives here.

---

## Mythic Initiative

Mythic creatures \- campaign-defining bosses and other singular threats \- do not act once per round. They are too fast, too vast, or too terrible for a single turn to contain them.

**Mythic Initiative (X):** the creature takes a full turn at its Initiative (`5 \+ MIND`, static \- nobody rolls initiative, see [[Initiative and turn order|exchange]]), and another at every **\-2** below it, X counts in all. A Mythic creature with Initiative 11 and Mythic Initiative (4) acts on **11, 9, 7 and 5**.

All of a Mythic creature's counts are public and stated openly at the start of combat. The party always knows exactly when the beast will act \- surviving it is another matter.

**Its Tempo Pool refills in full on its first count, and it regains 1 die on each count after that.** A Mythic (4) creature with DEX 3 opens the round with 4 dice and sees 7 across the whole of it \- deep, and drainable. **Shock still takes dice off it**, an emptied Mythic creature still eats unanswered blows and Openings, and a party that concentrates can still strip it between counts. What Mythic buys is that it refills three more times than you do.

**Repetition:** A Mythic creature's unique abilities (breath weapons, signature spells, lair-shaking special attacks) can each be used only once per round, no matter how many turns the creature takes. Basic attacks, movement, and mundane actions face no such limit.

### **Turns & Effects**

A Mythic creature's turns are real turns. Anything that references "a turn" applies to each of them:

- Saves against conditions that allow an attempt at the end of the creature's turn (Frightened, channelled spells, and similar) are attempted at the end of every Mythic turn. A Mythic (3) creature gets three chances per round to shake off an effect. Conditions land on Mythic creatures \- they just don't stay long.
- Ongoing damage such as Bleeding triggers at the start of every Mythic turn. A bleeding Mythic (3) creature takes its Bleed value three times per round.
- Start-of-turn and end-of-turn traits (regeneration, auras, recharging abilities) trigger on every turn unless the creature's stat block says otherwise.
- **Tempo Dice:** its pool tops up on each of its counts as described above, so a Mythic (3) creature Parries and makes Opportunity Attacks out of a pool that is replenished three times a round rather than once.

Mythic creatures do not need condition immunities or special resistances. Their many turns are their resistance \- and their many turns are also their weakness. Choose your poisons accordingly.
