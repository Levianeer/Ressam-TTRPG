Magic schools are Feats, not Skills. See [[Magic Overview|magic_overview]]'s Casting section for the roll itself; this chapter is only how a caster buys into a school in the first place.

---

## The Shape of a Magic Feat

Every one of the ten schools - Aeromancy, Geomancy, Hydromancy, Pyromancy, Shadowmancy, Benediction, Cultivation, Invocation, Necration, Subjugation - uses the exact same template. Nothing below is school-specific; swap the school's name in and the rule is identical for all ten. A fully worked example (Pyromancy) follows the template so you can see it applied.

### **Tiers**

| Tier | Character Level | Workings Unlocked | Difficulty |
| :---- | :---: | :---: | :---: |
| **Novice** | 1st | Lesser | 5+ |
| **Adept** | 3rd | Common | 7+ |
| **Expert** | 5th | Greater | 9+ |
| **Master** | 8th | Legendary | 11+ |

**Master is the ceiling.** Nothing sits above it - a character's magic stops deepening at Level 8, and Feats from there on go to General, Martial, Skill, or Prestige picks, or to a different school's tiers, or to Combination Feats (below).

### **Unlock Feats**

**"\<School\>: Novice" / "\<School\>: Adept" / "\<School\>: Expert" / "\<School\>: Master"**

Taking a tier's Unlock Feat is what lets you learn and cast that school's workings at that tier's difficulty (see the table above and [[Magic Overview|magic_overview]]'s Learning Workings). **Unlocking a tier doesn't unlock the ones below it automatically for a new school** - the tiers form a straight line: you cannot skip Novice to take Adept, or Adept to take Expert, or Expert to take Master.

**Prerequisites:**

- **Novice:** Level 1
- **Adept:** Level 3, `<School>: Novice`
- **Expert:** Level 5, `<School>: Adept`
- **Master:** Level 8, `<School>: Expert`

There is no cap on how many different schools' Unlocks you hold at once beyond the Feat slots it costs you to buy them; the Feat economy is the only limiter (see `feats_overview.md`'s note on prerequisites vs. slot scarcity).

### **Focus Feats**

**"\<School\>: Novice Focus" / "\<School\>: Adept Focus" / "\<School\>: Expert Focus" / "\<School\>: Master Focus"**

Focus is built around [[Magic Overview|magic_overview]]'s Progression menu, spent one item at a time as you take each tier. **Unlike Unlock Feats, Focus Feats stack cumulatively** - each tier is its own Feat, held alongside the ones before it, not a replacement:

| Tier | Benefit |
| :---- | :---- |
| **Novice** | Choose one working you know as a **Signature Working**. Its difficulty is treated as one tier lower for you when you cast it (Common 7+ effectively 5+, and so on) - a Lesser-tier working has no lower tier to drop to, so this only pays off on a Common working or higher. |
| **Adept** | Channelling a Signature Working costs 1 less Trauma (minimum 0), by tier. |
| **Expert** | Choose a second Signature Working; both carry every benefit above. |
| **Master** | **Attunement.** Once per scene, the first Will point you spend is refunded immediately, before you finish committing the rest of the pool. |

**Prerequisites:** the matching tier's Unlock Feat in that school, plus the previous Focus tier (`<School>: Adept Focus` needs `<School>: Adept` and `<School>: Novice Focus`, and so on) - the same straight-line shape as Unlock Feats. A Focus Feat is always optional on top of its Unlock, never required - you can hold `Pyromancy: Adept` with no Focus at all and simply cast at the ordinary cost. Choosing which known working(s) are your Signature happens when you take the Feat, and can be changed on a Long Rest.

### **Combination Feats**

**"\<School A\> + \<School B\>: \<Working Name\>"**

A Combination Feat grants exactly one specific working that draws on two (occasionally more) schools at once - an effect neither school could produce alone. The working's own tier sets its DC and scope, same as any other working (see [[Magic Overview|magic_overview]]).

**Prerequisites:** the matching tier's Unlock Feat in **every** contributing school. A Common-tier Combination working needs `<School A>: Adept` and `<School B>: Adept` both held, not just one; a Lesser-tier Combination working only needs Novice in each.

Combination Feats are the pressure valve for late-game Feat slots once a build has run its schools up to Master with nothing higher to buy - see the worked example below for the shape one actually takes. The full roster (one or more per plausible school pairing) is a follow-up content pass, not part of this chassis.

---

## Worked Example: Pyromancy

### **Pyromancy: Novice**

You've learned to hold a working's shape in your mind long enough to loose it.

**Prerequisites:** Level 1
**Benefit:** You may learn and cast Pyromancy workings of Lesser difficulty (5+).

### **Pyromancy: Adept**

Fire no longer fights you on the way out - you shape the working instead of just surviving it.

**Prerequisites:** Level 3, Pyromancy: Novice
**Benefit:** You may learn and cast Pyromancy workings of Common difficulty (7+) and below.

### **Pyromancy: Expert**

You don't call fire anymore. You tell it where it already wanted to go.

**Prerequisites:** Level 5, Pyromancy: Adept
**Benefit:** You may learn and cast Pyromancy workings of Greater difficulty (9+) and below.

### **Pyromancy: Master**

The flame answers before you finish the thought.

**Prerequisites:** Level 8, Pyromancy: Expert
**Benefit:** You may learn and cast Pyromancy workings of any difficulty, Legendary (11+) included.

### **Pyromancy: Novice Focus**

**Prerequisites:** Pyromancy: Novice
**Benefit:** Choose one Pyromancy working you know as your Signature Working. Its difficulty is treated as one tier lower for you (Common 7+ effectively 5+, Greater 9+ effectively 7+, Legendary 11+ effectively 9+).

### **Pyromancy: Adept Focus**

**Prerequisites:** Pyromancy: Adept, Pyromancy: Novice Focus
**Benefit:** Channelling your Signature Working costs 1 less Trauma (minimum 0).

### **Pyromancy: Expert Focus**

**Prerequisites:** Pyromancy: Expert, Pyromancy: Adept Focus
**Benefit:** Choose a second Signature Working. It carries the difficulty discount and the Channelling Trauma discount too.

### **Pyromancy: Master Focus**

**Prerequisites:** Pyromancy: Master, Pyromancy: Expert Focus
**Benefit:** **Attunement.** Once per scene, the first Will point you spend on a Pyromancy working is refunded immediately.

### **Pyromancy + Geomancy: Molten Lance**

Where fire alone gutters and stone alone sits inert, this working keeps neither still - a lance of rock carried on its own melting heat, punching through what either school would only dent.

**Prerequisites:** Pyromancy: Adept, Geomancy: Adept
**Benefit:** Grants the Common-tier working *Molten Lance* (a targeted, dodgeable-shape working - see [[Casting|magic_overview]]). Full effect and damage dice are a content-pass item; this entry exists to show a Combination Feat's shape, not to finalize the working.

---

**Note:** Beyond this worked example, the full Unlock/Focus/Combination roster for the remaining nine schools is deliberately not written out here - see `TODO.md` for the follow-up pass that generates it, alongside the wider spell-list rebalance and expansion already flagged there.
