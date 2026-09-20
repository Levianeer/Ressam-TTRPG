# The Exchange - design log

Working notes behind `exchange_draft.md`: why the rules are shaped the way they are, what was measured, what was tried and rejected, and what is still open. **None of this is player-facing.** The rules doc is self-contained; this file exists so that nobody re-derives a dead end or re-adopts a withdrawn finding.

> ## STOP - READ ITEM 54 AT THE END OF THIS FILE FIRST *(2026-08-22)*
>
> **Item 54 is the state of `exchange_draft.md`.** It is a full read of the draft against the live files it has to merge into, and it **supersedes every "open", "pick up here" and "still to do" list anywhere above it.** Start there. Everything before it is how the draft got that way, and item 53 carries the downstream merge checklist that item 54 amends.
>
> **The system, in five lines.** Melee resolves through a **Tempo Pool** - `DEX \+ 1` dice, each sized by STR (`1d4` at STR 1 to `1d12` at STR 5), refilling at the start of your turn and funding attack and defence alike. An attack is `1d(Tempo Die) \+ Weapon Skill \+ Distance \+ type`, one die each, **with the whole sequence declared and paid up front**. **There is no unpaid defence of any kind**: a Tempo Die buys a Parry, and an attack nobody pays for lands and pays the attacker an Opening as though they had won by 5. Higher total wins, ties to the defender; margin 5\+ takes an Opening (4 or 3 with a sharp weapon), and **there are no critical hits** - the margin-10 crit was deleted at the merge, see item 62. **Every landed blow strips a Tempo Die (Shock).** Distance is two ranges on a square grid with **four Measure Bands** across them, `\-2` one Band off and no roll two Bands off. `Initiative \= 5 \+ MIND`, static. Armour is AR and its decay, and nothing in a fight reads Armor Penalty.
>
> **Pruned 2026-08-22, and the numbering is not contiguous because of it.** This file previously carried around 1,300 lines describing the **pre-Tempo-Pool system** - Reactions, the hex track, the Advance/Hold/Withdraw Cycle, Stance, Funding, Posture, Oppose and the Margin tiers - along with a SIGN-OFF block that had declared itself stale and every open question that had since closed. All of it is deleted. **Item 31 is now the earliest entry**, and it is the rebuild that made the rest history. So: a reference to an "item" numbered below 31, to a `Levers tried` entry, or to the SIGN-OFF block points at cleared text and should be read as *"recorded before the rebuild"*; and in the trailing **Open questions** list, 1, 2, 4, 5, 7, 8, 9 and 14 are gone, their content absorbed into items 40-52, the laws block and question 3.
>
> **Nothing in the current draft has been simulated since item 52, and item 54 measured nothing at all.** `tools/tempo_sim.py` is the only live tool. `tools/exchange_sim.py` and `tools/exchange_solver.py` model a system that no longer exists and should be deleted rather than adapted.

---

## 31. Ground-up rebuild: the Tempo Pool. The current system starts here *(2026-08-21)*

**Decision: `exchange_draft.md` was rewritten from nothing. Reactions are deleted as a resource, the four-Band hex track and the Advance/Hold/Withdraw Cycle are deleted, and melee now resolves through a single dice pool that funds both attacking and defending.** Driven by playtester feedback, not by a measurement in this file.

### The system in five lines

- **`Tempo Pool \= DEX` dice, each sized by STR** (`1d4` at STR 1 through `1d12` at STR 5). Refills at the start of your turn.
- **One pool funds everything off-turn and every extra thing on-turn.** Reactions are gone; `1 Reaction` converts to `1 Tempo Die` one-for-one.
- **Attack: `1d(Tempo Die) \+ Weapon Skill \+ Distance`.** Free as a **Basic Attack**; spend a die to make it **Feint**, **Press**, or **Measured**.
- **Defend by spending a die** on **Parry**, **Block**, or **Dodge**, or spend nothing and stand on **Passive Evasion**. Ties go to the defender.
- **Margin 5\+ takes an Opening** (Riposte, Called Shot, Disarm, Shove, Break Away, Strip Tempo, Feats). **Margin 10\+** is the new critical hit.

### Why the pivot was accepted rather than argued with

The design that this file spent thirty items tuning had one structural property nobody could tune away: **defending was free.** A Reaction count you had not touched all round decided whether you got to answer a blow, so the decision was made for you by a counter rather than by you. The Cycle, Stance, Funding, Posture and the reactive-step limit were all, in retrospect, machinery bolted on to manufacture a decision that a shared pool produces for free.

**The shared pool is the whole design.** Offence and defence drawing on the same dice is what makes the third swing on your turn cost the guard you will not have when the answer comes. Item 4's finding - *"the model has no reason for anyone ever to be attacked, so patience is free in it"* - is finally answered structurally rather than by rule: patience now costs dice, and so does aggression, out of the same bag.

**Passive Evasion became load-bearing and that is the second-best thing here.** Declining to defend is a real play with a real floor, so an empty pool costs you quality rather than participation. This is the same instinct as the old draft's refusal to let a conscious fighter not roll, arrived at more cheaply.

### What was knowingly given up

**The spatial layer, more or less entirely.** Four Bands on hexes became two distances on 5ft squares (Adjacent / Reach), and three reach classes became `Short` (Adjacent only), `Arming` (both), `Long` (Reach at 0, Adjacent at \-2). The approach - the multi-Exchange closing sequence that made a spear feel different from a sword *over time* - does not survive this. Depth moved from *where you are standing* to *what you are spending*. The user's own framing: "this is definitely the weaker side of things, but it is worth the sacrifice and can be workshopped later."

**Half of this was a misreading, corrected 2026-08-22 - see item 51.** The four Bands were meant to *map onto* the two distances (Close/Middle at Adjacent, Long/Far at Reach), not to collapse into three classes. The Bands are back; the track, the approach and the Cycle are what actually went.

**The `1d12` universal roll**, in combat only. Every other check in Ressam is `1d12 \+ stuff`; melee is now `1d4` to `1d12`. This is the largest single Elegance cost in the draft and it is unavoidable if STR's contribution is to be anything other than a flat bonus. Direct consequence: a STR 1 caster contests melee with `1d4` and effectively cannot. Flagged to the user before writing; accepted as likely intent.

**Natural-roll criticals.** A `1d4` cannot carry a natural-max crit rule (25%). Crit is now `margin 10\+`, and Feats that widened a crit range convert to Feats that lower the crit threshold, one point per step.

**Everything measured before this item** (items 1-30, since cleared from this file). The reach curve, `ADVANCE_ALWAYS_CLOSES`, `TEMPO_MODE = "margin"`, `CYCLE_BONUS`, `REACTIVE_STEP`, the shield pricing from items 21 and 23, the declaration-policy solver from item 18 - none of it describes a mechanic that still exists. **The `Adopted-lever index` below and every figure above it are history.** The one durable transferable finding is item 21's *method*: a shield and a two-handed weapon compete for the same hand, so the two-hander sets the shield's price ceiling, measured at \+13 to \+16 points of win rate.

### What survived unchanged

`Initiative \= 5 \+ DEX` static, both rungs of Surprise as ruled on 2026-08-19 (Caught Out now costs the Major Action and keeps the pool; Ambushed now removes the pool entirely), `Passive Evasion \= 5 \+ DEX \- Armor Penalty`, `Damage \= Weapon Damage \+ Attribute \- AR`, Ward, and "no defence against a ranged attack" from item 15.

### One deliberate new rule for bosses

**A Mythic creature refills its Tempo Pool on every one of its Initiative counts.** Under a pool economy, the obvious party strategy against any single large enemy is to drain it and then act with impunity, which would make Mythic creatures *easier* the more turns they take. Refilling per count inverts that: a boss cannot be drained, and fighting one is about managing your own pool rather than exhausting its.

### Nothing here is measured, and the tools no longer apply

`tools/exchange_sim.py` and `tools/exchange_solver.py` model Bands, declarations and the Cycle. All three are gone, so both tools should be **rewritten, not adapted**. Every number in the new draft is a first-draft guess. The three most in need of a tool, in order:

1. **Whiff rate and round length.** A defended attack now misses roughly half the time and returns no damage when it does. The old system's Bind and Trade tiers meant both sides usually hit; that is gone, and combat may have quietly doubled in length.
2. **Whether emptying the pool on offence is dominant.** The cumulative \-2 on each attack after the first is the only brake on an alpha strike. If it is too weak the entire economy is decorative.
3. **`Pool \= DEX` at DEX 1.** One die per round may be unplayable. `Pool \= DEX \+ 1` is the obvious repair and should be decided early, since every other number is priced against pool size.

### Open, and carried into the draft

The draft's own *Open questions* section holds seven items. The three that could still change the shape rather than the numbers:

- **Whether Dodge should answer a ranged attack.** Item 15's "no defence against ranged" is a much harder position to hold under a universal defensive spend than it was under Reactions. Repair if wrong is small and pre-written: *Dodge may answer a ranged attack at \-2 and takes no Opening.* Do not spend it before an archer-heavy fight has been run.
- **DEX is now doing four jobs** - Tempo Pool, Passive Evasion, Initiative, and the Dodge Attribute - against STR's two. Probably the better Attribute as written. Repairs are upstream of this chapter.
- **Whether Riposte is simply the correct Opening every time**, which would make the other six entries on the menu decorative.

---

## 32. Four rulings on the Tempo Pool draft, all closed the same day *(2026-08-21)*

Four items from item 31's open list, settled by the designer within hours of the draft landing. None is measured; all four are judgement calls, and three of them close questions the draft itself had flagged.

### The free attack is deleted, and the reason it was wrong is worth keeping

**Decision: there is no untyped, no-cost attack. Every attack costs a Tempo Die and every attack is a Feint, a Press, or a Measured.**

The free **Basic Attack** existed as a floor - so that a fighter with an empty pool never had a dead turn. **That floor was guarding a state that cannot occur.** The pool refills at the *start of your turn*, so you always begin your own turn with `DEX \+ 1` dice; an empty pool is something that happens to you during somebody else's turn, and on somebody else's turn the only thing you would have spent a die on is defending, which Passive Evasion already covers for free.

What the free attack actually did, having no floor to hold up:

- **It made the first swing of every turn the one swing that was not a decision.** Every fighter opened identically, every turn, forever.
- **It made the pool a dishonest count.** "Your pool is how many things you do this round" was false by exactly one.
- **It sat awkwardly beside Measured**, which is the same idea priced properly - a swing that can cost you nothing, at `\-2` and only if you win it.

**Measured inherits the job.** This is the substantive consequence and it is not free: Measured is now the only attack in the chapter that can pay for itself, which is a much stronger position than it held with a genuinely free swing sitting next to it. **New open question, now the draft's number 1:** whether `\-2` is far too cheap for a full refund, in which case a fighter opens every turn with Measured until one lands and Feint and Press are decorative. Three repairs are pre-written in ascending order of disruption - price it at `\-3`, refund only on an Opening, or refund only the first Measured of your turn - and **none should be spent before the dumping question is answered**, because Measured is the main thing that makes dumping affordable.

**Term retained:** a **plain attack** (no type, cannot take an Opening) still exists, but only as something that *arises* - from a Riposte taken as an Opening, or from an Opportunity Attack. It is never a thing you choose.

### `Pool \= DEX \+ 1`

**Decision: adopted, exactly as the draft proposed it.** At `DEX` flat a DEX 1 fighter has one die per round - one attack or one parry, never both - which is not a lean build but a character who cannot participate in a round. The `\+1` is constant across the range so it changes no build's ranking, and it is the difference between a hard choice and no choice at the bottom.

### Dodge does not answer arrows - closed, not deferred

**Decision: the 2026-08-17 ruling stands unchanged. No Tempo Die answers a ranged attack; ranged attacks cannot be Parried, Blocked, Dodged, or take Openings.**

The draft had flagged this as "the most likely thing in the chapter to be wrong" on the grounds that a universal defensive spend which stops at arrows is a rule players will push on. Overruled, and the hedging removed from the draft text. Two reasons now stated in the rules rather than the log:

1. **It is the entire ranged/melee distinction.** *A threat you fight* versus *a threat you solve with the map* is the only structural difference between the two in this system. Making Dodge universal buys a small gain in intuitiveness and spends that distinction to get it - and an archer who is answered the same way a swordsman is has no reason to exist as a build.
2. **The fiction is the right way round, not a concession.** You do not see the arrow; you see the bow, before it is loosed, and everything you can do about it you do then. That is exactly what the rule models - your answer to archery is taken on your own turn, with your feet, against the shooter rather than against the shot.

### Initiative moves to MIND

**Decision: `Initiative \= 5 \+ MIND`**, static, unrolled, Armor Penalty still not applied. Was `5 \+ DEX`.

**Why it moves cleanly.** DEX is already the whole of your reflexes, priced as the Tempo Pool - it buys how many times you get to react, which is what a reflex is. Turn order is a different question: who reads the room, who sees the fight starting, who has already decided while everyone else is deciding whether. `attributes_and_skills.md` describes MIND as intelligence and reasoning, which is that faculty.

**Two things it fixes.** It takes one of four jobs off DEX (which retains the Tempo Pool, Passive Evasion and the Dodge roll against STR's die size and damage - still probably the better Attribute, now the draft's open question 3). And it gives the party's thinkers, who have no Tempo Pool worth the name, one thing they are structurally first at.

**Note the `5 \+ Attribute` shape is preserved**, so it is still a Passive-Ward-conventioned number that most sheets already carry. Mythic Initiative's `\-2` spacing is unaffected; a party's spread of MIND scores is comparable to its spread of DEX scores, so the counts still interleave.

### One consistency bug fixed in passing

Passive Evasion read *"lands if the attacker's total meets or beats"* while the contest rule read *"ties go to the defender."* Those disagree. **Passive Evasion is now treated exactly as a defence roll that came up at that number, ties included: an attack must exceed it.** Both worked examples were rebuilt against the new pool sizes and the corrected tie rule.

### Next

Agreed with the designer: build a fresh simulator, and point it first at **whether emptying the pool on offence is dominant**. Nothing else in the chapter can be tuned honestly until the policy question is answered, because every number is currently priced against a play pattern we are guessing at.

---

## 33. First measurement of the Tempo Pool. Dumping is fine; the STR ladder is not *(2026-08-21)*

**New tool: `tools/tempo_sim.py`.** Written from scratch; `exchange_sim.py` and `exchange_solver.py` model Bands, declarations and the Cycle and were not adapted. 1v1, both Adjacent at reach modifier 0 for the whole fight, no terrain, no movement, no Feats, no off-hand tools, no Conditions. Reach is deliberately excluded so it cannot confound the policy question. Win rates are symmetrised across turn order. Three builds, all Skill 3, all Longsword `1d6 \+ 2`:

| | STR | die | DEX | pool | AR | Passive Evasion |
| :---- | :----: | :----: | :----: | :----: | :----: | :----: |
| **Baseline** | 3 | `1d8` | 2 | 3 | 4 | 5 |
| **Quick** | 2 | `1d6` | 4 | 5 | 2 | 8 |
| **Strong** | 5 | `1d12` | 1 | 2 | 4 | 4 |

### The question we asked: is dumping the pool dominant? **No. It is bad.**

Mirror match, row policy's win rate against column policy. `hold N` \= keep N dice back on your turn.

| Baseline (pool 3) | dump | hold 1 | hold 2 |
| :---- | :----: | :----: | :----: |
| **dump** | 48.8% | **18.1%** | **9.3%** |
| **hold 1** | 81.1% | 47.9% | 51.3% |
| **hold 2** | **90.0%** | 46.7% | 50.2% |

Dumping loses to holding one die 81-19 and to holding two 90-10. At pool 2 (Strong) it is a wash, because there is nothing meaningful to hold. **The escalating `\-2` is not too weak - it may be too strong**, and the defensive half of the pool is not decorative at all.

**The cost is fight length.** Baseline mirror: 2.58 rounds at dump, 3.94 at hold 1, **6.02 at hold 2**. Turtling works and it drags. That is the tuning tension in this system, and it is a better one to have than the alternative.

**Two model bugs were found and fixed mid-run**, both understating Measured: the attack budget was frozen at the top of the turn so a Measured refund never bought another attack, and `winrate` reported an all-draw matchup as `0.0%` instead of flagging a stall. Every figure above is post-fix.

### The question we did not ask, and the actual finding: **a flat `\±2` means five different things**

Measured and Press are written as flat `\-2` and `\+2`. Against a `1d4` that is half the die; against a `1d12` it is a sixth of it. Measured out of a `1d6` is close to a concession.

| Baseline (pool 3), row type vs column type | measured | press | mixed |
| :---- | :----: | :----: | :----: |
| **measured** | 49.4% | **23.9%** | 36.6% |
| **press** | **75.6%** | 51.4% | 55.5% |
| **mixed** | 61.5% | 42.4% | 47.7% |

For Quick (`1d6`), Press beats Measured **98.6-1.4**. Only at Strong (`1d12`) does the sign flip and mixed/Measured beat Press.

**This inverts the draft's open question 1**, which worried that Measured was too cheap and would dominate. It does not dominate anywhere except at the top of the die ladder. **Press dominates**, and it dominates hardest on exactly the builds that can least afford to be hit.

### And the reason underneath all of it: the ladder is not a 4-point gap, it is near-exclusion

Closed-form, `P(attacker's contest roll exceeds defender's)`, equal Skill, no other modifiers:

| atk \\ def | `1d4` | `1d6` | `1d8` | `1d10` | `1d12` |
| :---- | :----: | :----: | :----: | :----: | :----: |
| **`1d4`** | 37.5% | 25.0% | 18.8% | 15.0% | **12.5%** |
| **`1d6`** | 58.3% | 41.7% | 31.2% | 25.0% | 20.8% |
| **`1d8`** | 68.8% | 56.2% | 43.8% | 35.0% | 29.2% |
| **`1d10`** | 75.0% | 65.0% | 55.0% | 45.0% | 37.5% |
| **`1d12`** | 79.2% | 70.8% | 62.5% | 54.2% | 45.8% |

Three things are visible at once and all three matter:

1. **`1d4` against `1d12` is 12.5%, not "four points down."** Both sides roll, so the variance gap compounds with the mean gap. STR 1 is not a weak melee build, it is a non-participant.
2. **The diagonal is never 50%.** Because the attacker must *exceed*, a mirror match is 37.5% at `1d4` rising to 45.8% at `1d12` - so losing ties is a bigger tax on small dice too.
3. **Passive Evasion is a hard wall, not a floor.** `1d4 \+ Skill 3` **cannot exceed a Passive Evasion of 7 at all**, ever. `1d6 \+ 3` clears a Passive Evasion of 8 only 16.7% of the time, and Measured takes that to 0%.

**Consequence: the Quick mirror match stalls 100% of the time.** Two STR 2 / DEX 4 fighters cannot kill each other - `1d6 \+ 3` against Passive Evasion 8 with five dice to spend on defence is a fight that never resolves. That is not a tuning problem, it is a broken state reachable by a legal build.

**Cross-build, each playing its best policy:** Strong beats Baseline **81.5-18.5** and beats Quick **89-11**. The STR build is not one of two viable directions; it is the direction.

### Diagnosis: `Passive Evasion \= 5 \+ DEX` was calibrated for a `1d12` game

This is the load-bearing sentence of the whole item. Under the previous draft everyone rolled `1d12 \+ Skill` and a Passive Evasion of 8 was ordinary. **The number was carried into the new draft unchanged while the die under it shrank to as little as `1d4`**, and a static target that was a speed bump against `1d12` is a wall against `1d6`.

It compounds with the second structural problem: **DEX buys the pool *and* Passive Evasion.** Every point of DEX makes you harder to hit and gives you another die to be hard to hit with, while STR buys the only thing that gets through.

**Confirmed by trying to fix the ladder alone.** A compressed ladder (`1d6/1d8/1d8/1d10/1d10`) does end the Quick stall - fights resolve in 16.6 rounds - and flips Quick vs Strong from 32.5% to 65.4%. But it also flips Baseline vs Quick to **25.8%**: once the dice are close, DEX's double dividend takes over completely. **Narrowing the ladder without moving Passive Evasion off DEX just swaps which Attribute is dominant.** (A "narrow" ladder that only raises STR 1 from `1d4` to `1d6` measured identically to the draft, because no test build has STR 1 - it addresses the dead zone and nothing else.)

### Four candidate repairs, none adopted, in ascending order of disruption

1. **Attacker wins ties.** Cheapest possible change, worth roughly `\+12` points in a mirror match, and it fixes the arithmetic oddity that a `1d4` fighter is taxed twice for losing ties. Measured on its own: nowhere near enough (Baseline vs Quick moved 59.8% to 56.4%; the Quick stall survived it).
2. **Type modifiers proportional to the die instead of flat.** Press and Measured as one die *step* (`1d8` becomes `1d10` / `1d6`) rather than `\±2` would mean the same thing at every STR. Costs a lookup at the table; buys the only version of these three types that is balanced across the ladder.
3. **Re-base Passive Evasion for the new die.** Either drop the constant (`5 \+ DEX` to `3 \+ DEX`) or take DEX out of it entirely. **This is the one the measurement most directly supports**, and taking DEX out also fixes the double dividend that repair 4 otherwise runs into.
4. **Compress the ladder.** Fixes the `1d4` dead zone and the stall, and must be paired with repair 3 or it simply hands dominance to DEX.

**Recommendation: 3 first, then re-measure before touching anything else.** It is the repair with the clearest causal story, it is upstream of the other three, and both 2 and 4 change meaning depending on what Passive Evasion is doing.

### Carried into the draft

The draft's open questions were rewritten against these figures. Open question 1 was inverted (it worried about Measured; the problem is Press), and open question 2 - the dumping question - is **closed**.

---

## 34. Passive Evasion deleted. The free Dodge replaces it - and STR still beats DEX *(2026-08-21)*

**Decision: `Passive Evasion` is removed from the Exchange entirely. Every attack is answered by a roll. A Dodge is free; a Tempo Die buys a better defence.** Designer's call, on a fictional argument, and the measurement supports it on two independent counts.

### The argument, which is the better one

*"Functionally there is no way to passive evade something, that is just your opp missing."* A blow that does not land is the attacker's **error**, not the defender's statistic. A static score models that backwards - as a wall the attacker must clear, rather than a swing that can go wide. This is the same instinct as item 31's refusal to let a conscious fighter not roll, applied one level deeper.

### The shape adopted

| Defence | Costs | Requires | Roll | Opening |
| :---- | :----: | :---- | :---- | :---- |
| **Dodge** | **nothing** | nothing at all | `1d(die) \+ DEX \- AP \- 2` | No |
| **Dodge, committed** | 1 die | an empty adjacent square | `1d(die) \+ DEX \- AP` | Break Away, Shove |
| **Parry** | 1 die | a weapon that acts at this Distance | `1d(die) \+ Skill \+ Distance` | full menu |
| **Block** | 1 die | a shield | `1d(die) \+ Skill \+ Guard` | Shove, Shield Bash |

**The free roll is a Dodge specifically** because Dodge is the defence that requires nothing - no weapon, no shield, no training, no Distance. A free Parry would mean an unarmed man parries.

**New ruling, and it earns Dodge a real niche: the Distance modifier applies to attacks, Parries and Blocks, never to a Dodge.** You are not answering with the weapon, so its length is not the question. This is what a polearm fighter who has been closed on actually has left, and it is the first thing in the draft that makes the `\-2` at Adjacent survivable rather than simply bad.

**Automatic hits now exist, and only where they belong.** A target who cannot act - unconscious, Incapacitated, helpless, or Ambushed in Round 1 - does not roll at all and the attack simply lands. That is the only auto-hit in the chapter.

### What it fixed, measured

**The stall is gone.** Two STR 2 / DEX 4 fighters previously could not kill each other - `1d6 \+ 3` against a Passive Evasion of 8, with five dice to spend on defence, stalled **100%** of the time. With the free Dodge they resolve.

**Fight length landed where it should.** Mirror matches run roughly **2 rounds**, against the previous system's measured 2.23. That was not a given: the free-Dodge modifier was swept at `\+0`, `\-1`, `\-2`, `\-3`, and it trades balance against length monotonically.

| free-Dodge mod | Base v Quick | Quick v Strong | Quick mirror | Base mirror |
| :---- | :----: | :----: | :----: | :----: |
| `\+0` | 75.6% | 12.2% | **STALL** | 2.5 rds |
| `\-1` | 61.4% | 20.6% | 8.2 rds | 2.1 rds |
| **`\-2`** | **55.2%** | **24.7%** | **5.0 rds** | **1.9 rds** |
| `\-3` | 51.5% | 28.2% | 3.3 rds | 1.6 rds |

`\-2` was adopted as the compromise: stall gone, length in line with precedent. **It is a number picked off a four-point sweep, not a solved one.**

### Two alternatives measured and rejected before landing on the free Dodge

**A flat DC for undefended attacks** (the "difficulty of connecting with a living person"): swept at 4, 6, 8, 10. Every setting either dragged fights out enormously (DC 6 gave a 22.7-round Quick mirror; DC 8 stalled again) or skewed the field hard (DC 4 put Baseline over Quick at 88%). **A static number is a static number** - re-basing it does not fix what is wrong with having one.

**Auto-hit on an empty pool.** Best-balanced column of anything tested (Base v Strong 48.5%, Quick v Strong 68.0% - the only configuration where the quick build beat the strong one) and **unusable**: fights ended in **1.0 to 1.1 rounds.** Whoever acts first wins. Recorded because the balance figure is genuinely interesting and may be worth revisiting if lethality is ever addressed upstream.

### What it did NOT fix, and this is now the headline problem

**Passive Evasion was not why STR beats DEX.** With gear, Skill and Attribute total held identical, mean win rate against the whole field, measured *after* the removal:

| | S5/D1 | S4/D2 | S3/D3 | S2/D4 | S1/D5 |
| :---- | :----: | :----: | :----: | :----: | :----: |
| **mean vs field** | 66.2% | **72.9%** | 56.2% | 36.0% | **17.6%** |

S4/D2 beats S1/D5 **98.9-1.1**. Spread across the field: **55 points.**

**The cause is that the two currencies have different return curves, and this is structural.** Die size has **no** diminishing returns - a bigger die improves every roll you make, offensive and defensive, first attack and fourth. Extra dice have **sharp** ones: every attack after the first takes a cumulative `\-2`, so the fourth die buys a markedly worse attack than the first. **Count is taxed; quality is not.** No exchange rate fixes that, because it is not an exchange-rate problem.

**Confirmed by removing STR from the damage formula:** 98.3% to 97.6%. Damage is not the cause.

**Confirmed again by sweeping the ladder**, which only chooses which end wins:

| Ladder | Dominant | Spread |
| :---- | :---- | :----: |
| `1d4`-`1d12` (as written) | STR, heavily | 25-56 pts |
| `1d6`/`1d6`/`1d8`/`1d8`/`1d10` | roughly even, middle builds best | **22 pts** |
| flat `1d8` (no ladder at all) | DEX, heavily | 44-50 pts |

The flattest configuration found anywhere is **the narrow ladder with the sequence penalty at `\-1`**, at 22 points. Nothing tested is flat. The honest reading: **a count-versus-size split has no flat setting, and the ladder width is a dial for choosing which extreme you are willing to make weaker.**

**A third job STR is doing, and it is upstream of this chapter.** `wounds_and_survival.md` keys the Wound Threshold table to STR, so a high-STR fighter takes fewer Wounds from identical damage. That was harmless when combat rolls were `1d12 \+ Skill` and STR touched neither of them. It is not harmless now: STR sets the contest die, the damage bonus, and the durability ladder, against DEX's pool count and Dodge.

### Also settled here

**Ranged needed a target once Passive Evasion was gone**, and it could not be a defence roll, because Dodge does not answer arrows (item 32). Adopted: **a Shot DC set by range, cover and movement - a property of the situation, not of the target.** A quick man and a slow one are equally hard to shoot standing in the open. This is the last static number in the chapter and it is static because it describes the shot. **Entirely unmeasured** - `tempo_sim.py` models melee only; the base of 7 was hand-set so a trained shooter hits an exposed target about three times in four.

### Tool

`tools/tempo_sim.py` was rewritten to this model - `passive_evasion` replaced by `free_dodge`, the defender's spend decision rebuilt around "is the paid defence better, and is this attack beatable but not already beaten," and the STR-vs-DEX field test promoted to a first-class section since it is now the live question. `FREE_DODGE_MOD` and `SEQ_PENALTY` are module-level switches.

---

## 35. The escalating `\-2` deleted. Largest balance change in this document *(2026-08-21)*

**Decision: there is no penalty and no cap on repeated attacks. Every attack costs 1 Tempo Die and rolls exactly like the first.**

### Where the rule came from, which is the point of this entry

It was **added speculatively in the first Tempo Pool draft, before anything had been measured**, against a hypothesised problem. The note attached to it at the time read: *"Without a brake, DEX 5 alpha-strikes. This is the only brake and it is the thing I most expect to need tuning."* It was never justified by evidence, and when evidence arrived it justified the opposite.

**Worth recording as a failure mode:** the rule survived two rounds of measurement because item 33's headline finding - *dumping is not dominant, 81-19* - was taken as confirmation that the brake worked, when it was equally consistent with the brake being unnecessary. **A measurement taken with a mechanism in place cannot tell you the mechanism is needed.** The question was only settled by switching it off.

### What it was actually doing - three jobs, one intended

| seq penalty | dumping brake | STR/DEX spread | mirror length |
| :----: | :---- | :----: | :----: |
| `0` | weak (dump wins ~52%) | **21.2 pts** | 1.31 rds |
| `\-1` | strong (dump 19-39%) | 45.9 pts | 1.88 rds |
| `\-2` (as written) | crushing (dump 2-27%) | 55.0 pts | 2.78 rds |

1. **The alpha-strike brake it was built for is redundant.** Every attack already costs a die and dice are also your defence; **the opportunity cost is the brake.** At `0` dumping wins ~52% in a duel - a slight edge, not dominance. And the sim is 1v1, which *understates* held dice: the value of a reserved die scales with how many people are attacking you, so a 52% duel edge very likely inverts in a party fight. (Unconfirmed - no multi-opponent sim exists.)
2. **It was setting fight length**, which it was never meant to do and which belongs to the Wounds layer.
3. **It was making STR the better Attribute.** An escalating penalty on *count* is a tax on precisely what DEX buys, while die size - what STR buys - has no diminishing returns at all.

**Deleting it cut the STR/DEX spread from 55.0 to 21.2 points**, the largest single balance result in this document, and removed a subtraction from every attack after the first. Mean win rate against the field:

| | S5/D1 | S4/D2 | S3/D3 | S2/D4 | S1/D5 |
| :---- | :----: | :----: | :----: | :----: | :----: |
| **with `\-2`** | 67% | **73%** | 57% | 36% | **18%** |
| **without** | 56% | 57% | 55% | 46% | **36%** |

### A cap was measured as the replacement and is worse

| Config (penalty at 0) | spread | length |
| :---- | :----: | :----: |
| no cap | **28.5 pts** | 1.84 rds |
| cap 4 attacks | 39.7 pts | 2.75 rds |
| cap 3 attacks | 49.8 pts | 3.66 rds |
| cap 2 attacks | 54.3 pts | 7.05 rds |

**General law worth keeping: any limit on how many times you may act is a DEX tax**, because only high-DEX builds ever reach the limit. A cap is that tax with a harder edge and no compensating simplicity. Nothing should be added back in this shape.

### Do not also narrow the die ladder

The two repairs are **substitutes, not complements.** Together (narrow ladder `1d6/1d6/1d8/1d8/1d10` plus no penalty) they overcorrect to **41.9 points with DEX dominant** - S1/D5 at 74%, S4/D2 at 32%. Penalty removal alone is the better of the two: 21.2 versus the narrow ladder's 28.1, and a cleanly decaying shape rather than the ladder's odd valley at S2/D4.

### The consequence: pacing is now the Wounds layer's job, and it is not set for it

Fights run **1.31 rounds** at `Max Wounds 3`, against the previous system's measured 2.23. Max Wounds is the valve that works:

| Medium Max Wounds | 3 | 4 | 5 |
| :---- | :----: | :----: | :----: |
| **length** | 1.31 rds | 1.55 rds | **1.81 rds** |
| **spread** | 21.2 pts | 23.6 pts | 28.1 pts |

**The Wound Threshold table is NOT a second valve, contrary to expectation, and the reason is worth recording.** At ordinary weapon damage against ordinary AR, essentially every landed hit is already exactly **1 Wound**:

| Weapon | vs AR 3 | vs AR 5 |
| :---- | :---- | :---- |
| Longsword `1d6 \+ 2` | **1 Wound 100% of the time, at every STR** | 1 Wound 67-100% |
| Broadsword `1d10` | 1 Wound 90%, 2 Wounds 10% | 1 Wound 60-100% |
| Greatsword `1d12` | 1 Wound 75%, 2 Wounds 25% | 1 Wound 58-92% |

**Nothing in the weapon list reaches the 3-Wound band at all.** The three-tier table produces tier one and almost nothing else, so widening or shifting the bands moves fight length by approximately zero. It becomes a real valve only if weapon damage rises or AR falls - which is itself a finding about `wounds_and_survival.md` independent of this chapter, and arguably means that table is currently doing much less work than its design intent claims.

**What the Thresholds *are* is a mild balance lever**, because they are keyed to STR - a third job STR does against DEX's two. Flattening them is worth ~4 points of spread; flattening and shifting up, ~5. The best pairing measured is `Max Wounds 5` with flat shifted Thresholds: **19.9 points at 1.81 rounds.** `Max Wounds 5` alone gives 28.1 at the same length and touches far less of the repo.

**Not adopted - both are upstream of this draft** and change every creature in the game. Recorded so the decision can be made on numbers.

### Tool

`SEQ_PENALTY` remains a module-level switch in `tools/tempo_sim.py`, defaulted to `0`, so this finding can be reproduced rather than taken on trust.

---

## 36. Max Wounds raised. And the reason length and balance keep fighting each other *(2026-08-21)*

### Adopted: Max Wounds Small 3 / Medium 4 / Large 5

**Written into `core/wounds_and_survival.md`** - the first change this rework has made to a live `core/` file. `\+1` across the board; **5 is the stated ceiling a player reaches without Feats**, on a Large race.

**Why it was needed.** The old baseline was set against a system where a character made at most one attack per turn. Under the Exchange a character attacks as many times as they will spend Tempo Dice on, so the same Wound pool empties far faster. Measured, with the escalating penalty gone: **1.31 rounds at Max Wounds 3, 1.55 at 4, 1.81 at 5.**

**Note this is a live-system change.** `core/` still describes the Oppose system, which this lengthens too. Acceptable - the direction is right for both - but it is the one place so far where the unmerged draft has reached into the merged rules.

### The Wound Threshold table: the tweak it needs is *flat*, and that is a design decision

Item 35 established the table is nearly inert - a Longsword deals exactly 1 Wound **100% of the time**, and nothing in the weapon list reaches the 3-Wound band. Making it bite means narrowing the bands drastically. Measured at Max Wounds 4, with `W` as the width of the 1-Wound band (`1..W`, `W+1..2W`, `2W+1+`):

| Threshold table | STR/DEX spread | length |
| :---- | :----: | :----: |
| current (inert) | 26.1 pts | 1.54 rds |
| `W \= 4 \+ STR` | 30.2 pts | 1.46 rds |
| `W \= 3 \+ STR` | 33.9 pts | 1.39 rds |
| `W \= 2 \+ STR` | **35.2 pts** | 1.33 rds |
| `W \= 7` flat | **24.9 pts** | 1.46 rds |
| `W \= 6` flat | 27.6 pts | 1.39 rds |
| `W \= 5` flat | 26.3 pts | 1.33 rds |

**Two findings, and the first is the important one.**

**Narrowing the bands while they stay keyed to STR makes STR dominance materially worse** - 26.1 to 35.2 points. Obvious in hindsight: a table that never fires cannot express a bias, and the moment it fires, its STR keying becomes a real third job for STR on top of the contest die and the damage bonus. **If the Threshold table is going to matter, it has to stop being keyed to STR, or it will undo the gain from item 35.**

