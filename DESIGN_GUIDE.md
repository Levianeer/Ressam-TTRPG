# Design Pillars \- Ressam

Ressam is built around deliberate design goals, each one addressing a specific problem found in other TTRPGs. Every mechanic, item, and rule should be measured against these pillars.

---

## Realism

Ressam aims to *feel* like (dated to 1517 AD) 16th-century combat \- not simulate it. There's a meaningful difference. Armor in reality would rarely degrade at all, and only against firearms or crossbows; but having it degrade over a fight *feels* right for the setting. This is the guiding principle: mechanics should evoke the setting, not replicate it literally. Realism should be delivered through "realistic-lite" systems that hold up emotionally, not clinically.

**Martial combat specifically is HEMA-lite.** The melee exchange loop takes its structure - a shared engagement distance both sides read and manipulate, a contested exchange that can chain rather than resolve in one roll - from historical European fencing systems (German and Italian longsword traditions chief among them). This is a *reference*, not a mandate to import real-world terminology wholesale: the same "feel, don't simulate" logic above applies, and the same plain-naming instinct the Feat Design Guidelines already ask for ("describe the technique, don't reach for foreign or archaic jargon") should guide new martial mechanics here too. Draw on HEMA for how an exchange *should feel* at the table \- not as license to reach for period jargon by default.

## Elegance

Each individual mechanic must be simple on its own. Ressam's depth comes from *layering* simple rules \- not from making any single complex system. If a mechanic requires a calculator, or causes eyes to glaze over mid-explanation, it should be questioned.

## Scarcity

D\&D was designed for 6-8 encounters per day. Modern play rarely exceeds 1-2, meaning players arrive at every fight fully resourced \- breaking the intended economy of attrition. Ressam addresses this directly: give players fewer resources and make rest harder to abuse. Fewer encounters are needed to achieve the right feel of tension and scarcity.

### **Scarcity applies to prerequisites too, in the opposite direction**

A Feat slot is already scarce - six of them across twelve levels at a **C** priority, against 5th Edition's five Ability Score Improvements plus whatever a class hands out. **The slot is the cost; the prerequisite is only there to say what kind of character this is.** Charging twice - a scarce slot *and* a high Attribute - is what puts a Feat out of reach entirely rather than making it feel earned.

The comparison worth keeping in mind: Ressam's Attributes now map almost exactly onto 5th Edition's ability *modifiers* (our 2 is a 14-15, our 3 a 16-17, our 5 a 20), and its standard array is nearly ours - **\+2, \+2, \+1, \+1, \+0, \-1** against our **C**'s 2, 2, 1, 1, 0, 0. That makes 5e a usable yardstick for numbers of this shape, and the yardstick reads: **every ability-score prerequisite in 5e is exactly 13 - a \+1 modifier - and never higher**, with its later General feats using a flat *Level 4\+* gate instead of a bigger number. Ressam allows 2 on an ordinary Feat and 3 on a Prestige Feat, which is already a step and two steps past what 5e ever asks. See [[Feats|feats_overview]] for the rule as written.

**The mirror is a sanity check, not a target.** Ressam is a lethal, crunchier game and is supposed to say no more often than 5e does - but it should say no through the Feat economy, Skill investment, and the Attribute a build actually needed anyway, not by naming a number the character cannot reach until Level 8.

### **Know the ceiling of your own dice before you set a number**

Every roll in Ressam is `1d12` plus a single number from 0 to 5 - Skill Ranks on a Check, an Attribute on a Ward. Two facts follow, and both are load-bearing whenever a DC, a prerequisite or a threshold gets written:

- **The highest total anyone can produce is 17.** Not "very unlikely" - impossible. The nine-tier DC scale used to run to 20 and had two rungs nothing could reach; Alchemy asked DC 20 for Rare concoctions and spent the ingredients on the guaranteed failure. Neither was a balance decision anybody made, they were arithmetic nobody checked.
- **The d12 is flat, so 2 points of DC is exactly one step of one in six**, at every modifier, with no curve to soften the edges. A number set one tier too high does not become "harder," it becomes 16.7 points of probability removed, and four tiers too high removes all of it.

**A roll that cannot succeed is worse than a ruling**, because it tells the player they had a chance. If the fiction demands a number past the ceiling, say no and move on - that is the "rulings not rules" the foreword asks for, applied honestly.

### **A Ward is not a Skill Check, and must not be priced like one**

A Skill Check is an attempt the character **opted into**, using training they chose to buy - so its DC may fairly assume the roller invested. A Ward Check is the reverse: **the danger names the Attribute**, and a standard array leaves most characters with two Attributes at 0. The same number is a different rule depending on which side of that line it sits on.

