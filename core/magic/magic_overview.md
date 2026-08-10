Magic is the manipulation of energy \- the two methods of manipulation fall into two schools of thought; precise formulae (Arcane) or divine petition (Divine). It is rare not just because people lack potential, but because they lack education and resources. With literacy rates below \~15%, magic remains confined to the wealthy, the religious, and the exceptionally lucky. Because talent is worthless if you have no way to learn.

**The Literacy Barrier:** The vast majority of people will never read a spell formula or holy text. Even those with high ARC or FAI cannot learn what they cannot read \- see [[Literacy|core_rules]]: only a character with **MIND 3+** is literate by default, and only a literate character can invest in an Arcane or Divine school.

- **Arcane Magic** requires reading complex magical formulae, access to spellbooks or teachers, materials for scribing, and years of study.  
- **Divine Magic** requires reading holy texts and scriptures, understanding theological doctrine, and genuine faith.

This is why hedge wizards are suspicious, wandering priests are valuable, and spellbooks are worth more than gold.

**For the deeper physics behind why magic behaves this way - and how to rule on an effect no spell list covers - see [[Laws of Magic|laws_of_magic]].**

---

## Universal Magic Rules

These rules apply to **all** spellcasting, whether Arcane or Divine.

### **Mana Pool**

**Maximum Mana \= MIND × 2**

Mana is your magical fuel, shared between Arcane and Divine magic if you practice both - one pool, spent on either path's spells.

**Casting at 0 Mana \= Death.** If you have no Mana and attempt to cast a spell with a Mana Cost, you instantly die.

### **Casting Requirements**

- **Spoken:** You must speak the spell's incantation aloud  
- **Free Hand:** At least one hand free for gestures  
- **Sound:** Spells create audible noise (radius \= Mana Cost × 5 feet)  
- **Line of Sight:** You must see your target (unless noted otherwise)

### **Armor and Spellcasting**

Armor Penalty applies to all Arcane spell rolls. Each rank in Armorer reduces the penalty by 1 (minimum 0). Divine's Petition Roll has no modifier for Armor Penalty to touch - see below.

---

## Magic in Combat

### **Spell Modifier (Arcane)**

Arcane spells use a single modifier when you cast:

**Spell Modifier \= Magic School Skill \- Armor Penalty**

Divine spells don't use a Spell Modifier at all - see Divine: The Petition Roll, below.

### **Arcane: Spell Attacks & Spell Overcomes**

**Spell Attacks:** Some Arcane spells require you to hit a target's physical defenses \- dodging, reflexes, and positioning.

**Roll:** 1d12 \+ Spell Modifier vs. target's **Evasion**

**Spell Overcomes:** Some Arcane spells target a creature's mental fortitude, physical resilience, or force of will rather than their ability to dodge. You roll to overcome the target's Ward.

**Roll:** 1d12 \+ Spell Modifier vs. target's Ward (5 \+ Attribute)

A spell will specify which attribute it targets (e.g. "Roll vs. target's MIND Ward"). This is a [[Contested Check|core_rules]] \- the target's Ward is their static defensive score, not a roll.

**Critical Hits:** Spell Attacks can crit on a natural 12 (roll damage twice, take the higher result, per the Critical Hits rules in Combat). Spell Overcomes cannot crit \- their power lies in their effects, not raw damage.

### **Divine: The Petition Roll**

Every Divine spell \- whatever it does, whoever or whatever it targets \- lives or dies on a single roll. It isn't a contest against the target at all: your god either answers or doesn't, and the target's own toughness, reflexes, or force of will never enter into it.

**Roll:** 1d12 vs. **DC 7**, a flat 50/50 with no modifier at all \- not Skill, not FAI, not Armor Penalty. Every Divine caster, from a dabbler with one rank in a school to a fully-invested specialist, lands a Petition at the same rate. Spell- or Feat-granted bonuses (Advantage, a flat \+2 to rolls in a specific school, and the like) still apply on top when something explicitly grants them \- what's gone is the *persistent* baseline modifier every roll used to carry.

- **Success:** The spell's full effect applies, exactly as written.
- **Failure:** Nothing happens. The Mana is spent regardless \- your god simply didn't answer this time.

No exceptions, no partial effect on a near-miss, and no crit on a natural 12 \- a Petition either lands whole or doesn't land at all. This is a deliberate departure from Arcane's contested rolls, above: Divine magic never checks a target's Evasion or Ward, and Divine spells never carry a Resist clause. See DESIGN\_GUIDE.md's Overcomes guideline for why this is intentional rather than an oversight.

