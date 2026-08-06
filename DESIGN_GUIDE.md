# Design Pillars \- Ressam

Ressam is built around deliberate design goals, each one addressing a specific problem found in other TTRPGs. Every mechanic, item, and rule should be measured against these pillars.

---

## Realism

Ressam aims to *feel* like 16th-century combat \- not simulate it. There's a meaningful difference. Armor in reality would rarely degrade at all, and only against firearms or crossbows; but having it degrade over a fight *feels* right for the setting. This is the guiding principle: mechanics should evoke the setting, not replicate it literally. Realism should be delivered through "realistic-lite" systems that hold up emotionally, not clinically.

## Elegance

Each individual mechanic must be simple on its own. Ressam's depth comes from *layering* simple rules \- not from making any single complex system. If a mechanic requires a calculator, or causes eyes to glaze over mid-explanation, it should be questioned.

## Scarcity

D\&D was designed for 6-8 encounters per day. Modern play rarely exceeds 1-2, meaning players arrive at every fight fully resourced \- breaking the intended economy of attrition. Ressam addresses this directly: give players fewer resources and make rest harder to abuse. Fewer encounters are needed to achieve the right feel of tension and scarcity.

## Niches

Ressam doesn't need to be perfectly balanced, but everything in it must have a purpose. Every item, weapon, class feature, race, and feat should fill a clear and distinct role. If something lacks a reasonable intended use, ask whether it needs to exist at all.

## Distinction

The power gap between Martials and Casters is a known problem. Ressam aims to narrow it \- not by making them equal, but by making them *different*. Casters should dominate at control, area damage, and utility. Martials should out-sustain them in extended fights and lead in close-range and long-range single-target damage, with reliable but clunkier utility options. A Martial should never feel strictly *worse* than a Caster \- only different.

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

Each School of Magic must feel wholly unique in play. For every spell, ask: *Does this feel like its school? Could it belong to another? What makes it a strong fit here?* No spell should be a copy of another with only its damage type or rider effect swapped \- that's the role of Spell Crafting.

## Faith

Faith magic always requires Faith \- no exceptions. The source doesn't have to be a god or deity, but no mechanic should bypass faith or prayer entirely. Prestige Feats are the sole exception.

## Healing

Magical healing should almost always restore Temporary Wounds rather than permanent Wounds, outside of exceptional circumstances. Wounds are worth more than the old HP pool ever was, so a single healing effect should restore **1 Temporary Wound** as the baseline; **2-3** is reserved for effects that cost noticeably more (higher Mana Cost, an Action economy tax, a real drawback), and **no single effect should ever exceed 3**, even at its highest scaling tier. This caps both flat amounts and anything that scales off a variable (a target's max Wounds, additional Mana spent, dice size) - scaling healing off an open-ended variable is the thing to avoid, not just picking a big flat number.

**Cultivation and Alchemy are the only two sanctioned healing systems.** Every other school, Feat, or piece of equipment should route around Wound restoration entirely rather than adding a smaller version of it - a Necromancer's life-drain should refund Mana, not Wounds; a Divine Feat available to non-Cultivation casters shouldn't hand out Temp Wounds. This exists so healing stays legible as two deliberate build choices rather than a background hum every class and item quietly does a bit of. Racial traits are the narrow exception - a race's inherent, self-only, heavily-drawback-gated healing (a vampire's regeneration, a kill-triggered battlefield trait) is identity, not a repeatable system a party can lean on, and doesn't compete with Cultivation/Alchemy the way a spell or Feat available to any caster of a type would.

## Bypass

Spells should not bypass existing mechanics without a meaningful cost or drawback.

## Spellblades

Magic should not directly enable a Gish (martial/mage hybrid) playstyle. Invocation is the sole exception, with Benediction a partial one. A Gish should always be a compromise \- a character who uses Feats to bridge the gap, not one who naturally blends both modes without trade-offs.

---

# Feat Design Guidelines

## Real-World Grounding