Set a Ward **one tier below** what the same fiction would take as a Skill Check, and keep an unannounced hazard at Very Hard or lower. At the top of the scale a Ward stops being a roll for anyone who did not build that Attribute - it is damage with a die attached, and the die is decoration.

## Niches

Ressam doesn't need to be perfectly balanced, but everything in it must have a purpose. Every item, weapon, class feature, race, and feat should fill a clear and distinct role. If something lacks a reasonable intended use, ask whether it needs to exist at all.

## Distinction

The power gap between Martials and Casters is a known problem. Ressam aims to narrow it \- not fix, but narrow by making them *different*. Casters should dominate at control and area damage. Martials should out-sustain and dominate in single-target damage.

---

# Spell Design Guidelines

Magic is difficult to balance in a system grounded in 16th-century martial combat. Every spell should be evaluated through the following lenses. Several of these (Creation, Healing, Summoning, Faith, Bypass) are the production-side rule for something `core/magic/laws_of_magic.md` states as in-fiction physics (Borrowed Substance, Conservation, the Soul, Reciprocity) - that file is where the *why* lives, and where to check when a proposed spell's legality isn't obvious from these lenses alone.

## Overcomes

Arcane Overcomes should always do *something*, even on a failure. Save-or-suck spells are a design failure: a binary of overwhelming effect or nothing. Arcane Overcome spells carry a guaranteed minimum effect (a Resist clause), with their successes being less powerful than their D\&D equivalents as a trade-off for that reliability.