**Narrowing the bands shortens fights rather than lengthening them** - more multi-Wound hits, faster deaths. So the Thresholds are a *lethality-shape* dial (does a greatsword hit differently from a longsword?) and Max Wounds is the *length* dial. They are not two versions of the same valve, which is what was assumed going in.

**Recommended, not adopted:** `W \= 7` flat - 1 Wound on 1-7, 2 Wounds on 8-14, 3 Wounds on 15+, identical at every STR. It is the only tested option that both restores weapon differentiation (Greatsword 58% / 42% one-vs-two Wounds, Longsword 83% / 17%) and *improves* balance over the inert table. **Held for a decision because it deletes a stated design intent** - `wounds_and_survival.md` currently argues that what STR buys you is softer hits - and that is the designer's to remove, not mine.

### The structural reason length and balance keep trading against each other

Every attempt to lengthen fights has cost STR/DEX balance, in every lever tried:

| Lever moved toward longer fights | length | spread |
| :---- | :----: | :----: |
| free Dodge `\-2` (adopted) | 1.54 rds | **23.7 pts** |
| free Dodge `\-1` | 2.02 rds | 33.8 pts |
| free Dodge `\+0` | 2.53 rds | 44.7 pts |
| free Dodge `\+1` | 3.53 rds | **55.6 pts** |

**The cause: the Tempo Die is in every roll, including the free Dodge.** STR therefore scales with how much *rolls matter*; DEX scales only with how many rolls you get. Anything that makes combat longer or grindier means more rolls per fight, and more rolls per fight is STR's axis. **Length and STR-favour are the same dial as long as defence rolls the Tempo Die.**

### The lever that breaks the tension - proposed, not adopted

**Take Dodge off the Tempo Die entirely:**

- free Dodge \= `1dD \+ DEX \- Armor Penalty`
- committed Dodge \= `1dD \+ DEX \- Armor Penalty \+ 2` (1 die, empty square, Opening)
- Parry and Block unchanged, still `1d(Tempo Die) \+ Skill (\+ Guard)`

| Dodge die | spread | length |
| :---- | :----: | :----: |
| `1d6`, commit `\+2` | 23.5 pts | 2.06 rds |
| `1d8`, commit `\+2` | 24.2 pts | **2.70 rds** |
| `1d10`, commit `\+2` | 25.6 pts | 3.36 rds |

**This does not reduce the spread - it removes the trade-off.** Getting to 2 rounds previously cost 34 points; it now costs 23.5, which is no worse than the 1.5-round configuration. Length becomes free to tune.

**The fiction is also better than the current version.** Your involuntary flinch is a function of quickness, not of how strong you are - a fixed human die plus your DEX. Strength lives in the weapon, which is where Parry and Block still roll it.

**Honest caveat: it flips the direction rather than flattening it.** S5/D1 falls to 37% and S2/D4 rises to 61%, because a fixed `1d8` is an enormous upgrade for a build that was rolling `1d4` and a downgrade for one rolling `1d12`. The spread is comparable, mirrored.

**A correction worth recording, because it nearly became a finding.** A first pass at this measured **12.2 points of spread at 2.59 rounds**, which would have been the best result in this document by a wide margin. It was wrong: the defender's spend decision compared *bonuses* while the two options rolled *different dice*, so the model let fighters take defences they would never actually choose. Re-run against the real rule it is 24.2. **No figure from a mixed-die comparison is trustworthy unless the policy compares expected totals.**

---

## 37. Dodge comes off the Tempo Die. The coupling is broken *(2026-08-21)*

**Adopted:**

| Defence | Costs | Roll |
| :---- | :----: | :---- |
| **Dodge** | nothing | `1d8 \+ 2 \- Armor Penalty` |
| **Dodge, committed** | 1 die | `1d8 \+ 2 \+ DEX \- Armor Penalty` |
| **Parry** | 1 die | `1d(Tempo Die) \+ Weapon Skill \+ Distance` |
| **Block** | 1 die | `1d(Tempo Die) \+ Weapon Skill \+ Guard` |

**A Dodge always rolls a flat `1d8`.** Parry and Block still roll the Tempo Die.

### The diagnosis this closes

Items 33-36 each hit the same wall from a different direction: *every lever that lengthened a fight cost STR/DEX balance.* The cause, finally stated properly: **the Tempo Die sat in every roll, so STR improved everything you did and DEX improved only how often you did it.** More rolls per fight is STR's axis by construction, so a static Passive Evasion, an escalating attack penalty, a cap on attacks, and a stronger free defence all failed identically.

**Taking Dodge off the die breaks the coupling.** STR now lives in the weapon - attack, Parry, Block - and the body's own flinch is the same die for everyone.

| | spread | length | stalls | dumping |
| :---- | :----: | :----: | :----: | :----: |
| Dodge on the Tempo Die | 23.9 pts | 1.56 rds | 0 | 51% |
| **Dodge off it (adopted)** | **13.8 pts** | **2.11 rds** | 0 | 51% |

Build means across the field: **52 / 49 / 54 / 53 / 41** (STR 5/DEX 1 through STR 1/DEX 5). Flat except the STR 1 build, whose problem is the `1d4` attack die and nothing else.

**Length stopped costing balance.** That is the actual result - not the ten points, but that `1d8 \+ 3` and `1d8 \+ 4` buy 2.7 and 3.8 rounds at a *known* price now, instead of the price being "STR wins."

### Why DEX is on the committed Dodge and not the free one

Measured, and it is not a small effect: with DEX on both, spread 20.1 with a stall; with DEX on neither, **39.6** and heavy armour at 42%; with DEX only on the committed Dodge, **13.8**. The fiction agrees - the involuntary flinch is not a talent, a quick man and a slow one both turn their head. What quickness buys is the *deliberate* evasion, so DEX appears the moment you spend a die and not before.

### Two false results found in validation, both worth recording

**The 12.2-point figure was real but the config behind it was not.** An earlier pass gave 17.9 points at 2.13 rounds with DEX in the free Dodge and pool `DEX \+ 2`. Validation broke it: the STR 1 / DEX 5 **mirror match stalled**, because `1d4 \+ 3` cannot beat a free Dodge of `1d8 \+ 4`. **The field metric was averaging stalls in as 0.5 draws and hiding them.** The metric now counts stalls separately. Any figure in items 33-36 that came off the field average should be read with that in mind.

**Pool `DEX \+ 2` was tried and dropped.** It looked like it helped low-DEX builds survive unlimited attacks, and it did - but it also shortened fights and only looked good because of the hidden stall. Pool stays `DEX \+ 1`.

### The cost: armour got worse, and it was already bad

**Heavy armour (AR 6 / AP 4) beats light (AR 2 / AP 0) only 15% of the time.** It was 35% before this change.

**Cause: the free Dodge is now the most-rolled thing in the game, and Armor Penalty lands on it every time.** Under Passive Evasion, Armor Penalty degraded one static score. Now it degrades the roll that answers most attacks in a fight.

**Second cause, upstream: AR barely prevents Wounds.** The Threshold bands are so wide that cutting a hit from 8 damage to 2 still yields exactly 1 Wound - **AR reduces the damage and the Threshold table throws the reduction away.** Narrowing the bands helps (flat `W \= 5` takes heavy armour 14% to 21%) but nowhere near enough alone.

**Measured and rejected: exempting the free Dodge from Armor Penalty.** Fixes armour (heavy to 63%) and costs everything else - spread back to 30 points, because a better free roll for everyone means longer fights and longer fights favour STR. Half Armor Penalty is the same trade at half size: armour 34-41%, spread 30-32.

**This is now the draft's open question 1**, and it wants a pass on `armor.md` and `wounds_and_survival.md` together rather than a patch here. It is also the oldest unresolved item in the project - the pre-rework log raised *"armour has no defensive term that persists"* and never settled it. It is now measured.

### Tool

`DODGE_DIE`, `DODGE_FLAT` and `DODGE_COMMIT_DEX` are module-level switches in `tools/tempo_sim.py`; setting `DODGE_DIE = None` restores the Tempo-Die Dodge for comparison. `Combatant.best_paid()` compares **expected totals**, not bonuses, because the options roll different dice - the bug that produced item 36's bogus figure.

---

## 38. Adding an Attribute to attack rolls: tested, rejected, and a new instrument *(2026-08-21)*

**Question: what happens if the attack roll adds STR or DEX on top of the Tempo Die and Weapon Skill?** Answer: both are worse than adding nothing, for two independent reasons, and the investigation turned up a measurement instrument the tool should have had from the start.

| Attack roll | spread | length | heavy armour | build means (S5/D1 to S1/D5) |
| :---- | :----: | :----: | :----: | :---- |
| **`\+ Skill` only (adopted)** | **14.7 pts** | **2.10 rds** | 14% | 53 / 49 / 56 / 53 / 41 |
| `\+ Skill \+ STR` | 37.9 pts | 1.17 rds | 31% | 65 / 57 / 54 / 47 / 27 |
| `\+ Skill \+ DEX` | **50.5 pts** | 1.17 rds | 6% | 27 / 33 / 47 / 65 / **78** |
| `\+ Skill \+ half STR` | 34.6 pts | 1.56 rds | 23% | 60 / 59 / 53 / 55 / 25 |
| `\+ Skill \+ half DEX` | 30.1 pts | 1.56 rds | 9% | 34 / 42 / 48 / 64 / 62 |

### Why STR fails: it is already on the attack roll

