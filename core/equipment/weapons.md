Weapons deal one of three Physical damage types: **Piercing**, **Slashing**, or **Blunt** \- see [[Damage Types|rest_and_survival]] for what each one does in a fight.

## Weapon Properties

- **Attacks:** Sets your [[Tempo Pool|exchange]] size beyond the baseline \- `\+1` for a **Light** weapon, `\-1` for a **Two-Handed** one, `\+0` for everything else. A shield's own Attacks modifier stacks on top (see [[Shields|weapons]]).

- **Light:** A weapon light enough to earn `\+1` Attacks. Carrying a second one changes nothing on its own \- see [[Weapons in Hand|exchange]].

- **Two-Handed:** Requires both hands to use, `\-1` Attacks, and can't be paired with a shield.

- **Versatile:** Can be used one or two-handed with different damage. **Gripped two-handed, it can't be paired with a shield either** \- both hands are full \- even though its Attacks modifier doesn't change.

- **Reach:** Every melee weapon carries a **Reach** \- Normal, Reach 1, or Reach 2 \- see [Reach](#reach), below.

- **Signature:** The Opening (see [[Openings|exchange]]) this weapon takes on a win by 3 instead of 5. Ranged weapons carry none \- a shot never takes an Opening.

- **Throwable:** Can be thrown (normal range/max range in feet) \- resolves as a shot off the [[Shot DC|exchange]] table, taking no Opening, same as any ranged attack.

- **Penetrant:** Lowers the target's Dent Line and Rend Line by half your ranks in that weapon's associated Skill (rounded down), for that attack only.

- **Ignores Guard:** A shield's Guard adds nothing to a Parry against this weapon.

- **Armor-Piercing (AP X):** A hit from this weapon lowers the target's Dent Line and Rend Line by X **for that hit only**, against worn armor \- it never touches the None line (Dent 0 / Rend 5). AP doesn't degrade armor any faster; that's a separate rule (see [[Degradation|combat]]).

- **Reload (action):** Putting the next shot in this weapon costs the listed action(s), never a Tempo Die \- see [Reloading](#reloading), below. A weapon with no Reload tag needs none at all - the next shot is already ready.

- **Movement Gate:** This weapon needs you to have spent no more than half your Speed (round down) in Move this turn to fire it at all - see [[The movement gate|exchange]]. A weapon without this tag fires regardless of how far you've moved.

- **Charge:** If you hit with this weapon in the same turn your mount moved at least 20 ft toward the target, the attack's damage becomes the value listed in parentheses and gains Penetrant. **A mounted Charge always resolves at Reach 1, never Adjacent** \- Reach 1 never locks out mid-charge the way it would on foot.

- **Saddled:** Unlike other Two-Handed missile weapons, this weapon can be fired while on horseback, including on a moving mount, without penalty.

### Reach

**Every melee weapon carries a Reach, printed on it** \- see [[Distance \& Reach|exchange]] for how it's used in a fight:

| Reach | Squares | Weapons |
|:------|:-------:|:--------|
| **Normal** | Adjacent (0 squares) | Unarmed and every weapon in the ONE-HANDED BLADES, TWO-HANDED BLADES, RAPIERS \& FENCING, HAFTED WEAPONS, and DAGGERS \& KNIVES tables |
| **Reach 1** | Adjacent through 1 square | Spear, Halberd, Glaive, Quarterstaff, Lance |
| **Reach 2** | Adjacent through 2 squares | Pike |

**Hafted Weapons and Polearms split by Reach, not grip.** Hafted Weapons (Mace, Battle Axe, Club, War Maul, Greatclub, Whip, Weighted Chain, Chain Flail) are Normal Reach; every Polearm (Spear, Pike, Halberd, Glaive, Quarterstaff, Lance) is Reach 1 or Reach 2, even the ones short enough to grip close - the weapon still keeps a foe further off than Normal Reach lets one.

**A thrown weapon takes its held Reach until thrown**, then is a shot off the [[Shot DC|exchange]] table, and Reach governs only what it does while you are still holding it. A **Sling** has no melee Reach at all.

**Carrying Weapons:** every weapon on your person \- in hand, sheathed, or carried as a spare \- costs **1 Slot** unless it's the one you have equipped (see [[Carrying Capacity|rest_and_survival]]), Two-Handed weapons included.

## Openings

**No margin pays double damage** \- winning a contest by 5 or more takes an [[Opening|exchange]] instead. **Each weapon's Signature Opening** takes at a margin of 3 instead (see [Weapon Properties](#weapon-properties), above) \- any other Opening still needs 5.

## Firearm Rules

All weapons in the Firearms category (Pistols, Long Guns, and Heavy Firearms) innately have the following properties:

### **Ammunition & Reloading**

- **Firearm:** Can only fire with ammunition loaded \- every firearm uses Shot and Powder (see Ammunition, below).
- **Standard Reload:** Every firearm carries **Reload (Major Action)** \- see [Reloading](#reloading), below. The **Hackbut** is the exception and does not reload in a fight at all.

### **Lock Types**

Pistols and Long Guns each come in two lock types. A weapon's Damage and Range are set entirely by its category (Pistol or Long Gun) \- lock type only changes Cost, Misfire, and the quirks below.

- **Match-lock:** Cheapest, and the most reliable ignition (lowest Misfire score). Its slow match must be lit \- a Minor Action, or done for free before combat starts \- and stays lit for 10 rounds. A match that's doused (see Black Powder, below) or burns out mid-fight must be relit (Minor Action) before the weapon can fire again, and each weapon's match must be lit individually, even if you're already carrying another lit one. A lit match glows and smolders visibly: you gain no benefit from Stealth in darkness while carrying one lit.
- **Wheel-lock:** Prohibitively expensive, with a higher Misfire score than Match-lock. Self-contained and always ready to fire the instant it's loaded \- no match, no extra step. Both lock types can be pre-loaded and chain-fired: drop the spent weapon as a Free Action, draw a fresh loaded one as a single Lesser Action (draw any number this way at once, hands permitting), and fire it with your Major Action, all in the same turn \- but only Wheel-lock does it with no strings attached.

### **Environmental Limitations**

- **Very Loud:** Firearms are loud, shooting one alerts everyone within **300 ft**.
- **Black Powder:** A firearm submerged in water or drenched in particularly heavy rain can't be fired unless dried for at least 1 hour, any wet ammunition is lost.

### **Multiple Barrels**

When a weapon with the firearm property is created, it may be made with more than one barrel (excluding the Hackbut and Hand Mortar).

- Additional barrels add to the misfire score. Each additional barrel increases misfire by \+1. For every 2 barrels after the first, the misfire increases by an additional \+1. (Example: 2 barrels \= \+1 misfire, 4 barrels \= \+2 misfire.)
- Each extra barrel adds **50 Crowns** to the price. Slots are unaffected \- a multi-barreled firearm is still 1 weapon.
- If a firearm has multiple barrels, each barrel reloads separately at the weapon's normal Reload cost. A double-barreled pistol (Reload (Major Action)) needs **2 Major Actions** to fully reload \- one barrel per turn, since a firearm's reload already costs your whole turn.

### **Firearm Special Properties**

- **Misfire X:** No separate roll \- **any Tempo Die you invested in the shot that comes up at or below X misfires the weapon**, checked against the same dice the shot itself rolled. A bow rewards committing dice to a shot; a gun punishes it, since more dice invested is more chances to jam. Misfire 1 (Match-lock) only jams on a bare natural 1; Misfire 2 (Wheel-lock, or a second barrel) jams on a 1 or 2, and so on. **A misfired shot still spends the Major Action it was fired with**, whether or not the shot itself would have hit. Clearing it costs a Major Action \+ a Minor Action, always your next turn at the earliest; you cannot attack or reload with it until cleared.
- **Mounted:** Requires Major Action to deploy, cannot fire at enemies within 5 ft, must be redeployed if moved.
- **Spread (X/Y ft cone):** Targets all creatures in the specified cone, the length of the cone preceding its width.
- **Explosive (X ft radius):** Deals its damage to all targets in its radius.

---

## Reloading

**Every missile weapon is loaded or it is empty, and firing empties it.**

> **Firing costs your Major Action, one shot a turn, no exception. Reloading costs the action(s) set by the weapon \- never a Tempo Die.**

| Weapon | Movement to fire | Reload |
| :---- | :---- | :---- |
| **Thrown** \- Dart, Throwing Axe, Javelin, Spear | No gate \- move freely | Take up the next one: **Lesser Action** |
| **Every bow, and the Sling** | **Half your Speed (round down) or less** | None \- drawing the next arrow or shot is part of firing |
| **Crossbows** | No gate \- move freely | **Reload (Minor Action)**, no Move that turn \- can't fire and reload in the same round |
| **Every firearm** \- pistols, arquebuses, the Hailshot Piece, the Hand Mortar | No gate \- move freely | **Reload (Major Action)**, no Move that turn \- can't fire and reload in the same round |
| **Hackbut** | No gate \- move freely | **Reload (2 Major Actions).** It does not fire twice in the same fight |

**The movement gate is a bow's (and the Sling's) cost, not the rule** - see [[The movement gate|exchange]]. Spend more than half your Speed, or climb, leap, or swim, and a bow or Sling can't fire this turn. **Crossbows and firearms are exempt and move freely**, paying with a real reload step instead - a Crossbow fires on the move but must reload standing still next turn; a firearm must stand still just to reload.

**A brace of loaded weapons is two weapons, not one reloaded.** Drawing the second is a Lesser Action, so a horseman with a pistol in each holster fires every turn without spending one on reload; the same trick works with a bow in hand and a knife on the belt.

**A Loaded weapon carries between scenes** - a fight that catches you already Loaded needs no reload for your first shot.

See [[The shot|exchange]] for the Shot DC a shot rolls against.

---

# Weapons

## MELEE WEAPONS

**ONE-HANDED BLADES** *(Cleaving Blades Skill)*

| Weapon | Damage | Reach | Attacks | Signature | Properties | Cost |
| :---- | :---- | :---: | :---: | :---- | :---- | ----- |
| Scimitar | 1d8 Slashing | Normal | `\+0` | Riposte | \- | 75 Crown |
| Broadsword | 1d8 Slashing | Normal | `\+0` | Disarm | \- | 85 Crown |

**TWO-HANDED BLADES** *(Two-Handed Blades Skill)*

| Weapon | Damage | Reach | Attacks | Signature | Properties | Cost |
| :---- | :---- | :---: | :---: | :---- | :---- | ----- |
| Longsword | 1d8 Slashing | Normal | `\+0` | Disarm | Versatile (Two-Handed 1d10) | 100 Crown |
| Greatsaber | 1d6 \+ 2 Slashing | Normal | `\+0` | Riposte | Versatile (Two-Handed 2d6) | 150 Crown |
| Greatsword | 1d12 Slashing | Normal | `\-1` | Riposte | Two-Handed | 200 Crown |
| Warblade | 1d10 \+ 2 Slashing | Normal | `\-1` | Riposte | Two-Handed | 350 Crown |

**RAPIERS & FENCING** *(Fencing Blades Skill \- DEX-governed, see [[Attributes & Skills|attributes_and_skills]])*

| Weapon | Damage | Reach | Attacks | Signature | Properties | Cost |
| :---- | :---- | :---: | :---: | :---- | :---- | ----- |
| Shortsword | 1d6 Piercing | Normal | `\+1` | Riposte | Light | 35 Crown |
| Rapier | 1d8 Piercing | Normal | `\+0` | Disarm | \- | 120 Crown |
| Estoc | 1d10 Piercing | Normal | `\-1` | Disarm | Two-Handed, Penetrant | 150 Crown |
| Stiletto | 1d4 Piercing | Normal | `\+1` | Disarm | Light | 20 Crown |

**HAFTED WEAPONS** *(Hafted Weapons Skill)*

| Weapon | Damage | Reach | Attacks | Signature | Properties | Cost |
| :---- | :---- | :---: | :---: | :---- | :---- | ----- |
| Battle Axe | 1d8 Slashing | Normal | `\+0` | Sunder | Versatile (Two-Handed 1d10) | 70 Crown |
| Mace | 1d8 Blunt | Normal | `\+0` | Shove | \- | 60 Crown |
| War Maul | 1d12 Blunt | Normal | `\-1` | Shove | Two-Handed | 100 Crown |
| Club | 1d6 Blunt | Normal | `\+0` | Shove | \- | 5 Crown |
| Greatclub | 2d4 Blunt | Normal | `\-1` | Shove | Two-Handed | 10 Crown |
| Whip | 1d4 Slashing | Normal | `\+0` | Disarm | \- | 10 Crown |
| Weighted Chain | 1d6 Blunt | Normal | `\+0` | Shove | \- | 20 Crown |
| Chain Flail | 1d8 Blunt | Normal | `\+0` | Shove | Ignores Guard | 80 Crown |

**POLEARMS** *(Polearms Skill)*

| Weapon       | Damage | Reach | Attacks | Signature | Properties | Cost      |
|:-------------| :---- |:--------:|:---:|:----|:----|-----------|
| Spear        | 1d8 Piercing | Reach 1 | `\+0` | Shove | Versatile (Two-Handed 1d10), Throwable (20/40 ft) | 30 Crown  |
| Pike         | 1d8 Piercing | Reach 2 | `\-1` | Shove | Two-Handed | 50 Crown  |
| Halberd      | 1d10 Slashing / Piercing | Reach 1 | `\-1` | Grapple | Two-Handed | 100 Crown |
| Glaive       | 1d10 Slashing | Reach 1 | `\-1` | Sunder | Two-Handed | 95 Crown  |
| Quarterstaff | 1d6 Blunt | Reach 1 | `\+0` | Shove | Versatile (Two-Handed 2d4) | 5 Crown   |
| Lance        | 1d8 Piercing | Reach 1 | `\+0` | Shove | Charge (2d8), One-handed while mounted; Two-Handed and loses Charge on foot | 100 Crown |

**DAGGERS & KNIVES** *(Daggers & Wrestling Skill)*

**Note:** A Knife thrown rather than swung uses the Thrown Skill instead \- see the THROWN table, below. A lighter, precision-thrusting alternative to the Dagger below \- the Stiletto \- is governed by Fencing Blades instead; see RAPIERS & FENCING, above.

| Weapon | Damage | Reach | Attacks | Signature | Properties | Cost |
| :---- | :---- | :---: | :---: | :---- | :---- | ----- |
| Dagger | 1d6 Piercing | Normal | `\+1` | Grapple | Light | 20 Crown |
| Knife | 1d4 Piercing | Normal | `\+1` | Grapple | Light, Throwable (20/40 ft) | 5 Crown |

---

## RANGED WEAPONS

**A shot is not an Exchange** \- it cannot be Parried and takes no Opening, but it still invests Tempo Dice exactly like a melee attack. Invest any number of Tempo Dice, take the highest, and add your Archery, Firearms, or Thrown Skill against the **Shot DC**, a number set by range, movement and position rather than by the target. Firing costs your Major Action, one shot a turn. See [[The shot|exchange]] for the table.

**Note:** Shooting with an enemy Adjacent raises the Shot DC by 4 (see [[Shot DC|exchange]]), and **a Two-Handed missile weapon cannot shoot at all** from there.

**Note:** A missile weapon's Reload, where it carries one, is paid in actions and never in dice \- see [Reloading](#reloading), above; a bow or Sling carries no Reload tag at all, paying with the movement gate instead. Holding a shot for a chosen trigger is [[Holding an attack|exchange]]: Major Action to declare, no Tempo Die paid yet, resolved as a plain attack (dice invested at that point) when the trigger fires.

**BOWS** *(Archery Skill)*

| Weapon        | Damage | Range      | AP  | Attacks | Properties          | Cost      |
|:--------------| :---- |:-----------|:---:|:---:|---------------------|-----------|
| Shortbow      | 1d6 Piercing | 80/160 ft  |  2  | `\-1` | Two-Handed, Movement Gate, no reload          | 50 Crown  |
| Longbow       | 1d10 Piercing | 150/300 ft |  2  | `\-1` | Two-Handed, Movement Gate, no reload          | 100 Crown |
| Composite Bow | 1d8 Piercing | 120/240 ft |  2  | `\-1` | Two-Handed, Saddled, Movement Gate, no reload | 150 Crown |

**CROSSBOWS** *(Archery Skill)*

| Weapon | Damage | Range | AP  | Attacks | Properties | Cost |
| :---- | :---- | :---- |:---:|:---:| ----- | ----- |
| Light Crossbow | 1d10 Piercing | 100/200 ft |  3  | `\-1` | Two-Handed, Reload (Minor Action), no movement gate | 125 Crown |
| Heavy Crossbow | 1d12 Piercing | 120/240 ft |  3  | `\-1` | Two-Handed, Reload (Minor Action), no movement gate | 175 Crown |

**THROWN** *(Thrown Skill)*

| Weapon | Damage | Range | Attacks | Properties | Cost |
| :---- | :---- | :---- | :---: |----- | ----- |
| Throwing Axe | 1d6 Slashing | 20/40 ft | `\+1` | Light | 15 Crown |
| Javelin | 1d6 Piercing | 30/60 ft | `\+0` | Versatile (Two-Handed 1d8), Penetrant (when thrown) | 10 Crown |
| Dart | 1d4 Piercing | 20/40 ft | `\+1` | Light | 5 Crown |
| Sling | 1d6 Blunt | 200/400 ft | `\+1` | Light, Uses Ammunition, Movement Gate, no reload | 5 Crown |

**Note:** A thrown Knife also uses this Skill \- see the DAGGERS & KNIVES table, above; it deals the same damage as its melee entry at the same 20/40 ft range as a Dart.

---

**FIREARMS** *(Firearms Skill)*

**PISTOLS**

| Weapon | Damage | Range | AP  | Attacks | Properties | Cost |
| :---- | :---- | :---- |:---:|:---:| ----- | ----- |
| Match-lock Pistol | 3d4 Piercing | 30/60 ft |  3  | `\+0` | Misfire 1 | 200 Crown |
| Wheel-lock Pistol | 3d4 Piercing | 30/60 ft |  3  | `\+0` | Misfire 2 | 800 Crown |

**LONG GUNS**

| Weapon | Damage | Range | AP  | Attacks | Properties | Cost |
| :---- | :---- | :---- |:---:|:---:| ----- | ----- |
| Match-lock Arquebus | 3d4 Piercing | 120/240 ft |  3  | `\-1` | Two-Handed, Misfire 1 | 300 Crown |
| Wheel-lock Arquebus | 3d4 Piercing | 120/240 ft |  3  | `\-1` | Two-Handed, Misfire 2 | 1200 Crown |

**HEAVY FIREARMS**

| Weapon         | Damage | Range | AP  | Attacks | Properties | Cost |
|:---------------| :---- | :---- |:---:|:---:| ----- | ----- |
| Hailshot Piece | 4d4 Piercing | 30/60 ft |  3  | `\-1` | Two-Handed, Spread (30ft/15ft cone), Misfire 2 | 700 Crown |
| Hand Mortar    | 2d10 Piercing | 40/80 ft |  4  | `\-1` | Two-Handed, Explosive (20ft radius), Misfire 3 | 1200 Crown |
| Hackbut        | 6d6 Piercing | 200/400 ft |  5  | `\-1` | Two-Handed, Mounted, Reload (2 Major Actions), Misfire 1 | 1500 Crown |

**AMMUNITION**

| Ammo Type | Cost | Slots |
| :---- | :---- | :---: |
| Arrow, Quiver (24) | 1 Crown | 1 |
| Crossbow Bolt, Case (20) | 1 Crown | 1 |
| Sling Bullet, Bag (50) | 20 Scale | 2 |
| Shot & Powder, Pouch & Horn (20) | 20 Crown | 1 |
| Hand Mortar Grenade (1) | 25 Crown | 1 |

**COLLECTING AMMUNITION**
After combat, roll 1d6:

- 1: Lose all expended ammunition used
- 2-5: Recover half ammunition used (rounded down)
- 6: Recover all ammunition used

**Note:** You cannot recover 'Shot & Powder' / 'Hand Mortar Grenades'.

---

**UNARMED**

**BRAWLING** *(Daggers & Wrestling Skill)*

| Attack | Damage | Reach | Attacks | Signature | Properties |
| :---- | :---- | :---: | :---: | :---- | ----- |
| Punch | 1d6 Blunt | Normal | `\+1` | Grapple | \- |
| Kick | 1d8 Blunt | Normal | `\+1` | Grapple | \- |
| Headbutt | 1d10 Blunt | Normal | `\+1` | Grapple | You take the same damage dealt |

**Note:** Grappling is an Opening, taken for winning a contest by 5 or more (3 or more with a Brawling attack, since it's each one's Signature), and every weapon in the game can take it \- see [[Grappling|exchange]].

**Combination:** As a Minor Action immediately after an unarmed attack of yours lands, you may spend **1 Tempo Die** to make one follow-up unarmed attack of a type you haven't already made this turn (e.g. hit with a Punch, follow up with a Kick or a Headbutt \- but not another Punch) at `\-4` to the attack roll. This is innate to fighting unarmed, not a Feat \- no prerequisite beyond a free hand.

---

## SHIELDS

Shields don't add protection the way armor does \- they make a Parry better. A shield's whole identity is one number: **Guard**, added to **every Parry you make while it is equipped**, whatever you actually parry with. Unlike armor, a shield is also something you can swing on your own turn \- see Shield Bash, below.

### **Shield Table**

| Shield        | Guard | Attacks | Speed | Against shots | Properties | Price |
|:--------------|:-----:|:-------:|:-----:|:---------------------------|:--|:---------:|
| Buckler       | `\+1`  | `\+0`   | \-    | \-                          | Fist-held: stays on the hand while you reload, hold a torch, or work a lock | 40 Crown  |
| Heater Shield | `\+2`  | `\+0`   | `\-1` | Light cover (`\+2` Shot DC) | \- | 80 Crown  |
| Pavise        | \-    | \-      | `\-1` | \-                          | Deployable, carries no Guard | 120 Crown |

**Neither shield costs a Tempo Die.** **Carrying Shields:** every shield on your person \- equipped or carried as a spare \- costs **1 Slot** unless it's the one you have equipped (see [[Carrying Capacity|rest_and_survival]]), the Pavise included.

### **Shield Descriptions**

**Buckler** is a small fist-held shield used for parrying rather than blocking. Popular in civilian dueling and among those who value mobility.

**Heater Shield** is the iconic knightly shield, shaped like a clothing iron. Solid, dependable coverage for a soldier who still needs to move and swing a weapon, and broad enough to count as **Light cover** against a shot aimed at its bearer (see [[Shot DC|exchange]]). Often bears heraldic devices.

**Pavise** is a large rectangular shield originally designed to protect crossbowmen while reloading. **It is not a wielded shield and carries no Guard.** As a **Major Action**, it can be deployed as standing cover: whoever is wholly behind it has Cover and cannot be shot ([[Cover|positioning]]). The wielder cannot move while it's deployed, but counts as in Cover themselves. **The `\-1` Speed applies whenever you're carrying it, deployed or not.**

### **Using Shields**

Guard requires a shield equipped in one hand \- since a shield occupies a hand, it's only ever paired with a one-handed weapon (or nothing) in the other, never a Two-Handed weapon or a Versatile weapon gripped two-handed.

Guard is passive: it applies whenever you have a shield equipped, no roll or Skill required, to every Parry, not only to the ones the shield itself answers. **Only one shield's Guard ever counts.** A creature with spare hands (an Alsahli's Four Arms, say) may equip more than one, and only the **highest** Guard among them applies.

**A shield Parries using Daggers \& Wrestling**, the same Skill that swings a Shield Bash.

**Ignores Guard:** a Chain Flail's Guard-ignoring property (see [Weapon Properties](#weapon-properties), above) sets your Guard to 0 against that weapon for as long as it is the thing swinging at you.

### **Shield Bash**

A shield carries no Skill of its own to fund Guard, but nothing stops you from swinging it \- the rim and boss make a serviceable blunt weapon, thrown the same way an off-hand punch is.

**SHIELD BASH** *(Daggers \& Wrestling Skill)*

| Attack | Damage | Reach | Attacks | Signature | Properties |
| :---- | :---- | :---: | :---: | :---- | ----- |
| Shield Bash | 1d4 Blunt | Normal | `\+0` | Shove | Requires shield equipped |

### **Shield Durability**

Shields share durability with your armor \- they don't track separately. **A shield's Guard degrades by 1 whenever a Parry it added to is lost.** A won Parry never touches it, so Guard only wears down at the moment it failed to do its job. Guard cannot drop below 0, and is restored by [[Rest \& Repair|rest_and_survival]] alongside your armor.