**Divine spells are the deliberate exception.** Every Divine spell resolves on a single Petition Roll against a flat DC (see `magic_overview.md`'s Magic in Combat section) - full effect or nothing, no Resist clause, no partial credit. This isn't an oversight of the rule above; it's Divine trading Arcane's soft partial-effect safety net for a mechanic that ignores the target's defenses entirely. Divine spellcasting *is* save-or-suck, on purpose - that's the cost of a check that never asks what the target brings to the moment, not a hole in this guideline. Don't extend this exception to Arcane by analogy; the two paths are meant to feel different here.

## Summoning

Summoning belongs almost exclusively to Necromancy. Creating living creatures should be severely limited \- tied to story beats rather than combat mechanics.

## Creation

Magic cannot create matter or resources from nothing \- only transform, move, or accelerate what's already there. Water is drawn from an existing source or ambient moisture, not conjured; fire needs fuel and spark to work with, not a flame from nothing; food is ripened or preserved, not generated. This exists to protect Scarcity \- rations, water, and light sources (torches, oil) are tracked resources, and a spell that manufactures them for free quietly guts that tracking rather than working within it.

## Schools

Each School of Magic must feel wholly unique in play. For every spell, ask: *Does this feel like its school? Could it belong to another? What makes it a strong fit here?* No spell should be a copy of another with only its damage type or rider effect swapped \- a reskin like that doesn't earn its own slot on the list.

## Faith

Faith magic always requires Faith \- no exceptions. The source doesn't have to be a god or deity, but no mechanic should bypass faith or prayer entirely. Prestige Feats are the sole exception.

## Healing

Magical healing should almost always restore Patched Wounds rather than permanent Wounds, outside of exceptional circumstances. Wounds are worth more than the old HP pool ever was, so a single healing effect should restore **1 Patched Wound** as the baseline; **2-3** is reserved for effects that cost noticeably more (higher Mana Cost, an Action economy tax, a real drawback), and **no single effect should ever exceed 3**, even at its highest scaling tier. This caps both flat amounts and anything that scales off a variable (a target's max Wounds, additional Mana spent, dice size) - scaling healing off an open-ended variable is the thing to avoid, not just picking a big flat number.

**Cultivation and Alchemy are the only two sanctioned healing systems.** Every other school, Feat, or piece of equipment should route around Wound restoration entirely rather than adding a smaller version of it - a Necromancer's life-drain should refund Mana, not Wounds; a Divine Feat available to non-Cultivation casters shouldn't hand out Patched Wounds. This exists so healing stays legible as two deliberate build choices rather than a background hum every class and item quietly does a bit of. Racial traits are the narrow exception - a race's inherent, self-only, heavily-drawback-gated healing (a vampire's regeneration, a kill-triggered battlefield trait) is identity, not a repeatable system a party can lean on, and doesn't compete with Cultivation/Alchemy the way a spell or Feat available to any caster of a type would.

## Bypass

Spells should not bypass existing mechanics without a meaningful cost or drawback.

## Spellblades

Magic should not directly enable a Gish (martial/mage hybrid) playstyle. Invocation is the sole exception, with Benediction a partial one. A Gish should always be a compromise \- a character who uses Feats to bridge the gap, not one who naturally blends both modes without trade-offs.

---

# Feat Design Guidelines

## Real-World Grounding

General, Martial, and Skill Feats must be traceable to a real historical or modern martial art, tactic, or trade skill \- not an invented fantasy trick. Name and flavor plainly (describe the technique, don't reach for foreign or archaic jargon): "Double Charge" for double-shotting a matchlock, "Tradecraft" for a feel for tension and pins or a read on broken twigs and trail-sign, not an invented style name. Arcane and Divine Feats are the explicit exception \- magic is allowed the leeway these three categories aren't.

## No Flat Damage, No Extra Attacks

A Feat should never simply add flat damage to a hit, and should never grant an extra proactive attack. Bypassing AR (Seek the Seam, Double Charge), or a **Riposte taken as an Opening** \- a free attack *earned* by winning a contest by 5, not granted (exchange.md) \- are the sanctioned ways a Feat makes a fight more lethal \- not a bonus die tacked onto a hit.

## Lean Categories

Keep General, Martial, and Skill Feats to roughly 5-7 entries apiece. Prestige is exempt (capped at one-per-character by design, not a menu to prune or pad) and Arcane/Divine scale with their schools. A thin, sharply distinct list beats a long one padded with near-duplicates - if a new Feat doesn't fill a niche nothing else in its category covers, it doesn't earn a slot.

---

# Arcane & Divine Feat Guidelines

Feats that touch spellcasting sit closer to the Spell Design Guidelines above than to General/Martial/Skill Feats - lore and power creep are both easier to get wrong here than with an extra attack. Evaluate every Arcane or Divine Feat against these, on top of the shared Feat Design Guidelines above (Real-World Grounding is the one exception - Arcane and Divine remain exempt from that one, per its own text).

## Healing Stays Temporary

A Feat's healing effect follows the same rule as a spell's (Healing, above): restore Patched Wounds, not permanent ones, outside of exceptional circumstances. A Feat is not itself the exceptional circumstance - don't use one as a side door to permanent healing a spell wouldn't be allowed to grant.

## Anything Created Is Temporary

Same logic as Creation, above, extended to Feats: a Feat that conjures a wall, a weapon, a light source, or any other object is describing something that fades, melts, or dissipates - never a permanent addition to the world. This protects Scarcity the same way Creation does for spells; a Feat is not a loophole around it.

## Damage Riders and Buffs Should Be Rare

Arcane and Divine Feats are exempt from the flat "No Flat Damage" ban that governs General/Martial/Skill Feats (Feat Design Guidelines, above) - some genuinely earn a small damage or buff rider (Elemental Specialization's resistance-piercing, for instance). But the exemption should stay rare and earned, not the default shape of a magic Feat. If a Feat's whole benefit is "+X to a roll" or "+Xd_ damage," it's a flat numeric upgrade wearing a Feat's name, not a Feat.

## Must Not Invalidate a Martial's Niche

Mirrors Distinction, above. A magic Feat should never let a caster match or beat a Martial at sustained single-target damage or close/long-range weapon combat - that's the Martial's lane. Casters win at control, area effect, and utility; a Feat that blurs this at the Feat layer undoes what Distinction is already protecting at the spell layer.

## Must Not Bypass Mechanics for Free

Mirrors Bypass, above. A Feat that skips a Ward, an AR check, a Mana cost, or an action-economy cost needs a real, matching cost of its own - a worse trade-off, a **Tempo Die** spent, a resource consumed. The die is now the only currency in a fight, so "a real, matching cost" has exactly one honest shape. "Free" is the failure state, not the goal.

## Scale With Investment, Not Just Level

A magic Feat's power should grow with the rank you've put into the relevant school (or the Mana you spend), not sit as a flat, level-independent bonus. Metamagic and Elemental Specialization already do this - more options at \+2 ranks in a second school, resistance scaling per element chosen. Hold every new Feat to the same shape; it's the same "reward the climb, not the stat" instinct behind every other balance pass in this project.

## Faith Is Never Optional

Extends Faith, above, to the Feat layer specifically: a Divine Feat must be gated on Faith investment (FAI and/or a Divine school rank), like every current one already is. A Divine Feat that only checks CHA, or nothing at all, reopens the exact hole Unyielding Devotion was cut for.

## No Free Extra Casts

A Feat should never grant an additional spell cast, at reduced cost or for free, outside the existing Reactive Casting mechanic - this is magic's version of the "No Extra Attacks" rule (Feat Design Guidelines, above). If a Feat wants to let a caster do "more magic," it should shape or empower a cast already being paid for (Metamagic's model), not hand out a second one for free.