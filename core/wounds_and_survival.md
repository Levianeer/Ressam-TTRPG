## Damage Types

Every instance of damage \- a weapon's die, a spell's Overcome, a Feat's rider, a fall \- belongs to one of three broad categories: **Physical**, **Elemental**, or **Occult**. This isn't a new mechanic layered onto ordinary combat: AR reduces damage identically regardless of type, in the same order as always (roll damage, subtract AR, remainder converts to Wounds via the Wound Thresholds below \- see also Understanding Armor Stats in [[Armor|armor]] and Damage Roll in [[Combat|combat]]). What this section adds is a fixed vocabulary for Resistance, Vulnerability, and Immunity \- terms already scattered across Feats, spells, and racial traits \- instead of each source re-explaining "half damage" from scratch.

### Physical

**Piercing, Slashing, Bludgeoning** (a weapon's listed damage type, see [[Weapons|weapons]]) and **Poison** (envenomed weapons and toxins, see [[Alchemy|alchemy]]). Mundane damage, delivered by a blade, a blow, or a coating \- even when a spell or Feat is what put the weapon or the poison there.

**Magical vs. Non-magical:** Physical damage carries a second, independent tag \- whether its source is magical. An ordinary weapon, an unarmed strike, or a natural weapon with no stated exception deals **non-magical** Physical damage; an enchanted weapon or a natural weapon a race explicitly calls magical (a Varulf's Claws and Bite) deals **magical** Physical damage. Elemental and Occult damage is always treated as magical \- nothing mundane produces Fire from nothing or drains a soul \- so this tag only matters for Physical. It exists because a handful of traits scope their protection to only one half of Physical: Windform's immunity to non-magical Physical damage while incorporeal, or Invocation's Apotheosis granting resistance to non-magical Physical damage.

### Elemental

**Fire, Cold, Lightning, Acid.** Primal forces, sourced from the natural world even when magic is what channels them \- Pyromancy's flame, Hydromancy's frost, Invocation's lightning-wreathed Familiar, an Alchemy Acid Flask.

### Occult

**Necrotic, Radiant, Psychic.** Forces with no physical or elemental analogue: life-force drain and the touch of undeath (Necrotic \- Necration and Cultivation's signature), divine light and judgment (Radiant \- Benediction's signature), and a direct assault on the mind (Psychic \- Subjugation's signature).

### Reflavored Damage

A Feat or trait that reskins damage into its own named identity (Blood-Rule's **Bloodfire**, for a Stryg) creates a distinct type in its own right, not a costume worn over the mundane type it resembles. Bloodfire is explicitly not ordinary fire ("burning with a dark, organic heat unlike ordinary fire," see [[Prestige Feats|prestige_feats]]) \- Fire Resistance does nothing against it, and it doesn't trigger anything keyed to Fire specifically. Slot a reflavored type into whichever of the three categories above actually fits its fiction (Bloodfire, stolen life given a burning shape, reads as Occult) rather than inventing a fourth category. Unless a trait explicitly says its reflavor keeps interacting with the original type, treat the two as unrelated for Resistance, Vulnerability, and Immunity purposes.

### Resistance, Vulnerability, and Immunity

These three terms recur throughout Feats, spells, and racial traits, and always mean the same thing:

- **Resistance** to a damage type: halve incoming damage of that type (round down), before AR is subtracted.
- **Vulnerability** to a damage type: double incoming damage of that type, before AR is subtracted.
- **Immunity** to a damage type: take no damage of that type at all \- it never reaches AR or the Wound Thresholds.

**Order of operations:** Resistance, Vulnerability, and Immunity apply to the raw damage roll first; AR is then subtracted as normal; the remainder converts to Wounds via the Wound Thresholds below. A hit still degrades armor by 1 AR regardless of how much Wound damage it ends up dealing (see Armor Durability, [[Armor|armor]]) \- these three change how much you're hurt, not whether you were hit.

**Stacking:** Multiple sources of Resistance to the same type don't stack \- still just half. Resistance and Vulnerability to the same type cancel out entirely (normal damage), rather than compounding into some other multiplier.

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

### **Scars**

Whenever a hit deals Wound damage, its dominant Damage Type \- whichever type contributed the most to that hit's total, see Damage Types above \- flavors the injury in the fiction: nothing tracked, nothing on the sheet. Heal the Wound through any normal means (see Wound Recovery, below) and it closes clean, no lasting mark.

**Going Down:** The hit that reduces you to 0 Wounds is the exception. Its dominant Damage Type becomes a **Scar** \- a permanent injury that outlives the fight, and outlives ordinary healing.

| Damage Type | Scar          |
|:------------|:--------------|
| Piercing    | Puncture      |
| Slashing    | Laceration    |
| Bludgeoning | Fracture      |
| Poison      | Gangrene      |
| Fire        | Burn          |
| Cold        | Frostbite     |
| Lightning   | Fractal Burn  |
| Acid        | Chemical Burn |
| Necrotic    | Necrosis      |
| Radiant     | Brand         |
| Psychic     | Fray          |

**No mechanical effect:** A Scar carries no stat penalty \- it doesn't touch attack rolls, Wards, Skill Checks, or anything else on your sheet. It's mark, not math: a puckered burn, a hand that won't stop trembling, a hollow stare that wasn't there before \- proof you went down once and came back from it. What it costs you is narrative: how NPCs read you, what a noble court assumes about you, what it says about the life you've lived.

**Doesn't heal on its own:** A Scar is untouched by every existing form of recovery \- Patched Wounds, the Attended/Unattended Wound Recovery track (below), Cultivation, Alchemy, all of it. Once you have one, you have it until someone undoes it specifically.

**Removing a Scar:** Only a Cleric or Priest capable of true, deep restoration can undo one \- a working beyond what any Divine PC's Cultivation, or common village prayer, can manage. This isn't a service on offer in every town; it means seeking out a specific renowned healer, cathedral, or shrine, and paying for it. The price scales with how deep the wound that downed you went, and sits well beyond what common soldiers, laborers, or most working adventurers can raise:

| Downing Blow's Wounds |    Price     |
|:---------------------:|:------------:|
|           1           | 2,000 Crown  |
|           2           | 5,000 Crown  |
|           3           | 10,000 Crown |

**Note:** These figures anchor to the priciest mundane goods already in the game (Full Plate, the single most expensive common item, runs 2,000 Crown) and climb steeply past them on purpose \- a DM should feel free to retune per campaign, but the intent is that even the cheapest tier is a real, campaign-relevant sum, not pocket change.

### **Falling**

Take 1d6 bludgeoning damage per 5 ft fallen, creature is forced prone unless damage is avoided. Deliberately jumping, reduces the number of dice rolled by 4d6 (minimum 0), Landing on soft surfaces may reduce damage by half (DM discretion).

### **Food and Water**

On average, a character can go three days without rations, each day after they gain a level of Trauma and cannot be healed until they have consumed a ration. A full day of hex travel also consumes 1 ration per character (see [[Traveling|traveling]]).

### **Suffocation**

You can hold your breath for END minutes. After that, you drop to 0 Wounds and begin to die.

### **Patched Wounds**

Patched Wounds represent hasty field treatment \- a bandage, a burst of Cultivation magic, a swig of a healing draught \- propping you up before the underlying injury is actually closed. They keep you in the fight, not out of danger.

- **Maximum Patched Wounds:** Total Wounds − current Wounds  
- **Stacking:** Multiple sources add together, up to the Maximum above  
- **Damage Order:** Patched Wounds lost before Wounds  
- **Wound Penalty:** Not reduced by Patched Wounds. The penalty is based on your real, missing Wounds alone \- Patched Wounds buy you survival in the fight, not a reprieve from the penalty (see Wound Penalty, above)  
- **Resting:** A Rest sets your Patched Wounds to at least its tier's amount, never lower than what you already have \- see [[Carrying & Resting|carrying_and_resting]]'s Resting section

### **Wound Recovery**

Permanent Wounds don't refill on the Short/Field/Long Rest cadence (see [[Carrying & Resting|carrying_and_resting]]'s Resting section for Mana, Trauma, and Patched Wound recovery) \- they heal on their own, slower track:

-   **Attended:** Regain **1 Wound per 2 days** while actively attended by a medic or doctor (this may be a party member). The patient must rest and do nothing beyond light physical work; the medic is likewise occupied and cannot spend that time doing anything else productive.
-   **Unattended:** Regain **1 Wound per 2 weeks**. This is a deliberately punitive floor \- a medic-less party isn't stuck healing forever, but attended care is dramatically better.
-   A **Dying** character who has been Stabilized recovers their first Wound (ending Unconsciousness) on this same track \- Attended or Unattended, same rates as anyone else.

---

## Trauma

Trauma represents accumulated stress and strain beyond Wound loss \- fatigue, privation, and the toll of pushing your body or mind past their limits. It is a separate track from Wounds and the Wound Penalty, above: those cover the physical cost of being hit, Trauma covers everything else that wears you down.

| Level | Effect              |
|:------|:--------------------|
| 1     | Manageable          |
| 2     | Dangerous           |
| 3-4   | Critical            |
| 5     | **Automatic Death** |

**Note:** These labels describe how dangerous your condition is narratively \- the mechanical penalty scales continuously (subtract your current Trauma level from all rolls). No separate effect triggers at each band on its own.

**Penalties:** Subtract Trauma level from **all** d12 rolls, wards and checks.

**Sources:** Trauma is not a byproduct of ordinary combat damage \- there is no automatic Trauma from taking a hit, dropping to 0 Wounds, or being Dying (that cost is paid through the Wound Penalty instead). Trauma accrues only from specific, named sources: privation (starvation, Forced March \- see Food and Water and [[Traveling|traveling]]), a handful of paid Feat and spell costs that explicitly grant it (Deep Devotion's fasting, Temporal Fortification's backlash, and similar), and anything else that explicitly says so. If a rule doesn't name Trauma, it doesn't grant it.