General, Martial, and Skill Feats must be traceable to a real historical or modern martial art, tactic, or trade skill \- not an invented fantasy trick. Name and flavor plainly (describe the technique, don't reach for foreign or archaic jargon): "Double Charge" for double-shotting a matchlock, "Locksmith" for a feel for tension and pins, not an invented style name. Arcane and Divine Feats are the explicit exception \- magic is allowed the leeway these three categories aren't.

## No Flat Damage, No Extra Attacks

A Feat should never simply add flat damage to a hit, and should never grant an extra proactive attack. Bypassing AR (Seek the Seam, Double Charge), expanding crit range (Deadly Critical), or a Reaction-gated Riposte already earned through a won Maneuver exchange (maneuvers.md) are the sanctioned ways a Feat makes a fight more lethal \- not a bonus die tacked onto a hit.

## Lean Categories

Keep General, Martial, and Skill Feats to roughly 5-7 entries apiece. Prestige is exempt (capped at one-per-character by design, not a menu to prune or pad) and Arcane/Divine scale with their schools. A thin, sharply distinct list beats a long one padded with near-duplicates - if a new Feat doesn't fill a niche nothing else in its category covers, it doesn't earn a slot.

---

# Arcane & Divine Feat Guidelines

Feats that touch spellcasting sit closer to the Spell Design Guidelines above than to General/Martial/Skill Feats - lore and power creep are both easier to get wrong here than with an extra attack. Evaluate every Arcane or Divine Feat against these, on top of the shared Feat Design Guidelines above (Real-World Grounding is the one exception - Arcane and Divine remain exempt from that one, per its own text).

## Healing Stays Temporary

A Feat's healing effect follows the same rule as a spell's (Healing, above): restore Temporary Wounds, not permanent ones, outside of exceptional circumstances. A Feat is not itself the exceptional circumstance - don't use one as a side door to permanent healing a spell wouldn't be allowed to grant.

## Anything Created Is Temporary

Same logic as Creation, above, extended to Feats: a Feat that conjures a wall, a weapon, a light source, or any other object is describing something that fades, melts, or dissipates - never a permanent addition to the world. This protects Scarcity the same way Creation does for spells; a Feat is not a loophole around it.

## Damage Riders and Buffs Should Be Rare

Arcane and Divine Feats are exempt from the flat "No Flat Damage" ban that governs General/Martial/Skill Feats (Feat Design Guidelines, above) - some genuinely earn a small damage or buff rider (Elemental Specialization's resistance-piercing, for instance). But the exemption should stay rare and earned, not the default shape of a magic Feat. If a Feat's whole benefit is "+X to a roll" or "+Xd_ damage," it's a Spell Crafting upgrade wearing a Feat's name, not a Feat.

## Must Not Invalidate a Martial's Niche

Mirrors Distinction, above. A magic Feat should never let a caster match or beat a Martial at sustained single-target damage or close/long-range weapon combat - that's the Martial's lane. Casters win at control, area effect, and utility; a Feat that blurs this at the Feat layer undoes what Distinction is already protecting at the spell layer.

## Must Not Bypass Mechanics for Free

Mirrors Bypass, above. A Feat that skips a Ward, an AR check, a Mana cost, or an action-economy cost needs a real, matching cost of its own - a worse trade-off, a Reaction spent, a resource consumed. "Free" is the failure state, not the goal.

## Scale With Investment, Not Just Level

A magic Feat's power should grow with the rank you've put into the relevant school (or the Mana you spend), not sit as a flat, level-independent bonus. Metamagic and Elemental Specialization already do this - more options at \+2 ranks in a second school, resistance scaling per element chosen. Hold every new Feat to the same shape; it's the same "reward the climb, not the stat" instinct behind every other balance pass in this project.

## Faith Is Never Optional

Extends Faith, above, to the Feat layer specifically: a Divine Feat must be gated on Faith investment (FAI and/or a Divine school rank), like every current one already is. A Divine Feat that only checks CHA, or nothing at all, reopens the exact hole Unyielding Devotion was cut for.

## No Free Extra Casts

A Feat should never grant an additional spell cast, at reduced cost or for free, outside the existing Reactive Casting mechanic - this is magic's version of the "No Extra Attacks" rule (Feat Design Guidelines, above). If a Feat wants to let a caster do "more magic," it should shape or empower a cast already being paid for (Metamagic's model), not hand out a second one for free.