STR *is* the die. Adding it again as a flat term is the same double-dip the escalating `\-2` was, pointing the other way, and it lands at almost the same magnitude (37.9 against that rule's 55.0).

### Why DEX fails, which is less obvious

The algebra says it should work. Die EV is `STR \+ 1.5`, so with a fixed 6-point budget `STR \+ DEX \= 6`, an attack roll of `die \+ Skill \+ DEX` has **identical expected value at every build** - a perfectly flat offensive axis.

**That is exactly why it fails.** Flattening attack EV does not equalise the builds; it **removes STR's only compensation** while DEX keeps the larger pool *and* the DEX term on the committed Dodge. DEX ends up counted three times and STR once. Result: the DEX 5 build wins 78% against the field.

**Worth keeping as a general caution: equalising one axis is not the same as balancing, and can be the opposite.** The axes only balance in combination.

### Why both halve fight length, regardless of balance

A flat `\+1` to `\+5` on attacks with no matching term on defence collapses fights from **2.10 rounds to 1.17**. **Attack and defence bonuses have to move together or fight length moves** - and item 37 established that length is the thing this system is most sensitive to.

### The seductive near-miss, and the instrument that killed it

A follow-up looked outstanding: **move DEX from the committed Dodge to the attack roll**, and raise the free Dodge to `1d8 \+ 6 \- Armor Penalty` to compensate.

| | spread | length | stalls |
| :---- | :----: | :----: | :----: |
| `\+DEX` attack, DEX off commit-Dodge, Dodge `\+6` | **4.8 pts** | 2.56 rds | 0 |

Build means **47 / 49 / 51 / 52 / 50** - very nearly a flat line, the best balance figure this project has produced by a factor of three.

**It is degenerate, and no existing metric showed it.** With the free Dodge that strong, no paid defence is ever worth a die:

| config | paid-defence rate, S5/D1 | S3/D3 | S1/D5 |
| :---- | :----: | :----: | :----: |
| **adopted** | 47% | 38% | 26% |
| `\+DEX`, Dodge `\+2` | 46% | 45% | **0%** |
| `\+DEX`, Dodge `\+4` | 47% | **0%** | **0%** |
| `\+DEX`, Dodge `\+6` (the 4.8pt one) | **0%** | **0%** | **0%** |

**Zero. Nobody ever spends a die on defence in that configuration.** The balance is achieved by deleting the defensive half of the pool - which is the single idea the entire chapter is built on. The pool becomes a pure attack counter and "every die you swing is a die you did not keep" stops being true.

### New standard metric: paid-defence rate

`STATS`, `paid_defence_rate()` and `reset_stats()` are now in `tools/tempo_sim.py`, counting the fraction of attacks answered by a defence somebody **spent a die on** rather than by the free Dodge. **Check it before believing any spread figure.** Healthy is roughly 25-50%. The adopted configuration reads 47 / 38 / 26% across the STR-to-DEX field.

**Two earlier "good" results in this log look like the same failure mode** and should be re-read with suspicion: item 36's `1d8 \+ 2, no DEX, pool DEX+3` at 7.0 points, and the `W \= 9` flat-threshold configuration at 10.0. Neither was checked for paid-defence rate because the metric did not exist.

**A first version of this probe was also wrong**, counting Strip Tempo's pool reduction as a paid defence and reporting a healthy 36-46% for a configuration that is actually at 0%. The committed version instruments the `defended` branch directly.

---

## 38. Adding an Attribute to combat rolls - measured and rejected in every form *(2026-08-21)*

**Question: should the attack roll be `1d(Tempo Die) \+ Weapon Skill \+ Attribute` rather than Skill alone?** The motivation is sound - DEX has no *quality* term anywhere, only a count term, while STR has die size and damage. **Rejected on measurement. Every variant tried is worse than Skill alone, and one is worse in a direction nobody predicted.**

All figures against the adopted baseline: **13.7 points of spread, 2.10 rounds, no stalls**, field means 51 / 50 / 55 / 53 / 41.

| Variant | spread | length | field means (S5/D1 to S1/D5) |
| :---- | :----: | :----: | :---- |
| **Skill only (adopted)** | **13.7** | **2.10 rds** | 51 / 50 / 55 / 53 / 41 |
| `\+ STR`, attack and Parry | 43.2 | 1.17 rds | **67** / 64 / 55 / 41 / **24** |
| `\+ STR`, attack only | 38.1 | 1.12 rds | 65 / 57 / 53 / 48 / 27 |
| `\+ DEX`, attack and Parry | 51.7 | 1.17 rds | **24** / 34 / 51 / 66 / **76** |
| `\+ DEX`, attack only | 50.9 | 1.12 rds | 27 / 33 / 48 / 65 / 78 |
| `\+ governing`, attack and Parry | 30.1 | 1.19 rds | 53 / 46 / **35** / 53 / 65 |
| `\+ governing`, attack and all defences | 58.8 | 2.00 rds | 80 / 57 / **22** / 36 / 55 |
| `\+ half governing`, attack and Parry | 18.8 | 1.56 rds | 49 / 52 / **37** / 56 / 54 |

### Three separate reasons, any one of which is sufficient

**1. It is inflationary, because the free Dodge has no Attribute in it.** The free Dodge is `1d8 \+ 2 \- Armor Penalty`, a fixed number, and it answers most attacks in a fight. Anything added to an attack roll therefore lands against a static defence rather than a scaling one, and fight length collapses from 2.10 rounds to **1.12-1.19** in every variant that does not also scale the defence. This is a structural consequence of item 37 and would apply to any flat bonus, not just an Attribute.

**2. Naming either Attribute makes it dominant.** `\+STR` puts the field at 67-vs-24; `\+DEX` at 24-vs-76. Both are worse than the 55-point skew that items 35 and 37 were spent removing. **The Tempo Die already is STR on the roll** - adding STR again counts it a third time, alongside damage - and DEX is already the pool and the committed Dodge. There is no Attribute left that is not already priced in, which is precisely why Skill-only works.

**3. The realistic version punishes balanced builds, which is the surprise.** "Add the Attribute that governs your weapon's Skill" is what a table would actually produce, because players pick weapons that suit them - so in practice everybody adds their **best** Attribute. A STR 3 / DEX 3 fighter adds `\+3`; a STR 5 / DEX 1 and a STR 1 / DEX 5 both add `\+5`. **The middle of the field drops to 35%** (22% when defences scale too) while both specialists rise. It converts the Attribute spread into a flat roll bonus and pays it out for min-maxing - inverting the current shape, where the balanced build is quietly the best one.

**Half value does not rescue it.** `\+ half governing` still lands at 18.8 points with the balanced build at 37%, worse than doing nothing.

### Scope note: this is about *combat* rolls only

`tools/tempo_sim.py` models combat and nothing else, so none of this bears on **non-combat Skill Checks**, which are `1d12 \+ Skill Ranks` and were made Skill-only in the 2026-08-08 Attribute/Skill split. Adding an Attribute there is a different question with none of the three problems above: there is no contested roll to inflate, no free Dodge to outrun, and no weapon choice to convert the decision into "add your best stat." It would simply double the value of an Attribute point and widen the gap between a trained character and an untrained one - a legitimate design choice, and one this tool cannot speak to either way.

**What DEX not having a quality term actually costs is visible and small:** the STR 1 / DEX 5 build sits at 41% against a field otherwise spanning 49-55. That is the `1d4` attack die (see draft open question 4), not the missing Attribute term, and raising the ladder floor from `1d4` to `1d6` addresses it without touching the roll.

---

## 39. Correction: damage takes the weapon's governing Attribute, not STR *(2026-08-21)*

**`tools/tempo_sim.py` hardcoded `str_` into `Build.damage()`.** That is wrong. `combat.md` gives damage as **`Weapon Damage \+ Attribute \- AR`**, and the Attribute is the one governing that weapon's Skill - and `weapons.md`'s **Fencing Blades** line (Rapier `1d8`, Estoc `1d10`, Stiletto `1d4`) is **DEX-governed**. A DEX 5 fencer adds `\+5` to damage, not `\+1`.

Every field figure in items 33-38 was therefore measured with all five builds swinging a STR-governed Longsword, including the DEX builds who in practice would not be carrying one. **The error ran against the quick builds specifically**, which is the exact half of the field those items were worrying about.

### The effect: it improves the picture and changes no conclusion

Field means, STR 5 / DEX 1 through STR 1 / DEX 5, with each build carrying a weapon governed by its better Attribute:

| Weapon choice | spread | length | field means |
| :---- | :----: | :----: | :---- |
| everyone on a Longsword (the wrong model) | 14.6 pts | 2.12 rds | 52 / 49 / 55 / 53 / **41** |
| **STR builds Longsword, DEX builds Rapier** | **9.9 pts** | 2.12 rds | 52 / 49 / 53 / 52 / **43** |
| STR builds Longsword, DEX builds Estoc | 9.8 pts | 2.12 rds | 51 / 48 / 52 / 54 / **44** |
| everyone on a Rapier | 13.6 pts | 2.08 rds | 43 / 46 / 57 / 57 / 48 |

**About 10 points of spread is the best balance figure this project has produced**, and it came from fixing a measurement rather than changing a rule.

### The claim it corrects

Item 38 opened with *"DEX has no quality term anywhere, only a count term."* **That is false.** DEX buys the Tempo Pool (count), the committed Dodge, **and damage on every DEX-governed weapon** - which is a quality term landing on the half of the exchange that actually kills people. The motivation for adding an Attribute to the roll was partly built on a gap that does not exist.

### Item 38's conclusion survives intact

Re-run with damage attributed correctly:

| Variant | spread | length | field means |
| :---- | :----: | :----: | :---- |
| **Skill only (adopted)** | **12.5** | **2.10 rds** | 52 / 50 / 54 / 53 / 42 |
| `\+ STR` on attack and Parry | 42.9 | 1.16 rds | 68 / 63 / 53 / 40 / 25 |
| `\+ DEX` on attack and Parry | 52.3 | 1.16 rds | 23 / 34 / 50 / 66 / 75 |
| `\+ governing Attribute` | 29.9 | 1.16 rds | 53 / 46 / **35** / 52 / 65 |
| `\+ half governing` | 18.1 | 1.59 rds | 50 / 54 / **38** / 56 / 55 |

All three of item 38's reasons stand unchanged, including the surprising one: **the governing-Attribute version still punishes the balanced build**, which lands at 35% either way. The Tempo Die is still STR on the roll, and adding it again would now be counting STR a *fourth* time - die, damage, Wound Thresholds, and roll.

**Armour is also unchanged** by the correction: heavy 14.7%, mail 20.0%. Draft open question 1 stands exactly as written.

### Two process notes

**A design fact that lives in another file will not appear in a simulation unless somebody puts it there.** The tool was built from `exchange_draft.md`, which states damage correctly as "Weapon Damage \+ Attribute" - the error was in the model, not the rules text, and no amount of reading the draft would have caught it. Cross-check a tool against the files it *depends* on, not only the one it implements.

**Precision claimed in items 33-39 is higher than it deserves.** Spread figures come from 1,200-1,500 duels per cell and move roughly `\±2` points between seeds - the same configuration measured 9.9 and 12.5 on two different seeds in this item. Treat differences under about 5 points as noise.

---

## 40. The turtle. Two blind spots in the tool, and the attack cap measured and rejected *(2026-08-21)*

**"Attack once, bank the rest" is the dominant strategy in the draft as written, and the tool could not see it.** Every build's best hold, played against a balanced opponent at hold 1:

| Build | best hold | win rate |
| :---- | :----: | :----: |
| STR 5 / DEX 1 | 0 | 53% |
| STR 4 / DEX 2 | 0 | 54% |
| STR 3 / DEX 3 | 0 | 53% |
| STR 2 / DEX 4 | 3 | **71%** |
| STR 1 / DEX 5 | 3 | **86%** |

The STR 1 / DEX 5 mirror at its own best hold runs **38.4 rounds at 91% stalls**. That is not a long fight, it is a system that has stopped.

### Why six items of measurement missed it

**The STR vs DEX table pins every build at hold 1.** That was chosen early as "a sensible middling policy" and never revisited, and a policy table with one policy in it cannot find a dominant policy. The figure the sign-off block reports as *"dumping the pool vs holding: ~51%, neutral, as intended"* is true, correctly measured, and answers the wrong question - it compares dump against hold 1, which are the two ends nobody plays. The whole of the problem lives at hold 3 and above.

**Nothing had ever modelled being outnumbered.** The Tooling block says so explicitly and draws the right inference - *"the value of a held die scales with how many people are attacking you, so every policy figure here understates the case for holding dice"* - and then no one built the harness. The finding was sitting inside a caveat that had already been written down.

Both are now standing sections of `tools/tempo_sim.py`: a **best-hold sweep** and an **outnumbered** harness (`gang_fight`).

### The cause is one term: `\+DEX` on the committed Dodge

Holding the rest of the chapter fixed and changing only what a committed Dodge adds:

| Committed Dodge adds | best-hold peak | STR 1 / DEX 5 mirror |
| :---- | :----: | :---- |
| **`\+DEX`** (as written) | **86% at hold 3** | 38.4 rds, **91% stalls** |
| `\+Weapon Skill` | 44% at hold 3 | 15.8 rds, 2% stalls |
| `\+2` flat | 30% at hold 2 | 3.8 rds, 0% stalls |

**It is a double-dip.** DEX buys the size of the pool *and* a `\+5` swing on the roll each of those dice can buy, so a defensive die is worth most to exactly the build holding the most of them. The draft's design note claims *"Neither Attribute is added to the roll, and that is load-bearing rather than an oversight"* - that sentence is false as written, and the committed Dodge is where it breaks.

### Ruled out, each measured rather than argued

**Not the pool curve.** `DEX`, `2 \+ DEX/2`, `3 \+ DEX/2` and `ceil((DEX \+ 3)/2)` were all tested; every one still stalls at ~90%. Shrinking the pool shrinks the pool and changes nothing about what a die is worth.

**Not the Wound Threshold table, and not the die ladder.** `\+DEX` with flat `W \= 7` *and* a `1d6` ladder floor still reads **96% at hold 3**.

**Not information.** Making the defender commit before seeing the attack total - the obvious suspect, since the defender otherwise buys exactly enough - moves nothing at all.

**Not Measured's refund**, though that turned up a separate real fault: a STR 5 build with a pool of **2** averages **3.05 attacks per turn**, because Measured refunds on a win and a `1d12` wins often enough to make attacks effectively free. Redirecting the refund to defence-only fixes that (3.05 to 1.74) and costs 8 points of spread, because the refund is quietly load-bearing for STR. Left alone; recorded as a known distortion.

### Being outnumbered is decisive, not merely hard

One fighter against N identical STR 3 / DEX 3 attackers, each build playing its best hold:

| | STR 5/DEX 1 | STR 4/DEX 2 | STR 3/DEX 3 | STR 2/DEX 4 | STR 1/DEX 5 |
| :---- | :----: | :----: | :----: | :----: | :----: |
| **vs 2** | 2.6% | 1.3% | 1.4% | 2.6% | 8.9% |
| **vs 3** | 0.0% | 0.0% | 0.0% | 0.0% | 0.1% |

The draft says *"Being outnumbered is not a special rule - it is four attacks against three dice, and the fourth one gets the free Dodge instead of the good one."* Measured, 2-on-1 is a 97-99% loss for every build on the field. That may be the intended game - Ressam is meant to be lethal - but **the prose reads as a manageable pressure and the mechanic is close to absolute**, and one of the two should move.

Note also that the turtle is the *only* thing giving any build outnumbered survivability at all: capping it takes STR 1 / DEX 5 from 8.9% to 0.2%. Anything that prices holding dice must be judged against this table, not against a duel.

### Capping attacks per turn, with Tempo Dice stacked onto rolls instead - measured and rejected

The proposal answers the "any limit on attack count is a DEX tax" objection of item 35 directly and well: a cap only taxes DEX if the surplus dice are *wasted*, and if they can be poured into the roll instead, a quick fighter still spends everything they have. It was implemented in full and swept across attack caps of 1, 2, 3 and none, both stacking rules, both information models, both attacker heuristics, with and without a stack ceiling - **24 configurations. Every one is worse than the draft on both spread and length, and none of them touches the turtle.**

| | spread | length | STR 1/DEX 5 best response |
| :---- | :----: | :----: | :----: |
| **draft as written** | **10.5** | **2.17 rds** | 86% at hold 3 |
| cap 3, stacked | 20.9 | 4.21 rds | 92% at hold 3 |
| cap 2, stacked | 26.0 | 4.66 rds | 90% at hold 4 |
| cap 1, stacked | 30.9 | 4.26 rds | 77% at hold 3 |

**Two mechanisms, and both are general enough to be worth keeping.**

**A cap on attacks is a subsidy to defence.** It reduces the number of rolls a defender has to answer without reducing the pool they answer with, so every remaining defence is better funded. The relationship is monotone across the sweep - tighter cap, worse spread, longer fight - and it works against the turtle problem rather than with it. Item 35 found that a cap is a DEX tax; the fuller statement is that **a cap on attacks moves value from offence to defence, and defence is already where the dominant strategy lives.**

**Stacking makes DEX and STR compete on one axis, and the axis has no neutral setting.** DEX is meant to buy how many times you act and STR how well each act goes; stacking lets DEX buy how well an act goes too. Which Attribute it hands the game to depends only on the arithmetic of the stack:

| Stacking rule | field means, STR 5/DEX 1 to STR 1/DEX 5 |
| :---- | :---- |
| **sum** the k dice | 31 / 49 / 50 / 61 / 60 - **DEX wins**; many small dice sum high |
| **roll k, keep the highest** | 76 / 68 / 45 / 27 / 35 - **STR wins**; one big die beats a handful of small ones |

There is no rule between those two that is flat, because the flatness is not a tuning problem - the two Attributes are being asked to price the same quantity. `1d12` averages 6.5 and five stacked `1d4` average 3.7 under keep-highest and 12.5 under sum; nothing sits in the middle.

### Adopted: the ladder floor rises to `1d6`

**Note the interaction, measured after adoption:** every turtle figure above was taken on the old `1d4` floor. Re-run on the adopted ladder, the STR 1 / DEX 5 best response rises from **86% to 95%** and its best hold from 3 to 4 - **raising the floor makes the turtle worse**, because the die that improved is the quick build's. With `ONE_COMMIT_PER_ROUND` the same sweep peaks at **56%**. The two changes are complements, not alternatives.

**`1d6 / 1d6 / 1d8 / 1d10 / 1d12`.** The `1d4` rung is the single worst cell on the board - the STR 1 build sits at 33-43% against a field otherwise spanning 49-54 - and closing draft open question 5 is also what pays for any fix to the committed Dodge. **Known cost: STR 2 becomes a dead rung.** It rolls the same die as STR 1, so at equal Attribute points STR 1 / DEX 5 outperforms STR 2 / DEX 4 by about 12 points. Shifting the flat spot elsewhere (`1d6/1d8/1d10/1d12/1d12`, `1d6/1d8/1d8/1d10/1d12`) only moves the dead rung to the top or the middle and measures no better. Accepted as the cheapest of three warts, and second-order against everything else open.

### One law this item paid for

**A policy table with a fixed policy in it cannot find a dominant policy, and a duel cannot price a rule about defending.** Both of this item's blind spots were failures to vary the thing being measured, not failures of the model. Before trusting any figure, ask what was held constant to produce it.

### Tool

`tools/tempo_sim.py` gains `ONE_COMMIT_PER_ROUND`, a **BEST-HOLD SWEEP** section, an **OUTNUMBERED** section, and `gang_fight()` / `gang_winrate()`.

---

## 41. The party harness. The turtle is a duel artifact, and targeting outweighs every rule in the chapter *(2026-08-21)*

Item 40 found "attack once, bank the rest" beating a balanced fighter **95%** of the time and mirroring into a 38-round stalemate, and left the fix open because the only candidate also gutted outnumbered survivability. Both of those figures come from a duel. **Ressam is a party game, so the duel is an edge case, and it turns out to be the only place the problem exists.**

`tools/tempo_sim.py` gains `party_fight()`, `party_stats()`, `standard_party()` and `peer()`: four PCs on static Initiative against N identical peers, with targeting as a parameter.

### At party scale, holding dice is simply bad

Four PCs against 3 peers - a fight the party wins about three times in five - with everyone on the same policy:

| Policy | party win | length | Strong | Shield | Quick | Backline |
| :---- | :----: | :----: | :----: | :----: | :----: | :----: |
| **everyone holds 0** | **64.9%** | 2.1 rds | 31% | 48% | 59% | 5% |
| everyone holds 1 | 61.9% | 2.6 rds | 24% | 47% | 57% | 5% |
| everyone holds 2 | 54.3% | 3.5 rds | 17% | 39% | 51% | 3% |
| everyone holds 3 | **27.9%** | 4.9 rds | 4% | 18% | 27% | 0% |

Monotone, and steeply so. The same shape holds at 2 opponents and at 4.

### And it does not even pay the individual who does it

The interesting objection is that a party figure cannot refute an individually rational play. So: three PCs hold 1, one turtles.

| | party win | Strong | Shield | Quick | Backline |
| :---- | :----: | :----: | :----: | :----: | :----: |
| nobody turtles | 59.4% | 25% | 44% | 54% | 5% |
| Strong turtles | 61.2% | 24% | 44% | 57% | 3% |
| Shield turtles | 57.3% | **12%** | 48% | 53% | 2% |
| **Quick turtles** | **38.5%** | 11% | 24% | **37%** | 2% |
| **Backline turtles** | **67.1%** | 29% | 52% | 62% | **8%** |

**The Quick build - the one that wins 95% of duels by turtling - drops its own survival from 54% to 37% by doing it here.** Shield gains 4 points for itself and takes 13 off Strong, which is a real externality but a small one. Nobody has an incentive that survives contact with three other people.

**The exception is legible and correct: the Backline should turtle.** It is the only build whose attacks are worth less than its dice, so spending them on defence is right, and doing it lifts the whole party from 59% to 67%. A caster hanging back and buying guard rather than swinging is exactly what the chapter's Casters section describes, and the mechanic produces it without a rule saying so.

### Why the duel lied

In a duel the only person your offence protects is you, so a die spent attacking and a die spent defending buy the same good and defence buys it more efficiently. **At party scale offence buys something defence cannot: the enemy who is dead is not attacking your friends.** That term is missing from every 1v1 figure in this log, and it is worth more than everything the turtle was gaining.

**So `\+DEX` on the committed Dodge stays.** The dominant strategy exists only in single combat between two high-DEX fighters, where it produces a long, drawish fight - which is a defensible thing for two duelling fencers to produce, and not worth a per-round tick on every character sheet to prevent. `ONE_COMMIT_PER_ROUND` is kept in the tool as a switch, not adopted: at party scale it moves the needle from **16.6% to 16.5%** at 4 peers and 63.2% to 65.3% at 3. Its entire case rested on the duel.

### Targeting is worth more than any rule in the chapter

Same encounter, same builds, varying only who attacks whom:

| | party win | Strong | Shield | Quick | Backline |
| :---- | :----: | :----: | :----: | :----: | :----: |
| monsters focus fire, PCs focus fire | 64.6% | 25% | 48% | 60% | 5% |
| monsters focus, PCs spread | 40.3% | 13% | 26% | 37% | 2% |
| monsters go for the softest, PCs focus | 65.2% | 51% | 65% | 27% | 4% |
| **monsters spread, PCs focus** | **88.8%** | 80% | 78% | 80% | 61% |

**A 24-point swing from monster targeting alone, and 24 more from the party's.** No mechanical change measured in this entire log - not the escalating penalty, not Passive Evasion, not the Tempo-Die Dodge - moves a number that far. Two consequences worth carrying:

**Every balance figure in this log is conditional on a targeting assumption nobody wrote down.** The duel harness has no targeting, so it never had to state one.

**This belongs in GM guidance, not in the rules.** Whether the monsters concentrate is the largest dial the GM has, larger than how many of them there are, and the chapter currently says nothing about it.

### Numbers decide symmetric fights - and that is all this measures

Four PCs at hold 1, against N opponents: **2 of them 97%, 3 of them 63%, 4 of them 17%, 5 of them 1%.**

**The opponent used throughout this item is a PEER, not a mook.** STR 3 / DEX 3 / Skill 3 with a full Tempo Pool is a build made on the player's own axis, and `bestiary_overview.md` states the principle directly: Attributes and Skills share one cap across every character in the game, PC or NPC, so a creature built on that axis is about as dangerous as a PC regardless of the Level it is nominally worth. **Four PCs against four of these is a four-on-four, and the steepness above is what numbers do in any symmetric contest.** An earlier draft of this item called it an encounter curve and concluded "the difficulty range is one and a half monsters wide." That was wrong, and the error was in the label on the build, not in the arithmetic.

**No weak-creature tier was substituted, deliberately.** `core/bestiary/` predates both the 8-to-6 Attribute rework and the Tempo Pool, so there is nothing current to calibrate one against, and inventing one would produce a number with a real-looking decimal point and no grounding. Encounter-design questions stay unanswerable until the bestiary is rebuilt.

**What survives the correction** is the outnumbering finding at its own scale: a lone fighter loses to two attackers 97-99% of the time and does not survive three. That is measured against peers too, which is exactly the right comparison for it.

### What this harness does not model, and where that bites

No healing, no Feats, no spells, no terrain, no cover, no morale, and **nobody ever flees**. Most importantly, **0 Wounds is Dying in Ressam, not dead** ([[Wounds and Survival|wounds_and_survival]]) - so every "survival" percentage above is really "was not dropped," and the real death toll is lower by whatever Stabilization recovers. The shape of these results is trustworthy; the absolute lethality is an overstatement.

### One law this item paid for

**A result measured in a duel does not transfer to a party, because a duel cannot price the enemy you killed.** Offence has a defensive term at party scale and no defensive term at all in single combat, so any rule that trades offence against defence will measure differently in the two, and the party is the one the game is played in.

### Tool

`party_fight()`, `party_stats()`, `standard_party()`, `mook()`, `take_turn_multi()`, `pick_target()`, `initiative_order()`, and a `mind` field on `Build` for static Initiative. `ONE_COMMIT_PER_ROUND` retained as an unadopted switch.

---

## 42. Armour. Two modelling errors, one real cause, and a fix that only works if you measure both scales *(2026-08-21)*

### Two things the tool had wrong, both found by reading `armor.md` rather than the draft

**AR was a constant. It is not.** `armor.md`: *"Every successful hit against you reduces your armor's durability by 1"* and *"your current AR equals your current durability."* Armour is a decaying buffer, not a flat subtraction, and no figure in items 33-41 modelled that.

**The armour being tested does not exist.** Every armour figure in this log was taken on "heavy = AR 6 / Penalty 4" and "light = AR 2 / Penalty 0", which are invented. The real ladder is `\-1` at AR 2-3, `\-2` at AR 4-5, `\-3` at AR 6 for Flexible, and **Penalty equal to full AR** for Rigid: Breastplate `\-6`, Half-Plate `\-7`, Full Plate `\-8`.

This is item 39's lesson arriving a second time, from the same direction: **the tool was built from the draft, and the fault was in a file the draft depends on.**

### The real result is worse than "armour is bad"

Same build, same Skill, only the armour differing. 1v1 is the mean against the whole ladder; party is four PCs all in that armour against three peers.

| Armour | AR | Penalty | 1v1 | party |
| :---- | :----: | :----: | :----: | :----: |
| **none** | 0 | 0 | **74.6%** | **81.0%** |
| Buff Coat | 3 | \-1 | 67.0% | 74.8% |
| Mail Shirt | 4 | \-2 | 53.6% | 61.4% |
| Brigandine | 6 | \-3 | 45.2% | 45.8% |
| Breastplate | 6 | \-6 | 31.4% | 24.0% |
| **Full Plate** | 8 | \-8 | **30.2%** | **21.0%** |

**Monotone, at both scales. Wearing nothing is the best armour in the game, and every step up the ladder is a downgrade you pay money for.** The spread is 44 points in a duel and **60 points at party scale**.

### The cause is an accounting mismatch, not a number that needs nudging

**Armor Penalty is charged per defence roll. AR is charged per hit.** You are attacked far more often than you are hit, every attack is answered by a roll, and most of those rolls are the free Dodge - so the cost is paid several times for each time the benefit is collected. **AR then meets the Wound Threshold table and most of what it prevented is discarded**, because a hit reduced from 8 to 2 is still exactly 1 Wound.

Rigid armour is where this becomes absurd rather than merely bad. Full Plate's free Dodge is `1d8 \+ 2 \- 8`, which is **\-5 to \+2**. It cannot beat an attack roll. That is not a balance problem, it is a broken number.

### Durability was a red herring, and then it was not

Turning durability off changes almost nothing as the rules stand - Full Plate 30.2% to 30.0%, unarmoured 74.6% to 74.6% - because AR barely mattered either way. **Under the fixed numbers below it becomes load-bearing:** with the Wound bands narrowed so AR means something, removing durability takes Full Plate from 68.7% to **84.8%** at party scale and the ladder spread from 16.2 to 32.3.

**Durability is the brake that stops AR becoming an auto-take once AR is worth having.** It looked inert only because it was braking something that was not moving.

### The fix: three changes, and they only work together

| | 1v1 spread | party spread |
| :---- | :----: | :----: |
| as written | 44.4 | 60.0 |
| Wound bands flat `W \= 5` alone | 30.9 | 33.0 |
| softened Penalty alone | 36.5 | 40.6 |
| softened Penalty \+ `W \= 5` | 24.3 | 16.1 |
| **softened Penalty \+ `W \= 5` \+ half Penalty on the free Dodge** | **12.1** | **17.0** |

1. **Soften the Penalty formula: Rigid `\= ceil(AR/2)`, Flexible `\= ceil(AR/3)`.** Full Plate `\-8` becomes `\-4`, Breastplate `\-6` becomes `\-3`, Brigandine `\-3` becomes `\-2`. The current formula was written when Penalty degraded one static Evasion score; it now lands on a roll made several times a round.
2. **Wound bands flat at `W \= 5`** - draft open question 5, which has been recommended and held since item 36. AR cannot matter until the bands are narrow enough to notice it.
3. **The free Dodge takes half Armor Penalty, rounded down.** The involuntary flinch is not the athletic movement armour actually restricts; the deliberate evasion you spend a die on is.

Build balance is close to unaffected: the STR/DEX spread moves 14.9 to 16.7, which is inside the noise band this project treats as nothing.

### The case for measuring both scales, in one row

**Exempting the free Dodge from Armor Penalty entirely looks like the clean fix in a duel and is catastrophic at party scale.**

| | none | Buff | Mail | Brig | Breastplate | Full Plate |
| :---- | :----: | :----: | :----: | :----: | :----: | :----: |
| **1v1** | 45.7 | 45.0 | 43.8 | 52.0 | 51.3 | **62.6** |
| **party** | 53.4 | 69.4 | 72.9 | 83.9 | 83.4 | **92.8** |

A duel reads that as a 19-point spread and nearly flat; the party reads it as **39 points and Full Plate winning 93% of fights**. The mechanism is the same one that made the turtle a duel artifact in reverse: **at party scale you are attacked far more often, so anything priced per-defence-roll is worth several times what a duel says it is.** Half the Penalty is the version that survives both.

### Downstream, if this is adopted - none of it touched yet

`armor.md`'s Penalty formula is quoted in its own **Armor Penalty** section and its Rigid note, and Penalty also applies to **Acrobatics, Subterfuge and Spellcasting rolls** - softening it makes armour cheaper for casters and sneaks too, which is a real change well outside this chapter. The **Broken In** Feat (`general_feats.md`) is capped at `\-6` against a `\-8` Full Plate; against `\-4` that cap is meaningless and the Feat needs rescaling or removing. `wounds_and_survival.md`'s Wound Threshold table is STR-keyed by stated design intent, and `W \= 5` deletes that intent. Every armoured stat block in `core/bestiary/` carries a Penalty, though that file is stale against the Tempo rework anyway.

### Tool

`tools/tempo_sim.py` gains `DURABILITY` (default True), `FREE_DODGE_AP`, an `ARMOURS` table taken from `core/equipment/armor.md`, and `armoured()`. `Combatant.ar` is now current AR and degrades on every damaging hit; the Riposte path degrades it too, which it did not when AR lived on the Build.

---

## 43. Armour, second pass. The half-Penalty rule is dropped, and the fix gets simpler *(2026-08-21)*

Item 42's three-change fix was accepted on the first two changes and rejected on the third - **"the free Dodge takes half Armor Penalty" is clunky to explain, and this project is trying to remove steps from the table, not add them.** Correct call, and the replacement is better than the thing it replaces.

### First: two alternatives that do not work, recorded so nobody tries them twice

**Pricing armour in Tempo Dice instead of on rolls** - heavy armour costs you 1-2 dice from the pool, and Armor Penalty leaves combat entirely. It is the most attractive-sounding option on paper: it removes a modifier from every defence roll and prices armour in the chapter's own currency. **Measured, it is the worst option tried** - 31 to 56 points of ladder spread at both scales, across every cost vector. **A Tempo Die is far too coarse a unit.** The gap between `\-1` and `\-2` on a roll is small; the gap between four dice and three is enormous, and there is nothing in between.

**Applying Armor Penalty to Parry and Block as well as the Dodge**, which allows much smaller Penalty numbers and is one rule instead of two. Best case 15.5 / 21.9 - better than as-written, worse than what follows, and it makes armour punish the fighter who defends *well*.

### The finding that shaped the answer: any Rigid/Flexible gap in Penalty re-sinks plate

| Penalty vector | 1v1 spread | party spread |
| :---- | :----: | :----: |
| **`[0,1,1,2,2,3]` - no Rigid/Flexible gap** | 16.1 | **4.1** |
| `[0,1,1,2,3,4]` - a gap of 1 | 24.1 | 18.1 |
| `[0,1,1,2,3,3]` - a gap of 1 | 22.5 | 18.7 |
| `[0,1,2,2,3,4]` - a gap of 1 | 23.4 | 15.8 |

**A single extra point of Penalty on Rigid armour is enough to sink it** - Breastplate falls from 69% to 54% at party scale. That is what it means for a cost to land on the most-rolled roll in the game: one point there is worth far more than one point anywhere else. **So the Rigid/Flexible distinction cannot live in the Penalty formula.**

### And Breastplate is already a dead item, today, before any change

`armor.md` gives Brigandine **AR 6, Penalty \-3, 350 Crown, 3 Slots** and Breastplate **AR 6, Penalty \-6, 700 Crown, 3 Slots**. Same AR, same Slots, **twice the price and twice the Penalty**. There is no build for which Breastplate is the right purchase. It is strictly dominated as the table stands, and the only thing separating the two entries is the stat that makes one of them worse.

### Adopted shape: three changes, and the third one now *removes* a rule

| | 1v1 spread | party spread | STR/DEX |
| :---- | :----: | :----: | :----: |
| as written | 45.0 | 61.2 | 19.8 |
| item 42's three changes | 13.9 | 16.2 | 17.5 |
| **this** | **14.8** | **7.6** | **20.8** |

1. **One Penalty formula for all armour, derived from AR alone: `Penalty \= AR / 3`, rounded to nearest.** Gambeson through Mail Shirt `\-1`, Chain Mail through Half-Plate `\-2`, Full Plate `\-3`. This **deletes** the current two-branch rule (Rigid equals AR, Flexible equals half AR) rather than adding to it.
2. **Flat Wound bands at `W \= 5`**, unchanged from item 42. AR cannot matter until the bands are narrow enough to notice it.
3. **Rigid armour loses 1 durability every second hit instead of every hit.** This is where the Rigid/Flexible distinction goes now that it cannot live in Penalty, and it is the correct place for it in fiction as well - plate turns a blow that would cut mail. It also gives Breastplate a reason to exist: same AR and Penalty as Brigandine, twice the price, and it lasts twice as long under fire.

Result at party scale: **71.1 / 67.4 / 72.0 / 69.9 / 75.0 / 74.6** across none, Buff Coat, Mail Shirt, Brigandine, Breastplate, Full Plate. Armour is now mildly *positive* and rises at the top of the ladder, which is the right shape - you get what you pay for, and what you pay is money and Slots rather than combat effectiveness.

### Why this is a streamlining win and not a wash

**Removed:** the Rigid/Flexible Penalty split, and with it the "Rigid armor never fully cancels" special case. **Added:** one clause on durability, in a mechanic that already exists and is already tracked per hit. Net, the armour chapter loses a branch and gains a modifier-free defence roll.

### Downstream, still not touched

Softening Penalty makes armour cheaper for **Acrobatics, Subterfuge and Spellcasting** too, which is a real change outside this chapter and the reason a caster in mail is now a more reasonable proposition than it was. The **Broken In** Feat (`general_feats.md`) is capped at `\-6` against a `\-8` Full Plate; against `\-3` it is meaningless and needs rescaling or cutting - and its stated guarantee that "Rigid armour never fully cancels" refers to a rule that would no longer exist. `wounds_and_survival.md`'s STR-keyed Wound Threshold table is deleted by `W \= 5`.

### Tool

`RIGID_HALF_WEAR`, `AP_ON_ALL_DEFENCES`, a `rigid` flag and `hits_taken` on the combatant.

---

## 44. Armour, third pass. The exchange rate, and a fix that adds no rules at all *(2026-08-21)*

Item 43's package was accepted, with one addition: **the AR, Penalty, price and Slot numbers on the armour table are themselves changeable**, provided the entries stay realistic relative to one another. That turns out to be the lever that finishes the job, and it lets both of item 43's new rules be dropped.

### The design constant: one point of Armor Penalty costs 3 to 4 points of AR

Two identical builds, one carrying `(AR, Penalty)` and the other `(AR \+ k, Penalty \+ 1)`. The second one's win rate:

| starting from | `\+1` AR | `\+2` AR | `\+3` AR | `\+4` AR |
| :---- | :----: | :----: | :----: | :----: |
| AR 3, `\-1` | 37.3% | 40.4% | 41.4% | 48.9% |
| AR 5, `\-2` | 44.6% | 47.2% | **51.4%** | 55.4% |
| AR 7, `\-2` | 43.0% | 48.7% | **51.4%** | 59.2% |

**Break-even is around `\+3` AR, and nearer `\+4` at the light end.** Everything about armour in this project follows from that one number. The table as written charges a Penalty point per **2** AR for Flexible and per **1** AR for Rigid - **overpriced by two to four times**, at every rung, which is why the ladder was monotonically negative and why no amount of formula-tweaking fixed it.

This is the figure to design against, and it is more useful than any particular table: **a Penalty point must buy at least 3 AR, or the step down the ladder is a trap.**

### What that implies about the shape of the table

An AR span of 2 to 9 is seven points wide, so at 3 AR per Penalty point it supports **three Penalty bands and no more**. Attempts at four bands (`0/\-1/\-2/\-3`) measured 19-20 points of party spread; three measured 10-18.

It also means a perfectly flat ladder is impossible, and chasing one is a mistake. **Penalty is an integer, so the cheapest entry in each band always pays a full Penalty point for a single point of AR.** That residual sawtooth is real and it is about 8 points wide - and it is paid for in **gold and Slots**, which no simulation here models. Mail Shirt at 150 Crown and Brigandine at 350 sit in the same Penalty band; the difference between them is money, which is the correct place for that trade to live.

### Adopted: three changes, none of which is a new rule

| | 1v1 spread | party spread | band-tops, party | STR/DEX |
| :---- | :----: | :----: | :---- | :----: |
| as written | 45.0 | **61.2** | - | 19.8 |
| item 42's three changes | 13.9 | 16.2 | - | 17.5 |
| item 43's three changes | 14.8 | 7.6 | - | 20.8 |
| **this** | 22.9 | **10.3** | **86 / 84 / 85** | 20.3 |

1. **Armor Penalty is banded from AR alone: AR 2-3 is `0`, AR 4-6 is `\-1`, AR 7-9 is `\-2`.** This **deletes** the two-branch Rigid/Flexible formula, and the bands are three AR wide because that is what a Penalty point costs.
2. **The Wound Threshold table stops being keyed to STR and is fixed at its existing STR 1 row** - 1 Wound on 1-7, 2 on 8-14, 3 on 15+. Note this is a *smaller* change than items 42-43 proposed: `W \= 5` invented new numbers, `W \= 7` keeps the ones already printed and deletes only the per-STR keying.
3. **Rigid armour is re-statted `\+1` AR: Breastplate 7, Half-Plate 8, Full Plate 9.** A table change, not a rule. This is what makes Rigid worth its price now that Penalty no longer distinguishes it, and it fixes an item that is broken today regardless of any of this - **Breastplate is currently AR 6 / `\-6` / 700 Crown / 3 Slots against Brigandine's AR 6 / `\-3` / 350 Crown / 3 Slots, strictly dominated, with no build that should ever buy it.**

**Both of item 43's new rules are dropped.** Half-rate wear for Rigid armour is redundant once Rigid carries `\+1` AR - measured, it makes the ladder slightly *worse* (party spread 22.3 against 18.5 at `W \= 5`), because plate no longer needs the help. And the half-Penalty free Dodge was already dropped in item 43.

**Net effect on the rules text: two things are deleted and nothing is added.** The Rigid/Flexible Penalty formula goes, the STR keying on Wound Thresholds goes, and the armour table gets new numbers in two columns.

### Where it lands

Party scale, four PCs all in the same armour against three peers:

| none | Gambeson | Buff Coat | Mail Shirt | Chain Mail | Brigandine | Breastplate | Half-Plate | Full Plate |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| 77.2 | 80.3 | **85.6** | 75.3 | 81.8 | 83.9 | 77.5 | 80.0 | **84.9** |

**Comparing like with like - the best entry in each Penalty band - gives 86 / 84 / 85.** Armour is now a genuine choice: within a band you buy AR with money and Slots, and crossing a band costs a Penalty point and buys three AR.

The 1v1 spread is 22.9 and sawtoothed, which is the integer-Penalty artifact above rather than a fault to chase. Build balance is untouched at 20.3.

### Tool

`RIGID_HALF_WEAR` is retained as an unadopted switch. Recommended settings to reproduce: `WOUND_BANDS` flat at `(7, 14)`, `DURABILITY = True`, `RIGID_HALF_WEAR = False`, `FREE_DODGE_AP = 1.0`, `AP_ON_ALL_DEFENCES = False`, and the AR/Penalty ladder above.

---

## 45. Armour, adopted. Penalty `\-1` to `\-3`, the AR ladder raised to pay for it, and Broken In deleted *(2026-08-21)*

Item 44's ladder ran Penalty from `0` to `\-2`, which left the two lightest armours free and made wearing nothing competitive with wearing mail. **Adopted instead: Penalty spans `\-1` to `\-3`, every armour carries some, and the whole AR ladder rises to pay for it at the measured rate of 3 AR per Penalty point.**

### The adopted table

| Armor | AR | Penalty | | Armor | AR | Penalty |
| :---- | :---: | :---: | :--- | :---- | :---: | :---: |
| Gambeson | 4 | \-1 | | Chain Mail | 7 | \-2 |
| Buff Coat | 5 | \-1 | | Brigandine | 8 | \-2 |
| Mail Shirt | 6 | \-1 | | Breastplate | 9 | \-2 |
| | | | | Half-Plate | 10 | \-3 |
| | | | | Full Plate | 11 | \-3 |

**Penalty is banded from AR alone: 4-6 is `\-1`, 7-9 is `\-2`, 10-12 is `\-3`.** Bands are three AR wide because that is what a Penalty point costs. Rigid armour sits one AR above the Flexible piece sharing its band - Breastplate 9 against Brigandine's 8.

### Where it lands, against four candidate ladders

Four PCs in the same armour against three peers, `W \= 7` Wound bands:

| ladder | party spread | band-tops | none |
| :---- | :----: | :---- | :----: |
| AR 3-10, each band starts `\+3` | 11.3 | 80 / 79 / 78 | 76 |
| AR 3-11 | 12.6 | 79 / 79 / 83 | 75 |
| AR 2-11, gaps at boundaries | 15.6 | 75 / 80 / 82 | 76 |
| **AR 4-11 (adopted)** | **9.8** | **84 / 84 / 83** | **74** |

The adopted ladder is the only one where **every armour on the table beats wearing none**, which is the point of a scale with no free rung. 1v1 spread is 16.7 and unarmoured leads it at 58.5 against a best armour of 55.9 - going without armour stays a real choice in single combat, and stops being one in a party fight.

### A side effect worth keeping: heavy weapons matter again

At full durability a Full Plate harness (AR 11) turns a Longsword (`1d6 \+ 2 \+ STR`) almost every time and a Greatsword (`1d12 \+ STR`) still gets through. **That is the weapon differentiation item 36 said the Wound Thresholds had flattened out of the game, arriving from the armour side instead.** Nothing was designed for it; it falls out of raising the AR ladder.

### Broken In is deleted rather than repriced

`general_feats.md`'s **Broken In** reduces Armor Penalty by 2 per take, up to 3 takes and `\-6` total. Against a scale whose entire range is `\-1` to `\-3`, **a single take cancels the heaviest armour in the game.**

**And there is no smaller version worth having.** Armor Penalty is now the whole cost of armour and it spans three points. A Feat buying back even one point is buying a third of the axis - and at 3-4 AR per Penalty point, that one point is worth more than the gap between a gambeson and a breastplate, for a single Feat slot. **There is no version of this Feat that is not the best Feat in the game.** It also guarantees that *"Rigid armor never fully cancels"*, a rule that no longer exists.

Deleting it touches `general_feats.md`, the "Broken In (times taken)" input in `templates/character/character_sheet.html`, and `armor.md`'s line naming it as the only way to reduce Penalty.

### A general note on why the numbers moved so far

Three passes changed the fix and none of them changed the diagnosis. **The rate - one point of Armor Penalty costs 3 to 4 points of AR - was the finding; everything since has been arithmetic against it.** Items 42 and 43 tried to fix armour without touching the AR column, which was the wrong constraint: with AR fixed, the only free variable is Penalty, and Penalty could not be made small enough to balance the ladder without also making it meaningless. Being told the table's own numbers were changeable is what ended it.

### Tool

`ARMOURS` now holds the adopted ladder, `ARMOURS_OLD` the published one, and `armoured()` sets `rigid` automatically.

---

## 46. Armour, fourth pass. The tool was stale, three rungs were worse than bare, and the fix is one AR *(2026-08-21)*

**Item 45's ladder was adopted off a single seed, and it does not survive five.** Three of the eight armours sit at or below wearing nothing. The whole ladder rises one AR.

### First: `tempo_sim.py` on disk could not reproduce the last three items

`WOUND_BANDS` was still **keyed to STR**, which is the rule items 44 and 45 deleted - and item 44's own reproduction note says it ran with the bands *"flat at `(7, 14)`"*. The switch was made in the session and never written to the file, so the tool as committed models a system three items out of date. Anyone re-running it would have got different numbers and no warning.

**Fixed with `FLAT_WOUND_BANDS` (default `True`, bands `(7, 14)`)**, with the published STR-keyed table retained so the pre-item-44 finding stays reproducible. With that restored, item 45's figures reproduce to within a point or two - so **nothing in items 44-45 was measured wrong.** What was wrong is how thin the measurement was.

> The cost of the STR keying, for the record: it overstates the unarmoured party by about **5 points** (81.1 against 75.8), because a high-STR defender got wider Wound bands and armour got no credit for the damage it removed. Every armour figure before item 44 is inflated in bare's favour by roughly that much.

### The finding: the bottom rung of every band is worse than no armour at all

Four PCs in one armour against three peers, **5 seeds x 3,000 fights, standard deviation under 0.5**:

| | none | Gambeson | Buff Coat | Mail Shirt | **Chain Mail** | Brigandine | Breastplate | **Half-Plate** | Full Plate |
| :---- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| party win | 75.8 | 76.4 | 81.3 | 85.4 | **74.0** | 79.7 | 85.0 | **77.0** | 84.0 |
| vs bare | - | \+0.6 | \+5.5 | \+9.6 | **\-1.8** | \+3.9 | \+9.2 | \+1.2 | \+8.2 |

**Chain Mail loses to wearing nothing in every seed.** Gambeson (`\+0.6`) and Half-Plate (`\+1.2`) are inside noise of it. Item 45 reported bare at 74 and Chain Mail at 74 and read that as a tie; the tie was a seed.

**This is the one property that ladder had to have.** Item 45 chose it over three rivals specifically because *"every armour on the table beats wearing none, which is the point of a scale with no free rung."* It does not.

### The cause, mapped rather than argued

Sweeping AR 0-12 against Penalty 0-3 at party scale gives the whole surface, and it confirms item 44's constant exactly:

| starting from | AR needed to break even on `\+1` Penalty |
| :---- | :----: |
| AR 4-6 (the light end) | **\+4** |
| AR 7-9 | **\+3** |
| AR 8-10 (the heavy end) | **\+3** |

**A Penalty point costs 3 to 4 AR. Crossing a band boundary buys 1.** So the bottom rung of every band pays four for one, and there is always a bottom rung - the sawtooth is **structural**, and no arrangement of three-wide bands removes it.

**What is negotiable is where the sawtooth sits, not whether it exists.** A band-bottom armour being the poor buy in its band is correct and interesting. A band-bottom armour being worse than going bare is an item with no reason to exist.

### Adopted: every AR rises by one, and the bands rise with it

| Armor | AR | Penalty | | Armor | AR | Penalty |
| :---- | :---: | :---: | :--- | :---- | :---: | :---: |
| Gambeson | 5 | \-1 | | Chain Mail | 8 | \-2 |
| Buff Coat | 6 | \-1 | | Brigandine | 9 | \-2 |
| Mail Shirt | 7 | \-1 | | Breastplate | 10 | \-2 |
| | | | | Half-Plate | 11 | \-3 |
| | | | | Full Plate | 12 | \-3 |

**Penalty bands: AR 5-7 is `\-1`, 8-10 is `\-2`, 11-13 is `\-3`.** Bare stays at AR 0, so every armour gains a point on it.

| | worst rung vs bare | ladder spread | party ceiling | 1v1 spread |
| :---- | :----: | :----: | :----: | :---- |
| item 45's ladder (AR 4-11) | **\-1.8** | 11.4 | 85.4 | 16.5, bare ranks **1st** |
| **adopted (AR 5-12)** | **\+3.9** | 10.5 | 90.3 | 14.9, bare ranks 2nd |

**No rule changes and no relationship changes** - Penalty is still banded from AR alone, bands are still three wide, all armour still carries some, and Rigid still sits one AR above the Flexible piece in its band (Breastplate 10 against Brigandine 9). Two columns of numbers move by one.

**The price, stated plainly: the ceiling rises from 85 to 90.** Best armour now swings 14 points over bare at party scale rather than 9.6. That is a large dial - though still well under targeting's 24 (item 41) - and it is the intended direction for the main defensive purchase in the game.

### Two things this does not fix, recorded so nobody expects it to

- **The 1v1 sawtooth is untouched.** Chain Mail sits ~15 points under Mail Shirt in single combat under **both** ladders. That trough is the integer-Penalty artifact at its worst, and a duel is the scale where Penalty is charged most and AR credited least.
- **Bare is still first or second at 1v1** and only stops leading in a party fight. Item 45 accepted that on purpose; it is unchanged.

### Two rejected alternatives

- **Move the bands up without moving the AR column** (bare 0, Gambeson 4 at Penalty `0`). Identical spread and ceiling to the adopted ladder, but it makes a **padded jacket the joint-best armour in the game** at 90.2. The fiction has a veto here that the numbers do not.
- **Widen the bands to four AR.** The rate is 3-4, so a four-wide band charges a Penalty point at the top of what it is worth and makes the bottom rung worse, not better.

### One law this item paid for

**A single seed cannot establish an inequality between two things that are close.** The claim "every armour beats bare" rested on a 0-point gap read once. The project's own noise rule - `\±2` points, treat under 5 as nothing - already forbade reading it, and it was read anyway because it was the answer the ladder had been selected to produce. **Where a measurement is the acceptance criterion for a choice, it needs more seeds than a measurement that is merely reported.**

### Tool

`FLAT_WOUND_BANDS` added and defaulted on. `ARMOURS` holds the adopted ladder; `ARMOURS_45` holds item 45's, kept to reproduce the finding; `ARMOURS_OLD` is still the published file.

---

## 47. The ladder floor reverts to `1d4`, and half of the flat `\±2` turns out to be load-bearing *(2026-08-21)*

Two findings, and the second one only appeared because the first one was being regression-checked.

### The headline balance figure was two items out of date

It reads *"STR/DEX spread across the field: ~11 pts"* and *"the STR 1 build is what is left"*, meaning STR 1 was the **weak** build at 41%. Measured against the adopted rules, the spread is **21.5** and the STR 1 build is the **strongest thing in the game**:

| | S5/D1 | S4/D2 | S3/D3 | S2/D4 | S1/D5 | spread |
| :---- | :--: | :--: | :--: | :--: | :--: | :--: |
| 1v1 | 46.5 | 43.5 | 46.4 | 48.6 | **65.0** | **21.5** |
| party, 4 of them vs 3 peers | 85.1 | 82.9 | 86.7 | 90.2 | **98.3** | 15.4 |

The ~11 figure predates items 44-46. Item 44 itself reported 20.3 and nobody carried it forward to the sign-off block, since cleared.

### The cause is item 40's `1d6` floor, fixing a problem items 42-46 then fixed again

Item 40 raised the floor because the STR 1 build sat at 42-44%. **Repricing armour and unkeying the Wound Thresholds from STR both removed compensations STR was getting**, which lifted that build on its own - so by item 46 the raised floor was paying a debt already settled, and it was handing a free die upgrade to the build that already holds the largest pool and the best committed Dodge.

**Adopted: back to `1d4/1d6/1d8/1d10/1d12`, one rung per STR point.**

| | 1v1 spread | party spread | rounds | S1/D5 turtle peak |
| :---- | :----: | :----: | :----: | :----: |
| `1d6` floor (item 40) | 21.5 | 15.4 | 1.73 | 94% |
| **`1d4` floor (adopted)** | **5.4** | **7.3** | 1.93 | 87% |
| `1d6` floor, committed Dodge adds DEX/2 | 13.1 | 10.7 | 1.59 | - |
| `1d6` floor, pool capped at 5 | 12.7 | 11.7 | 1.80 | - |

5 seeds x 2,000. The revert is the only candidate under the project's own 5-point noise floor, it **removes** a rule where both alternatives add one, it deletes the dead STR 2 rung item 40 accepted as its cost, and it moves fight length toward the 2-round target rather than away. Both alternatives are **DEX taxes** - see the law item 35 paid for.

**What it costs is not measurable here: a `d4` is a bad die to roll.** Item 40's arithmetic still stands - `1d4` against `1d12` at equal Skill wins 12.5% of contests. What has changed is that this no longer produces an unbalanced *build*, because DEX 5 pays for it. The feel argument is the only one left, and it is a real one.

### Then: Press against Measured, and the half of it that must not be fixed

Both Press and Measured were written as a flat `\±2`. Against a `1d4` that is half the die and against a `1d12` a sixth, so **blanket-Press beat blanket-Measured 71.5% at `1d4` and 32.2% at `1d12`** - a 39-point range for one rule. It is a **shape** fault, not a size fault: widening to `\±3` takes the range to 45.4.

**The two halves are not the same problem**, which is the finding. Changing one at a time, 5 seeds x 2,000:

| Press | Measured | Press-vs-Measured range | STR/DEX field |
| :---- | :---- | :----: | :----: |
| flat `\+2` | flat `\-2` | 39.3 | **5.4** |
| **roll twice, higher** | **flat `\-2`** | **15.0** | **5.7** |
| flat `\+2` | roll twice, lower | 32.6 | **20.6** |
| roll twice, higher | roll twice, lower | 5.2 | **17.6** |

**Adopted: Press rolls the Tempo Die twice and takes the higher. Measured keeps its flat `\-2`.** The range falls by nearly two thirds, build balance does not move (5.4 to 5.7 is inside noise), and fight length does not move at all (1.93 to 1.94).

### Why Measured's `\-2` has to stay flat

**Measured is the attack you make most of the time**, so its modifier is effectively a term in almost every attack roll in the game - and **a flat term in every roll costs a small die more win probability than a large one**, because the contested roll's spread is narrower. That is currently **the main thing holding STR and DEX level.** Making it proportional costs **15 points** of field spread and hands the game to the high-DEX build.

**The `\-2` is not a wart. It is a STR subsidy spelled as an attack modifier**, and it was doing that job unnoticed. Recorded rather than hidden, because anyone tuning Measured for feel would silently break the Attribute field. If it ever has to change, **the 15 points must be replaced somewhere explicit, not given up.**

**Press's defensive debt stays at `\-2`**; at `\-1` the range is 33.2, worse. A flat number is right *there*, because the debt lands on defence rolls and **the Dodge is a fixed `1d8` for everybody.** Which is the rule of thumb the whole item produces:

> **Flat numbers are safe on defence and unsafe on the attack roll**, because one side of this chapter rolls a fixed die and the other rolls a variable one.

**What is left, and accepted:** Press still slopes, 47.9 at `1d4` to 32.9 at `1d12`. The residue is no longer the roll - at large dice the modifiers nearly cancel and the comparison reduces to **Measured's refund against Press's `\+2` damage and `\-2` debt**, which the refund wins by about 15. A sustainable attack beating a reckless one as a blanket policy is the correct result for a situational tool.

### One law this item paid for

**A regression check is where findings come from, not a formality.** The `1d4` revert was found by regression-checking a change to Press, and the load-bearing `\-2` was found by regression-checking the revert. Neither was the thing being measured. **Re-measure the headline figures after every adopted change** - the sign-off's stale ~11 survived two items precisely because nobody did.

### Tool

`LADDERS["draft"]` is the `1d4` ladder again; item 40's is kept as `floor_1d6`. `PRESS_MODE` (`"adv"` adopted, with `"flat2"`/`"flat3"`/`"step"` measured and rejected), `MEASURED_FLAT` (**do not make this proportional** - the comment says why) and `PRESS_DEBT` are separate switches, because the item's whole finding is that they are separate questions. `COMMIT_DEX_FRACTION` and `POOL_CAP` were added for the two rejected floor alternatives.

---

## 48. Declaration, Shock, and a Riposte that takes tempo - three borrows from The Riddle of Steel *(2026-08-22)*

**The problem: a turn holds too many attacks.** Measured, 3.85 on average with the top tenth of turns running to six. **The problem was not the pool.** A two-die fighter averaged 2.89 attacks and reached six, because the turn loop runs on the *live* pool and **a winning Measured refunds its die into another swing.**

### Capping is not available, and the cap does not have to be small to be expensive

| | STR/DEX field spread |
| :---- | :----: |
| no limit | **5.7** |
| cap of 3 | 29.3 |
| cap of 2 | 21.9 |
| **cap of 1** - the Major Action buys one attack | **52.0** |

The law from item 35 holds at three more points: **any limit on how many times you may act is a DEX tax, because only a large pool ever reaches a limit.**

### One attack per turn, measured properly, is a different game

Worth recording in full because it was a serious proposal and the failure is structural, not a tuning miss. Gate attacks to the Major Action and **the Tempo Pool stops existing in single combat**: you face one attack per round, so you can spend at most one die. Pool sizes of 2 flat, 3 flat, `DEX/2 \+ 1`, `DEX \+ 1`, and a convex defence cost **all produced the identical duel result.** The field goes 52 points to STR (S5/D1 at 79.7, S1/D5 at 27.8), fights run **9.3 rounds**, and stalls appear.

Six rescues measured: the attack also costing a die (45.6), four pool shapes (identical), DEX added to every defence roll (34.5, but 14.6 rounds and 12 stalls), Max Wounds cut by one (47.6) and by two (39.3). **All of them together: 25.9 spread, 10.2 rounds, 9 stalls.**

The reason is one sentence: **with one attack per attacker per round, attacks never outnumber dice, so nothing is ever scarce.** The pool becomes a pure anti-outnumbering resource - live at party scale, inert in a duel - and since DEX buys only pool size, DEX buys nothing in a duel.

### Adopted: three changes, taken from The Riddle of Steel

TRoS budgets a Combat Pool across a fixed two exchanges per round, allocates it **blind and simultaneously**, hands the initiative to whoever wins on defence, and strips dice automatically as Shock when a blow lands. Three of those transfer.

**1. The sequence is declared and paid up front.** How many attacks, and a type for each, before any of it is answered.

**2. Shock: every landed blow takes 1 Tempo Die.** Automatic, no margin, no choice. It **replaces** the Strip Tempo Opening rather than joining it, so the Opening menu loses an entry.

**3. Riposte cancels one of the attacker's remaining declared attacks**, as well as giving the free swing.

| | spread | attacks/turn | top tenth | duel rds | stalls | party | party rds |
| :---- | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| draft as written | 5.7 | 3.85 | 6 | 1.94 | 0 | 64.5% | 2.4 |
| \+ declaration | 7.7 | 2.95 | - | 2.27 | 0 | 70.8% | 3.5 |
| \+ Shock | 6.7 | 2.95 | - | 2.27 | 0 | 70.4% | 3.5 |
| **\+ Riposte cancels** | **6.2** | **2.79** | **4** | 2.39 | 0 | 70.8% | 3.6 |

5 seeds x 2,000, field pinned at hold 1 - the lens every figure in this log uses. **Spread 5.7 to 6.2 is inside noise.**

### Why declaration works where a cap does not

**It limits nothing.** You may declare as many attacks as you can pay for. What it removes is the **running start** - swinging until it stops working and pocketing the remainder - and with it Measured's refund loop. There is no threshold for a big pool to run into, so there is nothing for DEX to be taxed on.

Two consequences arrived free:

- **Measured now means what the chapter always said it meant.** Its refund returns to a sequence that is already fixed, so it can only fund defence: *"what a fighter with two dice and three enemies does all day."*
- **Feint became honest.** It is worth taking only with a follow-up, and the follow-up is now declared rather than hoped for.

### The Riposte variants, and why the cancellation needs the swing

| a won defence at margin 5 buys | spread |
| :---- | :----: |
| **free swing \+ cancel a declared attack** | **6.3** |
| free swing \+ strip a Tempo Die | 8.7 |
| cancel only, no free swing | **17.2** |

Stripping a die taxes DEX, because the pool is DEX's resource. **Cancelling with no swing is much worse**, because a purely subtractive counter pays whoever defends most often, which is the largest pool. **Lowering the trigger instead is worth almost nothing** - margins of 5, 4 and 3 measured within a round of each other. **If a counter is to matter, it must do more, not fire more often.**

### One part of the proposal did not survive: the defender has no choice

The sequence is declared in the open, so the defender sees everything coming and may ration. **Rationing is monotone worse at both scales:**

| defender holds back | duel | party |
| :---- | :----: | :----: |
| answers everything affordable | **51.7%** | **71.1%** |
| keeps 1 | 36.2 | 49.5 |
| keeps 2 | 27.4 | 37.8 |
| keeps 3 | 20.2 | 31.9 |

You already only pay when a paid defence would change the outcome, so there is never a reason to skip one you can afford. **An Exchange now contains exactly one decision and it is the attacker's.** Cheap at the table; possibly too cheap. Written as guidance, flagged as open question 16.

### Two costs, one of them intended

**Party fights run 2.4 rounds to 3.6 - this is the target, not a loss**, roughly three rounds being the aim. It follows the rule that held across every configuration measured today: **the total number of attacks in a fight is set by Wounds, not by the attack rules.** Cutting attacks per turn buys turns. Max Wounds is the only lever that moves the total.

**The turtle got slightly worse, 87% to 90%**, and that follows from the design - committing up front makes over-committing riskier, so holding back is safer than it was. Item 41 established it as a duel artifact that inverts at party scale, but it moved the wrong way and should not go unrecorded.

### What was left alone

The three attack types stay. Deleting them was measured at **24 points** (Measured's flat `\-2` is the STR subsidy of item 47) and would need the subsidy re-homed as a `\+2` on every defence to survive. Declaration already removes the refund loop that was a third of the reason to cut them.

### One law this item paid for

**When a mechanism cannot be limited without breaking, look for what is *extending* it rather than what is *permitting* it.** Attacks per turn were never bounded by the pool; they were bounded by the pool plus a refund loop plus the freedom to stop early. Three sessions were spent trying to cap the permission. **The fix was to delete the extension** - and it cost two points where every cap cost twenty-two to fifty-two.

### Tool

`DECLARE_UP_FRONT`, `SHOCK` and `RIPOSTE_MODE` added and defaulted on. `take_turn` is now a thin wrapper over `take_turn_multi` so both scales run the same declaration code - **they had drifted apart, and a party-scale figure was silently measured against the old loop once because of it.** `attack()` takes a `prepaid` flag; `take_riposte()` wraps `riposte()` with the cancellation.

---

## 49. The Dodge is deleted and Evasion comes back as a static score - reversing item 34 *(2026-08-22)*

**Decision: `Dodge` is gone in both its forms. The unpaid defence is `Evasion \= DEX \- Armor Penalty`, static, no roll. A Tempo Die buys a Parry or a Block and nothing else.** Designer's call, measured before adoption. **This reverses item 34**, which deleted Passive Evasion the previous day.

### Why reverse a decision that was right

Item 34's argument was fictional and it is still the better fiction: *"there is no way to passive evade something, that is just your opp missing."* Nothing measured here contradicts it. What the measurement found is that **the free Dodge was carrying two faults that were attached to it rather than caused by it**, and both die when it does:

- **`\+DEX` on the committed Dodge was the turtle engine** (item 41 named it and then accepted it as a duel artifact). DEX bought the pool *and* a `\+5` swing on every die in it.
- **Armor Penalty charged against the most-rolled number in the game** was why armour needed items 42-46 and still came out sawtoothed.

### What was measured, and in what order

**The proposal as asked measured badly at first**, and decomposing it is what found the real cause:

| | field spread (3 seeds) |
| :---- | :----: |
| control - draft as written | 6.3 |
| delete the committed Dodge, keep the free Dodge roll | **42.9** |
| static Evasion, keep the committed Dodge | 11.7 (best flat) |
| **both, at the swept-best constant** | **7.3** |

**Deleting the committed Dodge alone costs 36 points**, because it removes DEX's only quality term. Deleting the free roll alone costs 5. **Doing both is nearly free**, and that is not a coincidence: the static Evasion gives DEX back a quality term in the one place it cannot double-dip, since Evasion cannot be spent.

**The constant is the whole of the tuning, and zero is the answer.** Swept over 20 cells - flat 0-3 crossed with a DEX weight of 1.0-1.5:

| Evasion | spread | length | note |
| :---- | :----: | :----: | :---- |
| **`DEX \- AP`** | **5.5** | 1.84 rds | adopted |
| `1 \+ DEX \- AP` | 8.2 | 1.98 rds | turtle mirror returns at 99% stalls |
| `2 \+ DEX \- AP` | 18.2 | 2.24 rds | |
| `3 \+ DEX \- AP` | 25.6 | 2.85 rds | paid-defence rate falls to 9% |

**A static defence that is any good is a static defence nobody spends a die against.** At flat 3 the pool has stopped being a pool. Evasion has to be bad for the dice to be worth spending - which is also why the `1d8 \+ 2` free Dodge could not simply be converted to its own average of 6.5.

### What it fixed

**The turtle, which item 41 accepted as unfixable-without-a-rule.** Three seeds:

| | best-hold peak | S1/D5 turtle mirror |
| :---- | :----: | :---- |
| control | 89-90% | 40 rds, 100% stalls |
| **adopted** | **65-67%** (69% on the report's smaller sample) | **1.8-2.0 rds, 0% stalls** |

Best hold is now 0 for four of the five field builds. **No rule was added to achieve this** - the dominant strategy went away with the term that was funding it.

**The armour ladder, monotone for the first time.** Under the control, wearing nothing (61%) beat six of the eight armours. Party scale, three seeds, on the reverted ladder: **70 / 72 / 77 / 83 / 83 / 87 / 87 / 91 / 94.** Nothing beats the thing above it and everything beats bare.

### The exchange rate that governs armour changed by a factor of three

> **One point of Armor Penalty is worth about one point of AR, not three to four.**

Items 42-46 established 3-4 AR per Penalty point and raised the entire AR ladder to pay for it. **That rate was a property of the free Dodge**, which charged Penalty against every defence roll in the fight. Evasion charges it once, against a score the defender falls back on rather than relies on. Measured, **doubling every Penalty on the table moves the ladder by one point** (range 32 to 31); `\+1` across the board makes it *worse*.

**So the AR inflation is reverted** - `core/equipment/armor.md`'s published AR column, with Penalty re-derived in bands of three (1-4 is `\-1`, 5-7 is `\-2`, 8-10 is `\-3`). Keeping the inflated ladder measures bare 44% against Full Plate 76% in a duel: it runs away.

**Two levers to re-price armour were measured and rejected.** Penalty on Parry and Block as well: 3 points of build spread, armour range 26 instead of 24, and it punishes the fighter who defends well. Penalty on attack rolls too: over-corrects hard - bare becomes the best armour on the table at 59%, Full Plate falls to 38%, and the turtle returns at 40 rounds. **If plate needs a counterweight it has to be AR or durability, not Penalty.**

### What it cost

**A quarter of the fight length.** Duels 2.40 rounds to 1.83, party 3.6 to 2.7. **Widening the Wound bands from 7/14 to 8/16 buys back most of a round for 0.8 points of spread**, which is inside noise, and that is the compensation adopted. The sweep is monotone in both directions:

| Wound bands | spread | duel | party | armour range |
| :---- | :----: | :----: | :----: | :----: |
| 7/14 | 6.6 | 1.83 rds | 2.7 rds | 12 |
| **8/16 (adopted)** | **7.4** | **1.99 rds** | 2.7 rds | 8 |
| 9/18 | 9.2 | 2.14 rds | 2.9 rds | 8 |
| 10/20 | 10.0 | 2.26 rds | 2.9 rds | 4 |

**Roughly 0.15 rounds per point of spread.** Max Wounds `\+1` was measured as the alternative and is worse per round bought (0.39 rounds for 2.3 points). Shock off buys nothing (1.86 rounds).

**The defender's choice, which is now only whether to pay.** Most builds have exactly one paid defence. 38% of attacks go unanswered - either nothing purchasable reaches the number, or the pool is empty. Recorded as draft open question 16.

**Exhaustion is harsher.** An empty pool used to still roll `1d8 \+ 2`; it now meets a static 2 to 4 that stops almost nothing. The quick build's survival against two opponents falls from 34% to 7%.

### Something that is NOT this change's fault, checked because it looked like it was

**Blanket Press beating the mixed heuristic 67-87%** looked like a new break until the control was measured: **79 / 61 / 71% before the change.** Press dominance is pre-existing and belongs to the attack-type heuristic, not to the defence rework. The change does widen it for the high-DEX build (61% to 87%).

### A decomposition error worth recording

The first decomposition run reported "static Evasion with the committed Dodge kept" and "static Evasion without it" as **identical to the decimal** - because the patch dropped the committed Dodge whenever `PASSIVE_EVASION` was on, so variant B never ran. Two configurations producing the same number to three significant figures is not a finding, it is a bug. **Identical output from configurations that differ is the cheapest bug signal there is, and it should be checked for deliberately.**

### Tool

`tools/tempo_sim.py` gains `PASSIVE_EVASION`, `EVASION_FLAT`, `EVASION_DEX`, `COMMITTED_DODGE` and `AP_ON_ATTACK`, and the adopted defaults are now the configuration above. Evasion is encoded as a `(die \= 1, bonus \= E \- 1)` pair so every comparison in the resolver works unchanged - `roll(1)` is always 1, so the total is always exactly E, and the expected-value comparisons the spend decision uses stay correct. `FLAT_BANDS` moves to `(8, 16)`; `ARMOURS` reverts to the published AR with new Penalties, and items 45-46's ladder is kept as `ARMOURS_46`.

---

## 50. Parry and Block merge. They were one mechanic written as two rows *(2026-08-22)*

**Decision: there is one paid defence, called a Parry: `1d(Tempo Die) \+ Weapon Skill \+ Guard \+ Distance`.** Guard is 0 without a shield; a shield's own Distance modifier is 0. The full Opening menu is open to everyone. **The shield's damage-soak clause is deleted.**

**Motive is scope, not balance:** cut the chapter to a working core, then build depth back on top of it. This item is what that instruction found when pointed at the defence table.

### The finding that decided it

**`tools/tempo_sim.py` has never modelled Parry and Block as two things.** `Combatant.paid_defences()` has, since it was written, returned a single line - `die \+ Skill \+ Guard`. So **every figure in items 33 to 49 was measured against the merged rule already.** The draft was describing one mechanic as two, and the two rows differed only in which modifier came after the Skill.

**That is the whole argument and it is worth stating as a law:** a difference the tool cannot express is a difference no measurement in this log has ever supported. It does not follow that the difference is worthless - only that nothing here has ever priced it, and three rounds of "the numbers are fine" said nothing about it either way.

### The one clause that was a real rule, measured and cut

**"A Block reduces damage by its Guard even when it loses"** was the only part of Block that was not a modifier on the same roll. Modelled for the first time here (`GUARD_SOAK`), and it is worth almost nothing:

| | duel vs peer, soak off | soak on |
| :---- | :----: | :----: |
| Guard 1 | 42.5% | 42.7% |
| Guard 2 | 54.8% | 54.9% |
| Guard 3 | 66.5% | 67.3% |

Party-scale figures move inside noise. **The reason is structural:** under a static Evasion you only pay for a defence when it can change the outcome, so a *paid* defence that loses is rare, so the soak rarely fires. **Cut, with the switch kept.**

### What was kept, and where it was put

**The shield's exemption from the Distance modifier survives** - it is the only reason reach bites differently on different builds, and a shield genuinely does turn a spear thrust at any range. **It moved out of the defence rules and into the shield's own row in the off-hand table**, next to Guard. Same rule, no clause in the Defending section, which now carries one formula and no exceptions.

### Incidental, and larger than the thing being decided

**Guard is the biggest number on any piece of gear in the chapter.** No shield to a Guard 3 shield is **30.3% to 66.5%** in a duel against a peer - a wider swing than the entire armour ladder produces (70% to 94% at party scale). At party scale it is more modest, 70.5% to 78.1%.

**That was not measured before because Guard had never been swept**, only carried on one build in the standard party. With Parry and Block merged, Guard is now the *only* thing distinguishing a shield fighter, which makes it worth a pass of its own. Not opened as a fault - a shield being decisive in single combat is defensible - but it is the largest unexamined number left.

### Tool

`GUARD_SOAK` added and left at `False`. `Combatant.blocked` tracks whether the defender paid for the answer to a given attack, which the soak needed and nothing else uses. `paid_defences()` gains a docstring recording that its single-line form is now what the draft says, rather than a simplification of it.

---

## 51. The four Bands come back. The map has two distances, weapons have four *(2026-08-22)*

**Correction, not a redesign.** The 2026-08-21 rebuild read the instruction "reduce the track to Adjacent and one square away" as *"collapse the four Bands into the two distances."* It was meant as *"map the four Bands onto two distances"* - **Close and Middle are both fought Adjacent, Long and Far are both fought at Reach.** The map got smaller; the weapons were not supposed to. Three reach classes is the collapse; four Bands on two distances is what was asked for.

**Adopted, in [The four Measure Bands](exchange_draft.md#the-four-measure-bands):**

| Band | Adjacent | Reach |
| :---- | :----: | :----: |
| **Close** | 0 | cannot act |
| **Middle** | 0 | `\-2` |
| **Long** | `\-2` | 0 |
| **Far** | cannot act | 0 |

**One rule generates the whole table: your modifier is how many Bands you are from your own.** In Band 0, one off `\-2`, two off no roll at all. Nothing is memorised per class; the table is the arithmetic written out.

### What this restores that the three-class version had lost

**The Pike and the Dagger get their own tier back.** Under three classes a Dagger and a Broadsword were the same weapon at every distance, and a Spear and a Pike were the same weapon at every distance - which is exactly the granularity loss recorded against the original four-Band collapse (item 1's "the cost is granularity, and it is real") *and* the loss the 2026-08-10 five-Measure-Band split was itself made to fix. Restoring it costs no new arithmetic, because the two distances stay two.

**Reassignments from the three-class lists, all of them following the 2026-08-10 precedent:** Rapier moves down to **Middle** with the one-handed sidearms; Estoc stays with the two-handers in **Long** (it is Two-Handed in this chapter's own hands table, so it cannot join the one-handed row); Spear moves up to **Long** with the two-handers and out of the polearm class; Halberd, Glaive, Lance, Pike, Whip and Weighted Chain hold **Far**.

### The hole it opens, and the one rule spent on it

**On a two-wide map the extremes are strictly dominated.** Close is Middle minus its Reach option; Far is Long minus its Adjacent option. On the old four-hex track the extremes owned exclusive ground (Far was 3 hexes and nobody else could stand there); with two distances they own none, so the table alone makes a Pike a worse Spear and a Dagger a worse Broadsword.

**For Close that is correct and needs nothing.** Fists, daggers and shield rims are not meant to out-fight a sidearm - they are free, concealable, throwable, and the thing in your off hand. The chapter already pays them outside the Exchange.

**For Far it is not, and the fix is the one this log named years of runs ago:** *"the honest fix is a niche only a pike has, such as attacking past an adjacent ally, which is worthless in a duel and decisive in a line"* (a pre-rebuild note on Spear-and-Pike-are-identical, since cleared from this file - the sentence is quoted here in full). Adopted as written - **a Far weapon attacking at Reach ignores a creature in the intervening square, which also gives no Cover.** It is the only such clause in the chapter. **`tempo_sim.py` cannot see it**, by construction - the tool is 1-on-1 or N-on-1 with no geometry - so by item 50's own law nothing here prices it. It is adopted on fiction and on the Niches pillar, and it is a first candidate for whatever spatial tool gets written next.

### One ruling the split forced into the open

**An Opportunity Attack is resolved at the Distance the mover is leaving from.** Under three classes this never mattered, because no weapon was ever fully dead at either distance. With Far in the table it decides whether a halberdier gets a swing at the man stepping inside his point, and the answer is yes - the crossing is punished on the ground being given up. Written into [What you threaten](exchange_draft.md#what-you-threaten).

### Knock-ons in the draft

Parry's Distance clause, the hands table's one-handed row, the off-hand dagger's payoff, both worked examples, the threatened-squares rule and the glossary. **Example 1 was rewritten rather than renumbered:** a Broadsword is now *Middle*, so Toma parries the approach at `\-2` instead of not at all, and the drama moves to the other end - once she is Adjacent the Halberd is two Bands out and the die the bandit saved for defence buys him nothing. It teaches both new rows at once, and it states the Long/Far difference in the terms a player will actually feel: a Spear would have parried.

### Not measured

**Nothing here is simulated and nothing here can be by the current tool.** `tempo_sim.py` fixes both fighters Adjacent with weapons that act there at 0 and says so in its header. The `\-2` step, the two-Band wall and the Far weapon's clause are all first-draft guesses in the same sense as the rest of the chapter.

---

## Ten laws this session paid for

**A number doing load-bearing balance work from inside an unrelated rule is fragile, and has to be labelled.** **Measured**'s flat `\-2` is the main thing holding STR and DEX level: it is a term in almost every attack roll in the game, and a flat term costs a small die more win probability than a large one. Making it proportional - the obvious tidy-up, and the same repair that was free on Press - costs **15 points** of Attribute field spread and hands the game to the high-DEX build. **It is a STR subsidy spelled as an attack modifier.** Anyone tuning Measured for feel would silently break the Attribute field, so if it ever does change, the 15 points have to be replaced somewhere explicit rather than given up. (7, re-validated by 47)


**A difference the tool cannot express is a difference nothing in this log has ever priced.** Parry and Block were two rows in the draft and one line in the simulator for the whole of items 33-49, so every "the numbers are fine" said nothing at all about whether they should be two. **Before trusting a balance figure about a distinction, check that the model contains the distinction.** (50)

**Identical output from configurations that are supposed to differ is a bug, not a finding.** A decomposition run reported two variants matching to three significant figures because the switch for one of them was being overridden. Check for it deliberately - it is the cheapest bug signal available. (49)


**When a mechanism cannot be limited without breaking, look for what is *extending* it, not what is *permitting* it.** Attacks per turn were never bounded by the pool - they were bounded by the pool, plus Measured's refund loop, plus the freedom to stop early. Capping the permission cost 22 to 52 points; deleting the extension cost two. (48)


**A single seed cannot establish an inequality between two things that are close.** "Every armour beats bare" was read off a 0-point gap measured once, and it was false. Where a measurement is the **acceptance criterion** for a choice, it needs more seeds than one that is merely reported. (46)

**A regression check is where findings come from, not a formality.** The ladder-floor revert was found while regression-checking a change to Press; the load-bearing `\-2` was found while regression-checking the revert. **Re-measure the headline figures after every adopted change** - the sign-off's stale spread survived two items because nobody did. (47)


**Any limit on how many times you may act is a DEX tax**, because only high-DEX builds ever reach the limit. Caps and escalating penalties both. (35)

**Whatever is in every roll scales with how much rolls matter; whatever is in the pool scales only with how often you roll.** That is why every lever that lengthened a fight handed it to STR until Dodge came off the Tempo Die. (37)

**A measurement taken with a mechanism in place cannot tell you the mechanism is needed.** The escalating `\-2` survived two rounds of measurement on exactly that error. (35)

**A stall is a broken state, not a draw.** Averaging stalls in as 0.5 concealed a fault through two items and nearly promoted a degenerate config. (37)

## Tooling

`tools/tempo_sim.py` - run bare. Switches: `UNPAID_DEFENCE` (adopted **False** as of item 52 - there is no free defence; `True` plus `PASSIVE_EVASION` restores item 49's Evasion, `True` alone the free Dodge), `UNANSWERED_MARGIN`, `GUARD_SOAK`, `PASSIVE_EVASION`, `EVASION_FLAT`, `EVASION_DEX`, `COMMITTED_DODGE`, `AP_ON_ATTACK`, `AP_ON_ALL_DEFENCES`, `DECLARE_UP_FRONT`, `SHOCK`, `RIPOSTE_MODE`, `FLAT_WOUND_BANDS`, `FLAT_BANDS`, `SEQ_PENALTY`, `DODGE_DIE`, `DODGE_FLAT`, `DODGE_COMMIT_DEX`, `POOL_BONUS`, `FREE_DODGE_MOD`. Armour ladders: `ARMOURS` (adopted, published AR), `ARMOURS_46` (items 45-46's inflated ladder), `ARMOURS_45`, `ARMOURS_OLD`. **`tools/exchange_sim.py` and `exchange_solver.py` model a system that no longer exists and should be deleted.** Nothing models multiple opponents, casters, Feats, terrain, or ranged combat - and the value of a held die scales with how many people are attacking you, so **every policy figure here understates the case for holding dice.**

---

## 52. Evasion is deleted. There is no free defence at all - and armour is the only passive there is *(2026-08-22)*

**Decision: `Evasion` is gone. A Tempo Die buys a Parry; an attack nobody pays for lands, and pays the attacker an Opening as though they had won by 5. Never a critical.** Wound bands widen `(8, 16)` to `(9, 18)` to pay for the length. **This does not reverse item 49 so much as finish it** - item 49 reinstated Evasion as a static score and this deletes the score, but the thing item 49 was actually buying (DEX's quality term is not double-dipped, the turtle engine stays dead, armour prices cleanly) all survives, because none of it depended on the number being non-zero.

### The measurement item 49 never took

Item 49 swept Evasion's **side effects** - field spread, fight length, paid-defence rate - across a 20-cell grid and adopted flat 0 at full DEX. It never measured Evasion's **direct** effect: of the attacks that reach an unpaid Evasion, how many does it turn aside? Instrumented at party scale, three seeds:

| | `DEX \- AP` |
| :---- | :----: |
| attacks answered by Evasion rather than a Parry | 52.4% |
| ...that Evasion turned aside | **13.7%** |
| ...of those unpaid answers, taken with an **empty pool** | 84.7% |
| **Evasion's stop rate when the pool was empty** | **6.1%** |

**The number the chapter advertised as a floor was holding one swing in sixteen.** The 13.7% aggregate is carried almost entirely by the other 15% - *voluntary* stands, where the defender declined because a paid defence could not have changed the outcome either. Those are not Evasion working; they are Evasion recording a decision already made.

**The arithmetic says it could not have been otherwise.** An attack roll is `1d(Tempo Die) \+ Weapon Skill`. Against Skill 3 the minimum possible roll is 4, and ties go to the defender, so **an Evasion of 3 or less has a mathematically zero chance of stopping anything at any die size.** A trained fighter in a Mail Shirt has Evasion 2. Only four things in the chapter ever produce a roll low enough for Evasion to catch: Measured's `\-2`, a Band mismatch's `\-2`, Off-Balance, and an untrained attacker.

### What deleting it measures at

Three seeds. **Control reproduces `tempo_sim.py`'s unmodified defaults exactly**, which is the check that makes the rest of the row trustworthy - see the law below.

| | spread | duel | party | paid% | armour range | ladder dips |
| :---- | :----: | :----: | :----: | :----: | :----: | :----: |
| item 49 - `Evasion \= DEX \- AP` | 7.2 | 1.78 rds | 2.75 | 47.8 | 11.7 | **4** |
| no unpaid defence | 5.5 | 1.59 rds | 2.68 | 51.9 | 13.8 | **0** |
| **adopted - no unpaid defence, bands `(9, 18)`** | **5.7** | **1.72 rds** | **2.78** | **50.0** | 11.8 | **0** |

**It is better on the axis it was not aimed at.** Field spread improves 7.2 to 5.7, and the armour ladder becomes **monotone for the first time without a caveat** - item 49 got it monotone at party scale but left four inversions in this measurement; there are now none.

**The pool gets used more, not less.** Attacks answered by a paid defence rise from 48% to 50-52%. That is the opposite of the intuition - deleting a free defence ought to leave defenders poorer - and the cause is that a static score was absorbing *spend decisions*: if a number was going to hold, you kept the die. Take the number away and the die gets spent.

**Armour is what changed hands.** The unarmoured party falls and the armoured one does not, because **Evasion was the unarmoured character's substitute for armour**. Deleting it is what finally makes the chapter's own sentence true - *"when your dice are gone, what keeps you alive is your armour"* - rather than aspirational.

### The rule for an unanswered attack, which is NOT a measured decision

Three candidates: an unanswered attack lands at **margin 0** (no Opening ever), at **its full attack total** (Openings and criticals constantly), or at **exactly 5** (an Opening, never a critical).

**Adopted: exactly 5, and `tempo_sim.py` cannot tell you it is right.** The simulator does not model the attacker's Opening at all - only Shock and the defender's Riposte - so margin 0 and margin 5 measure **identically**. Do not cite a number for this choice; there is not one.

**It was decided on the incentive and on the fiction.** At margin 0, declining to defend makes you immune to Openings and criticals while a *failed Parry* does not - so the man who stands still is safer from a called shot than the man who tries to stop it, and against a big enough roll not defending becomes strictly correct. At full margin, running dry is not a bad turn but an execution. **At 5, declining costs you the Opening and saves you only the critical**, which is the one piece of generosity worth keeping: a man who never resisted should not be cut apart more thoroughly than one who did.

**It also deletes a special case rather than adding one.** The chapter used to carry a separate rule for targets who cannot act - lands automatically, Opening as though won by 5. That is now just what an unanswered attack does, so *helpless* stops being a mechanical category and becomes a description of somebody who never had the choice.

### Armor Penalty now does nothing in a fight, and that is the actual decision

> **The question was never "does Evasion survive." It was "does Armor Penalty have any job inside an Exchange."**

Evasion was Armor Penalty's last consumer in this chapter. With it gone, **AR is the entire mechanical presence of armour in a fight**, and Penalty is spent purely outside one - Stealth, Spell Modifier, Slots, gold. This is stated explicitly in [Armour and Wounds](exchange_draft.md#armour-and-wounds) rather than left to fall out of a defence rework, because it is a larger change than the one that caused it.

Item 49 had already measured a Penalty point at roughly 1 AR, so **very little moves numerically.** What moves is the rules text: a column that no longer has a reader. See open question 19.

### What it cost, and what paid for it

**Length, and the Wound bands paid it back.** Duel 1.78 to 1.59 rounds; `(8, 16)` to `(9, 18)` restores it to 1.72 with party fights slightly *longer* than before (2.78 against 2.75), for 0.2 points of spread. That is the second widening in one day - `(7, 14)` to `(8, 16)` to `(9, 18)` - and the dial's rate is unchanged from item 49's sweep at about 0.15 rounds per point of spread.

**One condition lost its entire mechanical content.** **Restrained** read *"your Evasion counts as 0"* and now reads *"your Parry is at Disadvantage and you cannot Move."* That is a substitution, not a measurement, and it is the weakest line in this item.

### A law this item paid for

**Encoding "no defence" as an enormous negative number is not encoding "no defence."** The first harness gave an unanswered attack a defence total of `\-999`, which cleared `CRIT_MARGIN` on every single one - so the first run scored **every unanswered attack as a critical hit** and reported deleting Evasion as costing 17% of fight length. It does not; it costs 11%, and the balance figures improved rather than held. **The bug was caught by a control that failed:** config A stopped reproducing the unmodified tool, because the same rewrite had also let a tie deal damage. **Re-run the control through the new code path and require it to match the old numbers before reading any experimental row** - a harness that changes the resolver has to prove it did not change the control first.

### Restrained, resolved properly *(same day, after the item was written)*

The item above left Restrained reading *"your Parry is at Disadvantage and you cannot Move"* - a substitution invented to fill the hole where *"your Evasion counts as 0"* had been, and flagged in this item as its weakest line. **Replaced with the 5e shape, at the designer's instruction:**

> **Attack rolls against you have Advantage; your own attack rolls have Disadvantage; your DEX Ward has Disadvantage; Speed 0.**

**Checking the published Condition first is what made this cheap.** `core/wounds_and_survival.md` already read *"Speed 0; disadvantage on attack rolls; `\-3` to DEX Wards; casting requires a MIND Ward (DC 18)"* - three of the four clauses were already there and already in the right shape. **What was missing was the only clause that matters in an Exchange:** attacks against a Restrained creature had no bonus at all, which is why the draft had needed a local invention in the first place. Two edits, both in `wounds_and_survival.md`: **add** the Advantage-to-attackers clause, and **convert** `\-3` to DEX Wards into Disadvantage so all four clauses run in one currency. It is a small softening - `core_rules.md` prices Disadvantage at about `\-2`.

**The load is on the attacker's die, not the defender's, and that is the correct side.** A Restrained fighter Parries at no penalty; what has gone wrong for them is that the swing coming in rolls twice. This is strictly better than the invented version, because **it is proportional.** By this log's own rule of thumb - *flat numbers are safe on defence and unsafe on the attack roll* (see the laws block) - a bonus against a Restrained target had to be Advantage rather than a flat number, or it would have meant half a `1d4` fighter's range and a sixth of a `1d12` fighter's.

**One collision the chapter had never had to answer.** **Press** is the chapter's own source of Advantage on the attack roll, and Restrained is now a second one. The Terms table gains the standard convention explicitly: **Advantage does not stack, and Advantage and Disadvantage cancel** whatever the count on either side. So Pressing a Restrained target rolls two dice, not three - the Press still buys its `\+2` damage and its defensive debt, it simply does not buy the Advantage twice.

### Prone and Off-Balance converted - and the measurement argued against it

**Adopted at the designer's instruction, with the cost stated.** Prone and Off-Balance were the two remaining flat `\-2` modifiers on rolls that a Condition imposes, and they now read in Advantage/Disadvantage like Restrained.

**Prone needed no invention at all - the published Condition was already right.** `core/wounds_and_survival.md` reads *"Disadvantage on attack rolls. Melee attack rolls against it have advantage; ranged attack rolls against it have disadvantage."* **It was the draft that had flattened it to `\-2`/`\-2`**, so this is a revert to the live file rather than a change to it, and `wounds_and_survival.md` needs no edit. The ranged clause is already carried by the Shot DC table's Prone rows, which stay flat correctly - a Shot DC is a flat DC, not a roll.

**Off-Balance stays on the DEFENDER's die, and that is load-bearing.** It could have been written as *"attacks against you have Advantage"*, matching Prone and Restrained. It is written as *"Disadvantage on every defence roll you make"* instead, because **Press already grants the attacker Advantage and Advantage does not stack** - so an Off-Balance that lived on the attacker's die would make **Feint into Press do nothing**, and Feint-then-Press is the obvious combination the type menu invites. On the defender's die the two are on different creatures' rolls, so they compose. **A rule that nullifies the chapter's own most natural sequence is a trap, whatever it measures at.**

### What it measured at, which is mildly worse

Three seeds, against the item-52 adopted configuration:

| | spread | duel | party | paid% | Press win% |
| :---- | :----: | :----: | :----: | :----: | :----: |
| control - both flat `\-2` | **5.7** | 1.72 | 2.75 | 49.9 | 70.1 |
| **Off-Balance to Disadvantage (adopted)** | **7.0** | 1.70 | 2.77 | 50.5 | 70.8 |
| Press's debt to Disadvantage (not adopted) | 6.3 | 1.71 | 2.77 | 50.5 | 71.1 |
| both | 7.2 | 1.70 | 2.76 | 50.2 | 71.5 |

**Everything except build spread is unmoved** - length, party win rate, paid-defence rate and the attack-type table are identical to the decimal. The cost is 1.3 points of STR/DEX spread, **inside the tool's documented `\+/-2` of seed noise but consistently signed across all three variants**, which is what makes it a cost rather than nothing.

**And the mechanism is worth writing down, because it corrects a guess made earlier in this item.** This subsection previously argued that the *"flat numbers are safe on defence"* law died with the unpaid defence, and therefore that converting would be an improvement. **The first half is right and the second half is wrong.** That law's original reason - *"the unpaid defence carries no die at all, so `\-2` off a static Evasion means `\-2` at every STR"* - is indeed void, because every defence is now a Parry rolling the Tempo Die. But flat is *still* the better-measuring option, for a reason item 7 never had to name:

> **A flat `\-2` hurts a small die proportionally; Disadvantage hurts a large die absolutely.** `\-2` is half a `1d4`'s range and a sixth of a `1d12`'s. Disadvantage costs a `1d4` defender 0.63 and a `1d12` defender 1.99. **Neither is neutral - they are biased in opposite directions**, and on a defence roll the flat version happens to sit closer to flat.

**Adopted anyway**, because currency consistency across Conditions is worth 1.3 points of a figure that is inside noise, and because the alternative is a chapter where Restrained uses one currency and Prone uses another for the same intent. **`OFF_BALANCE_DISADV = False` reverts it in one switch** if a later measurement makes the spread matter.

### Two flat modifiers deliberately left alone

**Press's own defensive debt stays `\-2`.** It is the same shape as Off-Balance and it measures the same way (6.3 against 5.7), but it was not part of the instruction, and unlike a Condition it is a *cost the player chooses to take* rather than something imposed on them - a flat, legible price on a voluntary option is defensible in a way an inconsistent Condition is not. `PRESS_DEBT_DISADV` exists as a switch.

**The Distance modifier stays `\-2`.** It applies to attacks and Parries alike and it is the Measure Band system's entire arithmetic; converting it would collide with Press's Advantage on the attack side and is a far larger change than this one. Not a candidate.

### One anti-synergy this creates, and it is accepted

**Advantage does not stack, so a Press against a Prone or Restrained target wastes the Press's Advantage** - the attacker keeps the `\+2` damage and still pays the defensive debt, but rolls two dice rather than three. It is mild, it is the standard consequence of the standard convention, and it is the price of putting Prone and Restrained on the attacker's die where the published Conditions put them. **Off-Balance is exempt by construction**, which is the whole reason it sits on the other side.

### A caveat on the 50% paid-defence figure

**The simulator's defender is now playing worse than the rules allow.** Its spend policy buys a defence only when the paid roll could still *win* - which was optimal while declining merely meant "hit," and is no longer, because declining now also concedes an Opening. A Parry that cannot win but can hold the margin under 5 is a real purchase the model never makes. **So 50% is a floor on the paid-defence rate, not an estimate of it**, and every figure in this item is measured against a defender who under-spends. Fixing the policy is the first thing to do before the next measurement of anything defensive.

### Tool

`tools/tempo_sim.py` gains `OFF_BALANCE_DISADV` (adopted `True`) and `PRESS_DEBT_DISADV` (adopted `False`), plus `roll_def()`/`ev_die()` so a defence roll can carry Disadvantage and the spend decision still compares expected totals correctly. It also gains `UNPAID_DEFENCE` (adopted `False` - `True` with `PASSIVE_EVASION = True` restores item 49 exactly, verified) and `UNANSWERED_MARGIN`. `FLAT_BANDS` moves to `(9, 18)`. The `EVASION_*`, `DODGE_*` and `COMMITTED_DODGE` switches are retained and are consulted only under `UNPAID_DEFENCE = True`.

---

## 53. The draft is cut to rules only - its Design notes and Open questions move here *(2026-08-22)*

**`exchange_draft.md` was streamlined into a player-facing chapter.** Everything removed from it that was argument rather than rules is preserved verbatim below: the "Design notes" and "Open questions" sections as they stood at the moment of the cut, including **item 17, the downstream merge checklist**, which is the inventory of what merging this chapter requires in the live files. **Item 54 adds three entries that checklist does not have** - see B2, B6 and C1 there.

Also removed from the draft and not repeated here, because it is recorded throughout this log: the per-rule "Why" commentary citing earlier drafts, point spreads and measurement dates; the "What this replaces" section; the armour win-rate ladder table; and the targeting win-rate table (open question 3 below keeps it).

## Design notes

**Not rules.** For people evaluating the system rather than playing it.

### The one idea

**Offence and defence draw on the same dice.** Everything else in the chapter is a consequence of that sentence.

It is what makes an attack a decision rather than a formality, because the third swing is paid for with the guard you will not have. It is what makes being outnumbered hard without a single rule written for it. It is what makes Measured a real choice against Press, and Feint a real choice against both. It is why there is no Reaction economy, no Stance, no declaration cycle, and no reactive step limit: the pool already does the work all four of those were doing, and it does it with one number.

**The second idea is that you spend it blind.** The whole sequence is declared and paid before any of it is answered, so the budget is a **prediction** rather than a running tally - and that is what stops "how many should I swing" from being a sum you can do at the table. It is also the only lever found that reduces attacks per turn without taxing DEX, because it limits nothing: it removes the running start. Every hard cap measured instead costs 22 to 52 points of build balance; declaring costs two.

The previous draft's core idea was that **melee is a distance**. This draft's is that **melee is a budget**. They are both true statements about fighting; this one is cheaper to run and the arithmetic is more visible to the player.

### Why two Attributes and not one

`Pool \= DEX \+ 1, die \= STR` is the load-bearing piece of Distinction. A pure count would make DEX the only combat Attribute. A pure die size would make STR it. Splitting them produces two builds that are the same points and play nothing alike, and neither can be described as a worse version of the other:

- **High DEX, low STR:** in every fight on the board. Wins by attrition, by Feints that set up a partner, and by never being the one who is out of dice. Loses any single contest it needs to win.
- **High STR, low DEX:** picks its moment. Every roll it makes is a favourite. Cannot afford to be attacked more than twice a round, which is a positional problem it must solve with the map and with armour.

**Neither Attribute is added to an attack roll, and that is load-bearing rather than an oversight.** The Tempo Die *is* STR on the roll - adding STR again would count it three times, alongside damage. **DEX is the pool and Evasion**, and since 2026-08-22 those are its only two jobs: the `\+DEX` that used to ride on a committed Dodge is gone, and with it the double-dip that made a defensive die worth most to whoever held the most. Measured, adding an Attribute to attacks makes whichever one you pick dominant (`\+STR` puts the field at 67-vs-24, `\+DEX` at 24-vs-76, against 51-vs-41) and collapses the average fight, because the unpaid defence is a fixed number with no die in it and everything added to an attack lands against a static score.

**Adding the weapon's *governing* Attribute - the version a real table would produce, since players pick weapons that suit them - is worse still, and in an unexpected direction: it punishes balanced builds.** A STR 3 / DEX 3 fighter adds `\+3` where both extremes add `\+5`, so the middle of the field drops to 35% while the specialists rise. It converts the Attribute spread into a flat roll bonus and pays it out for min-maxing.

### What was given up

**The spatial layer.** Four Bands on a hex track, an approach that took multiple Exchanges, and a read-and-counter-read cycle are all gone in exchange for two distances. **The four Bands themselves came back on 2026-08-22 (item 51)** - they now sit two to a distance rather than one to a hex - so what was actually given up is the *track*: the approach, the Cycle, and the multi-Exchange journey from out of Measure to inside the point. The depth that used to live in *where you are standing* now lives in *what you are spending*. That is a genuine trade and not obviously a gain - it is a gain in table speed and a gain in decision legibility, and a loss in the thing that made a spear feel different from a sword over the course of a whole approach.

**The universal `1d12`.** Combat now rolls `1d4` through `1d12` while every other check in the game rolls `1d12`. This is the largest Elegance cost in the draft and it is paid knowingly, because the variable die is the only place STR's contribution can live without becoming a flat bonus that reads as "STR is just better."

**Natural-roll criticals.** Unavoidable: a `1d4` cannot carry a natural-max crit rule.

### What has not been measured

**Nothing in this document has been simulated.** `tools/exchange_sim.py` and `tools/exchange_solver.py` model Bands, declarations, and the Cycle, and none of those exist any more. Every number here - the die ladder, `Pool \= DEX \+ 1`, the Opening threshold of 5, the crit threshold of 10, the \-2 escalation, the three typed attacks, all of the off-hand tools - is a first-draft guess.

The three that most need a tool pointed at them, in order:

**Measured five times on 2026-08-21** by `tools/tempo_sim.py`, and every pass changed the chapter.

The through-line of all five is one sentence: **the Tempo Die was in every roll in the game, so STR scaled with how much rolls mattered while DEX scaled only with how many rolls you got.** Every lever that made a fight longer therefore handed it to STR, which is why an escalating attack penalty, a cap on attacks, and a stronger free defence all failed the same way and for the same reason. Deleting the escalating `\-2` and taking the Dodge off the Tempo Die each cut a piece of that coupling: the STR/DEX spread went **55 points to 13.8** and the average fight went **1.3 rounds to 2.1**.

**A sixth pass, on 2026-08-22, reversed one of those five.** Reinstating **Evasion** as a static score and deleting the Dodge entirely holds the field flat (**7.0 points across three seeds**, against 6.3 for the draft it replaced - inside noise) and closes two faults that the free Dodge had been carrying rather than causing: *attack once, bank the rest* stops being dominant (the high-DEX build's peak falls from 89-90% to 65-69%, and its turtle mirror from 40 rounds at 100% stalls to about two rounds at none), and the armour ladder becomes monotone for the first time. **It cost a quarter of the fight length and most of the defender's tactical choice.** See item 49 of the design log.

See [Open questions](#open-questions) and items 33 to 37 and 49 of the design log.

---

## Open questions

**Pruned 2026-08-22 - the numbering is deliberately not contiguous.** Questions **1, 2, 4, 5, 7, 8, 9 and 14** closed and have been cleared; what they settled is recorded in items 40-52 and in the laws block above, and question 7's standing warning about Measured's `\-2` is preserved there rather than here. An older item citing one of those numbers is describing the draft as it stood at the time.

**What remains below is scoped to the system's tuning.** For the state of `exchange_draft.md` as a document - what contradicts what, what has no rule, and what breaks - see **item 54**, which supersedes this list wherever the two overlap.

**Measured across items 33 to 52 on 2026-08-21 and 2026-08-22** with `tools/tempo_sim.py`.


### 3. Numbers decide fights, targeting decides them hardest, and the chapter now says so

A lone fighter loses to **two** opponents of their own quality 97-99% of the time, and does not survive three. Four PCs against N such opponents: **2 of them 97%, 3 of them 63%, 4 of them 17%, 5 of them 1%.**

**Read that as a symmetric fight, not an encounter curve.** Attributes and Skills share one cap across every character in the game, so anything built on the player's axis is about as dangerous as a PC no matter what Level it is nominally worth. The steepness is what numbers do in any symmetric contest, and **it says nothing about encounter design until there is a weaker creature tier to measure against** - `core/bestiary/` predates both the 8-to-6 Attribute rework and the Tempo Pool.

[Situations](#being-outnumbered) previously read *"Nothing here is a special rule"* and described a manageable pressure. **It has been rewritten to say what the measurement says.** What remains open is not the prose but the design question behind it: whether a second enemy being worth more than any weapon, armour or Feat is the intended game. It is defensible for a lethal system, and it is worth deciding on purpose.

**A caveat that applies to every survival figure in this document.** The harness has no healing, no Feats, no spells, no terrain and no morale, and **nobody ever flees**. Most of all, **0 Wounds is Dying, not dead** ([[Wounds and Survival|wounds_and_survival]]) - so "survival" means "was not dropped." The shape is trustworthy; the absolute lethality is overstated.

**And targeting is the largest dial of all.** Same four PCs, same three opponents, same builds - varying only who attacks whom:

| | party win |
| :---- | :----: |
| enemy concentrates, party concentrates | 64.6% |
| enemy concentrates, party spreads | 40.3% |
| **enemy spreads, party concentrates** | **88.8%** |

**A 24-point swing from the enemy's targeting alone, and 24 more from the party's.** Nothing else measured for this chapter - not Passive Evasion, not the escalating penalty, not taking Dodge off the Tempo Die - moves a number that far. It is written into [Situations](#who-the-enemy-attacks) as guidance for both sides of the screen, and **the residual caveat stands: every balance figure in this document is conditional on a targeting assumption**, because the duel harness that produced most of them has no targeting to assume.


### 6. Adding STR or DEX to the attack roll - tested and rejected

Both are worse than adding nothing. **`\+ STR`** takes the spread from 14.7 to 37.9 points, because STR already *is* the die and a flat term double-counts it. **`\+ DEX`** takes it to **50.5** - the algebra flattens attack expected value at every build, which sounds like balance and is the opposite: it removes STR's only compensation while DEX keeps the bigger pool (and, at the time this was measured, the committed Dodge). **Both also halve fight length**, 2.10 rounds to 1.17, because a flat bonus on attacks with no matching term on defence has nowhere else to go.

Recorded here because the DEX version is genuinely tempting on paper. See item 38 of the design log.

**Re-tested after a correction, and it survives unchanged.** The simulator had been giving every build a STR-governed weapon, including the DEX builds - see item 39. With damage attributed properly the baseline improves to about **10-12 points**, and the rejected variants land at `\+STR` **42.9**, `\+DEX` **52.3**, governing Attribute **29.9**, half-governing **18.1**. Every one is still far worse than Skill alone, and the governing-Attribute version still punishes the *balanced* build hardest, at 35%.

**One reason the DEX version is less tempting than it looks:** DEX is not a count-only Attribute to begin with. Damage is `Weapon Damage \+ Attribute`, and Fencing Blades ([[Weapons|weapons]] - Rapier, Estoc, Stiletto) are **DEX-governed**, so a quick fighter with the right weapon already adds DEX to damage. The gap the `\+DEX` variant was meant to fill is partly not there.

### 10. The Shot DC is entirely unmeasured

`tempo_sim.py` models melee only. The base of 7 was set by hand so a trained shooter hits an exposed target about three times in four; everything else on that table is interpolation.

### 11. Openings may be doing too many jobs at once

The menu holds a free attack, a Condition applicator, a disarm, a shove and a disengage, and Feats are meant to extend it. There is a real chance **Riposte** is simply correct every time - and it is now *more* likely to be, because Riposte gained the cancellation. Unmeasured: the simulator models the defender's Opening as a Riposte, which assumes the answer rather than testing it.

**One entry has left the menu.** **Strip Tempo** is gone, replaced by [Shock](#shock) - every landed blow now takes a die automatically, rather than only when somebody won by 5 and chose it over a Riposte. That is a rule deleted and a mechanic that fires far more often.

### 12. Feint has no natural counter

Pure-Feint play cannot win a fight at all, so the simulator excludes it as a standalone policy and only exercises it inside a mixed heuristic. That may be fine - it is a setup tool, not a win condition - or it may mean Feint wants a cost beyond the die.

### 13. "Opening" versus "Riposte" as the name of the trigger

These rules use **Opening** for the thing you earn at margin 5 and **Riposte** for the free attack on its menu, because the attacker earns it as often as the defender does and "the attacker ripostes" reads wrong. If one word is worth more than the precision, collapse them.

### 15. Shock is a flat 1, and it should probably scale

Every landed blow takes exactly one Tempo Die, regardless of how bad the blow was. **The Riddle of Steel**, which is where this is borrowed from, scales its equivalent to the severity of the wound and splits it into immediate and lasting components. A flat 1 is what has been measured here and it costs nothing; **scaling it to Wounds dealt is untested**, and it would make heavy weapons and criticals compound in a way the flat version does not.

### 16. The defender's choice is now only whether to pay

**This got worse on 2026-08-22 and it is the clearest thing the Evasion rework gave up.** It was already true that rationing dice is not a real decision - measured, holding one back costs about 15 points of survival, two costs 25, three costs 30, monotone at both scales. What the free Dodge still provided was a choice of *which* defence to buy: Parry, Block, or a committed Dodge, with the answer legible off your sheet and different for a fencer than for a man in plate. **With the Dodge deleted and Block merged into Parry on the same day, every character has exactly one paid defence.** An Exchange now contains one decision on each side: the attacker picks a type, and the defender picks yes or no.

**One thing keeps that from being nothing:** the yes-or-no is live rather than automatic. Measured, 38% of attacks go unanswered - either nothing purchasable would reach the number, or the pool is empty. That is a real read on a real board, and it is the entire defensive game.

**Both halves of this were spent deliberately, and in the same direction.** The chapter is being cut to a working core first; depth is meant to come back on top of it. **The place to put it back is the Opening menu and Feats** - things that hang off a defence that already works - not a second defence row, which is what the last three versions of this chapter each tried and each had to delete.

**It is still thin, and it is the first place to look if the chapter ever feels passive to defend in.** Whatever fixes it has to come from somewhere other than how many dice to spend, and it cannot come from making Evasion better - see items 49 and 52, which between them measured the constant down to nothing.

**Item 52 sharpened the yes-or-no rather than thinning it further.** Deleting Evasion *raised* the paid-defence rate from 48% to 50-52%, because a static score was absorbing spend decisions - if the number was going to hold, you kept the die. The read is also harder now: declining costs an Opening as well as the blow, so "nothing I own reaches that number" no longer settles it on its own. **A second paid defence was measured again on the way and rejected again** - see item 52's rejected variants. Five versions of a Dodge, all either dominant or dead, for the structural reason that a Parry is `die \+ Skill \+ Guard` and a Dodge is `die \+ DEX`: the same roll with a different addend, so one is strictly better per character and there is nothing to choose between. **If a Dodge ever comes back it has to be differentiated by what it can ANSWER, not by how large it is** - the published `maneuvers.md` DEX Ward leg is the model, being the only leg that answers ranged, AoE and criticals. That points at [open question 10](#10-the-shot-dc-is-entirely-unmeasured), not at this one.

### 17. Downstream - what merging this chapter requires elsewhere

**Two live files carry numbers this chapter now overrides**, and both are published to the wiki:

- **`core/equipment/armor.md`** - **the AR column is unchanged** as of 2026-08-22; only the **Penalty column** is replaced, by the bands in [Armour and Wounds](#armour-and-wounds). **Item 52 makes this bullet's ownership questionable:** nothing in the Exchange reads Armor Penalty any more, so the bands are being defined by a chapter that does not consume them. The chapter still prints them, marked as carried rather than used. **Whether the derivation should simply move into `armor.md` is undecided and should be decided rather than inherited.** The 2026-08-21 draft rewrote both columns, and that inflation is reverted - reinstating Evasion moved where Penalty is charged, so the ladder no longer has to pay for it. The derivation note "Rigid armor's Penalty equals its AR, while Flexible armor's Penalty is half its AR" is **deleted**, along with the Rigid note that depends on it and the line naming Broken In as the only way to reduce Penalty. Durability, Slots and prices are unchanged. **Breastplate is a dead item as that file stands today** - AR 6, 3 Slots, 700 Crown against Brigandine's AR 6, 3 Slots, 350 Crown, identical but for a Penalty twice as large - and the new Penalty bands fix it as a side effect, by giving them the same Penalty and leaving the difference in Slots and gold.
- **`core/wounds_and_survival.md`** - the STR-keyed Wound Threshold table collapses to a single row, **two bands wider than its own STR 1 row**: 1 Wound to 9, 2 to 18, 3 beyond (widened again by item 52). **The Restrained Condition is already edited in that file** (item 52's follow-up): attacks against it now have Advantage, and its `\-3` to DEX Wards became Disadvantage. That is the second live change this rework has made, after Max Wounds. The extra point of width is this chapter's fight-length dial - see [open question 18](#18-fights-are-shorter-than-they-were-and-length-is-not-free). Max Wounds (Small 3 / Medium 4 / Large 5) is **already edited in that file** and is the only live change this rework has made so far.
- **`core/core_rules.md`** - **Evasion is deleted outright** as of item 52, reversing the "redefined, not deleted" note this bullet carried for one day. The published `5 \+ Evasion Skill Ranks \- Armor Penalty` has no successor in this chapter: there is no unpaid defence. That is a **wider** edit than redefining it, because a redefinition leaves every bestiary stat block, character sheet field, Feat and spell that references Evasion still meaning something. Now they reference nothing. Everything that modifies Evasion needs re-homing onto the Parry or deleting, one at a time.
  - **The Evasion Skill is now certainly cut, not possibly repurposed.** Its ranks were the formula's base and the formula is gone. Cutting it and refunding the ranks is the only option left on the table.
  - **Passive Ward is untouched.** `5 \+ Attribute` still governs STR Ward, MIND Ward and the rest; it was only *Passive Evasion* that carried the `\- Armor Penalty` clause, and only that line dies here.

**One Feat is deleted: Broken In.** It reduces Armor Penalty by 2 per take, capped at 3 takes and `\-6` total, against a scale whose entire range is now `\-1` to `\-3`. **A single take would cancel the heaviest armour in the game**, and there is nothing left to rescale it into - a Feat that moves a three-point axis by two points per purchase is not a choice, it is a switch. Its stated guarantee that *"Rigid armor never fully cancels"* also refers to a rule that no longer exists. **Cut it rather than repricing it.** Removing it touches `general_feats.md`, the "Broken In (times taken)" input in `templates/character/character_sheet.html`'s Feat Bonuses section, and `armor.md`'s reference to it as the only way to reduce Penalty.

> **Why deletion rather than a smaller version - and this reasoning weakened on 2026-08-22.** The original case was that Armor Penalty is the entire cost of armour and a point of it is worth 3 to 4 AR, so any Feat buying one back is the best Feat in the game. **Under a static Evasion a Penalty point is worth about one AR**, which makes a one-point Broken In merely good rather than absurd. The Feat still goes, for the smaller reason that a `\-1` to `\-3` axis cannot carry a repeatable Feat and Penalty no longer prices anything worth a slot - but the deletion is now a tidiness call rather than a forced one, and reinstating a single-take version would not break anything measured.

**Softening Penalty reaches outside combat**, which is a real change and not a side effect to wave through: Penalty also applies to **Acrobatics, Subterfuge and Spellcasting rolls**, so a caster or a sneak in mail is now a far more reasonable proposition than it was. That may be desirable; it should be decided rather than inherited.

**Two of this chapter's newer mechanics reach into the Feat files.** **Shock** means any Feat that granted or drained Reactions now interacts with a pool that also drains on every hit taken, and **declaring the sequence up front** invalidates any Feat written as "after your first attack, you may..." - those decisions no longer exist, because the sequence is fixed before the first roll. Both want a read of `martial_feats.md` specifically.

**The rest of the conversion is mechanical.** Reactions appear throughout `combat.md`, `basic_moves.md`, `positioning.md`, every Feat category, and `character_sheet.html`; all convert to Tempo Dice one-for-one, but every Feat granting extra Reactions or reducing Reaction costs needs re-reading, not just renaming. **Passive Evasion is defined in `core_rules.md` and referenced repo-wide** - deleting it touches that definition, every bestiary stat block, the sheet, and any Feat or spell that modifies it. **Initiative moving to MIND** touches `combat.md`, `positioning.md`, `bestiary_overview.md`, every stat block, and the sheet. `weapons.md`'s Reach column becomes a four-value Measure Band - Close / Middle / Long / Far (item 51) - and the Pike, Halberd, Glaive, Lance, Whip and Weighted Chain rows need the Far weapon's strike-past-an-intervening-creature clause. Every hex count becomes a square count. Every Feat with a widened crit range becomes a lowered crit threshold. Stat blocks need a Tempo Pool line - `DEX \+ 1` dice at the `STR` die.

**`core/bestiary/` is stale against all of this** - it predates the 8-to-6 Attribute rework as well as the Tempo Pool - so it wants rebuilding rather than converting. That is also what blocks any real encounter-design guidance: there is no current weak-creature tier to calibrate against.

**`tools/exchange_sim.py` and `exchange_solver.py` model a system that no longer exists; `tools/tempo_sim.py` replaces them and both should be deleted rather than adapted.**

### 18. Fights are shorter than they were, and length is not free

**Reinstating Evasion took the average duel from 2.40 rounds to 1.83, and party fights from 3.6 to 2.7.** Widening the Wound bands from 7/14 to 8/16 buys back most of a round for 0.8 points of spread, and that is the whole of the compensation applied.

**More is available and it is priced.** The bands were swept:

| Wound bands | spread | duel | party |
| :---- | :----: | :----: | :----: |
| 7/14 | 6.6 | 1.83 rds | 2.7 rds |
| **8/16 (adopted)** | **7.4** | **1.99 rds** | **2.7 rds** |
| 9/18 | 9.2 | 2.14 rds | 2.9 rds |
| 10/20 | 10.0 | 2.26 rds | 2.9 rds |

**Roughly 0.15 rounds per point of build spread, monotone, with no stalls anywhere on the sweep.** 8/16 is the last rung where the length is inside the noise of the measurement; everything past it is a real trade. **Length and STR/DEX balance are the same dial**, which is the same finding item 37 made from the other direction, and it means "make fights longer" is never a free instruction in this chapter.

**The part that is not about round count** is what a short fight does to a fighter whose pool has run out. Under the free Dodge, exhaustion meant defending badly; now it means not defending, because a static Evasion of 0 to 4 stops almost nothing. Combined with Shock, the spiral is steeper than it was, and being outnumbered is decisively worse - the quick build's chance against two opponents fell from 34% to 7%. **Whether that reads as lethal or as unfair is a table question the simulation cannot answer.**

**Updated 2026-08-22 by item 52.** The bands widened once more, `(8, 16)` to `(9, 18)`, to pay for deleting Evasion - so this sweep's 9/18 row is now the adopted rung and the sweep should be read one line down. **The rate held on re-measurement** (0.2 points of spread for 0.13 rounds), which is the third independent confirmation of ~0.15 rounds per point.

**The exhaustion half of this question got worse in fact and clearer in kind.** An empty pool now means no defence at all rather than a static 0-to-4, and the unanswered blow pays the attacker an Opening on top. But the practical delta is small, because Evasion was already stopping only 6% of the attacks it met with an empty pool - **what changed is that the chapter now says plainly what was already true**, instead of printing a number that implied a floor there was not. That is the whole of the defence: the question stays open, and it is now open honestly.

### 19. Armour is now priced entirely outside the Exchange - and after item 52, literally so

**The ladder is monotone for the first time and it is steep**: 70% bare to 94% in Full Plate at party scale, against a spread of 11 points under the free Dodge. Nothing inside a fight holds plate in check, because Armor Penalty - measured - is worth about one point of AR now that it is charged against a static score rather than against every defence roll. Doubling every Penalty on the table moves the ladder by a single point.

**What holds it in check is 2,000 Crown, six Slots, Stealth, Spell Modifier, and the reasons people did not sleep in harness** - none of which `tempo_sim.py` models, and all of which are real at a table. That may be exactly right: plate *was* better, and a system where it is a wash inside a fight is modelling something that did not happen.

**It is carried as open because it is unverified, not because it is suspected.** Two levers were measured and both are worse: charging Penalty on the Parry as well costs 3 points of build balance and punishes the fighter who defends well, and charging it on attack rolls over-corrects so hard that going bare becomes the best armour on the table. **If plate turns out to need a counterweight, it has to be an AR change or a durability change, not a Penalty change.**

**Item 52 removed the last hedge in this heading.** Evasion was Armor Penalty's only consumer inside an Exchange, so as of 2026-08-22 **no rule in this chapter reads Penalty at all** - armour's entire combat presence is AR and its decay. Numerically this barely moves, because item 49 had already priced a Penalty point at roughly 1 AR. What it does is make the two levers above the *only* levers: there is no longer a Penalty setting that could be turned, so the paragraph above is not a preference any more, it is the complete list.

**And it sharpens the question this heading was always asking.** Heavy armour in this chapter now has no in-fight downside whatsoever - it is strictly better once swords are out, and everything it costs is paid in Stealth, casting, Slots and gold. **Measured, the ladder is monotone and every armour beats bare, which is the intended shape**; whether "no in-fight cost at all" is the intended *reason* for that shape is a design call nobody has made explicitly. Make it before merging.

---

## 54. Full read of the draft against the live files. This item is the state of `exchange_draft.md` *(2026-08-22)*

> **This supersedes every "open", "pick up here" and "still to do" list above it.** Items 31-53 record how the draft got its shape and why each number is what it is; this item records what is *wrong with it now*. Read it before touching the draft, and before merging any part of the chapter into `core/`.

### How it was read, and what that scope excludes

Read in full against `core/combat/combat.md`, `basic_moves.md`, `maneuvers.md`, `positioning.md`, `core/wounds_and_survival.md`, `core/core_rules.md`, `core/equipment/weapons.md`, `core/equipment/armor.md`, `core/magic/magic_overview.md` and the arcane school files - and against this log, so that a decision already settled here is not re-raised as a defect.

**Nothing in this item was simulated and nothing in it is a balance finding.** These are rules faults of four kinds: text that contradicts itself, text that contradicts a live file, an option that no longer functions at all, and a case a table hits in its first session with no answer in the chapter. Small balance concerns were deliberately excluded; where a fault also happens to be a large balance problem that is noted, but the fault is why it is listed.

**Every finding carries a stable ID** so a later item can cite one without quoting it: **B** breaks something or kills an option, **C** contradicts a published file, **A** is an ambiguity that needs a ruling, **N** is minor. Line numbers are `exchange_draft.md` as it stood at this reading.

| | | |
| :---- | :---- | :---- |
| **B1** | Opportunity Attack resolution rule contradicts Example 1 | `:168`, `:367` |
| **B2** | Deleting Evasion orphans every Arcane Spell Attack | `:508` |
| **B3** | The Buckler line gives every build a free `\+1` Guard | `:525` |
| **B4** | A shield with no Distance modifier switches the Band system off | `:250`, `:524` |
| **B5** | Guard never degrades; Pavise loses its Guard but not its listing | `:249`, `:527` |
| **B6** | Breastplate is strictly dominated by Brigandine | `:334` |
| **B7** | Unarmed both can and cannot Parry | `:143`, `:254` |
| **B8** | Weapon crit ranges have no conversion to the margin system | `:293` |
| **B9** | A Mythic creature can answer every attack in the fight | `:429` |
| **B10** | Weapon properties keyed to deleted mechanics | `:146` |
| **C1** | Advantage stacking contradicts `core_rules.md` | `:39-40` |
| **C2** | Paralyzed/Unconscious auto-crit contradicts "never a critical" | `:229`, `:262` |
| **C3** | Initiative still DEX in `core_rules.md` and `combat.md` | `:411` |
| **C4** | `basic_moves.md` collides in four places, one a name collision | `:470` |
| **C5** | Grappling is not addressed anywhere in the chapter | - |
| **A1** | The declaration does not name targets | `:198` |
| **A2** | Riposte's cancellation has three unanswered cases | `:276` |
| **A3** | Riposte chains are not closed off | `:283` |
| **A4** | Can a plain attack crit? | `:206` |
| **A5** | A defender winning by 10\+ has nothing to double | `:96`, `:270` |
| **A6** | Shock's trigger is stated two ways in one section | `:297`, `:299` |
| **A7** | The unanswered rule does not say what the attack's *type* does | `:188` |
| **A8** | Does Press's `\-2` stack with itself? | `:187` |
| **A9** | Emptying your pool makes you immune to Shock | `:297` |
| **A10** | Called Shot is unbounded and undated | `:277` |
| **A11** | Example 2 ignores its own Called Shot | `:391`, `:397` |
| **A12** | Ranged combat has no roll, no die cost and no rate | `:485` |
| **A13** | Conditions and the pool need one general clause | `:466` |

---

### B - breaks, or renders an option useless

**B1. The Opportunity Attack rule contradicts the chapter's own worked example.** `:168` reads *"An Opportunity Attack is resolved at the Distance the mover is leaving from."* That is correct for the *leaving* half and nonsense for the *entering* half: somebody stepping from 2 squares out into Reach is leaving from **out of it**, where no Band can act, so entering a polearm's threatened ring can never be punished at all. **Example 1 resolves exactly that crossing at Reach** (`:367`, *"a halberd at Reach is in its own Band"*), so the rule as written forbids the example that teaches it. Needs "at the nearer of the two Distances", or "at the Distance where the boundary sits".

Two consequences fall out of the same clause even after it is fixed. A **Close** weapon can never make an entering Opportunity Attack (always resolved at Reach, where it cannot act), so half the rule is dead for it. A **Middle** weapon makes that attack at `\-2`, in a zone `:164` defines as *"the squares your weapon acts in at no penalty."* The zone definition and the resolution rule are measuring different things.

**B2. Deleting Evasion orphans every Arcane Spell Attack, and the chapter says otherwise.** `magic_overview.md:53` is `1d12 \+ Spell Modifier vs. target's Evasion`; `aeromancy.md:12`, `geomancy.md:12` and `hydromancy.md:12` all read *"vs. target's Evasion"*. The draft's only statement on this is `:508`, *"Spells resolve against **Ward** as they always have"* - which is true of Spell Overcomes and false of Spell Attacks, an entire resolution mode that now has no target number anywhere in the game. **This is the largest hole in the merge** and it wants a decision in this chapter rather than at conversion time: a flat DC, the Shot DC table, or a Parry.

Item 53's downstream checklist already flags Passive Evasion as repo-wide, but it frames the work as re-homing *modifiers*. This is not that. It is a missing target number for three schools' worth of published spells.

**B3. The Buckler line hands every build a free `\+1`.** `:525` - *"light enough that it does not occupy the hand for anything else."* That contradicts the hands table nine rows above it (`:516`, Two-Handed: *"May carry something in the off hand: **Never**"*) and `weapons.md:296` (*"never a Two-Handed weapon"*). As written, a Greatsword fighter buys a 40-Crown buckler and adds `\+1` to every Parry for the rest of the campaign at no cost in hands, dice or actions. Either it occupies the hand or it is not a shield.

**B4. A shield with no Distance modifier switches the Measure Band system off.** `:250` and `:524` give the shield a flat `0` at any Band. Anyone with a free hand therefore parries at full Skill plus Guard from any distance - **including the halberdier who has been closed on**, which is the exact failure Example 1's payoff is built on (`:377`, *"a Spear would have parried"*). It also makes the off-hand dagger (`:526`) strictly worse than the cheapest shield, so the *"one problem the Bands create"* already has a better and cheaper answer than the tool the chapter spends a paragraph justifying.

The roll is also under-specified. A Parry is `1d(Tempo Die) \+ Weapon Skill \+ Guard \+ Distance` (`:220`), and `:247` says what you are holding decides *"two of the roll's terms"* - Guard and Distance - which leaves **Weapon Skill** unaccounted for when the shield is the thing parrying. Holding a Pike and a Heater, is it Hafted & Polearms? Holding only a shield, what Skill at all? `weapons.md:298` is explicit that *"a shield carries no Skill of its own"*, and this chapter has no Block Skill to fall back on.

**B5. Guard never degrades, and Pavise is listed twice at two different values.** `weapons.md:316` ties Guard decay to *"reduc[ing] a losing Oppose margin"* - a mechanic this chapter deletes - so in the draft Guard is a permanent flat bonus while AR decays on every hit. That is a rule that used to exist quietly disappearing rather than being decided. Separately, `:527` gives the Pavise *"nothing at all in an Exchange"* while `weapons.md:281` gives it Guard 3, which makes the draft's own *"Guard, `\+1` to `\+3`"* (`:38`, `:249`, `:565`) wrong in three places: the real in-Exchange range is `\+1` to `\+2`, and `:249`'s *"largest number on any piece of gear in this chapter"* is off by one.

**B6. Breastplate is a dead item, and the fix item 53 predicted did not land.** `:334` - AR 6, `\-2`, 3 Slots, **700 Crown**, against Brigandine at AR 6, `\-2`, 3 Slots, **350 Crown**. Identical in every mechanical column, double the price, and *worse* on repair, since `combat.md` bars Rigid armour from field repair once broken. Item 53's downstream note predicted the new Penalty bands would fix this *"by leaving the difference in Slots and gold"* - but the Slots are equal, so only the gold is left and it points the wrong way. Breastplate needs an AR, a Slot, or a price before this table is published.

**B7. An unarmed fighter both can and cannot Parry.** `:143` lists **Unarmed** among the Close-band weapons; `:254` and `:480` say a fighter with no weapon and no shield *"cannot spend a Tempo Die on defence at all."* Since the caster's entire balancing position rests on the second reading (`:508`, and the *"dagger in the off hand is the cheapest thing in the game to fix it"* line), this has to be explicit. If fists parry, the caster paragraph collapses; if they do not, Unarmed should not be in the Band table as a defensive implement.

**B8. Weapon crit ranges have no conversion, and the naive one is enormous.** `:293` converts only *Feats*: *"a Feat that reads 'crit on 11-12' reads 'crit on a margin of 9 or more.'"* Every melee weapon in `weapons.md` carries a Critical column - Dagger and Stiletto at 9-12, Shortsword/Scimitar/Rapier/Estoc/Battle Axe/Mace at 10-12, Longsword/Greatsword/War Maul/Glaive/Chain Flail at 11-12. At one point per step a Dagger crits at **margin 7**, against an Opening threshold of 5. That is not a fringe interaction; on an opposed roll it fires on a large share of won contests, and it makes small blades the best critical platform in the game. Either the column converts explicitly and is retuned against the 5/10 ladder, or it is deleted here and the weapons lose the line.

Note the width the chapter is working in: Opening at 5, critical at 10. There are only five points between them, so any conversion that moves a threshold by three is a structural change, not a weapon perk.

**B9. A Mythic creature can answer every attack in the fight.** `:429` refills the pool on every Initiative count. A Mythic (4) with DEX 3 has **16 dice a round** - more than a four-PC party can generate attacks - so it Parries all of them at `1d12 \+ Skill`, and Shock, the chapter's compounding mechanic, cannot touch it. The chapter's stated and measured win condition is numbers (`:450`, *"a second enemy is worth more than any weapon, any armour, and any Feat"*); this rule switches that off precisely where the party most needs it. Deliberate per item 31, but *"it is never out of dice"* understates what the rule actually does.

**B10. Weapon properties keyed to mechanics this chapter deletes.** Chain Flail's only distinguishing property is **Bypasses STR Ward**; the STR Ward Oppose leg no longer exists, so an 80-Crown weapon becomes a plain `1d8`. **Lashing Reach** is worse than dead - `weapons.md` states Whip and Weighted Chain *"can't actually strike out to 2-3 squares"*, while the draft's Band table (`:146`) puts both in **Far**, which makes them Reach-only, unusable Adjacent, and holders of the strike-past-an-intervening-creature clause (`:156`) at 10 and 20 Crown. Also unreferenced and now meaningless: **Guard and Control** (`weapons.md:302`), **Guard and Measure** (`:300`), and Weighted Chain's *"can grapple at Reach"*.

---

### C - contradicts a published file

**C1. Advantage stacking.** `:39-40` states *"It does not stack"* and *"Advantage and Disadvantage cancel, **whatever the count on either side**"*, and attributes both to Core Rules. `core_rules.md:27` says the opposite: *"Compare total sources of each; the side with more wins. If equal, roll normally."* Two Advantage plus one Disadvantage is Advantage there and a flat roll here. **Item 52's Off-Balance reasoning depends on the draft's version** - it is the whole argument for keeping Off-Balance on the defender's die - so `core_rules.md` is the file that moves, and this is a live-file edit the chapter creates rather than inherits.

**C2. Paralyzed and Unconscious auto-crit.** `wounds_and_survival.md:190,197` both read *"any melee attack that hits it is a critical hit."* The draft says an unanswered attack is **never a critical** (`:229`, `:262`, `:466`), and `:397` builds a teaching moment on that generosity being deliberate. Direct conflict, in a file the draft's own header says is unchanged. Item 52 chose margin-exactly-5 on the incentive argument; that argument does not survive two Conditions that hand out an automatic critical for the same state.

**C3. Initiative.** `core_rules.md:38` lists DEX as governing initiative and `combat.md:11` is `1d12 \+ DEX`, against the draft's `5 \+ MIND` (`:411`). Known downstream work, listed here because the Attributes table is what a player reads at chargen, so it is the one that misleads first.

**C4. `basic_moves.md` collides in four places.** *Disengaging* is still a Major Action that suppresses Opportunity Attacks, against `:470`'s *"There is no third way and no free disengage."* *Shoving* and *Disarming* are contested Major Actions, now duplicated as free, uncontested Openings. And *Feint* is a Minor Action Manipulate check against static Insight - **an entirely different mechanic sharing a name with the draft's attack type**, which is the one that will actually confuse a table rather than merely duplicating.

**C5. Grappling is absent from the chapter entirely.** It is a Major Action in `basic_moves.md` that applies **Restrained** - a Condition the draft *does* rule on, at `:465`. So the chapter rules on the output of a mechanic it does not mention, and never says whether a Grapple costs a Tempo Die, how it interacts with a declared attack sequence, or whether the escape check still exists. `Weighted Chain`'s grapple-at-Reach hangs off the same gap (see B10).

---

### A - ambiguities a table hits in the first session

**A1. The declaration does not name targets.** `:198` - *"Say how many attacks you are making, pay that many Tempo Dice, and name a type for each."* No target is declared, so the commitment the chapter calls *"the whole of the cost"* (`:202`) is much softer than the text claims: you may swing, watch the first enemy drop, and aim the remainder elsewhere. If targets *are* meant to be fixed, the chapter also needs a ruling for an attack whose target dies or leaves Distance before its place in the sequence - refunded, wasted, or retargeted. This is the single most likely thing to be house-ruled at a table, in either direction.

**A2. Riposte's cancellation has three unanswered cases.** `:276`. (a) Who chooses which of the remaining attacks is cancelled, the riposter or the attacker? (b) What if the person riposted has no declared sequence at all - it was an Opportunity Attack on somebody else's turn - does it eat a future attack or simply nothing? (c) An attacker who wins by 5 on their own turn takes Riposte for a bonus plain attack, but the cancellation clause is dead weight for them, so the same menu entry is worth materially different amounts to the two sides. Open question 11 already suspects Riposte is simply correct every time; (c) is a reason it might be correct for only one of them.

**A3. Riposte chains are not closed off.** `:283` bars *plain attacks* from taking Openings. It does not bar the person **defending against** a plain attack from taking one. So: A attacks, D parries and wins by 5, D ripostes, A parries and wins by 5, A ripostes, and so on for as long as either side has dice. One sentence closes it - or explicitly allows it, which is a defensible and rather good outcome, but it should be a decision.

**A4. Can a plain attack crit?** `:206` bars Openings only; `:96` grants the margin-10 critical to *"either"*. An Opportunity Attack that wins by 12 - does it roll damage twice?

**A5. A defender winning by 10\+ has nothing to double.** `:96` and `:270` say *"roll damage twice and take the higher"*, while `:99` says winning a defence deals no damage. The intent is presumably that the Riposte taken as the Opening is the critical, but the Riposte is a separate contest with its own margin. As written the top tier of the chapter's own reward ladder is a null result for half the people who reach it.

**A6. Shock's trigger is stated two ways in one section.** `:297` reads *"Every blow that **lands**"*; `:299` reads *"any hit that **deals damage**."* Those come apart whenever AR absorbs the whole hit, which is common in the heavier half of the armour table - and the answer decides whether armour also protects you from the attrition spiral, which is a much larger question than the wording, given open question 19's finding that nothing in a fight holds plate in check. It also decides whether a winning **Feint** (`:186`, deals no damage) causes Shock and degrades armour.

**A7. The unanswered rule never says what the attack's type does.** Both worked examples assume a Measured that goes unanswered refunds its die (`:373`, `:391`), but the rule reads *"**If you win**, the die returns"* (`:188`) and an unanswered attack has no contest to win. The same gap covers a Feint's Off-Balance and a Press's `\+2`. **The examples are currently the only place this is resolved**, which means the rule is being carried by the fiction of two fights.

**A8. Does Press's `\-2` stack with itself?** `:187` - *"Until the start of your next turn, every defence roll you make takes `\-2`."* Declaring three Presses is either `\-2` or `\-6`, and that is the difference between an aggressive sequence and an unplayable one.

**A9. Emptying your pool makes you immune to Shock.** Shock takes a die you have, so the fighter who declared everything has none left and a mid-turn Riposte costs them nothing, while the cautious fighter who kept two back loses one. **The chapter's compounding mechanic exempts exactly the play the chapter is trying to price.** Probably not decisive - item 41 measured dumping as bad at party scale for other reasons - but the incentive points backwards and it is free to fix.

**A10. Called Shot is unbounded and undated.** `:277` - *"a Condition appropriate to what you named."* `wounds_and_survival.md`'s table includes **Paralyzed**, **Stunned**, **Petrified** and **Unconscious**. There is no permitted list, no duration, no save, no cap on stacking them, and the Opening it rides on fires on roughly a quarter to a third of won contests, free. It needs a short menu with durations attached. Two knock-ons: **"Slowed" is not a Condition** in that file, and it is one of the three examples `:277` gives; and see A11.

**A11. Example 2 ignores its own Called Shot.** Beren blinds Kadir at `:391`. On Kadir's turn at `:397` he Presses, and the example rolls two `1d12` and takes the higher. **Blinded** imposes Disadvantage on attack rolls, which under `:40` cancels Press's Advantage - the roll should be flat. As printed, the chapter's most carefully worked example demonstrates the interaction being forgotten. Separately and larger: **Blinded** *"automatically fails any check or Ward that relies on sight"*, which is a much sharper question about whether a Parry is possible at all than the attack-roll clause the example was thinking about.

**A12. Ranged combat has no roll, no die cost and no rate.** `:485` gives a Shot DC and never says what is rolled against it - `1d12 \+ Skill`, per `combat.md`, or the Tempo Die, per everything else in this chapter. It also never says whether shooting costs a Tempo Die, or how many shots a turn. As the draft stands an archer spends nothing from the pool and therefore walks into melee with **more defensive dice than a swordsman**, which is a real asymmetry that should be deliberate rather than implied by omission. And `:479`'s *"Yes, against melee, **if armed**"* does not say whether a bow is a legal parrying implement.

Open question 10 already records that the Shot DC's numbers are unmeasured. This is the separate problem that the *procedure* is missing.

**A13. Conditions and the pool want one general clause.** **Stunned** (*"only one action of any type"*) predates the pool: does it cap Tempo Dice, or only actions? **Incapacitated** is handled at `:466`; Stunned is not. And several Conditions - Poisoned, Frightened, Blinded - impose Disadvantage on *attack rolls* only, so as written a poisoned fighter Parries perfectly. One sentence stating that a Condition touching attack rolls does not touch your Parry unless it says so settles the whole table at once, instead of leaving fifteen Conditions to be re-read against a resolution system none of them was written for.

---

### N - minor

- **N1. `:52`, STR 0 gives a flat `1`.** `1d(Tempo Die)` does not parse for that row; the fighter's rolls become fully deterministic, so an opponent knows the exact number to beat; and Press buys nothing but its `\+2` damage. STR 0 is reachable - `core_rules.md:36` runs the scale from 0.
- **N2. `:338`, *"every hit that lands costs 1"*.** War Maul degrades 2, and every firearm degrades 2 (`weapons.md`, Armor-Piercing). The exception line is missing.
- **N3. `:516`, the hands table has no row for Whip, Weighted Chain or Lance.** The One-handed row reads *"Every Close and Middle weapon"*, which excludes all three now that the draft puts them in Far. Lance is additionally one-handed mounted and Two-Handed on foot, and mounted combat is not addressed.
- **N4. `:35`, "Weapon Skill" is not a Skill.** There are six - Cleaving Blades, Two-Handed Blades, Fencing Blades, Hafted \& Polearms, Daggers \& Wrestling, plus Ranged and Thrown. Worth one clarifying clause, and it interacts directly with B4. Same at `:36`: the damage formula says *"Attribute"* where item 39 settled it as the weapon's **governing** Attribute, which the chapter never states.
- **N5. Units.** The draft is in squares; `basic_moves.md` shoves *"5 ft"*, weapon ranges are in feet, `traveling.md` and Speed are in feet. Not a rules problem - the largest remaining mechanical sweep. Related: `:491`'s *"the first **range increment**"* is not a term `weapons.md` uses; it prints normal/max as `80/160 ft`.
- **N6. `:194` is factually wrong.** *"Its refunded die comes back to a sequence that is already fixed, so **it can only ever fund defence**."* A returned die can also pay for an Opportunity Attack or a Feat cost (`:65`). Small, but it is a load-bearing sentence about why Measured is the safe attack.
- **N7. `combat.md`'s Held Action and Ready Volley are Reaction-priced** and have no home in a chapter with no Reactions. Ready Volley in particular is the ranged game's only tactical option, and item 53's downstream note converts Reactions to Tempo Dice one-for-one without saying whether a ranged character may spend dice at all (see A12).
- **N8. `:539`** duplicates the row above it and slightly implies the first attack is free.

---

### What was checked and is correct

Recorded so the next read does not redo it.

- **Both worked examples' arithmetic is right**, every roll, every pool count, in both fights - the only defect found in them is A11's forgotten Condition, and B1's rule/example conflict, which is the rule's fault rather than the example's.
- **The four-Band table covers every melee weapon in `weapons.md`** with none missing and none listed twice, including Shield Bash and Unarmed.
- **The Penalty bands match the armour table row for row** - AR 1-4 at `\-1`, 5-7 at `\-2`, 8-10 at `\-3`, correct for all eight entries. The bands run to AR 10 against a table topping out at 8, which is right: natural armour reaches higher.
- **Press's `\-2` persisting into the next combatant's turn is correctly worked in Example 2** (`:397`), which is the fiddliest timing in the chapter.
- **Prone's ranged clause is correctly re-homed** to the Shot DC table rather than double-counted (`:464`).
- **The Opening menu, Shock, the declaration rule and the Distance modifier are internally consistent** with items 48, 51 and 52 as adopted. No adopted decision in this log was found to have been transcribed into the draft incorrectly.

### Where this leaves the merge

**B2, B6 and C1 are live-file edits this chapter creates**, not conversions it inherits, and none of the three is in item 53's downstream checklist. Add them.

**B1, A6, A7 and A10 are drafting faults in rules that are otherwise settled** - the decision exists, the sentence does not carry it. They are the cheapest fixes on this list and they are also the ones most likely to be discovered at a table rather than at a desk.

**B4 is the one to look at first.** It is not a wording problem: the off-hand shield rules as written undo the Measure Band system, which is the part of the chapter carrying the most weight per rule and the part item 51 spent an entire item restoring.

### Not measured

**Nothing in this item.** No simulation was run and `tools/tempo_sim.py` was not touched. Several findings have obvious balance consequences - B8's crit thresholds, B9's Mythic pool, A9's Shock exemption - and none of them has a number attached. By item 50's law, do not cite one.

---

## 55. Every finding in item 54 is closed. The draft is finished as a document *(2026-08-22)*

> **This item disposes of item 54's list, ID by ID.** Item 54 recorded what was wrong with `exchange_draft.md`; this one records what was done about each thing and why. **Where the two disagree, this item wins** - item 54 is now history rather than a worklist. What remains open after this is tuning (the surviving Open questions in item 53) and the merge itself, not the document.

**Four of the thirty-six were design calls rather than drafting faults**, and they were put to the author rather than settled from precedent: the target number for Arcane Spell Attacks (B2), the whole ranged procedure (A12), whether the declaration names targets (A1), and how weapon Critical ranges convert (B8). Three more were decided the same way because they set a direction rather than closing a hole: Shock's trigger (A6), the Breastplate (B6), and the Mythic pool (B9). **Every other finding was closed from a decision this log had already made**; where one was not, that is said below.

### Nothing here was simulated

**`tools/tempo_sim.py` was not run and not touched.** Item 50's law applies: none of the numbers introduced or moved in this item has a measurement behind it. **Six of them have obvious balance consequences and are listed at the end of this item** so that the first person to point a tool at this chapter knows where to point it.

---

### The seven decisions

**B2. Spell Attacks resolve against the Shot DC.** `1d12 \+ Spell Modifier` vs. the table in [There is no defence against a ranged attack], crit at a margin of 10 rather than on a natural 12. Chosen over making them Parryable and over folding them into Overcomes.

The reasoning is that the Shot DC is not an archery rule, it is a rule about **effects you cannot answer at Measure**, and a hurled bolt of flame is exactly that. It also costs nothing: the table already exists, it is keyed to the map rather than to a sheet, and it leaves Spell Overcomes and the Petition Roll untouched. Making spells Parryable was rejected for the opposite reason - it would have handed swordsmen a defence against casters that archers do not get, and let a spell take Openings.

**A12. A shot costs 1 Tempo Die and rolls `1d(Tempo Die) \+ Ranged or Thrown Skill`.** Declared, targeted and paid in the same sequence as a melee attack; the rate limiter is the weapon's Reload property, not a rule in this chapter. **The alternative on the table was `1d12 \+ Skill` for the same die cost**, keeping marksmanship off STR; it was not taken.

**That means STR now sizes the ranged die too, and the chapter argues the point rather than hiding it:** the shot and the swing are the same body doing the same work, and DEX keeps the archer - it is the number of shots, and it is ranged damage, which is DEX-governed for every missile weapon already. **A quick, weak archer is a fast shooter who does not shoot hard**, which is the same shape the melee table gives a quick, weak swordsman.

Two things fall out and both are wanted. **An archer who empties the quiver meets the charge with the same nothing a swordsman does**, which closes item 54's asymmetry at the root instead of taxing it. And **a bow, crossbow or long gun is not a parrying implement** - most are Two-Handed, so closing on a shooter is now the strongest counter to one, which is where that answer belongs.

**A1. Targets are declared with the sequence, and only a dead or departed target may be swapped.** If a declared target drops or leaves Distance before its attack comes up, that attack may be redirected to any other enemy it could legally reach; the count, the types and the dice never move.

The commitment item 48 bought was supposed to be *"the whole of the cost"*, and without targets it was only a commitment to how many dice you spend. **The exemption exists so that the punishment does not fall on killing well** - overkill on a corpse is a fiction problem, not a budget one, and the version that wastes the attack was declined for that reason.

**B8. The Critical column converts to a margin threshold, anchored so that `\-` and 11-12 both sit at 10.** 10-12 becomes a margin of 9; 9-12 becomes 8. Feats that widen a range lower the threshold by 1 per step from wherever the weapon already sits, **and nothing goes below 7.**

**Two points of spread across the whole table instead of three**, and the two most common rungs collapse into the chapter's own baseline, which is the point: a Longsword needs no property at all. The naive one-per-step conversion put a Dagger at margin 7 against an Opening threshold of 5, which - as item 54 said - is a structural change dressed as a weapon perk. **The floor of 7 is there so no future Feat can walk a critical down onto the Opening.**

The cost is that `\-` and 11-12 now mean the same thing, so the Critical column as published loses a rung. **At merge it should be rewritten as a property rather than a column** - a `Keen (9)` / `Keen (8)` line on the eight or so weapons that have one - since two thirds of the table would otherwise carry a value that does nothing.

**A6. Shock fires on every attack that lands, wounded or not.** A blow whose damage AR eats entirely still costs a Tempo Die and still costs 1 durability. **Armour protects your Wounds; it never protects your tempo.**

The alternative - Shock only on a blow that gets past AR - was the more thematic reading and was declined because of what it stacks. Open question 19 already records that nothing inside a fight holds plate in check; giving plate a second, quieter benefit against the chapter's own compounding mechanic would have made the man in harness immune to the spiral as well as to the damage. **One axis, and it is AR.**

**A winning Feint is the single exception.** It deals no damage, takes no die, and degrades no armour: it takes the position instead. That is stated in three places because it is the kind of thing a table will rule the other way by reflex.

**B6. Rigid armour loses no durability to a blow it absorbs entirely.** Flexible armour loses 1 to every hit that lands; Rigid loses 1 only when the blow got through. Chosen over repricing the Breastplate and over deleting the Brigandine.

**This is the first thing the Rigid/Flexible label has ever done inside a fight** - the draft previously said, in as many words, that the split changed nothing. It fixes the Breastplate by giving it a reason to exist next to a Brigandine at the same AR 6 (a coat of plates is cut apart doing a job a cuirass shrugs off) and it pairs with a drawback `combat.md` already imposes, where Rigid armour cannot be repaired in the field. **Rigid wears slowly and recovers slowly; Flexible wears fast and comes back after every rest.**

**It strengthens plate**, which open question 19 flagged as already unchecked in a fight, and it is unmeasured. That is the trade knowingly taken: the alternative fixes were a Slot here or a price there, neither of which makes the label mean anything.

**B9. A Mythic creature refills in full on its first count and regains 1 die on each later count.** Mythic (4) at DEX 3 opens with 4 dice and sees 7 across the round, against 16 under the old rule.

The old rule made the boss immune to the one thing the chapter measured as decisive. **The party's win condition is numbers** (open question 3), and a boss ought to be the hardest creature in the game to make numbers work against - not the one creature where the mechanic is switched off. Under the new rule Shock bites a Mythic creature, an emptied one eats unanswered blows and Openings like anybody else, and concentrating fire can strip it between counts. What Mythic still buys is refilling three more times than a PC does, which is a large advantage stated honestly.

---

### The rest of the B list

**B1. An Opportunity Attack is resolved at the Distance the attacker threatens** - Adjacent for Close and Middle, Reach for Long and Far. Not "the Distance the mover is leaving from", which forbade the chapter's own Example 1, and not "the nearer of the two", which needed a second clause to be legible.

**This version makes the threat zone and the roll measure the same thing**, which is what item 54 pointed out they were not doing: your threatened squares are the squares your weapon is good at, so a blow thrown across their edge is thrown at the range that made them yours. The threatening weapon is therefore never at a Distance penalty for an Opportunity Attack, in either direction of travel, and both of item 54's consequences vanish with the clause that caused them - a Close weapon can punish an entry, and a Middle weapon never swings at `\-2` inside its own zone. **What the crossing decides is what the mover can answer with**, which is the interesting half and the half Example 1 was always teaching.

**B3. A Buckler occupies the off hand like any other shield.** The *"does not occupy the hand for anything else"* line is gone, and with it the free `\+1` for a Greatsword build.

Its new distinguishing property is that it is fist-held rather than strapped: **it is the only shield you can keep on the hand while reloading, holding a torch, or working a lock.** That replaces `weapons.md`'s *"keeps full Guard at Short"*, which was written for a Measure rule this chapter deleted, and it is worth something to exactly the character who historically carried one without touching a single number in an Exchange.

**B4. A shield is a Close-Band implement, and its Guard and its blade are separated.**

- **Guard applies to every Parry you make while the shield is equipped**, whatever you actually parry with, at either Distance. That is the shield-wall spearman, and it is the reason Guard is still the largest number on any piece of gear here.
- **The shield as the thing doing the parrying works only at Adjacent**, at no Distance modifier, using **Daggers \& Wrestling** - the Skill that already swings a Shield Bash, which settles item 54's unaccounted-for Weapon Skill term. It cannot Parry at Reach at all.

**The failure item 54 was actually worried about is closed by the hands table rather than by this rule.** A halberdier who has been closed on cannot reach for a shield because a halberd takes both hands; three of the four Far weapons are Two-Handed. What a shield does rescue is the **Long** weapon's user - the spearman, the quarterstaff - and that is correct rather than a hole, since spear-and-shield is the formation the whole Band system is describing.

It also leaves the off-hand dagger a real choice rather than a strictly worse one: a quarter of the price, a blade that can Riposte with something that hurts, and throwable. The chapter says so plainly instead of arguing for the dagger on grounds that were no longer true.

**B5. Guard degrades when a Parry it added to is lost**, and is repaired with armour. That is the nearest surviving translation of `weapons.md`'s *"reduces a losing Oppose margin"*: the shield was in the way and the blow came through it anyway. It restores a rule that had quietly disappeared rather than being decided.

**The Pavise is not a wielded shield.** It carries no Guard in an Exchange and is portable cover on the map, which is what its Deployed rules always described. **That makes the in-Exchange Guard range `\+1` to `\+2`**, corrected in all four places the draft printed `\+3`.

**B7. Bare hands Parry only what is fought in the Close Band** - fists, a dagger, a knife, a shield rim. Not a broadsword, and no roll for trying.

Both readings item 54 found were defensible and both broke something: fists that parry anything collapse the caster's position, fists that parry nothing strand every wrestler who is not holding a knife. **The Band system already had the answer** - it is the one part of the chapter that says which implements meet which attacks - so Unarmed stays in the Close Band and simply behaves like a Close-Band implement on defence as well as offence. **A caster with empty hands can stop a knife and nothing longer**, which is a more honest sentence than the draft's *"cannot spend a Tempo Die on defence at all"* and costs the dagger paragraph nothing: 20 Crown still turns "no roll at all" into a bad one, against everything that matters.

**B10. The dead weapon properties are disposed of, and one weapon moved Band to do it.**

- **Whip and Weighted Chain move from Far to Long.** `weapons.md` says outright that neither can strike out to 2-3 squares, and Far's one benefit is striking past an intervening creature - so a Band that made them unusable Adjacent *and* handed them a polearm's privilege was wrong twice. At Long they sit with the quarterstaff and the spear, which is what they are. **Far is now four rigid polearms and nothing else**, and the strike-past clause reads as a property of the shaft rather than of the reach.
- **Chain Flail's "Bypasses STR Ward" becomes "Ignores Guard"** at merge. The STR Ward Oppose leg does not exist; a flail head coming over the rim of a shield is the same weapon doing the same thing against the defence this chapter actually has, and it makes an 80-Crown weapon worth its price again.
- **Deleted at merge: Lashing Reach, Guard and Control, Guard and Measure, and Weighted Chain's "can grapple at Reach."** The first three key to mechanics that are gone; the fourth is absorbed by Grappling now being an Opening, which is Adjacent by definition.

---

### The C list, and what it means for the live files

**C1. `core_rules.md` moves, not the draft.** Advantage does not stack, and Advantage and Disadvantage cancel wholesale whatever the count. Item 52's entire argument for keeping Off-Balance on the defender's die depends on the draft's version, and **Example 2 now turns on it**: a Blinded Kadir Presses and rolls flat, which is the clearest demonstration in the chapter of why the rule is worth changing a published file for.

**C2. The Paralyzed and Unconscious auto-crit clauses are cut** from `wounds_and_survival.md`, and the draft says so where it handles the helpless. A margin nobody contested is a margin of 5 - that is the whole of the unanswered rule, and it cannot hold with two Conditions handing out automatic criticals for the same state. Item 52 chose margin-exactly-5 on the incentive argument that a man who never resisted should not be cut down more thoroughly than one who did; these two clauses were the counterexample, so they go.

**C3. Initiative** stays known downstream work - `core_rules.md`'s Attributes table, `combat.md`, `positioning.md`, `bestiary_overview.md`, every stat block, the sheet.

**C4. `basic_moves.md` loses four entries.** *Disengaging* (there is no free disengage), *Shoving* and *Disarming* (both are Openings now), and *Feint* - the Minor Action Manipulate check against static Insight, which is an entirely different mechanic sharing a name with an attack type and is the one that would actually have confused a table.

**C5. Grappling is an Opening**, and the Major Action version in `basic_moves.md` goes with the other three. A Grappled creature is Restrained while you stay Adjacent and keep a hand on it; **breaking out costs a Major Action and 1 Tempo Die, `1d(Tempo Die) \+ Athletics` against `7 \+ the grappler's Daggers \& Wrestling`**, or any Opening taken against them.

**This is the only finding closed by adding a mechanic rather than by deleting or restating one**, and it was done that way because the alternative was a contested Major Action - a second resolution system inside a chapter that spent four items deleting the last one. As an Opening it costs no new economy, it fires off the same margin as everything else, and it puts the knife and the clinch on one Skill at one range, which is what Daggers \& Wrestling already is. **The fiction it produces is also better:** you do not walk up and try to wrestle a man in harness, you fight him until a blow goes well enough that he is inside your arms.

---

### The A list

Each of these was a sentence that did not carry a decision the log had already made. They are listed briefly because none of them changed the system.

- **A2. Riposte cancels the *next* attack still to come**, no choice involved. **If there is none left to cancel, nothing is cancelled and the swing still happens.** The asymmetry item 54 flagged as (c) is kept and stated in the chapter: the cancellation is dead weight to an attacker and live to a defender, and **defending well is meant to be the better half of that menu entry.**
- **A3 and A4. No Opening comes from a plain attack or from beating one, and neither side criticals on one.** One clause closes the Riposte chain, and it closes it by principle rather than by exception: Openings and criticals are what committed acts pay out.
- **A5. A defender's margin-10 critical is the Riposte's damage**, rolled twice. Said in the outcome table where the problem was, rather than in a footnote.
- **A7. An unanswered attack counts as won at a margin of exactly 5 for every purpose the chapter has** - damage, Shock, the Opening, and the attack's own type. A Measured refunds, a Feint applies Off-Balance, a Press adds its `\+2`. **The examples were carrying this rule; now the rule carries the examples.**
- **A8. Press's `\-2` does not stack** with itself.
- **A9. Shock against an empty pool carries one die into the next turn**, and never more than one however many blows land. That removes the exemption the chapter was accidentally granting to exactly the play it is trying to price, and the cap keeps it from becoming a death spiral nobody measured.
- **A10. Called Shot is a fixed four-item menu** - Blinded, Deafened, Bleeding, or Speed halved - with durations attached (end of your next turn, except Bleeding, which runs by its own entry). **Paralyzed, Stunned, Petrified and Unconscious are never available**, and the same Called Shot does not stack with itself. "Slowed", which was never a Condition, is gone. The rule is now that nothing free and repeatable removes a character from a fight; that is what damage, Wounds and Coup de Grace are for.
- **A11. Example 2 is reworked** so the Called Shot it inflicts actually applies. Kadir is Blinded, his Press's Advantage and Blinded's Disadvantage cancel, and he rolls one flat `1d12`. **The example is stronger for it** - it now ends on a whole Major Action's aggression being deleted by one Opening, which is the best argument in the chapter for what the menu is worth.
- **A13. One clause settles the Conditions table:** a Condition that imposes Disadvantage on *attack rolls* does not touch your Parry unless it says so. **Three things do and all three say so** - Off-Balance, Blinded, and your own Press. **Stunned** caps you at one action and refills your pool to half, rounded down. Blinded's automatic-failure clause does not reach a Parry, which is neither a check nor a Ward.

### The N list

All eight closed. **N1:** STR 0 rolls `1d4` at Disadvantage rather than a flat 1, so no opponent reads an exact number off the sheet. **N2:** War Maul and firearms degrade armour by 2. **N3:** the hands table gains Whip, Weighted Chain and a Lance row (one-handed mounted, Two-Handed and Chargeless on foot). **N4:** "Weapon Skill" now names the five melee Skills, and Damage names the weapon's *governing* Attribute. **N5:** "first range increment" becomes "the weapon's normal range", matching `weapons.md`'s `80/160 ft`; the wider feet-to-squares sweep stays merge work. **N6:** the Measured sentence is corrected - a refunded die cannot buy another attack that turn, but it can buy a Parry, an Opportunity Attack, or a Feat cost. **N7:** Held Action and Ready Volley become **Holding an attack** - declared and paid in your sequence, resolved as a plain attack on a named trigger, lost if the trigger never comes, one at a time. **N8:** the duplicated cost row is gone.

---

### What the merge needs that item 53's checklist does not have

Item 54 added B2, B6 and C1. **This item adds seven more**, all created by decisions above rather than inherited:

- **`weapons.md`** - the Critical column becomes a `Keen (9)` / `Keen (8)` property on the few weapons that have one; Chain Flail's property becomes **Ignores Guard**; **Lashing Reach**, **Guard and Control** and **Guard and Measure** are deleted, as is Weighted Chain's grapple clause; **Whip and Weighted Chain move to the Long Band**; the **Buckler**'s property is rewritten; the **Pavise** loses its Guard rating in favour of its cover rules; and **Shield Durability** is rewritten around a lost Parry.
- **`armor.md`** - carries the **Rigid does not wear when it wins** rule, which is a behaviour change to armour and not just a Penalty column swap.
- **`wounds_and_survival.md`** - the **Paralyzed** and **Unconscious** auto-crit clauses are cut (C2).
- **`magic_overview.md`, `aeromancy.md`, `geomancy.md`, `hydromancy.md`** - *"vs. target's Evasion"* becomes *"vs. the Shot DC"*, and Spell Attacks crit on a margin of 10 rather than a natural 12 (B2).
- **`basic_moves.md`** - **Grappling** is deleted along with Disengaging, Shoving and Disarming (C5).
- **`combat.md`** - Held Action and Ready Volley become **Holding an attack** (N7).
- **`martial_feats.md`** - on top of item 53's two sweeps, every Feat that widens a crit range converts against the new anchor (`\-` and 11-12 are both baseline), and nothing may take a threshold below 7.

### Six things to point a tool at, in order

**None of these has a number.** They are listed in the order a simulator would find them cheapest to answer.

1. **The Rigid absorb rule (B6)** - it strengthens the half of the armour ladder that open question 19 already says nothing checks. This is the one most likely to be wrong.
2. **The Mythic pool (B9)** - 7 dice a round against a four-PC party is a guess. The old rule was measured at nothing because it could not lose.
3. **Ranged on the Tempo Die (A12)** - the first mode in this chapter to spend the pool without ever being answered. Item 16's paid-defence rate is the number to watch.
4. **Crit thresholds (B8)** - two points of spread on a five-point ladder between Opening and critical.
5. **Shock's carry (A9)** - capped at one die precisely because nobody has measured what an uncapped version does.
6. **The Called Shot menu (A10)** - Blinded is now purchasable on a quarter to a third of won contests, and it costs an attacker their Press.

### Where this leaves the chapter

**`exchange_draft.md` is finished as a document.** Every contradiction, every dead option, every unruled case item 54 found is closed, and no finding was deferred. What is not finished is the tuning - **the surviving Open questions in item 53 are untouched by this item**, and they should be, because every one of them is a question about a number and nothing here was measured.

**The next piece of work is the merge**, against item 53's checklist plus item 54's three additions plus this item's seven. It is a large mechanical sweep across `core/`, and `core/bestiary/` still wants rebuilding rather than converting.

### Addendum: `DESIGN_GUIDE.md` is an eighth merge target, and it came from `exchange_review.md` *(same day)*

**Recovered while retiring `exchange_review.md`** (the 2026-08-17 outside read of the Cycle-era draft, deleted as stale). Four of that file's five concrete defects died with the system they were written against; **its defect D did not, and nothing in this log had it** - `DESIGN_GUIDE.md` is not named anywhere in items 31-55.

Two lines in that file reference mechanics this rework deletes:

- **`:81`** sanctions *"a Reaction-gated Strike already earned through a won Oppose exchange (maneuvers.md)"* as one of three legal ways a Feat may add lethality. **Oppose, Reactions and `maneuvers.md` are all gone**, and this is the guide's only *concrete* example of the rule - so the sentence that does the most work in that section currently points at nothing. It restates cleanly as **a Riposte taken as an Opening**, which is the same idea in this chapter's vocabulary: a free attack earned by winning decisively, not granted.
- **`:81` again and `:111`** price a Feat's bypass at *"a Reaction spent"*. The one-for-one conversion is **a Tempo Die spent**, and it is a better example than it was: the die is the only resource in the chapter, so "a real, matching cost of its own" now has exactly one currency.

**Also on `:81`:** *"expanding crit range (Deadly Critical)"* is sanctioned as written, and under item 55's **B8** a crit range is no longer a thing a Feat expands - it lowers a threshold, by 1 per step, floored at 7. The guideline survives; its example needs the new wording.

**Why this is worth an addendum rather than a silent fix at merge.** `DESIGN_GUIDE.md` is the file every future Feat, spell and item is measured against, and it is the one document in the repo that is *about* the reasoning rather than the rules - so a dangling reference in it decays differently from one in a chapter. A rule that points at a deleted mechanic gets caught the first time somebody plays it. A **guideline** that points at a deleted mechanic just quietly stops constraining anything, and the Feats written under it drift.

---

## 56. A fresh read against the live files after item 55 declared the draft finished. Five hard errors, one withdrawn finding, and four merge targets nobody had listed *(2026-08-22)*

> **Item 55 closed thirty-six findings and ended with "`exchange_draft.md` is finished as a document."** This item is a cold re-read of the draft against the files it actually depends on - `weapons.md`, `armor.md`, `wounds_and_survival.md`, `attributes_and_skills.md`, `carrying_and_resting.md`, `maneuvers.md`, `combat.md` - rather than against this log. **It found five hard errors, all now corrected in the draft**, six gaps still open, and four downstream files that neither item 53's checklist nor item 55's seven additions name.

**The pattern in all five is the same and worth naming:** every one of them is a place where the *prose* did not absorb a decision the *log* had already made correctly. Item 55's B4 knew that three of the four Far weapons are Two-Handed; the off-hand table still promised a Far weapon's user a Parry. A9 established Shock's carry; Example 2 demonstrated the opposite. **Nothing here is a design fault. They are drafting faults in the one place a drafting fault is most expensive - the worked examples and the flavour text, which are what a table actually reads.**

---

### The five errors, and what was done

**E1. Example 2 violated Shock's own carry rule.** Beren's fourth Measured lands on Kadir while Kadir sits at **0 dice** - the row says so. Under A9 that Shock carries, so Kadir refills to **2**, not 3. The draft said *"minus nothing: no Shock landed on him while he was empty"*, contradicted by the line directly above it.

**Corrected, and the correction cascades:** Kadir now declares one attack and keeps one, and his Press is paid from a pool of 2. **The fourth-Measured row now flags the carry at the moment it fires**, because Example 2 is the chapter's only demonstration of A9 and it was demonstrating the reverse.

**E2. The Riposte's cited example was unreachable.** *"If they have none left to cancel - it was an Opportunity Attack, or you turned aside the last of them."* An Opportunity Attack is a **plain attack**, and A3 established that no Opening comes from beating one - so a Riposte off an Opportunity Attack cannot occur, and the clause illustrated the rule with the one case the rule forbids.

**The correct second case was already written twenty lines below**, in the Openings commentary: an **attacker** who wins by 5 on their own turn has nothing to cancel, because the defender never declared a sequence. That is now what the clause says.

**E3. The Full Plate flavour claim was wrong at every STR, and inverted at the top of the ladder.** The draft said AR 8 *"turns a Longsword (`1d6 \+ 2 \+ STR`) about half the time and a Greatsword (`1d12 \+ STR`) rarely."* Computed against the real profiles:

| STR | Longsword 1H | Longsword 2H | Greatsword |
|:---:|:---:|:---:|:---:|
| 2 | 67% | 50% | 50% |
| 3 | 50% | 38% | 42% |
| 4 | 33% | 25% | **33%** |
| 5 | 17% | 12% | **25%** |

**The Greatsword is never rare** - 25% to 50% across the ladder - and from STR 4 up **plate turns it more often than a Longsword.** The sentence argued the reverse of what the numbers do.

**Rewritten around figures that hold, and it now carries the more interesting fact.** Against a flat subtraction, `1d8 \+ 2` beats `1d12` at every STR on the ladder, because **the `\+2` is on every swing and the extra die faces are not**. That is the opposite of what those two weapons do to an unarmoured man, and it is the clearest argument in the chapter for why AR is a real defence rather than a tax. **Steady damage beats a big die the moment armour is in the way.**

**E4. "Rigid armour cannot be repaired in the field" is a misstatement, and cited the wrong file.** `armor.md:129,146` restricts field repair only **once Rigid armour reaches 0 durability** - a cuirass at 3 of 6 repairs like anything else. The rule lives in `armor.md`, not `combat.md`, which the draft named.

**This matters to B6 and not only to the sentence.** B6's bargain was stated as *"rigid wears slowly and recovers slowly"*, and the second half is far narrower than that: Rigid recovers normally until it is destroyed, and then not at all. **The corrected pairing is "rigid wears slowly and fails hard; flexible wears fast and always comes back"** - which is a sharper trade than the one B6 thought it was buying, and still a real one.

**E5. The off-hand dagger promised a rescue it cannot deliver.** *"A **Far** weapon's user parries at all rather than not at all."* Every Far weapon is Two-Handed except a Lance on horseback, so there is no off hand to put the dagger in - **and the block quote in the same section says exactly that** (*"What neither of them can do is help a man holding a halberd"*). B4 had this right; the table row did not.

**Now states the opposite**, matching B4 and its own block quote.

**Two residual slips were caught while verifying the above.** The Beren passage said he spent *"his last die"* when he held three; and the E3 rewrite initially overclaimed that a Dagger can never scratch plate, which is true to STR 4 and false at STR 5 (1d4 \+ 5 gets 1 through a quarter of the time). Both fixed. **The second is a small lesson about this log's own habit:** a corrected number is still a number, and item 50's law applies to sentences written *while* fixing something as much as to the thing being fixed.

---

### One finding withdrawn: Guard does not degrade faster than it used to

**The first read of this sweep recorded a sixth error and it was wrong.** The claim was that the draft broadened Guard's wear: `weapons.md:318` degrades Guard *"each time it actually reduces a losing Oppose margin"*, which reads like a limiter, against the draft's *"whenever a Parry it added to is lost"*, which reads like every loss.

**`maneuvers.md:86` settles it against the claim.** Shield Guard applied **only when your Margin came out Minimized or Failed** - it was loss-mitigation added after the roll, never a bonus to it. So *"each time it reduces a losing margin"* already meant *every lost defence*, and the draft's wording preserves the rate exactly. **No change was made and none is needed.**

**What actually changed at B4 is different, deliberate, and worth measuring instead:** Guard moved from shrinking a loss to a flat bonus on every Parry, win or lose. That is strictly better for the shield-bearer - it now helps you *win* defences, which it never did - and it is unmeasured. **It belongs on item 55's six-things list; the wear rate does not.**

---

### Still open - six gaps the draft does not rule on

None of these is a contradiction. Each is a case a table hits and the chapter does not answer.

1. **Shield Cap stacking is unaddressed, and it breaks the stated Guard range.** `weapons.md:304` lets a creature with spare hands equip two shields and **add their Guard together**. Under B4's *"Guard applies to every Parry you make while the shield is equipped"*, an Alsahli with two Heater Shields carries **`\+4` on every Parry** - against a chapter that says the range is `\+1` to `\+2` and calls Guard the largest number on any piece of gear. **B5 recalculated that range by deleting the Pavise and never looked at the Cap.** The old Shield Durability rule also had a Cap clause (both counting shields degrade together, one past the cap does not) which the draft drops.
2. **The Wound Threshold table has no zero row.** It begins at 1 damage, so *"a blow that deals no damage at all after AR"* - the entire trigger for B6 - is never defined in the chapter that replaces the table defining it. `wounds_and_survival.md:31` implies it today. **One clause: damage of 0 or less inflicts no Wound.**
3. **Stunned refills your pool to "half its size."** *Size* is a defined term here - it is the STR column. The sentence reads as *half your die size*. **Say "half as many dice, rounded down."**
4. **Bows have no rate limit.** A12 made Reload the limiter, but `weapons.md:185-188` gives bows no Reload property at all. **A DEX 5 archer fires six undefendable longbow shots a turn; a crossbowman fires one.** That makes the bow strictly dominant within its own class, and the split is an artefact of the property table rather than a decision anybody made.
5. **Measured against a drained target is free.** Unanswered counts as won, and a won Measured refunds. So attacking a fighter with an empty pool costs the attacker nothing and returns them to full. Bounded by pool size per turn, since a refund cannot buy another attack - but **the spiral is steeper than Shock alone implies**, and nothing in the chapter says so.
6. **The Estoc moved Band without being told to.** `weapons.md:32,139` puts it in Medium beside the Rapier; the draft's **Long** band takes it while the Rapier stays in Middle. Defensible - it is a long two-handed thruster - but B10 announces only the Whip and Weighted Chain, and the Spear's Far-to-Long move is likewise only implied by *"Far is now four rigid polearms."* **Two Band changes are riding on an aside.**

---

### Four merge targets neither item 53 nor item 55 lists

- **`core/carrying_and_resting.md:9-17`** - a **Size to Measure Band** table on the old five-band scale, giving Small and Medium creatures a natural reach of **Medium**. The draft puts Unarmed in **Close**, and the two cannot both be right. Huge maps to **Far**, which would hand a giant's fists the strike-past-an-intervening-creature clause the draft reserves for *"four rigid polearms and nothing else."* **This file appears in no checklist in this log.**
- **`core/wounds_and_survival.md:31`** - *"A hit still degrades armor by 1 AR regardless of how much Wound damage it ends up dealing."* **B6 contradicts this outright.** Only that file's auto-crit clauses are on the C-list; this line is the one that actually conflicts with the new Rigid rule.
- **`templates/Home.md` and `templates/_Sidebar.md`** - `CLAUDE.md` requires both whenever a chapter is added, renamed or removed under `core/`, and this rework does all three. Both currently list Oppose and Measure Bands. **They are hand-edited in the wiki UI and the sync workflow will never catch them.**
- **`core/character/attributes_and_skills.md:20`** - defines DEX around *"Passive Evasion and the flat, untrained Evasion-leg of an Oppose roll."* Covered in spirit by item 17's *"referenced repo-wide"*, but this is the **definitional** occurrence and deserves naming.

**One smaller thing, pre-existing rather than caused by this rework:** `attributes_and_skills.md:48-49` leaves the **Greatsaber, War Maul and Greatclub** with no Skill - Two-Handed Blades lists only *"longswords, greatswords, and warblades"*, and Cleaving Blades scopes itself to *"every other **one-handed** melee weapon."* The table headers in `weapons.md` cover all three, so it is a prose gap only. It matters here because the draft's Terms table leans on *"whichever of the five melee Skills your weapon trains under"* being answerable.

---

### The draft is written in British English and the repo is not

| | `armour` | `armor` | `defence` | `defense` |
|:---|:---:|:---:|:---:|:---:|
| `core/` | 1 | **198** | 0 | **11** |
| `exchange_draft.md` | **27** | 13 | **30** | 0 |

**The draft is also internally mixed** - it prints "Armor Penalty" and an `| Armor |` column header inside prose about "armour." Global-replace to `armor` and `defense` before merge. It is the cheapest item on any of these lists and the most visible on a published wiki page.

---

### What this says about item 55's closing line

**"Finished as a document" was true of the rules and not of the prose.** Every mechanical decision item 55 made survived this read intact - B4, B6, A9, A3 and B10 were all *correct*, and four of the five errors were the chapter failing to say what those decisions already were. **The document was checked against this log, and this log was right. What had not been done was checking the document against itself and against the live files.**

**The practical lesson for the merge:** the worked examples are load-bearing. They are the only place the chapter demonstrates Shock's carry, the Riposte cancellation, and Advantage-Disadvantage cancelling, and one of the three was demonstrating the opposite of the rule. **Re-run both examples line by line after any number in this chapter moves**, the same way `tools/` gets re-run after a mechanic moves.

**Nothing in this item was simulated.** Item 50's law stands: E3's table is arithmetic over the damage expressions, not a fight.

---

## 57. Second sweep - the seams rather than the prose. Five contradictions with live files, and the Far Band is currently unfunded *(2026-08-22)*

> **Item 56 read the draft against itself and found drafting faults.** This item re-read it against the files it silently *changes*, which is a different question and turned out to be the more productive one. **Every finding below is a live rule the chapter contradicts without saying so** - not a sentence that came out wrong, but a downstream edit nobody has written down. Two of them are load-bearing: **G1 leaves the Far Band with no benefit at all**, and **G2 makes the Called Shot redundant.**

**The reason the first sweep missed these is worth recording.** Item 56 checked every number and every cross-reference the draft *makes*. These five are cases where the draft makes no reference at all - it simply assumes a rule that reads the other way in `core/`. **A silent assumption leaves no string to pull**, which is why the only way to find them was to read the live files forward rather than the draft backward.

---

### G1. Cover is binary in the live rules and graduated in this chapter, and the Far Band depends on the difference

**`positioning.md:75-81` gives Cover its own heading to deny exactly what this chapter assumes:**

> *"Cover in Ressam is a binary system - you either have it or you don't. **Cover:** Completely hidden behind solid obstruction. Cannot be targeted by attacks or most spells. **No Partial Cover:** Any exposure \= targetable."*

The draft assumes a graduated system in five places: the Shot DC table's **Partial cover `\+2`** and **Heavy cover `\+4`** rows, the Far weapon's *"they do not give Cover"* clause, *"put a body between you"* as one of the four answers to archery, and the Pavise as *"portable cover."*

**The consequence is larger than a table row.** Item 55's B10 settled that **Far is four rigid polearms and nothing else**, and that the Band's single compensation - the thing it is paid for having no answer once somebody is inside it - is striking past an intervening creature. **Under the live Cover rule an intervening creature gives nothing, so there is nothing to strike past.** A pike's entire justification is currently written against a rule that does not exist.

**`positioning.md`'s Cover section therefore needs rewriting, not converting**, and this is not covered by item 53's *"the Reach half of `positioning.md`"* - Cover is a different section of the same file. **Whether Ressam wants graduated cover at all is a real design question and should be decided rather than inherited**: the binary rule is deliberate and stated as such, and this chapter overturns it as a side effect of needing a Shot DC table.

### G2. A free Minor Action already hands out Blinded, and it beats the Called Shot that is supposed to be the rare version

**Item 55's A10 established the principle in as many words:** *"nothing free and repeatable hands out a Condition that removes a character from the fight - that is what damage, Wounds and Coup de Grace are for."* The Called Shot menu was built around it, and Blinded was priced at an **Opening**: a margin of 5 or better on a contest you had to win.

**`basic_moves.md:50-57` gives it away for nothing.** **Blind** - throwing dirt into an opponent's eyes - is a **Minor Action**, costs **no Tempo Die**, requires only a free hand, and inflicts Blinded on a contested DEX Ward.

**It is also the better version.** The Basic Move lasts *until the end of the target's next turn*; the Called Shot lasts *until the end of yours*. **So the free repeatable option has the longer duration**, and the earned one is strictly dominated. **Blind appears on no delete or convert list in this log.**

Three ways out, and the choice is a design call rather than a cleanup: delete it with the other four Basic Moves; charge it a Tempo Die like every other combat act; or cut its duration below the Called Shot's. **The middle option is the one that fits the chapter** - *"every act in this chapter costs a Tempo Die"* is the whole premise, and Blind is a combat act that currently sits outside it.

### G3. Shift Measure is dead, and it is not on the list

**`basic_moves.md:41-47` moves *"the shared measure between you and one engaged opponent one Measure Band, in or out."*** This chapter has no shared measure. Distance is a fact about squares, changed with a Move Action, and Bands are a property of the weapon in your hand rather than of the engagement. **C4 deletes Disengaging, Shoving, Disarming and Feint; Shift Measure belongs with them and was missed.**

**It is also in `combat.md:24`**, listed among the Minor Action examples (*"Sheathe weapon, drink potion, open door, Shift Measure"*). That line is on no checklist either.

**What falls out is a structural decision rather than a deletion.** After C4, C5 and this, `basic_moves.md` holds **three entries** - Dashing, Blind and Taunting - of which one is G2's problem. **Whether a three-entry file survives, or folds into `combat.md`, should be decided at merge**; item 53 says the chapter replaces *"most of"* that file, and the honest figure is closer to all of it.

### G4. The chapter rewrites five Conditions and the checklist records none of them

C2 cuts the **Paralyzed** and **Unconscious** auto-crit clauses, and item 17 notes **Restrained** was already edited. **Those are the only Condition changes any item in this log has recorded.** The draft makes five more:

| Condition | `wounds_and_survival.md` today | What the draft needs |
| :---- | :---- | :---- |
| **Off-Balance** | **does not exist** | **added to the table** - it is a Feint's whole payload and the Glossary already treats it as a Condition |
| **Blinded** | Disadvantage on attack rolls; **attacks against it have advantage** | adds **Disadvantage on Parries**, and is silent on whether the advantage half survives - if it does, a Blinded defender is penalised twice |
| **Prone** | standing costs **half** its maximum movement; ranged attacks against it have disadvantage | standing costs **your whole Move**; the ranged clause moves to the Shot DC table |
| **Stunned** | one action of any type, nothing further | **adds** *"your pool refills to half, rounded down"* |
| **Grappled** | ends if moved beyond the grappler's reach | **adds** *"or you are knocked Prone"* |

**`Incapacitated` also still enumerates "Reaction"** among the action types it blocks, which is the one-for-one rename item 17 already anticipated - but the other five are substantive, and **Off-Balance is an addition rather than an edit**, which is a category no checklist in this log currently has.

**Blinded is the one that needs a ruling rather than a transcription.** The draft says Disadvantage on Parries; the live entry says attacks against it have Advantage. **Both applying means a Blinded defender rolls at Disadvantage against a roll made at Advantage**, which is a far heavier condition than the draft's own gloss (*"you can still answer a blow you never saw, just badly"*) suggests.

### G5. `attributes_and_skills.md` needs three edits nobody has listed, on top of the Evasion one

C3 names *"`core_rules.md`'s Attributes table"* for the Initiative move. **`attributes_and_skills.md` has its own Attributes table and its own per-Attribute prose, and it is the definitional file for both.**

- **`:12`** gives **DEX** *"initiative"* in the governs column, and **`:20`** repeats it (*"sets your place in the initiative order"*). **MIND's row needs it added** - `:13` currently reads *"Intelligence, reasoning, mana pool"*, which is the file that has to carry Initiative's new home.
- **`:19`** says STR drives *"your Wound Threshold."* **The draft makes Wound Thresholds flat and identical for everybody** - *"Nothing about your Attributes changes this table"* - so this is a second, separate contradiction in the same file, and item 17 lists only `wounds_and_survival.md` for the threshold change.
- **`:20`**'s Evasion clause was already flagged in item 56's merge-target list; it is the same line as the Initiative one, so both are fixed in one pass.

---

### Minor

- **`:252` overstates the case against Evasion.** *"A trained attacker's worst possible swing already beat the best Evasion anybody could carry."* Against item 49's `Evasion \= DEX \- AP`, the best carryable score is 5 and a Skill 3 fighter's worst swing is 4. **The claim holds only at Weapon Skill 5.** It should go: the argument does not need it, because **the measured one-swing-in-sixteen figure (item 52) carries the whole point on its own** and is not an overstatement.
- **`:272` and `:611` both say a weaponless caster's *"pool is offence and a wrestler's defence."*** It is neither sentence's fault twice over: **spells cost Mana, not Tempo Dice**, so a caster's pool is **pure defence**. The chapter's own *"Who fights an Exchange"* table says so - Caster, *"Attacks in Exchanges: No."*
- **`:116` restates the five-foot grid** that `positioning.md:7` already declares for the whole book (*"every Speed, Reach, and Range value in this book is already denominated in that unit"*). Harmless duplication, but it should be decided which file owns the statement.
- **Speed units are mixed.** The Terms table says Speed is *"in squares"*; `carrying_and_resting.md` says *"Speed drops to 5 ft"* and every weapon range is in feet. Item 17 converts hexes to squares and does not mention feet.

---

### What this changes about the merge

**Item 56 concluded that item 55's decisions were all correct and only the prose lagged. That still holds - and this item does not.** G1 and G2 are not drafting faults. **They are two live rules that make a designed mechanic either worthless (the Far Band) or redundant (the Called Shot)**, and neither can be closed by a sweep across `core/` - both want a decision first.

**Order of operations, then:**

1. **Decide whether Ressam has graduated cover.** Everything else in G1 follows from it, and the Far Band cannot be evaluated - by a tool or a table - until it does.
2. **Decide what happens to Blind.** Charging it a Tempo Die is the answer that fits the chapter's premise; deleting it is the answer that fits A10's principle. Either closes it.
3. The rest - G3, G4, G5 and the minors - are mechanical, and belong on item 53's checklist alongside item 56's four.

**Nothing in this item was simulated either.** The Far Band's value and the Called Shot's rate are both on item 55's six-things list, and **both of those measurements are currently meaningless**, because one mechanic has no benefit to measure and the other has a free substitute nobody was modelling.

---

## 58. Binary Cover is the source of truth. The Far Band is repaid out of the intervening square instead, and Blind is deleted *(2026-08-22)*

> **Both of item 57's blocking decisions are made.** Cover stays binary exactly as `positioning.md` publishes it - **this item reverses item 57's G1, which said that file's Cover section needed rewriting; it does not.** The Far Band keeps striking past a body as its selling point, re-expressed so that it never touches Cover at all. **Blind is deleted** rather than repriced.

---

### The Far Band, repaid out of geometry rather than concealment

**The old clause was a no-op and that is why it read so well.** *"They do not give Cover"* is a true sentence about a rule under which nobody ever gave Cover, so the Far Band was being paid in a currency worth nothing. **Item 57 found the hole; this item fills it from the map instead of from the cover rules.**

**The fix is available for free in the Distance table.** Reach is defined as *"1 square between you"* - so at Reach there is **exactly one** square between the two combatants, always, and *"is it occupied?"* is a well-formed binary question with no concealment in it anywhere.

> **If a creature occupies that square - ally, enemy or otherwise - a Long weapon can make no roll at Reach across it: no attack, no Parry, no Opportunity Attack. A Far weapon makes all three as though the square were empty.**

**What makes this worth something is that it is a restriction on Long weapons first and a Far privilege second.** The old clause tried to hand Far a benefit against a baseline where nothing was blocked; there was no baseline to be better than. Now the second rank is genuinely closed to a spear, a longsword and a quarterstaff, and a pike walks through it. **The exemption is worth exactly what the restriction costs, which is the only way a Band can be paid for anything.**

**It is a line-of-attack rule and it is stated as one.** What stops the Long weapon is the haft, not the concealment: there is a body in the way and the weapon is not long enough to go round it. **Cover never enters the sentence**, so `positioning.md`'s Cover section survives untouched - and G1's downstream cost drops from *"rewrite a published section"* to *"nothing."*

**Close and Middle weapons never meet the rule at all**, since Adjacent has no square between it to occupy. **The rule exists only at Reach**, which is where the whole Band question lives.

### The symmetric half is the dangerous half, and it is deliberate

**A blocked fighter cannot Parry either.** That follows from a principle the chapter already states twice - *"Distance is a property of the thing in your hand, so it touches every roll that thing makes"* - and refusing it here would have made the Distance rules asymmetric for the first time.

**It also produces the sharpest thing in the chapter.** A pikeman in the second rank swings at a swordsman who **has no answer at all**: not a bad Parry, no Parry. Every blow lands, at a margin of 5, with an Opening. **The counters are all positional and every one costs a turn** - kill the body in the way, go round it, shoot him, or carry a polearm of your own - and the pikeman still pays a Tempo Die per swing and is still helpless the moment anyone reaches him.

**This is now the single most dangerous unmeasured number in the chapter**, ahead of everything on item 55's six-things list, because it is the only place where a fighter can be attacked repeatedly with no defence available and no Condition on them. **The chapter's one other unanswerable attack mode is archery**, and that one is justified by a distance you can close.

**The softer variant, if it proves too much:** block the *attack* only and let the blocked fighter Parry. That keeps Far as the only Band that can initiate past a body while removing the unanswerable loop. **It was not taken, because it breaks the symmetry the Distance rules are built on** - but it is the first dial to reach for, and it should be reached for on evidence rather than on nerve.

### What binary Cover costs the ranged rules, stated rather than hidden

**Both cover rows are gone from the Shot DC table.** Cover is now asked *before* the table: wholly behind solid obstruction means **no shot at all**, and anything less is exposed. There is no `\+2` for a low wall.

Three consequences, all of them now written into the chapter:

- **Half-measures buy nothing.** A low wall, a tree trunk and a friend standing in the way all set the same Shot DC as open ground. **This makes archery harsher, not gentler**, which is consistent with a chapter that already says an arrow cannot be answered.
- **"Put a body between you" is deleted as an answer to archers**, leaving two: break line of sight entirely, or close the distance. **A creature in the line never blocks a shot** - that clause belongs to Far weapons and to melee alone, and the chapter says so where the confusion would otherwise be.
- **The Pavise gets stronger and is now described honestly.** Deployed, it is solid obstruction: whoever is wholly behind it **cannot be shot at all.** That is `positioning.md`'s own rule rather than a new one, but under binary Cover it is a much larger effect than *"portable cover"* implied, and it is the one thing in the game that answers massed archery. It costs a Major Action and immobility, and it still carries no Guard in an Exchange.

**Spell Attacks follow the arrow**, as B2 established - answered by breaking line of sight and by distance, not by a body in the way.

### Blind is deleted

**Removed from `basic_moves.md` at merge, joining C4's list** - Disengaging, Shoving, Disarming, Feint and (per item 57's G3) Shift Measure.

**Repricing it at a Tempo Die was the other option and was not taken.** The objection to Blind was never only that it was free; it was that **a repeatable Minor Action was handing out the Called Shot's headline result at a longer duration**, and charging a die would have left a second, cheaper route to the same Condition sitting beside the Opening menu. **A10's principle is that nothing free and repeatable removes a character from a fight; the cleanest way to hold that line is for Blinded to have exactly one source.** It now does.

**`basic_moves.md` is down to two entries** - Dashing and Taunting. **Item 57's G3 called the survival of that file a decision to be made at merge; with Blind gone it is close to made.** Two Basic Moves is not a chapter, and both belong in `combat.md` beside the action economy they spend.

---

### What this does to the merge list

- **`positioning.md`** - Cover is **untouched**, reversing G1. The Reach half still goes.
- **`basic_moves.md`** - **Blind** joins the deletions. What remains is Dashing and Taunting, and the file should probably fold into `combat.md` rather than survive.
- **`weapons.md`** - the Far Band's strike-past clause, already on item 53's list, is reworded: it is an **intervening-square** rule, not a Cover rule, and it applies to Parries and Opportunity Attacks as well as attacks.

### Not measured

**Nothing in this item was simulated**, and one thing in it is a genuine outlier: **the unanswerable second-rank attack.** `tools/tempo_sim.py` currently models no map, no facing and no allied bodies, so it cannot see this rule at all - **which means the chapter's most dangerous new mechanic is invisible to the only tool that could price it.** Any simulator pointed at this chapter now needs a notion of occupied squares before its numbers mean anything about polearms.

---

## 59. Taunting is deleted and `basic_moves.md` with it. Dashing needs no new home because it already has two *(2026-08-22)*

> **`core/combat/basic_moves.md` is deleted outright at merge.** Item 58 left it holding two entries and called its survival "close to made"; this item makes it. **Taunting goes with Blind. Dashing does not move anywhere** - the file's last surviving rule turns out to be a third copy of something already published twice.

### Dashing is a duplicate, not a chapter

**"Move Dashing" was the wrong instruction to give me and the right instinct to have.** Checking where it would go found that it is already there:

- **`positioning.md:38`** - *"**Dash:** Major Action for additional movement equal to speed"*, sitting under **Movement in Combat**, which is where a movement rule belongs.
- **`combat.md:23`** - listed in the Major Action row of the action-economy table, beside Attack and cast spell.

**So `basic_moves.md`'s Dashing entry is a third statement of a rule with two homes already**, and deleting the file costs nothing. **One clause is worth rescuing before it goes:** `basic_moves.md` says the extra movement is *"equal to your current speed (after all modifiers, difficult terrain, etc.)"*, and neither of the other two says which speed. **That parenthetical should be folded into `positioning.md:38`** - it is the only content in the file that is not published elsewhere.

**This is the cleanest possible end for that chapter.** Every one of its nine entries is now accounted for: Disengaging, Shoving, Disarming and Feint deleted by C4; Grappling converted to an Opening by C5; Shift Measure deleted by item 57's G3; Blind deleted by item 58; **Taunting deleted here; Dashing already redundant.** Nothing is lost and nothing needs rehoming.

### Why Taunting goes

**It is Blind's problem in a different costume.** A free **Minor Action**, no Tempo Die, that imposes **Disadvantage on attack rolls** - a combat effect bought with nothing, in a chapter whose premise is *"every act in this chapter costs a Tempo Die."*

**It is also a second resolution system.** Taunting is a **Contested Check** against a Passive Skill, which is a different machine from the Exchange sitting next to it and doing combat work. Items 44 through 48 spent their length deleting exactly that - three named Reaction rolls collapsed into one Oppose, then one Parry - and C5 declined to close Grappling with a contested Major Action for the same reason. **Keeping a contested check for aggro while deleting one for wrestling would have been inconsistent.**

**And the economics moved underneath it.** Taunting was written for a game where drawing attacks onto yourself was a sacrifice. In this chapter **being attacked drains your Tempo Pool through Shock**, so pulling swings onto yourself is not only a cost you absorb, it is the mechanism by which you are taken apart. **A rule that forces attacks toward one fighter now interacts with the compounding spiral in a way nobody has modelled**, and it was not designed with that in mind because it predates the pool.

### What is lost, stated plainly

**Ressam now has no mechanical lever on target selection at all.** That matters more than it sounds, because the chapter itself says so: *"Who the enemy attacks - this is the largest dial in the chapter, and it is larger than the number of enemies."* **Taunting was the only thing on the player's side of that dial.** What remains is positioning, the Far Band's new blocking rule, and the GM's judgement - which the chapter already names as the difficulty setting.

**That is defensible and it is a real loss, not a tidy-up.** A defender or protector archetype has nothing to build toward at present.

**If one is wanted later, it should be a Feat written as an Opening**, not a Minor Action - earned on a margin of 5, paid for out of a won contest, on the same menu as Riposte and Shove. That is the shape every other special act in this chapter takes, and it is the shape a taunt should have taken from the start: **you do not announce that a man must fight you, you fight him until he has no better option.**

---

### What this adds to the merge list

- **`core/combat/basic_moves.md`** - **deleted.** Fold its Dash parenthetical into `positioning.md:38` first.
- **`core_rules.md:142`** - the *"Continued in"* line enumerates all nine Basic Moves and links the file. **Rewrite without it.**
- **`core_rules.md:133`** - the **Contested Check** definition gives four examples: *"Grapple, Disarm, Feint, Taunting."* **All four are deleted or converted by this rework** - Grapple and Disarm are Openings, Feint is an attack type, Taunting is gone. The mechanic may well survive for non-combat uses, but **every example it offers is dead**, and a definition illustrated entirely by deleted rules is item 55's `DESIGN_GUIDE.md` problem repeating: it stops constraining anything without ever looking broken.
- **`martial_feats.md:98,109`** - two Feats link `[[Basic Moves|basic_moves]]` for **Disarm/Shove** and **Grapple**. Both now point at Openings in this chapter instead.
- **`positioning.md:29`** - Shift Measure's Minor Action, already flagged in G3, links the same dead file.
- **`combat.md:23`** - the Major Action row lists **Disengage**, which this rework deletes ("there is no free disengage"); **`combat.md:64`** repeats it under Held Action. Neither was on a list.
- **`positioning.md:39`** - *"**Disengage:** Major Action to avoid Opportunity Attacks this turn"* - the same deletion, third occurrence.
- **`bestiary/universal.md:65`** - the Bandit's tactics note uses Taunting by name. The bestiary is being rebuilt regardless.
- **`templates/Home.md:7,47` and `templates/_Sidebar.md:36`** - both link Basic Moves; already flagged in item 56 as unlisted wiki nav work, now with a concrete deletion to carry.

### Not measured

**Nothing here needed measuring and nothing was.** The one open consequence is qualitative: **no player-side targeting lever exists any more**, and whether a party misses it is a table question rather than a simulator one.

---

## 60. Disengage is reinstated as a Major Action, the Contested Check branch turns out to have no surviving users, and the grapple escape DC is impossible at low STR *(2026-08-22)*

> **Two questions were put; the second one uncovered a third problem.** Disengage comes back, rewritten. The Contested Check examples come out of `core_rules.md` - and checking what would replace them showed that **the entire Passive Skill branch of that mechanic has no user left in the book once this rework lands.** While confirming that, the grapple-escape roll C5 introduced was computed for the first time and **it cannot be passed at all below STR 3.**

---

### Disengage comes back, priced in the one currency a losing fighter still has

**C4 deleted it on the reasoning "there is no free disengage." That reasoning was right and the deletion was wrong**, because it left the chapter giving advice it had made untrue.

> [Being outnumbered](#being-outnumbered) says, in bold: *"The answer to being outnumbered is a door, a corridor, a friend, or leaving."*

**Under C4, leaving was not an answer.** A man surrounded by four provokes four Opportunity Attacks on the way out, and he is running in the first place *because his pool is empty* - so he cannot Parry any of them. **Four unanswered attacks, each landing at a margin of 5 with an Opening, is not an exit. It is an execution**, and it is a worse outcome than standing still.

**The reinstated rule:**

> **Disengage: your Major Action. You move your full Speed this turn and provoke no Opportunity Attacks. It costs no Tempo Die.**

**Three reasons this is the right shape and not a softening:**

- **It is priced in the only thing a losing fighter still owns.** His pool is gone; his Major Action is not. **Charging a Tempo Die charges him something he does not have**, which is the same as charging nothing or forbidding it outright, depending on the round. The Major Action is the honest price, and it is a large one: it is every attack he would have made.
- **It costs no Tempo Die on purpose.** His guard stays intact the whole way out, which is what a fighting retreat *is*. A retreat that also strips your defence is not a retreat.
- **It does not make Break Away redundant, because they never compete for a slot.** Disengage is a Major Action, so it exists only on your own turn and only by deciding in advance not to fight. **Break Away is an Opening, taken on anybody's turn** - most often a defender's, mid-attack. **No Major Action can be spent on someone else's turn, and no Opening can be planned.** One is a decision; the other is an escape you earned while being hit.

**This shrinks the merge rather than growing it.** `combat.md:23`, `combat.md:64` and `positioning.md:39` all list Disengage today and were on item 59's deletion list. **All three now stay**, needing only a wording pass to match the version above.

---

### The Contested Check branch has no surviving users

**The instruction was to strip the combat examples from `core_rules.md:133` and keep the mechanic. Checking what should replace them found there is nothing to replace them with.**

`core_rules.md:131-134` splits Contested Checks into two shapes. **They are in very different health:**

- **Contested Ward** (`1d12 \+ X` vs a Passive Ward) is used everywhere and is untouched by this rework: `skill_feats.md:30`, `divine_feats.md:16`, `prestige_feats.md:163`, `daemons.md:27,29`, `khoridae.md:23`, `weapons.md:264`, `magic_overview.md:53,59`. **Healthy, keep as is** - with the one edit item 17 already records, since its own example list names *"an Attack Roll against Evasion"* and Evasion is deleted.
- **Contested Check** (`1d12 \+ Skill` vs a **Passive Skill**, `5 \+ Skill`) is used by **Grapple, Disarm, Feint, Taunting and Oppose, and by nothing else in the book.** Every one of those five is deleted or converted by this rework. **After the merge, the Passive Skill has zero callers.**

**So the honest edit is larger than removing four words.** The options are to delete the Passive Skill branch outright, or to keep it as a documented tool for the GM to reach for when a ruling needs one - **"rulings not rules" is the stated tone outside combat**, and a defined shape for *training against training* is worth having even with no rule currently invoking it.

**Recommendation: keep the branch, cut the examples to non-combat ones, and say plainly that no published rule uses it.** A mechanic held in reserve for adjudication is fine; a mechanic that *looks* like it has callers and does not is item 55's `DESIGN_GUIDE.md` failure again - **it stops constraining anything without ever looking broken.** Arm-wrestling, a haggle, a forced march of wills, picking a pocket against a wary mark: those are the examples that would be true.

**Not edited yet.** `core_rules.md` is a live file and this rework is still one merge pass rather than a trickle of edits; **say the word and it can be done now instead.**

---

### The grapple escape cannot be passed below STR 3

**C5 set it at `1d(Tempo Die) \+ Athletics` against `7 \+ the grappler's Daggers \& Wrestling`. Nobody computed it. Against an even matchup - Athletics 3, Daggers \& Wrestling 3, DC 10:**

| Escaper's Tempo Die | Chance to break free |
| :---- | :----: |
| `1d4` (STR 0-1) | **0%** |
| `1d6` (STR 2) | **0%** |
| `1d8` (STR 3) | 25% |
| `1d10` (STR 4) | 40% |
| `1d12` (STR 5) | 50% |

**The top two rows are not "unlikely", they are impossible.** `1d6 \+ 3` cannot reach 10 on any face of the die. **A STR 2 character grappled by an equal-skill opponent can never escape by rolling** - only by taking an Opening against them, which requires winning a contest by 5 while Restrained (attacks against you at Advantage, your own at Disadvantage).

**Two things went wrong at once, and both are worth naming:**

1. **The base moved from 5 to 7 without a derivation.** A Passive Skill is `5 \+ Skill` everywhere else in the book. C5 wrote `7 \+ Skill` and gave no reason.
2. **The die shrank at the same time.** The old contested check rolled `1d12`; this rolls a **Tempo Die**, which is `1d8` or smaller for most characters. **Raising the target while shrinking the die compounds** - the two changes were made in one sentence and neither was checked against the other.

**The fix is to put the base back to 5**, which restores the book's own Passive Skill shape and makes the even matchup `1d6 \+ 3` vs 8 - possible but poor, which is what escaping a grapple should be. **That is a recommendation, not a change:** it is a number, item 50's law applies, and it should be set deliberately rather than by me while writing it up. **What is not optional is that the two impossible rows go.**

---

### Merge list changes

- **`combat.md:23,64` and `positioning.md:39`** - **removed from item 59's deletion list.** Disengage survives; reword to the Major Action version above.
- **`core_rules.md:133`** - cut the four combat examples. Decide whether the **Passive Skill** branch is kept for adjudication or deleted; if kept, say that no published rule calls it.
- **`core_rules.md:134`** - *"an Attack Roll against Evasion"* and *"Passive Evasion, specifically"* both die with Evasion. Already implied by item 17, stated here.
- **`exchange_draft.md`** - the grapple escape DC is open, pending the call above.

---

## 61. The draft is read against itself, the simulator turns out to have been measuring a different system, and two deletions buy back 11 points of Attribute balance *(2026-08-23)*

> **Three passes in one session.** A read of the draft against itself and against the live files found five hard contradictions - all five were things the chapter had decided and then failed to say consistently. Six of them were put to the author and settled. **Then `tempo_sim.py` was diffed against the draft for the first time since the ranged rules existed, and six mechanics in it did not match** - including one, Shock's carry, that had never been modelled at all and turned out to be the single largest source of STR/DEX imbalance in the game. **Two rules were deleted as a result and one whole subsystem was rebuilt.** Item 60's open grapple DC is closed here.

---

### The document pass

**Five hard contradictions, every one of them the chapter failing to say what it had already decided:**

1. *"You can never begin your own turn empty"* was false at DEX 0, where a pool of 1 meets Shock's carry, Stunned's halving, or Ambushed. **Fixed with a refill floor of 1 die and Ambushed named as the sole exception.**
2. **Called Shot promised a defender something it cannot deliver.** It rides on a blow that lands and a won defense has no such blow. The Parry row advertised *"the full menu."* **Called Shot is now attacker-only and never off a Feint**, said in four places.
3. **Shock was never scoped to melee**, so read literally an arrow - undefendable by design - stripped a Tempo Die. See below; this became a real decision rather than a typo.
4. **The Greatsword/Longsword box claimed its result held "at every STR on the ladder."** It holds from STR 3 up and **inverts below it**: at STR 0-1 the Longsword is turned more often, at STR 2 they are level. Both readings are now printed, with the figures.
5. **No table row for STR 6 or DEX 6**, both reachable because `character_creation.md:74` exempts racial modifiers from the Attribute cap and nine races grant one. **STR 6+ stays `1d12`; DEX 6+ is `\+1` die per point.**

**Eight of item 56-57's open items were closed in the same pass**: Stunned's "half its size" (it now says *dice*, not size), the Wound table's missing zero row, the Shield Cap, Measured-against-a-drained-target stated outright, the Estoc and Spear Band moves announced rather than implied, Bands for the thrown weapons, Minor Action and Object Interaction added to the Terms table, and **the whole draft converted from British to American spelling** - 29 `armour`, 29 `defence`, plus `offence` and `armoured`.

---

### Six rulings put to the author

| | Ruling |
| :---- | :---- |
| **Plain attacks critical** | The clause *"neither side criticals on a plain attack"* was simply wrong. A plain attack is a real contest with a real margin. **A defender's critical rides on the Riposte and is lost if the Riposte is parried**; criticals do not stack. |
| **A held shot does not fire** | And **does not empty the weapon** until the trigger comes. The Major Action and the die buy readiness. If the trigger never comes the die is gone and the bolt is still in the groove. |
| **Mythic reads a count as a turn** | Shock treats each Mythic count as a full turn. With the carry deleted this reduces to: the refill is the refill, at every count. |
| **Two-handed fighters can Grapple** | It is **Ringen**. The sword stays in the fist - pommel, cross and haft are part of the hold. Every weapon in the chapter can Grapple. |
| **The absolutism goes** | *"Every act in this chapter costs a Tempo Die"* had too many exceptions to survive the ranged rework. Now scoped to attacks and defenses. |
| **Shield Cap: highest Guard only** | Guard applies to **every** Parry you make, and a rule that broad cannot also stack. Two Heater Shields would put `\+4` on every roll. **This overturns `weapons.md:304`'s two-shield stack.** |

---

### The grapple escape, resolved - closing item 60

**Item 60's table described a character who cannot exist.** Athletics is STR-governed and `core_rules.md:70` caps a Skill at its governing Attribute, so **Athletics 3 requires STR 3**, which is a `1d8`. The `1d4`-with-Athletics-3 rows were illegal builds.

**The real fault was worse than the impossible rows, and item 60 named it without following it through: STR was being counted twice**, once as the die and once as the Skill the die is added to. That is what made the curve run from 0% to 92% across the ladder.

> **Adopted: `1d12 \+ Athletics` against `7 \+ the grappler's Daggers \& Wrestling`. The Tempo Die is still paid; it is no longer rolled.**

**Breaking a hold is a Skill Check, not an act in an Exchange**, so it rolls the `1d12` every other check in the book rolls. The die is the cost, not the resolver - **the only place in the chapter where those two come apart**, and it is said so in the text. The base stays at **7** rather than reverting to the book's `5 \+ Skill`, deliberately: at 5 an even matchup escapes 67% of the time, at 7 it is a coin flip that has already cost the escaper their whole turn.

| Athletics | vs D\&W 0 | 1 | 2 | 3 | 4 | 5 |
| :---- | :----: | :----: | :----: | :----: | :----: | :----: |
| **0** | 50% | 42% | 33% | 25% | 17% | 8% |
| **3** | 75% | 67% | 58% | **50%** | 42% | 33% |
| **5** | 92% | 83% | 75% | 67% | 58% | 50% |

**No cell is impossible and the floor is 8%.** Item 60's requirement - that the two impossible rows go - is met without reverting the base.

---

### The simulator had drifted from the draft in six places

**Every figure `tempo_sim.py` printed before this session was measuring a system nobody had written.** Diffed against the draft, six mechanics did not match:

| | The sim did | The draft says |
| :---- | :---- | :---- |
| **Shock on absorbed blows** | Only fired when damage got through | *"whether the blow wounded them or their armor ate the whole of it"* |
| **Shock's carry** | **Not modelled at all** | Carried a die into the next refill |
| **The refill floor** | Not modelled | Never below 1 die |
| **Riposte** | Could not crit, and caused no Shock | Both |
| **Rigid zero-wear** | Only `RIGID_HALF_WEAR`, a *rejected* candidate | A blow absorbed entirely costs Rigid nothing |
| **Firearms' AR degrade** | 1 like everything else | **2** - found later, while pricing the reload rules |

**The Shock-on-absorbed one is the ugly one.** It silently exempted exactly the high-AR targets the rule exists to catch, and it had been quietly flattering heavy armour in every figure this log has printed since item 42.

**Rigid zero-wear, modelled for the first time, works but the draft names the wrong exemplar.** Frontliner survival, 4 PCs vs 3 peers, three seeds at n=4000: Brigandine 36.6%, **Breastplate 37.4%**, Half-Plate 41.2%, Full Plate 50.8%. The chapter calls this rule *"what separates a Breastplate from a Brigandine at the same AR 6."* **It separates them by 0.8 points for twice the price.** Its real beneficiary is Full Plate, where AR 8 absorbs enough blows for it to be worth about 6 points. **The prose should name Full Plate, or the Breastplate needs another reason to exist.**

---

### Shock's carry is deleted

**Modelled for the first time, it was worth 15 points of STR/DEX imbalance and nothing else.** Field spread over three seeds: **19.8 with the carry, 4.8 without.**

**The mechanism is that a flat one-die penalty is doubly regressive against pools that run from 2 to 6:**

| Build | Pool | Eats a carry | Cost as a share of its turn |
| :---- | :----: | :----: | :----: |
| S5/D1 | 2 | **83.8%** of turns | **41.9%** |
| S3/D3 | 4 | 49.4% | 12.3% |
| S1/D5 | 6 | 33.1% | 5.5% |

**The small pool eats it two and a half times as often and pays seven times as much for it** - about eight times the burden, landing on the build least able to absorb it. **And it bought nothing:** party win vs 3 peers 78.4% with against 76.5% without, mean fight length 1.99 against 1.98.

**Three ways to keep it were measured and all are worse than deleting it:** carry only for pools of 4+ (spread 8.0, and no fiction behind it), carry only if you emptied yourself attacking (10.6). **The second is the one that matches the rule's stated intent** - *"Emptying your pool is not a way to become weightless"* is about the voluntary dump - **and it still fails, because a two-die fighter has to dump to attack at all.** With pools this small no fixed one-die penalty can be made non-regressive.

**Worked Example 2 demonstrated the carry and had to be rewritten.** Kadir now refills to 3 and takes two attacks, and a second exchange was added so the example still shows something.

---

### Melee damage is STR, and only missiles keep DEX

**The Fencing Blades carve-out is deleted. Every melee weapon and every melee Skill adds STR.** Missiles keep DEX.

| | S5/D1 | S4/D2 | S3/D3 | S2/D4 | S1/D5 | STR to DEX gap |
| :---- | :----: | :----: | :----: | :----: | :----: | :----: |
| **Finesse adds DEX** (old) | 38.3 | 45.0 | 49.2 | 54.3 | 62.0 | **\+23.7** |
| **Everything adds STR** | 42.3 | 48.9 | 51.7 | 52.4 | 55.1 | **\+12.7** |

**11 points, bought by deleting a rule rather than adding one** - and it makes the chapter's own opening sentence literally true for the first time. **DEX is how many times you can act; STR is how well each act goes**, with nothing else attached to either.

**Missiles are the exception on purpose and the reasoning is load-bearing.** [Loading](#loading) already took rate of fire off DEX and handed it to the weapon. **Take DEX off missile damage as well and the archer's Attribute buys them nothing whatever.**

**The price is the Fencing Blades identity**, and it is real: a rapier duellist is now quick, and hits like the arm behind the blade. **`DESIGN_GUIDE.md` already says differentiation belongs in Feats**, and that is where it has to go.

---

### Ranged, rebuilt around Loading

**The old rule made the bow strictly dominant by accident** - `weapons.md` gives bows no Reload property, so a DEX 5 archer fired six undefendable shots a turn while a crossbowman fired one. That was an artefact of the property table, not a decision.

> **Fire costs 1 Tempo Die. Reloading costs your Minor Action *and* the weapon's dice. One Minor Action a round means two shots a turn, for everybody.**

| Weapon | Reload | Two shots costs | Reaches 2 shots at |
| :---- | :---- | :----: | :----: |
| **Thrown** | Object Interaction, no dice | 2 dice | DEX 2 |
| **Sling, every bow** | Minor \+ 1 die | 3 dice | DEX 3 |
| **Crossbows** | Minor \+ 2 dice | 4 dice | DEX 4 |
| **Every firearm** | Minor \+ 3 dice | 5 dice | DEX 5 |
| **Hackbut** | **2 Major Actions** | \- | never |

**The ladder is a staircase in DEX, and that is the whole of the differentiation.** Each class needs one more point to fire twice. Measured at standoff 2, each weapon jumps as it crosses its own threshold: Heavy Crossbow 47.4% at DEX 3 and **78.2% at DEX 4**; Arquebus 56.7% at DEX 4 and **90.7% at DEX 5**. **The Arquebus is a DEX 5 weapon and nothing else.**

**Shock is melee only. A shot never causes it.** Shock exists to tilt the *next* contest and a shot begins no contest to tilt. **It is also the one thing standing between the archer and the whole of a fight** - a shot cannot be answered at all, so a shot that stripped dice would empty a line's guard from complete safety.

**A brace of pistols is two loaded weapons, not one weapon reloaded** - an Object Interaction to draw the second, two shots for two dice, the Minor Action untouched. Which is what a brace was always for.

---

### Three candidates measured and rejected

**Do not re-propose these without reading the numbers.**

- **Escalating attack cost** - the Nth attack of a turn costing N dice, proposed to tax the pool directly. **It overshoots catastrophically**: full triangular cost puts the field 57 points to STR (S5/D1 71.4%, S1/D5 14.1%). Pools run 2 to 6, so a second attack at double price is enormous. **Even the gentlest rung that helps at all turns the field from a slope into a hump** where balanced builds beat both extremes by 8-14 points. Same shape of failure as item 35's escalating *roll* penalty.
- **Compressing the reload ladder to 0/1/1/2** - proposed because the ladder looks flat if you read the spend-everything row. **It hands the game to the Arquebus**: party win 86.3% at standoff 2 against a Longbow's 69.4%. **Reload 3 is the only thing restraining the biggest damage die in the game**, and reading the wrong row was the error - an archer with a sidearm keeps a die back, and on that row the ladder is the staircase above.
- **Major-Action reload for man-portable firearms** - the turn you reload is a turn you do not shoot. **A weapon on a two-turn cycle fires 2.5 times in a five-round fight against a bow's 8.5.** Party win 47.1% with an arquebus against **72.7% for simply bringing a fourth melee PC**; a pistol reads 30.3%. To break even at that rate a shot would need roughly **25 damage** and the Arquebus does 14. **No damage number rescues it inside a five-round fight.** Kept for the **Hackbut** alone, which is emplaced and crew-served and which no PC is expected to carry.

---

### Still open, and both structural

**STR/DEX is 12.7 points to DEX under optimal play** and no damage rule reaches the cause: **extra dice buy offence *and* defence, while die size only buys quality.** Everything that touches it directly costs more simplicity than it is worth. The field is at least a shallow monotone slope now, with no build below 42% or above 56%.

**An archer's worth swings about 45 points on closing time.** Party win with an archer in the line: **42.2% at standoff 0, 82.1% at standoff 3**, against an all-melee control of 72.7% that does not move at all. Break-even is around two rounds of shooting before contact. **The GM's choice of opening distance decides whether that PC exists** - a wider dial than any weapon choice, and second only to enemy targeting. The chapter already says archery is answered positionally; this says the archer's own value is positional to the same degree.

**A sidearm is worth 5-8 points** to a two-handed archer, real but smaller than the chapter's *"finished the instant the line reaches him"* implies.

---

### What this says about reading a simulator

**Item 50's law needs a companion, and this one cost a wrong number reported to the author mid-session.**

> **A policy table that pins every build at one setting is not a balance number.**

The STR/DEX field table pins both sides at hold 1. With Shock's carry deleted it reads a spread of **4.8** and looks solved. **Let both sides pick their best hold and the real figure is 12.7.** The file's own docstring already carried this warning for the turtle sweep and it caught the next reader anyway, because the warning was attached to the wrong table. **It is now printed above the STR/DEX table itself, at run time.**

**And the corollary, which is the larger lesson:** six mechanics in the simulator had silently stopped matching the draft. **Diff the model against the chapter before running it, not after a number looks wrong.**

---

### Merge list changes

- **`weapons.md`** - the **Reload** property rewritten to the ladder above; the **Reach** column rewritten to four Bands; **Shield Cap** replaced by highest-Guard-only; **Pavise**'s Guard 3; and the properties that no longer resolve: Chain Flail's *"Bypasses STR Ward"*, Weighted Chain's *"Can grapple at Reach"*, the Whip's **Trip**, Headbutt's surviving `1d12` roll, the contested Grapple row, the Buckler's Short-range clause. **Firearms need the AR-degrades-by-2 property the draft asserts and the table does not carry.**
- **`attributes_and_skills.md`** - line 20's *"Fencing Blades' melee damage"* dies with the carve-out. Initiative comes off DEX. **Athletics, Acrobatics and Daggers \& Wrestling all lose their Shove and Grapple roles** - the only surviving grapple check is the escape, and it is Athletics.
- **`wounds_and_survival.md`** - **Off-Balance** added to the Conditions table; Blinded reaching Parries; Grappled's end conditions; Prone's ranged clause; Incapacitated's Reaction language; both auto-crit clauses; the STR-keyed Wound Threshold table **and its "Design intent" paragraph**, which argues for a keying the flat table removes; and line 31's *"a hit still degrades armor by 1 AR regardless"*, which Rigid zero-wear and the firearm property both contradict.
- **`armor.md`** - Penalty column rebanded; the role table's Evasion and Buckler references.
- **`exchange_draft.md`** - **the grapple DC is closed.** Nothing in the document is open.

---

## 62. Merged. The draft is now `core/combat/exchange.md`, and the checklist from items 17, 53-61 is closed except where it was deliberately deferred *(2026-08-23)*

**`exchange_draft.md` is deleted.** Its contents are `core/combat/exchange.md`, converted rather than copied: British spellings normalized (`armour`/`defence` -> `armor`/`defense`, 27 and 30 occurrences), markdown-style `[Text](slug)` links converted to the repo's `[[Text|slug]]` wiki style, the `# The Exchange` H1 dropped (no `core/` chapter opens with one - the wiki takes its title from the filename), and the draft-era framing removed everywhere it said *"currently prints"*, *"on merge"* or *"this replaces"*.

**All internal anchors were validated** against the rendered heading slugs, and every `[[X|slug]]` target in `core/` was validated against the set of real basenames. Nothing in scope is broken. The only dangling links left in the repo are two `[[Oppose|maneuvers]]` references in `core/bestiary/`, which is deliberately out of scope - see below.

### What the chapter did not keep

Three sections of the draft were material the draft did not own, and they went to their owners rather than being printed twice:

- **The Armor Penalty band table and the full armor table** -> `armor.md`. This closes item 17's open question about ownership. The chapter keeps one line saying nothing in a fight reads Penalty and links out; `armor.md` carries the derivation, because its only surviving consumers (Acrobatics, Subterfuge, Spellcasting) are named there.
- **The Rigid-does-not-wear rule** -> `armor.md`'s Degradation section, as its own heading. It is a behavior change to armor, not a Penalty column swap, exactly as item 55's B6 said.
- **The Wound Threshold table** -> `wounds_and_survival.md`, replacing the STR-keyed one and its "Design intent" paragraph. The chapter restates the four bands as a quote and links out.

### Seven rulings the log had left open, put to the author and closed

1. **Blinded keeps the draft's Parry clause and loses the live entry's other half.** G4's warning stood up: Disadvantage on your Parries *and* Advantage on the attack answering them is a far heavier condition than the draft's own gloss, and Called Shot puts Blinded on a quarter to a third of won contests. The entry is now Disadvantage on attack rolls and on Parries, and nothing else.
2. **Size maps to Close / Close / Middle / Long** (`carrying_and_resting.md`), Small through Huge. **Nothing natural reaches Far** - which keeps the Far Band's intervening-square clause on four rigid polearms and nothing else, as the chapter claims. This closes the merge target item 56 found in a file no checklist had.
3. **The Contested Check branch survives with new non-combat examples and an explicit line saying no published rule calls it.** Item 60 found it had no users left; it is kept as an adjudication shape because the grapple escape DC (`7 \+ Skill`, one higher than a Passive Skill) is written against it and stops being legible without it.
4. **Weapon properties: convert where cheap, cut the rest.** Chain Flail's *"Bypasses STR Ward"* -> **Ignores Guard**. The Whip's **Trip**, the Weighted Chain's grapple clause, the Brawling table's contested **Grapple** row, and **Headbutt's Stun roll** are all cut - the last of those because handing out Stunned (half your pool) for free is exactly what the Called Shot menu refuses to do, and a free unarmed attack should not beat the menu.
5. **Reactive Casting is deleted** with the rest of `maneuvers.md`. The chapter's Casters section is already written as though it is gone, and reinstating it would be the one unpriced off-turn act in a chapter whose premise is that there are none. **`Casting Time: Reaction` is a different question and converted one-for-one** to *"Off-turn, 1 Tempo Die"* on the six spells and four racial Features that carried it - that is an action-economy label, not the deleted mechanic.
6. **`Evasion: N` stat lines become a Tempo Pool and a Parry**, derived from each entity's own Attributes: Necration's thrall, Blood-Rule's Fallen Thrall, Leadership's sample Cohort, and the three mounts in `traveling.md`. Shadowmancy's shadow instead gets an explicit *"no Tempo Pool, does not Parry."*
7. **Iron Path takes the literal conversion: you cannot Parry at all.** Its flavor text opens *"The warbands of Inggaz have no word for parry,"* and the Feat already trades away damage dice, criticals and Fencing Blades. Every attack against an Iron Path fighter lands with an Opening, and their armor is the whole of their defense.

### Feats, and the three that had to be rebuilt rather than reworded

**Deleted: Broken In.** A `\-1` to `\-3` axis cannot carry a repeatable Feat, and Penalty no longer prices anything worth a slot. Its references in `armor.md`, `magic_overview.md`, `prestige_feats.md` and `races/golems.md` were all rewritten to *"nothing reduces it."*

**Rebuilt, because their premise was deleted rather than renamed:**

- **Adaptive Guard** existed solely to break Stance's Funding lock. It now points at the thing that actually costs a defender a roll: once per round, Parry as though your weapon were **one Band nearer** the Distance you are being attacked from. A Long weapon answers Adjacent at 0; a Close weapon answers at Reach at `\-2` instead of not at all.
- **Half-Swording** granted Advantage on Disarm and Shove, which are now free Openings with no roll to have Advantage on. It instead moves a Two-Handed Blades weapon from **Long to Middle** while gripped - which is what half-swording is.
- **Shortened Grip** did the same job for polearms against the old Short Band; it now moves a Long or Far polearm to **Middle**, and explicitly loses the Far Band's intervening-square clause while shortened.

**Converted without argument:** Deadly Critical (crit range -> threshold, `\-1` per take, floored at 7), Joint Lock (the `\-2` moves onto the Athletics escape roll), Off-Hand Guard (Advantage on Parries **at Adjacent** - neither implement can answer a blow at Reach), Couched Lance (*"a Reach melee weapon"* -> Long or Far), Mounted Archery (the mount-movement Disadvantage -> a `\+2` Shot DC it ignores), Final Strike and Bulwark of Mind (Reaction -> Tempo Die), and Final Strike's surprise clause -> the two named rungs.

### The Called Shot collision, resolved by deletion

`combat.md` carried a **second** Called Shot - a Ready Volley rider with Legs/Arms/Head zones, an Aim Margin threshold, and a Head result that ignored AR outright. **Ready Volley, Held Action and that zone table are all deleted.** A held shot is [[Holding an attack|exchange]] like any other held attack, and Called Shot means one thing everywhere: an Opening off a fixed four-item menu. This was on no checklist in this log.

### What was deliberately left out of scope

**`core/bestiary/` and `tools/` were not touched, at the author's direction**, and neither was `templates/character/character_sheet.html` or the two hand-edited wiki nav pages. Item 17 was already right that the bestiary wants rebuilding rather than converting - it predates the 8-to-6 Attribute rework as well as this one - and there is no point calibrating it against a simulator that models Oppose. `TODO.md` now carries both as one entry with an explicit order: **rebuild the tooling first**, because item 58's intervening-square rule is invisible to any simulator without a notion of occupied squares, and there is no current weak-creature tier to calibrate a bestiary against until something can measure the Exchange.

**`bestiary_overview.md`'s Mythic Initiative section was the one exception** - it was converted, because leaving it would have been a direct contradiction the merge itself created (it said creatures *roll* initiative X times, and nobody rolls initiative any more). The chapter owns the core rule; that file keeps the stat-block-facing detail (Repetition, turns and effects) and the two now cross-link.

### Two pieces of pre-existing staleness fixed in passing

**`CLAUDE.md`'s `core/character/` bullet still described 8 Attributes, PRE and END, and a 24-Skill list with Melee/Block/Arcanism/Devotion** - all reversed by the 8-to-6 rework of 2026-08-11/12, which never updated the file. It now describes the real list. **`TODO.md`'s Stance section was deleted outright** (the mechanic is gone), and its bestiary/tooling entry was rewritten around the Exchange rather than around Parry/Block/Dodge.

### Nothing here was measured

**No simulation was run for this item, and none of the seven rulings above was tested.** Three of them move numbers a tool could see - the Blinded ruling, the Size-to-Band remap, and the three rebuilt Feats, all of which now shift a weapon a Band - and `TODO.md` records them as unverified alongside the tuning questions items 19 and 61 left open. The worked examples were re-read against the merged text and still hold, because no number inside the chapter moved; the only rules change at merge was Blinded, and neither example leans on the half that was dropped.

**The chapter is merged and unplaytested. That is the honest state of it.**

---

## 63. Criticals are deleted outright, and the weapons' Crit column becomes an Opening threshold *(2026-08-23)*

Found while pricing **Deadly Critical** during the downstream Feats pass, which could not be done without knowing how often a critical actually fires. The answer is that it does not.

### The measurement

Two methods, one of them exact rather than simulated.

**The margin ceiling is arithmetic.** Two fighters with the same Tempo Die and the same Skill can differ by at most **(die size \- 1)**. On a `1d8` that is 7, so a margin of 10 is not rare - it is impossible. Deadly Critical's step from 10 to 9 was worth **exactly zero** to every fighter below STR 4.

**Whole fights agree** (`tempo_sim.py`, 2,000 duels a cell, mixed types, hold 1, no Feats or shields; crits as a share of landed blows):

| Matchup | @10 | @9 | @8 | @7 | @6 |
| :---- | :----: | :----: | :----: | :----: | :----: |
| Quick v Quick (`1d6`) | 0.00% | 0.00% | 0.00% | 0.00% | 0.00% |
| Baseline v Baseline (`1d8`) | 0.00% | 0.00% | 0.00% | 0.30% | 0.85% |
| Strong v Strong (`1d12`) | 0.44% | 1.98% | 5.15% | 8.84% | 13.91% |

**Lowering the threshold does not rescue it**, which is what makes this structural. The suppressor is the chapter's own logic: **a roll high enough to win by a large margin is a roll the defender cannot beat, so a rational defender declines to spend a die on it - and an unanswered attack is pinned at exactly 5.** The better the swing, the more certain it is that nobody answers it. Strong (`1d12`) against Quick (`1d6`) - a mismatch of two full die steps - criticals **0.00%** of the time for precisely this reason.

**Missiles and spells fail the same test from the other end.** There is no defender to decline, but the Shot DC is low: a clear shot answers **DC 7**, so a critical needs a total of **17**, which no combination of Tempo Die and Skill in the game reaches except `1d12` with Skill 5 (8.3% of shots). A Spell Attack rolls a flat `1d12 \+ Spell Modifier` and reads the same line.

### The ruling

**There are no critical hits.** No margin pays double damage anywhere in Ressam - melee, missile, Spell Attack or Petition Roll. Damage is Weapon Damage \+ STR \- AR whether the contest was won by 5 or by 15.

**The weapons' Crit column becomes an Opening column**, on the reasoning that a sharp weapon should not hit harder but should *find the gap sooner*: `\-` is the standard **5**, and the sharper weapons read **4** or **3**. The mapping is one-for-one off the old column - 9 becomes 4, 8 becomes 3 - so Shortsword, Scimitar, Battle Axe, Rapier, Estoc and Knife open at 4, and Dagger, Stiletto and Throwing Axe at 3. **Deadly Critical becomes Deadly Opening** (`\-1`, floored at **3** rather than 7).

**This was the alternative to deleting the column**, and the reason it won: without it the **Scimitar** is a Shortsword that costs twice as much and deals less (1d6 against 1d6 \+ 1, same Band, both Light), and the **Rapier** is a Broadsword at 1.4x the price for 1d8 against 1d10. The Crit column was the only thing either weapon had.

**Bows, crossbows and firearms lose the column entirely** rather than carrying a dead number, because a shot takes no Opening at all. The **Shortbow** is the one loser here - its Crit 9 was a real edge and nothing replaces it. Thrown weapons keep a column, for the hand rather than the air. **Deadly Opening drops Ranged and Thrown from its weapon-group list** for the same reason, which removes it from archers entirely.

### What the new threshold is worth

Measured on the **defender's side only** - `tempo_sim` models the Riposte and nothing else on the Opening menu, so this is one half of the change and the attacker's half is unmeasured. Mirror duels, 4,000 a cell, rounds to a decision:

| Build | @5 | @4 | @3 |
| :---- | :----: | :----: | :----: |
| Quick (`1d6`, pool 5) | 1.71 | 1.55 | 1.37 |
| Baseline (`1d8`, pool 3) | 2.65 | 2.48 | 2.34 |
| Strong (`1d12`, pool 2) | 4.17 | 3.88 | 3.61 |

A 6-8% shorter fight at 4, 13-20% at 3, with **both** fighters carrying the sharp weapon. One character holding a Rapier gets about half of that. It is a real edge and not an explosive one.

### Everything the deletion touched

- **`exchange.md`** - the *Critical hits* section is replaced by *There are no critical hits* (which keeps the reasoning above, because players will look for the rule) and *Sharp weapons open sooner*. The at-a-glance table loses its `10\+` row; the unanswered rule, the helpless section, the plain-attack rule, both worked examples, the ranged section, the Spell Attack line and four glossary entries all lost crit clauses.
- **`weapons.md`** - *Criticals* becomes *Openings*; ten weapon rows remapped; five missile tables lost the column. **Misfire was fixed in passing**: it read *"roll under your misfire score on the d12 roll when you attack"*, and an attack has not rolled a `1d12` since the merge. It is now its own `1d12` beside the shot, rather than the Tempo Die - which would have made a `1d4` arquebusier misfire three times as often as a `1d12` one.
- **`combat.md`**, **`magic_overview.md`**, **`wounds_and_survival.md`** (two Conditions), **`leadership.md`**'s sample Cohort, **`DESIGN_GUIDE.md`**'s sanctioned-Feat list, `character_sheet.html` and `tempo_sim.py` (`CRITS = False`, switchable).
- **Rebuilt because their premise was the critical:** **Iron Path** traded away criticals and now trades away **the Opening menu entirely** - it wins by 5 all day and takes nothing, which is closer to what the Path always claimed to be. **Orkh Bloodlust** was still on a *natural-roll* crit range (11-12) that predated even the margin system and had never been ported; it now lowers the Opening threshold by 1 and forbids **Break Away**. **Soullance**'s impale rides on an Opening. **Overcharged Bolt** paid for itself by forfeiting a critical and now pays `\+2` Mana. **Ambush from Nothing** had *also* never been ported - it still read *"critical on 10-12 instead of just 12"* - and is now a further `\-2` to an already `\-4` Shot DC.

**`core/bestiary/` was not touched**, as before.

---

## 64. One attack a turn, dice invested instead of attacks stacked *(2026-08-30)*

A player-directed ruling, not a measurement - no `tempo_sim` run backs anything below, and it should sit alongside the other open tuning questions until one does.

**The change:** "Declare your whole attack sequence at once - how many attacks, and a target for each - and pay all the dice up front" is gone. Your Major Action is now **one attack**. You invest however many Tempo Dice you want in it, roll and sum every one (each at your Tempo Die's size), and add Weapon Skill. Riposte, Opportunity Attacks and a held attack's trigger all work the same way - invest as many dice as you have left - except **a Riposte's first die is free**, the reward for the Opening that earned it; further dice on it cost normally. **Parry got the same treatment for symmetry**: a defender can sink multiple dice into one Parry, summed the same way, so a heavily-invested attack doesn't run over a defender stuck at 1 die. Damage is untouched - Weapon Damage \+ STR \- AR regardless of dice invested - so the payoff for investing heavily is a bigger, more reliable roll and an easier Opening, never more damage, the same shape as the no-criticals ruling in item 63.

**What broke and got fixed:** Riposte's old "cancels the next attack still to come in the declared sequence" clause had nothing left to cancel - there is no sequence any more - and was replaced outright. **Apotheosis** (`invocation.md`) traded "the first attack in each sequence you declare costs no Tempo Die" for "the first Tempo Die you invest in your attack each turn costs nothing" - same intent, one attack instead of many. **Manifest Shadow** (`shadowmancy.md`) dropped its "any attack in your declared sequence" framing for "any attack you make," since there's no sequence for it to describe. **Economy of Motion** (`martial_feats.md`) and the **Instinct** Feat's Parry note were reworded around a roll already made rather than a sequence already declared. `bestiary_overview.md`'s Parry/Attack lines now read as a "1 die invested" baseline an NPC can build past, same as a PC. Ranged Shooting kept its own multi-shot "Declaring the sequence" text, unaffected by this item - see item 65, which removed it too, for a different reason.

**Left stale:** `tools/tempo_sim.py` explicitly models multiple declared attacks per turn (`seq_cost`, `max_attacks`, "attacks declared per turn", Riposte cancelling a queued attack) - the exact mechanic this ruling deleted. Its shot/reload modeling is unaffected by this item (see item 65 for that). Rebuilding it against the current rules is open work; `CLAUDE.md` says so directly now.

---

## 65. Ranged weapons lose the Tempo Pool entirely *(2026-08-30)*

Also player-directed, also unmeasured - a follow-on to item 64, requested in the same sitting once melee no longer paid for extra attacks with dice: **"Tempo stays solely a martial focus, and not a ranged focus."**

**The change:** Tempo Dice never touch a shot, on either side of it - not firing, not reloading. A shot rolls `1d12 \+ Ranged or Thrown Skill` vs. the Shot DC, the same shape as a Skill Check or a Spell Attack (which never used the Tempo Die either, see item 63's Misfire fix), and firing costs a Major Action - one shot a turn, the same cap item 64 put on melee. Reloading became pure action economy instead of a Minor Action plus dice: **Thrown** - Object Interaction; **Sling and every bow** - Minor Action; **Crossbows** - Minor Action \+ Object Interaction; **every firearm** - a full Major Action, so firing and reloading can no longer both happen in the same round; the **Hackbut** is untouched, since its reload was already action-only. The old "fires twice a turn off a Minor Action and extra dice" mechanic is gone with it - a brace of loaded weapons now buys back the reload turn, not a second shot in the same turn.

**What broke and got fixed:** Misfire's old explanation ("dice are spent on declaration, not on the roll... any further shot from that weapon still waiting in the same declared sequence does not fire either") assumed a shot cost dice and could queue behind others in a sequence; rewritten around two independent `1d12` rolls and a Major Action instead. **Practiced Loader** (`martial_feats.md`) used to shave a Tempo Die off reload; it now shaves an action tier instead, and its firearm case is now strictly stronger than before - fire and fully reload in the same round, Major Action then Minor Action, which no version of the old Feat could do. `core_rules.md`'s Attribute table stopped crediting DEX with "ranged accuracy," since no Attribute touches the shot roll any more, only the Skill. Every weapon's **Reload (X)** tag (bows, crossbows, sling, firearms, Hackbut) now prints the actual action cost instead of a die count, and the duplicate `Reload (action)` property definition that only the Hackbut used got folded into the one general definition.

**Left stale:** the same `tools/tempo_sim.py` caveat as item 64 - its `shot_cost`/`shots_affordable` functions price shots and reloads in Tempo Dice, which no longer happens at all.

---

## 66. Armor replaces AR with two printed lines, and the flat Wound Threshold table is deleted *(2026-08-30)*

User-directed, unmeasured - a design proposal from outside this file's usual tempo/margin tuning, worked out collaboratively and confirmed step by step rather than run through `tempo_sim.py`.

**The change:** `armor.md`'s single AR number becomes two, **Dent Line** and **Rend Line**, printed per armor (Gambeson 3/7, Buff Coat 4/8, Mail Shirt 5/9, Chain Mail 6/10, Brigandine 7/11, Breastplate 7/11, Half-Plate 8/12, Full Plate 9/13). The formula is `Wound = old AR + 1`, `Deep = Wound + 4` - a constant 4-point gap, chosen because it reproduces all three of the user's own worked examples (Gambeson 3/7, Mail Shirt 5/9, Breastplate 7/11) exactly. A landing hit rolls weapon dice (summed) `\+ STR` (missiles: `\+ DEX`) and compares the total to the two lines instead of subtracting AR and reading a flat table: below Wound is **Turned Aside** (no Wound, armor chips 1 durability - 0 for Rigid, unchanged from the old absorbed-blow rule), at or above Wound is 1 Wound, at or above Deep is 2. **Rolling maximum on every die "finds a gap"** - a fixed die-face outcome, not a margin bonus, so it doesn't reopen item 63's deletion: if the roll would have been Turned Aside it lands for 1 Wound instead, and if it already scored a Wound it applies Bleeding on top. **Unarmored targets skip the roll entirely and take a flat 2 Wounds** on every landing hit - a deliberate, simpler replacement for the old STR-keyed-then-flattened Wound Threshold table (`wounds_and_survival.md`), which is deleted outright along with its 1-9/10-18/19+ bands. Per-hit Wound severity is capped at 2 now, not 3.

**Durability:** starts equal to Dent Line and both lines fall together, 1 for 1, keeping their gap - the same mechanic as the old "current AR = current durability," just applied to a pair. At 0 durability the armor is Broken and the wearer resolves every hit as Unarmored rather than reading a bottomed-out pair of lines (a Gambeson driven to 0 would otherwise read 0/4, which is a real difference from "no protection at all").

**Why a formula and not just two typed numbers per armor:** `Wound = AR + 1` keeps every armor's old ranking intact and stays inside the game's real ceiling (weapon die + STR tops out at 17, `DESIGN_GUIDE.md`'s dice-ceiling rule) - a Dagger (max roll 9) can just barely wound Full Plate (Wound 9) and never Deep it, while a Greatsword or Warblade (max roll 17) reliably Deeps even Full Plate. That's the weapon differentiation item 36 found the old flat Wound Threshold table had flattened out of the game (see item 36's finding, quoted again in item 61's summary at `:838` and `:1028`) - it falls out of the two-line system for free, the same way it fell out of the old raised-AR-ladder proposal that was never adopted.

**Rigid vs. Flexible, confirmed unchanged:** the user was asked directly whether Rigid's free-absorb-on-a-stopped-blow rule should survive the rework, given the new phrasing read as "every armor chips 1 on a landed hit." Kept as-is - Rigid still loses 0 durability to a Turned Aside hit, Flexible still loses 1. This is the entire reason Breastplate costs double Brigandine for identical numbers, and dropping it would have been a real balance change smuggled in through a mechanic rewrite.

**What else got converted, in the same pass:** every file granting a flat `+X AR` bonus or an ignores/bypasses-AR effect was translated by one consistent rule - **a flat bonus shifts both lines up by X together** (mirroring how durability shifts them down together), and **an ignore/bypass effect lowers both lines by the stated amount, for that attack only.** "Degrades armor by N AR" became "costs N durability" throughout, matching the Degradation mechanic already in place. Touched: `arcane_feats.md` (Overcharge Spell Attack), `prestige_feats.md` (a Prestige Feat's decayed-flesh stat line), `martial_feats.md` (Seek the Seam, Follow-Through, Double Charge, Half-Swording's Penetrant, Shield Wall, Broadhead/Bodkin, a Blunt-weapon rider now keyed to Turned Aside instead of "damage reduced to 0"), `weapons.md` (the generic Penetrant property definition, Armor-Piercing, the War Maul's table row), `shadowmancy.md` (Manifest Shadow's stat line), `geomancy.md` (four spots: a reactive stone shield, the slab's own stats, Terrae Motus Pulse's self-buff, the stone wall's stats, the earth-prison's stats), `cultivation.md` (a self-buff, and Bark Skin's temporary-AR spell), `necration.md` (two armor-degrading Petition effects, the Raise Thrall stat line), `invocation.md` (Soulward), three racial traits (`varulf.md`, `tapio.md`, `golems.md` - Golem's Metal form also had its degrade-floor and regeneration numbers converted), `alchemy.md` (an acid oil's ignore/lower effects, a protective oil's flat bonus), `character_creation.md`'s derived-stats table, and NPC/mount/follower stat blocks in `traveling.md` and `leadership.md` (the latter's sample Squire also had a pre-existing Gambeson-AR-6 mismatch against the real item table quietly corrected to the real Gambeson values while converting it). The character sheet (`character_sheet.html`) had its Armor table split into Dent/Rend/Max Dent/Max Rend columns (renamed `data-col` keys `ar\`→\`dent`, `maxAr\`→\`maxDent`, generic serialization means an old save's fields are simply ignored, recomputing fresh - the sheet's own established behavior for every prior rework), its Wound Log severity capped at 2 options instead of 3, and its Armor Penalty banding re-keyed to Max Dent (3-5/6-8/9-11); `sheet_test.js` was updated to match and its 140 assertions pass.

**Naming, settled after the mechanic:** "Wound Line" and "Deep Line" were the working names through the mechanical design above, but "Wound" was already spoken for (the Wounds resource itself), so the user asked for a rename. Tested by how each candidate reads said out loud at the table ("that attack grazes/proofs/bites/dents") and filtered to armor-centric verbs rather than injury-centric ones (ruling out Gash, Grievous, Bite-as-injury) - landed on **Dent Line** (the armor visibly gives, 1 Wound) and **Rend Line** (it's torn clean through, 2 Wounds), reusing the pattern's user-proposed "Rend" over this file's own "Breach" suggestion. Applied as a global rename across every file the mechanic touched above, including the compound labels ("Wound/Deep" → "Dent/Rend") that a plain phrase-substitution missed on the first pass.

**Left untouched, on the established precedent:** `core/bestiary/` - already stale against the Exchange merge per `TODO.md`, and item 63 set the precedent of leaving it alone through a combat-adjacent rework rather than hand-patching stale files ahead of the bestiary's own dedicated rebuild pass. `tools/` likewise untouched, for the same reason.