### **Rite Mastery (Divine Only)**

If the roll itself never improves, what does investing in a Divine School actually buy you? Spell Access (below) is one answer - Skill Rank still gates which spells you can even learn. **Rite Mastery** is the other: your Divine School Skill Rank in a given school is how many times per Long Rest you may reroll a failed Petition Roll for a spell of that school.

- Spend 1 charge to reroll a failed Petition Roll. You must take the new result, even if it's worse.
- Only one reroll per casting \- charges don't stack on the same roll.
- Charges are tracked per school (a Rank 3 Benediction caster who's also Rank 1 in Cultivation has 3 Benediction charges and 1 Cultivation charge, not 4 of either).
- Charges refresh only on a **Long Rest** \- not a Field Rest. This is deliberately scarcer than a Field Rest's partial Mana: Skill's technique only resets after real, sustained downtime.

This is the split between the two stats that used to share a job: **FAI is how much your god gives you** when a Petition lands (the flat damage/effect bonus baked into most Divine spells) - **Skill is how many times you get to try again** when the first attempt doesn't. A dabbler and a specialist succeed at the same rate on any single roll; over the course of a Long Rest, the specialist's prayers fail far less often in practice, because they can afford to ask twice.

### **Magic Damage**

Subtract the target's AR from spell damage, then convert remaining damage to Wounds via the Wound Thresholds (see [[Wounds and Survival|wounds_and_survival]]). This applies whether the damage came from a successful Arcane Spell Attack/Overcome or a successful Divine Petition Roll.

## 

---

## The Two Paths of Magic

| Aspect | Arcane (Scribing) | Divine (Prayer) |
| :---- | :---- | :---- |
| **Mana Source** | Short Rest (small), Field Rest (partial), or Long Rest (full) \- full recovery needs civilization | Same Rest ladder as Arcane, same amounts \- but also requires genuine devotion performed during that Rest, or it grants no Mana at all |
| **Resolution** | Spell Attack vs. Evasion or Spell Overcome vs. Ward \- contested, scales with Skill/ARC, partial effect on a Resist, crits on a natural 12 | Petition Roll vs. a flat DC 7 \- no modifier, same odds for every caster, binary: full effect or nothing. Rite Mastery (Skill-gated rerolls) is where investment shows up instead |
| **Preparation** | Scribe scrolls, spending Mana in advance | None \- cast straight from your Mana pool |
| **Casting** | Consume scroll (no Mana cost at cast time) | Spend Mana per cast |
| **Flexibility** | Must predict what you'll need | Cast any known spell spontaneously |
| **Sharing** | Can give scrolls to allies | Personal only |
| **Risk** | Scrolls can be lost/destroyed; Stable-Scribed reserves have a carry cap | No physical component to lose |

Both paths draw from the same Mana pool if you practice both \- a hybrid caster's Rest fills the one shared total, provided any Divine devotion requirement for that Rest is also met (see Divine Magic: Faith & Prayer, below).

### 

## Arcane Magic: Study & Scribing

Arcane spells are scribed onto scrolls, then consumed to cast. There are two ways to scribe: **Quick Scribing**, done for free during a Field Rest or Long Rest, and **Stable Scribing**, a slower and costlier process reserved for trained professionals. Both draw on the same Mana \- the difference is time, cost, and how long the result lasts.

|  | Quick Scribing | Stable Scribing |
| :---- | :---- | :---- |
| **Time** | During a Field Rest or Long Rest | 1 day per Mana Cost |
| **Cost** | Mana \+ 1 sheet of Arcane Parchment per scroll | Mana \+ 1 sheet of Arcane Parchment per scroll \+ 100 Crown per Mana Cost |
| **Source** | Any caster, anywhere | Mage's Guild workshop or master-level teacher |
| **Decay** | Fades at your next Field Rest or Long Rest if unused | Does not decay |

### **Quick Scribing**

Each Field Rest or Long Rest, prepare spells by scribing them onto scrolls:

1. Choose spells from those you know  
2. Spend Mana equal to each spell's Mana Cost  
3. Consume 1 sheet of Arcane Parchment per scroll (Writing & Scholarly Supplies)  
4. Create scrolls (each \= one casting, consumed when used)

Scrolls can be traded, sold, or given to allies. A Quick-Scribed scroll's magic fades the moment you complete your next Field Rest or Long Rest, whether you used it or not \- the parchment survives, but the spell must be re-scribed. This is deliberate: Quick Scribing is a daily choice, not a stockpile. Decide what you'll need before you set out, because today's leftovers don't carry over to tomorrow.

**Losing Your Spellbook:** If lost, you can only scribe memorized spells (DM discretion \- perhaps 1-2 favorites). This is catastrophic.

### **Stable Scribing**

A scroll that resists decay takes far more effort to produce than a quick field-scribing \- precise, time-consuming work reserved for trained professionals rather than something managed between fights. Pay the Time and Crown cost above (in addition to the Mana cost and Arcane Parchment) at a Mage's Guild workshop, or under a master-level teacher, to produce a scroll that survives past your next Field Rest or Long Rest.

Stable Scribing is the only way to build a lasting reserve outside your daily prep \- and the carry cap below exists specifically to keep that reserve from growing into a bottomless armory.

### **Instability (Stable-Scribed scrolls only)**

Quick-Scribed scrolls never last long enough to build into a real hoard \- they're gone by your next Field Rest or Long Rest regardless. A permanent Stable-Scribed reserve is different: carrying too much concentrated, undecaying magic at once is dangerous, so it's capped outright.

**Carry Cap \= Maximum Mana.** You may carry Stable-Scribed scrolls up to a combined Mana Cost equal to your Maximum Mana. Quick-Scribed scrolls don't count against this. No Mage's Guild will scribe you past the cap, and any excess scroll you acquire by other means (looted, gifted) must be sold, given away, or destroyed before you can carry it.

## Divine Magic: Faith & Prayer

Divine magic is limited by Mana alone, same as Arcane, and it recovers on the same Short Rest / Field Rest / Long Rest ladder, in the same amounts, under the same shelter and food requirements ([[Resting|carrying_and_resting]]). Resting works the same for both paths. The one thing that's different: a Divine caster doesn't get that Rest's Mana for free.

### **Devotion Required**

If you have any ranks in a Divine school, receiving a Rest's Mana requires performing your deity's specific devotional act (see [[Divine Overview|divine_overview]]'s Prayer Requirements) at some point during that Rest. Skip it, and you regain no Mana from that Rest at all \- even if you also practice Arcane, since there's a single shared Mana pool, not a separate Arcane portion sincerity can't touch.

This is no longer flavor text with no mechanical weight: Ressam's gods are real and provable, and a Divine caster who's genuinely stopped believing, or can't credibly perform their god's proof under the circumstances, gains no Mana from that Rest. A pure Arcane caster with no Divine ranks never triggers this at all. DM's call on what counts as genuine; err toward the player's stated intent unless they're plainly not even trying.

A Rest's other benefits (Patched Wounds, Trauma recovery) are unaffected either way, whether or not the devotion requirement is met.

---

## Learning Spells

**Learning New Spells:** Learning new spells requires time, money and practice. When creating a new character you may spend 50 Crown per Mana Cost to ‘buy’ your starting spells. Otherwise you must invest the following:

|            | Arcane                              | Divine                                 |
|:----------:|:------------------------------------|:---------------------------------------|
|  **Time**  | 1 day studying per Mana Cost        | 1 day studying per Mana Cost           |
|  **Cost**  | 50 Crown per Mana Cost in materials | 50 Crown per Mana Cost in offerings    |
| **Source** | Scroll, spellbook, or teacher       | Holy scroll, vision, or priest teacher |

**Spell Access:** Your skill rank must **equal or exceed** the spell's Mana Cost, both for character creation and learning new spells after.

---

## Channeling Spells

Some spells have Channel as their duration, this means it requires concentration.

**Upkeep:** At the start of each of your turns you continue channeling, you must pay half the spell's Mana Cost (rounded down, minimum 1) to sustain it. If you can't or choose not to pay, the spell ends immediately. A Held channeled spell pays this same half-cost the moment it's released instead, since it may resolve before your next turn arrives.

**Breaking Concentration:** Whenever you take damage while channeling, you must succeed on a MIND Ward check or the spell ends immediately. The DC equals 15 or the damage you took, whichever is higher. Concentration also breaks automatically if you fall unconscious or die.

**Limit:** Casting a new channeled spell immediately ends the previous one.

---

**For small, instinctive Mana effects that fall outside a normal spell, see [[Minor Magic|minor_magic]].**
