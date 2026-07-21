# Voice: core/setting/ (lore-bible register)

Derived from `setting_overview.md`, `calendar.md`, `geography.md`,
`nations.md`, `religions.md`, `heroes.md`. **`history.md` excluded on
purpose** - see `lore-bible/CLAUDE.md`. Use this as the reference before
drafting new setting content; it's the reusable distillation so you don't
have to re-read all six chapters to catch the register each time.

## The one thing to internalize

This is **reference-book prose, not scene prose**. Nothing here is written
as if a character is speaking or a moment is being lived through (that's
what got `history.md`'s myth sections excluded). Every entry reads like an
in-world encyclopedia/gazetteer article: confident, declarative, third-person,
no hedging, no "as you may know." When in doubt, write the sentence a
scholar-chronicler in Ressam would write, not the sentence a narrator would.

## Structural patterns, by content type

**Gazetteer entries** (nations, continents, planes, some religions) follow a
label-led shape almost every time:

> **Overview.** [scene-setting paragraph - what it is, tone, one or two
> vivid concrete details]
>
> **Key Details:** / **Inhabitants.** / **Key Locations.**
> * [bulleted facts, terse, one per line]

Don't break this shape without reason - a reader scanning `nations.md`
expects Overview-then-bullets every time. The **bolded label followed by a
period, inline with the paragraph** (`**Overview.** A colossal...`) is the
house style - not a heading.

**Enumerable content never gets prosified.** Pantheons, festivals, ongoing
wars, currencies-per-nation - all of it drops straight into bullets. See the
Tagarian pantheon (16 gods as flat bullets grouped under five sub-pantheon
headers) or the "Key Ongoing Conflicts (402 RC)" list in `history.md`'s
sibling section. If you catch yourself writing "there are also several
festivals, including X, Y, and Z" as a sentence, stop and bullet it instead.

**Character/hero entries** (`heroes.md`) are the shortest register in the
whole sample set - 1 to 4 sentences, no Overview/bullet scaffold at all:

> ## Alfred Sibbell Hunter
>
> A legendary Human Night-Terror hunter, one of only a few to survive a
> journey to the Fields of Nocturne.

The pattern is almost always **[Name/Epithet header]** then **[Race/Title +
one defining feat or trait]**, sometimes a second sentence complicating it
(Aldric Grimthorn: hero to some, irredeemable to others). Resist the urge to
pad these into full biographies - the brevity *is* the effect; a figure gets
one sharp, memorable fact, not a résumé. The one outlier in the sample
(Victor Ardan gets three padded, repetitive sentences) reads as weaker for
it - don't use it as the model, use Alfred Sibbell Hunter or Ghorzuk Firemaw
instead.

**Cosmic/celestial phenomena** (Mourning Star, the twin moons) get an
italicized epithet subtitle under the header:

> ## The Mourning Star
> ### *The Servant Sun*

Major deities with real personality get the same treatment (`## Vessel` /
`### *Shepherd of Souls*`, `## Davil` / `### *God of Thieves, Winds and
Skies*`). This subtitle is doing real work - it's the one-line thesis of the
entry, delivered as a title rather than a topic sentence. Use it for
entries that deserve a "read this as: ___" framing; skip it for entries that
are pure inventory (a nation's Key Details don't need one).

**Signature institutions get a denser, longer paragraph than everything
around them.** The Portatores, the Donati, the Golden Choir each get one
unbroken, image-dense paragraph nested as a bullet inside their nation's
entry, markedly richer than the terse bullets next to them:

> **The Portatores:** [...] In combat they advance in absolute silence, no
> war cries, no commands, no sound but the thunder of their guns and the
> crash of their halberds. Off the battlefield they are men with bonds and
> humor; in formation they become faceless instruments of divine judgment,
> identical and interchangeable.

This is a deliberate pacing move: everything else in a nation's write-up is
scannable fact, and then one elite order/unit gets a paragraph that rewards
close reading. Use this sparingly - one per nation/faction at most - so it
keeps its weight. The tell of a well-written one: a short, punchy final
sentence that lands the whole paragraph's thesis (e.g. "To face them is to
face an inevitable wall of silent iron that shoots you at distance and
butchers you up close.").

## Sentence and word-level habits

- **Invented terms are bolded and unglossed on first mention.** `**Plethic**
  serves as the common tongue...` - the term is never "explained" beyond
  what the sentence needs; no "(a language)" parentheticals. Trust the
  reader.
- **Rhetorical pairing/contrast is a recurring move**, especially for
  factions with a self-serving justification: "not simply overwhelming
  opposition through raw force" / "the ultimate paradox: the one mortal with
  the power to save everyone, who chooses instead to damn them all." Good
  for antagonist factions specifically - it signals "this faction has a
  story it tells itself," which is more interesting than flat villainy.
- **Concrete sensory detail over abstraction**, even in short entries:
  "the air is thick with sulphur," "geysers of steam and ash," "shimmering
  mirages and dangerous predators." Every continent entry earns its
  atmosphere from a couple of specific images, not adjective stacking.
- **Numbers and specificity ground otherwise mythic claims**: "high tides
  occurring up to four times daily," "nearly 10 feet tall," "circa 390 RC."
  A concrete number lands harder than a vague superlative.
- **Dry understatement for scale/threat**, more common in `nations.md` and
  `religions.md`: "a threat to even minor immortal gods," "the strongest
  infantry unit in Ressam." State the superlative once, plainly, and move on
  - don't stack intensifiers around it.
- **Naming convention**: figures are usually introduced as `[Given Name],
  [Epithet]` (Ghorzuk, Firemaw / Durnir, the Ironhand) or `[Title] [Name]`
  (High Lord Victor Ardan). Pick one per figure and keep it consistent
  across every future mention.

## Escaping and formatting (mechanical, carries over from root CLAUDE.md)

- No em dashes or en dashes anywhere - hyphens only.
- Apostrophes, hyphens in contractions, and ampersands inside prose destined
  for `core/setting/` are backslash-escaped in the checked-in Markdown
  (`Sundering \- a pivotal moment`, `Renos \& Ferrins`) because the source is
  exported from Google Docs. Match this when editing existing text so
  re-exports/diffs stay clean; it's fine to write unescaped in `work/drafts/`
  and add the escaping only when the text is promoted into `core/setting/`.
- Formulas/derived stats don't apply to this domain (that's the rules side),
  but the horizontal-rule (`---`) section-break convention between major
  entries is used exactly the same way here as in the rules chapters.

## What NOT to imitate (and why it's excluded, not just skipped)

`history.md`'s Age of Mythos and the Sundering sections are written as
continuous mythic narrative with implied dialogue and interiority ("For a
brief moment, the world knew peace, and Aldric thought he had finally
prevailed..."). That's a fundamentally different craft mode from everything
above - it's telling a story, not cataloging a world. Nothing else in
`core/setting/` writes this way, including `history.md`'s own back half (the
RC-dated "Third Age" sections snap back to the terse chronicle register,
closer to the rest of this file). Treat the myth-narrative mode as a one-off
that already happened, not a register available for new lore.
