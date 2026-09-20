## Carrying Capacity

**2026-09-20:** carrying capacity is one pool, not two. **Slots \= 6 \+ STR, minimum 1.** Whatever you're actively wearing or wielding \- one weapon, one suit of armor, one shield \- is free; every other item you carry, including each bundle of ammunition, costs **1 Slot**, spares included. There's no tier to look up beyond that: count what's in the pack.

**Encumbered** (items exceed your Slots): Speed drops to 5 ft; disadvantage on physical checks; cannot rest. **Push/Drag/Lift:** up to 2x your Slots in equivalent bulk, but Speed drops to 5 ft.

**Size** (see below) - How much room a creature occupies, in grid squares (see [[Battlemap \& Positioning|positioning]]).

| Size | Wound boxes | Space (Squares) |
|:------:|:-----------:|:---------------:|
| Small | 4 | 5 ft (1x1) |
| Medium | 5 | 5 ft (1x1) |
| Large | 6 | 10 ft (2x2) |

Huge and bigger aren't player-legal Sizes; a GM statting one is free to keep scaling Wound boxes up.

---

## Rest & Repair

Bodies and gear recover on the same schedule.

| Rest | Length | Wounds healed | Armor & shields repaired | Will (see [[Magic Overview|magic_overview]]) |
|:----------|:--------------------------------------------------------------------|:---------------------------------------------------------|:--------------------------------------------------------------------------------|:-----------------------------|
| Short | A pause of minutes to an hour, catching your breath between fights | None | None | 1 |
| Field | A night camped outside a town \- shelter, watch rotation, 1 ration per character | 1 | 1 point to each line (Dent, Rend, Guard) | Equal to MIND, minimum 2 |
| Long Rest | A full day, in a town, with Good Shelter and Good Food | 1, or 2 if a medic passes a Chirurgery check (DC 7) that day | 1 point to each line, or 2 if a smith passes a Smithing check (DC 7) that day | Full |

**A character cannot take more than 2 Short Rests per day**, and a Short Rest only counts against that cap if something happened first \- a fight, a scene, a stretch of travel. **A character benefits from at most one Field Rest per day.** Long Rest needs no such cap.

**Every rest, Short included, ends any Sustained working the character is maintaining** (see [[Magic Overview|magic_overview]]).

**Repair never exceeds an armor or shield's printed starting values** (see [[Armor|armor]] and [[Weapons|weapons]]) \- Dent, Rend, and Guard each cap where they began. Chirurgery checks need a Healer's Kit; Smithing checks need Armorer's Tools (see [[Supplies|supplies]]).

