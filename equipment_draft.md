# Ressam - Equipment (Playtest Draft)

*Playtest draft - these rules are still being tested and may change between sessions.*

Every stat a character card needs for gear: weapons, armor, shields, and what's left in the adventuring kit once the fight's over. The rules that read these numbers - the Exchange, Openings, Damage & Armor, Shields & Guard, Ranged Attacks - live in `combat_draft.md`. This file is data only. All distances are in squares.

---

## Weapons

**Attacks, Reach, Skill,** and **Signature** are defined in `combat_draft.md` (Weapons, Distance & Weapon Reach, Openings). **Damage type** is defined there too, under Damage & Armor, and it now carries real weight - see Damage types in the Reference section below. The columns below give each weapon's values.

| Weapon       | Damage                 | Reach   | Attacks | Skill               | Signature | Cost |
|:-------------|:-----------------------|:--------|:-------:|:--------------------|:----------|:----:|
| Unarmed      | 1d4 Blunt              | Normal  |  `+1`   | Daggers & Wrestling | Grapple   |  -   |
| Dagger       | 1d6 Piercing           | Normal  |  `+1`   | Daggers & Wrestling | Grapple   |  2   |
| Shortsword   | 1d6 Piercing           | Normal  |  `+1`   | Fencing Blades      | Riposte   |  4   |
| Rapier       | 1d8 Piercing           | Normal  |  `+0`   | Fencing Blades      | Disarm    |  20  |
| Scimitar     | 1d8 Slashing           | Normal  |  `+0`   | Cleaving Blades     | Riposte   |  12  |
| Broadsword   | 1d8 Slashing           | Normal  |  `+0`   | Cleaving Blades     | Disarm    |  15  |
| Longsword    | 1d8 Slashing           | Normal  |  `+0`   | Two-Handed Blades   | Disarm    |  15  |
| Greatsword   | 1d12 Slashing          | Normal  |  `-1`   | Two-Handed Blades   | Riposte   |  30  |
| Mace         | 1d8 Blunt              | Normal  |  `+0`   | Hafted Weapons      | Shove     |  8   |
| Battle Axe   | 1d8 Slashing           | Normal  |  `+0`   | Hafted Weapons      | Sunder    |  12  |
| Club         | 1d6 Blunt              | Normal  |  `+0`   | Hafted Weapons      | Shove     |  1   |
| War Maul     | 1d12 Blunt             | Normal  |  `-1`   | Hafted Weapons      | Shove     |  20  |
| Quarterstaff | 1d6 Blunt              | Reach 1 |  `+0`   | Polearms            | Shove     |  5   |
| Spear        | 1d8 Piercing           | Reach 1 |  `+0`   | Polearms            | Shove     |  20  |
| Halberd      | 1d10 Slashing/Piercing | Reach 1 |  `-1`   | Polearms            | Grapple   |  20  |
| Glaive       | 1d10 Slashing          | Reach 1 |  `-1`   | Polearms            | Sunder    |  25  |
| Pike         | 1d8 Piercing           | Reach 2 |  `-1`   | Polearms            | Shove     |  10  |

**Two-Handed Blades is a Skill name, not a handedness flag** - it groups blades by fighting style, not grip. The Longsword trains under it at `+0` Attacks (one-handable); only a `-1` Attacks weapon is mechanically Two-Handed. **Cleaving Blades and Fencing Blades work the same way** - Scimitar and Broadsword are both one-handed despite the Cleaving Blades name, same as Rapier under Fencing Blades.

**Hafted Weapons and Polearms split by Reach, not grip** - Hafted Weapons are Normal Reach; every Polearm is Reach 1 or 2.

**Reach and gap-seeking pull against each other, and that's the point.** Only a **Normal-Reach Piercing** weapon can find the gaps in a Restrained or Downed foe (see Damage & Armor, `combat_draft.md`) - so the Dagger, Shortsword and Rapier are the armor answer, and the Spear and Pike, for all their Reach, are not. The Rapier and the Spear cost the same 20 Crowns and roll the same 1d8: one buys Reach and Ignores Guard, the other buys the knife through the visor. That's the trade.

**The Spear's Cost is priced up from its `weapons.md` source, not pulled straight across like the rest of this table.** At a handful of Crowns it strictly dominated every other 1d8 weapon for a third of their price. 20 Crowns puts it level with the weapons it used to outclass; watch whether that's still too cheap for what it does.

**The Shortsword and Quarterstaff are priced against the Club and Dagger, not the source list** - at 10 and 1 Crown respectively they were a dominated purchase and a runaway bargain. 4 and 5 put them where the choice is about Skill, Reach and Signature rather than about money.

