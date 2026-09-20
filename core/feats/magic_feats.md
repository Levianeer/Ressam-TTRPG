**2026-09-14: this file replaces `arcane_feats.md` and `divine_feats.md` outright.** Magic schools are no longer Skills funded by ARC or FAI (both deleted) - they're Feats. **2026-09-20:** retuned to the Lesser/Common/Greater/Legendary difficulty ladder and the Will/Push/Channel casting engine (see [[Magic Overview|magic_overview]]) - a fourth tier, Master, was added to cover Legendary workings, and Focus Feats were redesigned around Signature Workings rather than a flat roll bonus, since the new casting math has no slot for one. See [[Magic Overview|magic_overview]]'s Casting section for the roll itself; this chapter is only how a caster buys into a school in the first place.

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

**Master is the ceiling.** Nothing sits above it - a character's magic stops deepening at Level 8, and Feats from there on go to General, Martial, Skill, or Prestige picks, or to a different school's tiers, or to Combination Feats (below). *(Placeholder: Master's Level 8 gate hasn't seen table time - see `TODO.md`.)*

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

The new casting math (`1d12` per die of Will, take the highest, against a flat DC) has no room for a flat roll bonus the old rank system used - Focus is rebuilt around a **Signature Working** instead:

| Tier | Signature Workings | Benefit on each |
| :---- | :---: | :---- |
| **Novice** | 1 | Costs 1 less Will to cast (minimum 1) |
| **Adept** | 1 | As Novice, and may be Channelled once per Rest at no Trauma cost |
| **Expert** | 2 | As Adept |
| **Master** | 2 | As Adept, and Channelling it costs no Will either |

**Bonuses don't stack across tiers** - taking a higher Focus replaces the lower one's benefit outright; you never hold two Focus tiers in the same school at once. Choosing which known working(s) are your Signature happens when you take the Feat, and can be changed on a Long Rest.

**Prerequisites:** the matching tier's Unlock Feat in that school (`<School>: Novice Focus` needs `<School>: Novice`, and so on). A Focus Feat is always optional on top of its Unlock, never required - you can hold `Pyromancy: Adept` with no Focus at all and simply cast at the ordinary cost.

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
**Benefit:** Choose one Lesser-tier Pyromancy working you know as your Signature Working. It costs 1 less Will to cast (minimum 1).

### **Pyromancy: Adept Focus**

**Prerequisites:** Pyromancy: Adept
**Benefit:** As Novice Focus, and your Signature Working may be Channelled once per Rest at no Trauma cost. Replaces Pyromancy: Novice Focus; it does not stack with it.

### **Pyromancy: Expert Focus**

**Prerequisites:** Pyromancy: Expert
**Benefit:** As Adept Focus, and you gain a second Signature Working. Replaces Pyromancy: Adept Focus; it does not stack with it.

### **Pyromancy: Master Focus**

**Prerequisites:** Pyromancy: Master
**Benefit:** As Expert Focus, and Channelling either Signature Working costs no Will either, on top of no Trauma. Replaces Pyromancy: Expert Focus; it does not stack with it.

### **Pyromancy + Geomancy: Molten Lance**

Where fire alone gutters and stone alone sits inert, this working keeps neither still - a lance of rock carried on its own melting heat, punching through what either school would only dent.

**Prerequisites:** Pyromancy: Adept, Geomancy: Adept
**Benefit:** Grants the Common-tier working *Molten Lance* (a targeted, dodgeable-shape working - see [[Casting|magic_overview]]). Full effect and damage dice are a content-pass item; this entry exists to show a Combination Feat's shape, not to finalize the working.

---

**Note:** Beyond this worked example, the full Unlock/Focus/Combination roster for the remaining nine schools is deliberately not written out here - see `TODO.md` for the follow-up pass that generates it, alongside the wider spell-list rebalance and expansion already flagged there.