**Trauma never comes down on this ladder.** Rest heals bodies and gear, not minds \- see [Revelry \& Leisure](#revelry--leisure), below, for the only thing that clears it.

---

## Damage Types

Every instance of damage \- a weapon's die, a working's damage, a Feat's rider, a fall \- belongs to one of three categories: **Physical**, **Elemental**, or **Occult**. A target's Dent Line and Rend Line read every damage type identically (see [[Dent Line and Rend Line|armor]]).

### Physical

**Piercing, Slashing, Blunt** (a weapon's listed damage type, see [[Weapons|weapons]]) and **Poison** (envenomed weapons and toxins, see [[Alchemy|alchemy]]). Mundane damage, delivered by a blade, a blow, or a coating. **Each type now carries one rule, and only one:**

| Type | What it does |
|:-----|:-------------|
| **Blunt** | Degrades both of a target's worn armor lines by **2** per landed hit instead of 1 \- **Unarmed** is the exception, at 1. |
| **Piercing** | At **Normal Reach**, against a **Restrained or Downed** target, treats their armor as None for that hit (see [[Armor and Wounds|exchange]]). |
| **Slashing** | Nothing special \- which is why the biggest dice in the weapon list are Slashing. |

**Magical vs. Non-magical:** Physical damage carries a second, independent tag \- whether its source is magical. An ordinary weapon, an unarmed strike, or a natural weapon with no stated exception deals **non-magical** Physical damage; an enchanted weapon or a natural weapon a race explicitly calls magical (a Varulf's Claws and Bite) deals **magical** Physical damage. Elemental and Occult damage is always magical, so this tag only matters for Physical - it exists because a handful of traits scope their protection to only one half of it (Windform's immunity to non-magical Physical damage while incorporeal, Invocation's Apotheosis granting resistance to it).

### Elemental

**Fire, Cold, Lightning, Acid.** Primal forces, sourced from the natural world even when magic is what channels them.

### Occult

**Necrotic, Radiant, Psychic.** Forces with no physical or elemental analogue: life-force drain and the touch of undeath (Necrotic), divine light and judgment (Radiant), a direct assault on the mind (Psychic). **A working carries no damage type at all** (see [[Designing Workings|magic_overview]]) - none of the type rules above ever reach one, since a working bypasses armor outright rather than needing to defeat it.

### Reflavored Damage

A Feat or trait that reskins damage into its own named identity (Blood-Rule's **Bloodfire**, for a Stryg) creates a distinct type in its own right, not a costume worn over the mundane type it resembles. Slot a reflavored type into whichever of the three categories above actually fits its fiction rather than inventing a fourth category. Unless a trait explicitly says its reflavor keeps interacting with the original type, treat the two as unrelated for Resistance, Vulnerability, and Immunity purposes.

### Resistance, Vulnerability, and Immunity

- **Resistance** to a damage type: halve incoming damage of that type (round down), before it's compared to the target's Dent Line and Rend Line.
- **Vulnerability** to a damage type: double incoming damage of that type, before comparison.
- **Immunity** to a damage type: take no damage of that type at all \- it never reaches a Dent Line or Rend Line.

**Order of operations:** apply Resistance, Vulnerability, and Immunity to the raw damage roll first; the adjusted total is then compared to the target's Dent Line and Rend Line as normal. A hit still degrades armor regardless of how many Wounds it ends up dealing \- these three change how much you're hurt, not whether you were hit.

**Stacking:** multiple sources of Resistance to the same type don't stack \- still just half. Resistance and Vulnerability to the same type cancel out entirely.

---

## Wounds & Death's Door

**2026-09-20 (the Reach/Tempo rework):** this whole section replaces the old Wound Threshold/Death Clock/Patched Wounds/damage-flavored Scars system outright - see [[Damage Roll|combat]] for the roll itself.

### Named Characters

**Named** means player characters and any NPC the GM gives a name. Named characters go to **Downed** when their Wounds fill (below). **Named NPCs** also have MIND 1 minimum (see [[Magic Overview|magic_overview]]). Everyone else is **Unnamed** and has neither - rank and file simply die when their Wounds fill.

**Named status only ever touches Wounds, Downed, and what a failed Nerve check costs** (see [[Morale|exchange]]). Every other track - Trauma included - works identically for Named and Unnamed alike.

A creature's Attributes, Skill, weapon, armor, and Tempo Pool size are built the same way a PC's are - there's no separate stat block format.

### Wound Penalty

Each Wound you're currently missing from your maximum imposes **`\-1` to Checks**, cumulative - a character missing 3 of 5 Wounds checks at `\-3`. This includes Ward Checks, Chirurgery, Resolve checks, and Nerve. **It never touches a Tempo roll** - attacks, Parries, shots, casts, and resists are unaffected, so there is no combat death spiral: a character on their last Wound still fights at full capability. The cost of injury lands on the strategic layer, not the fight you're bleeding in.

**A hit that deals 2 Wounds also deals 1 Trauma** (see [Trauma](#trauma), below).

### Downed

When your last Wound box fills:

- **Unnamed** characters die.
- **Named** characters are **Downed** instead. Any Wounds beyond the last box are ignored.

While Downed, you're **Prone**, can't stand, and can't take a Major Action. **Any further Wound kills you.** You can still Parry, at most 1 die. Armor still protects you against Blunt and Slashing - a hit that's Turned Aside deals no Wound - but **a Normal-Reach Piercing weapon finds the gaps** (see [[Armor and Wounds|exchange]]), so the dagger standing over you is the thing to fear, harness or no harness.

**A Downed creature doesn't threaten.** It isn't a living enemy for Engaged (see [[Distance \& Reach|exchange]]) and can't make Opportunity Attacks or take Openings. Allies can walk past or away from it freely.

**Getting up.** Healing 1 Wound ends Downed. In a fight, an Adjacent ally can use their Major Action and a Healer's Kit to attempt a **Chirurgery check (DC 7)**; success heals 1 Wound. An Adjacent ally can instead administer a Healing Draught with their Minor Action (see [[Supplies|supplies]]) - **a Downed character can't drink one themselves**, and nobody gets up alone.

**Every Wound healed costs 1 Trauma, however and whenever it happens** - a Chirurgery check, a draught, a working, or a Rest. A fight that draws blood leaves a mark even on a decisive win. **Standing back up mid-fight costs 1 further Trauma on top of that.**

**Dragging.** An ally Adjacent to a Downed or Restrained creature can move it with them; every square they move counts double, as difficult terrain does. Dragging a Restrained creature this way doesn't end the Grapple.

### Falling

Take 1d6 Blunt damage per 5 ft fallen, and the creature is forced Prone unless the damage is avoided. Deliberately jumping reduces the number of dice rolled by 4d6 (minimum 0). Landing on soft surfaces may reduce damage by half (GM discretion).

### Food and Water

On average, a character can go three days without rations; each day after, they gain a level of Trauma and cannot be healed until they've consumed a ration. A full day of hex travel also consumes 1 ration per character (see [[Traveling|traveling]]).

### Suffocation

You can hold your breath for STR minutes. After that, you drop straight to Downed (Named) or death (Unnamed) and begin taking 1 Wound per round until it ends.

### Environmental hazards

Falling aside, an environmental hazard (fire, drowning, poison, and the like) deals **1 Wound**, or **2** if the GM judges the hazard severe enough to reach the Rend line. No roll, no armor - a GM call on severity, not a subsystem.

---

## Trauma

**2026-09-20:** shared with [[Magic Overview|magic_overview]] - one **0-20** track, not just a combat one. Wounds are what kill your body; Trauma is what breaks you. When Trauma reaches 20, the character dies.

| Trauma | Band | Reached by |
|:------:|:--------------------|:--|
| 0-4 | Clear | A few Exerts, a Push or a Channel |
| 5-9 | Manageable | Patching up after a fight or two: every healed Wound taxes it |
| 10-14 | Dangerous | An expedition without a town, healing up after several fights |
| 15-19 | Critical | Stacking every source across a long trip \- and a Resolve check (see [Scars](#scars), below) if a fight ends here |
| 20 | **Automatic Death** | \- |

**Trauma carries no roll penalty of its own** - see [Wound Penalty](#wound-penalty), above, for what a roll actually loses to injury. Trauma's own cost is longer-range: it gates Scars (below) and kills outright at 20.

You gain Trauma from:

- **A hit that deals 2 Wounds:** 1.
- **Healing a Wound, by any means** (see [Downed](#downed), above): 1 per Wound, Rest included.
- **Standing back up from Downed mid-fight:** 1 further, on top of the Wound healed.
- **Exerting** (see [[Exerting|exchange]]): 1 per Exert die, flat, at most 1 die per Parry.
- **Failing a Fear check** (see [[Fear|exchange]]): 1.
- **Failing a Nerve check, Named characters only** (see [[Morale|exchange]]): 1 per failed check.
- Channelling, Pushing a roll, and certain workings - see [[Magic Overview|magic_overview]].

**Trauma never comes down in the field.** Rest heals Wounds, not minds - the only way Trauma comes off is [Revelry \& Leisure](#revelry--leisure), below, in a town.

---

## Revelry & Leisure

Downtime spent relaxing in a town is the only thing that clears Trauma.

**Each character chooses how many nights to spend, 1 to 7, and rolls `1d12` per night.** Cost is set per night by the town and party's means - a placeholder of **10 Crown per character, per night** is a reasonable starting point until [[Supplies|supplies]]'s price list is checked against it.

**Roll each die separately against DC 5, minus your Wound Penalty.** Each success removes **2 Trauma**; each failure removes **1**. Recompute your Wound Penalty before each night's roll - Wounds closing mid-stay lower the penalty on later nights.

Then count the dice:

- **More successes than failures:** gain a **boon** - a contact, a rumor, a favor owed.
- **More failures than successes:** a **Mishap** - a debt, a brawl, a loose tongue, lost gear.
- **Tied:** just the rest.

An odd number of nights can never tie, so a 1-, 3-, 5-, or 7-night stay always ends in a boon or a Mishap. The GM describes both. Nights of revelry are still days in town for [Rest \& Repair](#rest--repair).

Chirurgery handles bodies and Scars. Revelry & Leisure handles minds.

---

## Scars

The number comes down. The marks do not.

**Your Scar Line is the highest Trauma band you have ever checked at** - Clear, Manageable, Dangerous or Critical. It starts at Clear and is one value on your character card.

**When a fight ends, compare your band to your Scar Line.** If your band is higher, make one **Resolve check** for each band you climbed, then set your Scar Line to your current band. If your band is equal or lower, nothing happens.

**Your Scar Line drops whenever your Trauma drops into a lower band**, however that happens - Revelry & Leisure, or a working that moves Trauma. Climb back later and that band checks again.

**Resolve check:** `1d12 \+ CHA` against the band's rung, minus your Wound Penalty - the same ladder as every other DC in the game.

| Band reached | DC |
|:----------------|:--:|
| Manageable (5) | 7 |
| Dangerous (10) | 9 |
| Critical (15) | 11 |

**Pass, and the fight leaves no mark.** **Fail, and roll `1d6` on the table below**, or let the GM choose one that fits what happened.

**If you roll a Scar you already hold, or one that would have no effect on you** (Hollow at MIND 0, say), **you take Steeled instead** - or nothing at all, if you already hold Steeled. One roll, one outcome; never a reroll.

| `1d6` | Scar | Effect |
|:-----:|:-----------------|:-----------------------------------------------------------------------------------|
| 1 | **Flinching** | You cannot Exert. |
| 2 | **Haunted** | Your first Parry each fight costs 1 extra Tempo Die. |
| 3 | **Hollow** | Your Will pool is reduced by your MIND (see [[Magic Overview|magic_overview]]). |
| 4 | **Wary** | You cannot take Openings. |
| 5 | **Hair-Trigger** | On your first turn of any fight you must attack the nearest enemy if you are able. |
| 6 | **Palsied** | `\-1` to damage totals, minimum 1. |
| \- | **Steeled** | The first Trauma you would take in any fight is ignored. |

Scars are untouched by Revelry & Leisure. They come off only with treatment in a town: one week of downtime and a **Chirurgery check (DC 11)**, one Scar at a time. **Steeled is permanent and is never treated away.** A character can hold more than one Scar, and they stack.

---

## Conditions

Conditions can be applied by numerous different sources and in a multitude of ways, magically or mundanely.

| Condition | Effects |
| :---- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Bleeding** | At the start of each of its turns, the creature takes its Bleed value - half the damage of the hit that applied Bleeding (rounded down, does not degrade armor). Ending it takes a Major Action and a Chirurgery check (DC \= Bleed value), made on itself or by an adjacent creature. |
| **Blinded** | Can't see. Automatically fails any Check or Ward that relies on sight. Disadvantage on attack rolls and on Parries. |
| **Broken** | Unnamed only - see [[Morale|exchange]]. Flees by the safest route it can see, attacks no one, and can be ignored for the rest of the fight. |
| **Charmed** | Can't attack the charmer or target it with harmful effects. The charmer has advantage on Skill checks to interact with the creature socially. |
| **Deafened** | Can't hear. Automatically fails any Check or Ward that relies on hearing. |
| **Downed** | See [Downed](#downed), above. |
| **Flying** | Gains a flying Speed equal to the granting effect's value or its walking Speed, whichever is higher. If it loses this Speed or is knocked Prone while aloft, it falls (see [Falling](#falling), above). |
| **Frightened** | While the source of its fear is within line of sight: disadvantage on attack rolls and Skill checks. It can't willingly move closer to the source. Distinct from a Fear rating (see [[Fear|exchange]]), which is a creature trait rather than an imposed condition. |
| **Grappled** | Restrained. Ends the moment the grappler lets go, moves away, or is knocked Prone - see [[Grappling|exchange]] for how a hold is taken and broken. While you hold a Grapple, your own Tempo Pool drops by 1 - one hand is full. |
| **Incapacitated** | Can't take actions of any kind and has no Tempo Pool - attacks against it land automatically and the attacker takes an Opening. Movement is unaffected unless another effect says otherwise. |
| **Invisible** | Attack rolls against it have disadvantage; its own attack rolls have advantage. Counts as heavily obscured for hiding and has advantage on Stealth checks. |
| **Paralyzed** | Incapacitated, Speed 0, and can't speak. Automatically fails STR and DEX Wards. Attacks against it land automatically and the attacker takes an Opening. |
| **Petrified** | Incapacitated, Speed 0, and unaware of its surroundings. Becomes a nonmagical stone object: weight x10, aging stops, resistance to all damage. All other conditions and ongoing effects are suspended until it's freed. |
| **Poisoned** | Disadvantage on attack rolls and Skill checks. |
| **Prone** | Disadvantage on attack rolls; attacks against it have Advantage. **Parries at no penalty.** Can't move except to stand up, which costs its whole Move Action. A shot at a Prone target reads the [[Shot DC|exchange]] table instead of this line. |
| **Restrained** | Speed 0; attack rolls against it have advantage; disadvantage on its own attack rolls; disadvantage on DEX Wards; casting requires being unengaged as normal but the working still resolves. Breaks for 1 Tempo Die, no roll (see [[Grappling|exchange]]). While Restrained, invest at most 1 die in each Parry. **A Restrained creature can be knifed through the gaps in its armor** - see [[Armor and Wounds|exchange]]. |
| **Silenced** | Can't speak or cast workings. |
| **Stunned** | On its turn it can take only one action of any type instead of its normal allotment, and its Tempo Pool refills to half as many dice, rounded down (never below 1). |
| **Unconscious** | Incapacitated, Speed 0, can't speak, and unaware of its surroundings; it falls Prone and drops what it's holding. Automatically fails all Checks and Wards. Attacks against it land automatically and the attacker takes an Opening. |

**The 1-die Parry cap counts every die, including an Exert die** (see [[Exerting|exchange]]).

**Sources:** Trauma is not a byproduct of ordinary combat damage beyond what's listed under [Trauma](#trauma), above - a Wound that deals 1, dropping to 0 Wounds as Unnamed, or Downed itself grant none on their own. If a rule doesn't name Trauma, it doesn't grant it.