**Ranged** (Attacks works as it does on any weapon - a shot invests Tempo Dice like any attack; movement gate, Loaded/Empty, reload timing and misfires live in `combat_draft.md`'s Ranged Attacks section). **In melee, every ranged weapon counts as Normal Reach and fights as Unarmed** - Parry, Opportunity Attacks, Engaged, and Disarm (but never Sunder, which needs a Reach 1 or 2 weapon) all read off that - see `combat_draft.md`'s Weapons in Hand. Unarmed is Blunt, so a bow swung in melee never finds gaps.

| Weapon         | Damage        | Range (squares) | Hands | Attacks | AP  | Skill    | Cost | Ammunition    |
|:---------------|:--------------|:----------------|:-----:|:-------:|:---:|:---------|:----:|:--------------|
| Shortbow       | 1d6 Piercing  | 16/32           |  Two  |  `-1`   |  2  | Archery  |  25  | Arrows        |
| Longbow        | 1d10 Piercing | 30/60           |  Two  |  `-1`   |  2  | Archery  |  40  | Arrows        |
| Light Crossbow | 1d10 Piercing | 20/40           |  Two  |  `-1`   |  3  | Archery  |  30  | Bolts         |
| Heavy Crossbow | 1d12 Piercing | 24/48           |  Two  |  `-1`   |  3  | Archery  |  45  | Bolts         |
| Pistolet       | 3d4 Piercing  | 6/12            |  One  |  `+0`   |  3  | Firearms |  40  | Powder & Shot |
| Arquebus       | 3d4 Piercing  | 12/24           |  Two  |  `-1`   |  3  | Firearms |  50  | Powder & Shot |

**Armor-Piercing (AP).** A hit from a missile weapon lowers the target's Dent Line and Rend Line by its AP value **for that hit only**, and **only against worn armor** - it never touches the None line (Dent 0 / Rend 5), so a bolt in an unarmored body is exactly as bad as it always was, no worse. AP doesn't degrade armor any faster; that's a separate rule (see Damage & Armor, `combat_draft.md`).

**Bows and bolts do different jobs.** A bow's AP 2 is a bodkin point - enough to trouble a gambeson, never enough to open plate. Bows earn their keep on **rate of fire and range**: no reload, the two longest range bands on the table, and a shot every single round. Crossbows and firearms are the anti-armor weapons, bought at the price of a reload turn and, for the guns, a misfire. Neither line is meant to be the better one; they're meant to be bad at different fights.

---

## Shields

A shield adds **Guard** to every Parry, and may cost either Attacks or Speed to carry - the Attacks cost stacks with the weapon's own, the Speed cost with the armor's; the Buckler costs neither. See `combat_draft.md`'s Shields & Guard for how Guard is used and degraded.

| Shield        | Guard | Attacks | Speed | Against shots              | Cost |
|:--------------|:-----:|:-------:|:-----:|:---------------------------|:----:|
| Buckler       | `+1`  |  `+0`   |   -   | -                          |  5   |
| Heater Shield | `+2`  |  `+0`   | `-1`  | Light cover (`+2` Shot DC) |  10  |

**Neither shield costs you a Tempo Die any more, so the choice is about what kind of defence you want.** The Buckler is a parrying tool: free to carry, `+1` Guard, and it's gone after a single lost Parry. The Heater is a wall - `+2` Guard, Light cover against shots - paid for in mobility, which also bites on the ranged movement gate (see `combat_draft.md`). Both are ignored entirely by Reach 1 and Reach 2 weapons, which is what keeps them from being automatic.

---

## Armor

**Dent Line** and **Rend Line** are what a landed hit's total is compared against. **Speed** adjusts the wearer's Speed. These are starting values, and also the ceiling repair can never exceed - see `combat_draft.md`'s Damage & Armor and Rest & Repair.

| Armor      | Dent | Rend | Speed | Cost |
|:-----------|:----:|:----:|:-----:|:----:|
| None       |  0   |  5   | `+1`  |  -   |
| Gambeson   |  5   |  10  |   -   |  10  |
| Brigandine |  7   |  12  |   -   |  50  |
| Mail       |  9   |  14  | `-1`  | 100  |
| Plate      |  11  |  16  | `-2`  | 300  |

**Cost** mirrors `armor.md`'s price list at roughly 1/7 scale, matching the nearest tier by name and position: Gambeson from Gambeson (75 Crown), Brigandine from Brigandine (350 Crown), Mail from Breastplate (700 Crown - the nearest rung above Brigandine, not from any armor actually called "mail"), Plate from Full Plate (2,000 Crown).

**At the 100-Crown starting purse, Mail and Plate are out of reach**, which is why the Mail- and Plate-wearing pregens are issued that armor as kit rather than buying it - see Building a Pregen, `combat_draft.md`. Without that, the top half of this table only ever appears on the GM's side of the screen.

---

## Adventuring Gear

Most of this is tracked as a flag on the character card, not a subsystem. **Ammunition is the one exception** - each bundle below is a real counter, ticked down one per shot, because a bow or gun with none left simply can't fire (see Running dry, below).

| Item                      | Use                                                                                                                                                                                                      | Cost |
|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----:|
| Healer's Kit              | Required for any Chirurgery check - reviving a Downed ally (DC 7), a medic's day-in-town Wound check (DC 9), treating a Scar (DC 11). Single-use per check; restocked in a town.                         |  10  |
| Rations                   | One day's food for one person. Skips the question of what happens without it - a GM ruling, not a rule here.                                                                                             |  1   |
| Waterskin                 | Holds one day's water for one person.                                                                                                                                                                    |  1   |
| Torch                     | Lights a 6-square radius for 1 hour, then burns out.                                                                                                                                                     |  1   |
| Rope (10 squares)         | Climbing, hauling, binding a prisoner.                                                                                                                                                                   |  2   |
| Bedroll                   | What a Rest actually happens on, outside a town bed.                                                                                                                                                     |  2   |
| Arrows (quiver of 12)     | Ammunition for the Shortbow and Longbow. Firing spends one; empty, the bow can't fire until resupplied.                                                                                                  |  3   |
| Bolts (case of 12)        | Ammunition for the Light Crossbow and Heavy Crossbow. Same as Arrows.                                                                                                                                    |  4   |
| Powder & Shot (6 charges) | Ammunition for the Pistolet and Arquebus. Same as Arrows.                                                                                                                                                |  6   |
| Healing Draught           | Minor Action to administer: heal **1 Wound**. A Downed character can't drink one themselves - an Adjacent ally spends the Minor Action. Healing always costs Trauma (see `combat_draft.md`). Single-use. |  15  |

**The Draught is a second pair of hands, not a second life.** It heals exactly what a Chirurgery check does, with no check and no Healer's Kit, but it still needs an ally Adjacent, it still costs that ally an action, and it still costs the same Trauma any healing does - more, if it's also getting someone up off the floor. It buys reliability, not free revivals.

**Darkness.** Beyond Adjacent, a creature with no light of its own can't see clearly into an area outside every light source's radius (a Torch, a working, daylight) - treat anyone fully inside it as being in **Heavy cover** (`+4` Shot DC) to that attacker, and unaware of anyone who can see them but whom they can't see back (see Awareness, `combat_draft.md`). It is **not** Total cover: a shot or a working into the dark is a hard price, not an impossibility, which also keeps a caster from stepping into an unlit square and becoming untargetable. Two creatures Adjacent to each other in the same darkness are unaffected by either rule - this is about sightlines, not touch. A GM call on borderline light, not a roll.

**Running dry.** A ranged weapon with no shots left in its ammunition can't be fired or reloaded (see Loaded/Empty, `combat_draft.md`) until resupplied - in a town, or from a dead body carrying the same kind.

**Carry limit.** **Slots = 6 + STR**, minimum 1. Whatever you're actively wearing or wielding (one weapon, one suit of armor, one shield) is free; every other item on this list, including each bundle of ammunition, costs 1 Slot, spares included. Over the limit is a GM call - leave something behind, or slow down.

---

## Reference

**Currency:** the **Crown**. Weapon, armor, and ammunition Cost columns above are pulled from the full ruleset's price lists (`weapons.md`, `armor.md`) and rescaled to roughly 1/6-1/7 of their Crown price, matching this slice's smaller economy - they're sourced, not arbitrary, but still untested at the table. The Spear, Shortsword and Quarterstaff are deliberate exceptions, repriced against each other rather than against the source (see Weapons, above). Revelry & Leisure's 10 Crowns per character per night (see `combat_draft.md`) and the Healing Draught's 15 Crowns sit on the same scale but have no full-ruleset equivalent to source from, so they remain independent placeholders.

**Skills used above:** Daggers & Wrestling, Fencing Blades, Two-Handed Blades, Cleaving Blades, Hafted Weapons, Polearms, Firearms, Archery, **Chirurgery**, **Smithing**. The full skill list is still in progress.

**Damage types: Blunt, Piercing, Slashing.** Each now does one thing, and only one:

| Type         | What it does                                                                                                                     |
|:-------------|:---------------------------------------------------------------------------------------------------------------------------------|
| **Blunt**    | Degrades both of a target's worn armor lines by **2** per landed hit instead of 1. You ruin the harness rather than opening it.  |
| **Piercing** | At **Normal Reach**, against a **Restrained or Downed** target, treats their armor as None for that hit (see `combat_draft.md`). |
| **Slashing** | Nothing special - which is why the two biggest dice on the table (Greatsword 1d12, Glaive 1d10) are Slashing.                    |

**Unarmed is the exception to Blunt**: a fist degrades armor by 1, not 2. This slice still doesn't test Resistance, Vulnerability, or Immunity to any damage type - nothing here carries one.
