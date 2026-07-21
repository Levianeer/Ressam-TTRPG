# CLAUDE.md (Lore Bible)

This file governs **narrative/lore-writing conventions** for `lore-bible/` -
it is separate from the repo root `CLAUDE.md`, which governs the rules
pipeline (weapons/spells/feats/progression) and does not apply here. Claude
Code loads whichever `CLAUDE.md` is closest to the files being worked on;
when writing setting/lore content, this is the one that matters.

## What this is

Ressam's setting is not a novel or a story - it's a **lore bible**: reference
material for the world (cosmology, history, geography, nations, religions,
legendary figures) that both feeds the published rulebook chapters and
guides GMs improvising beyond them. This directory's job is to keep new
setting writing consistent - in voice and in canon - with what's already
published, and to give fast reference to settled facts, timeline, and named
figures without re-reading full chapters every time.

## Author's space

Canon lore prose lives in `core/setting/` and is the actual source of truth
- it's published to the GitHub Wiki like the rest of `core/`:

- `setting_overview.md`, `calendar.md`, `history.md`, `geography.md`,
  `nations.md`, `religions.md`, `heroes.md`

Per-race culture/mythology lives in `core/character/races/` (one file per
race). **These are currently rated poor and slated for a rewrite - do not
treat them as canon-quality or style examples until that rework happens.**
Track that rewrite as an open item in `kb/issues/`, not as an input here.

`lore-bible/` does **not** duplicate `core/setting/` prose. It holds:
- derived/condensed reference material (`kb/`) distilled from that canon, and
- a workspace (`work/`) for drafting new setting content before it lands in
  `core/setting/` (or, once race lore is back in scope, `core/character/races/`).

When new lore is approved and ready to become canon, it gets written into
`core/setting/` directly (following that chapter's existing structure) -
`work/drafts/` is staging, not a permanent home for finished content.

## KB structure

- `kb/canon/` - condensed, settled facts distilled from `core/setting/`,
  organized for fast lookup instead of re-reading full chapters (cosmology,
  currency, language, calendar, planes, and a link to the current 402 RC
  snapshot in `kb/timeline/`). Split into more per-domain files as it grows.
- `kb/timeline/` - the dated event ledger: Age of Mythos -> the Sundering ->
  Age of Revival -> Third Age, RC-dated wars and crises. Kept precise (not
  prose-summarized) since the 402 RC conflicts are live and may advance or
  resolve in future sessions - update this whenever a war, alliance, or
  succession changes.
- `kb/characters/` - named figures who recur across chapters, split into
  three tiers (see below): `immortal-gods.md`, `mortal-gods.md`, `mortals.md`.
- `kb/world/` - nations, factions, and geography: `nations.md`, `factions.md`,
  `geography.md`, plus `world/vocab.md` for that domain's dense proper-noun
  layer (nation/faction names, currencies, languages, continents).
- `kb/styles/` - `voice.md`, the voice analysis derived from samples (see
  Voice and Style below).
- `kb/samples/` - a pointer, not a copy (see Voice and Style below).
- `kb/issues/` - open worldbuilding questions, contradictions surfaced while
  drafting, and flagged-for-later items (e.g. the race lore rewrite, "to be
  written" stubs already in canon like Trere and the Black Blades).
- `kb/vocab.md` - cross-cutting invented terms used throughout the setting
  (Ressam, the Mourning Star, Reino Concordium dating, the Sundering, the
  God-Dragons, "mortal god" as an in-world tier, etc.) - domain-specific
  vocab lives in `world/vocab.md` instead of here.

## Character tiers

Named figures are tracked in three separate files under `kb/characters/`,
matching a distinction the setting text already draws on its own (the
Devaraja and Sir Davil are explicitly called "mortal-god[s]" in canon):

- **`immortal-gods.md`** - true divine beings: Thryzzaral, the Great Artists
  / Four Painters, the God-Dragons (Infierno, Rocas, Tempeste, Cascate), the
  Tagarian pantheon, Al'Nur Lehovil, the Dwergan Triad (Mischar, Nekama,
  Melacha) and the Great Mother/Matka. Cosmic in origin, not once-mortal.
- **`mortal-gods.md`** - beings who ascended from mortal (or mortal-adjacent,
  e.g. fallen-angel) origin to godhood and retain a flawed, personal nature:
  God-King Khor, Vessel, Tythe, Henri Gachet Gautier, Sir Davil, the Devaraja.
  Saints who are venerated but whose ascension status is ambiguous (e.g.
  Maarkest) also default here until confirmed otherwise - flag ambiguity in
  `kb/issues/` rather than guessing silently.
- **`mortals.md`** - everyone else notable and non-divine: rulers, heroes,
  guild masters, historical figures (Aldric Grimthorn, Voa Shadowhorn,
  Ghorzuk Firemaw, High Lord Victor Ardan, Thalorien, etc.).

When drafting a new named figure, decide the tier deliberately - it's a
worldbuilding signal (mortal-gods read as *personal and flawed* even at
world-shaking power; immortal gods read as *cosmic and impersonal*, even
the chatty ones) - and don't leave it unfiled in prose alone.

## Voice and style

**Samples:** six of the seven `core/setting/` files - `setting_overview.md`,
`calendar.md`, `geography.md`, `nations.md`, `religions.md`, `heroes.md`.

**`history.md` is deliberately excluded from style samples.** Its Age of
Mythos/Sundering sections use a lyrical, dialogue-and-myth-heavy narrative
register that is not one to replicate in future lore writing (the rest of
the setting doesn't write in-scene myth-retellings; it writes reference
entries). `history.md` still counts as canon for facts and dates and feeds
`kb/timeline/` and `kb/canon/` - it's excluded from `kb/styles/` and
`kb/samples/` specifically, not from the setting's canon.

Rather than copying sample prose into `kb/samples/`, `kb/samples/README.md`
just points at the live files above - `core/setting/` is wiki-published
canon, and a second copy under `kb/` would drift from it over time. Read the
samples directly; the analysis in `kb/styles/voice.md` is the reusable
distillation.

## Hidden canon

Some settled facts are true in-world but must not be stated plainly in
`core/setting/` (or any public-facing) prose - the reveal is the point.
Maarkest is the reference case: publicly he's a martyred saint who "helped
the God-Dragons"; the hidden truth (he *is* Tempeste, alive and amnesiac) is
tracked in `kb/characters/`.

- Mark these facts inline with **Hidden/GM-only:** so they can't be mistaken
  for public canon by a future pass.
- Say explicitly, next to the fact, what the *public* version is and where
  it lives (usually the vaguer existing wording in `core/setting/`) - so a
  writer drafting public-facing text has both versions side by side and
  can't accidentally leak the secret one.
- Never let a hidden fact silently overwrite or contradict the public
  wording already in `core/setting/` - the public version stays exactly as
  published unless the author explicitly decides to reveal it there.
- When a story/scene needs the hidden fact to surface in-world, treat that
  as a real narrative beat to write deliberately, not incidental exposition
  - log the intent to reveal it in `kb/issues/` first if it's a big enough
    swing that other lore should be checked against it.

## Conventions

- Dates use the Reino Concordium (RC) system; the Third Age begins at 1 RC.
  Give era + RC year for anything datable, matching `history.md`'s pattern
  (even though `history.md` isn't a style sample, its dating convention is
  canon and applies everywhere).
- New setting content defaults to landing at the 402 RC "current state"
  unless it's explicitly backstory (pre-Sundering, Age of Mythos, etc.).
  Update `kb/timeline/` whenever something moves the 402 RC status quo -
  don't let it go stale while `core/setting/history.md`'s "Current State"
  section is the only place tracking it.
- Follow the root `CLAUDE.md`'s content conventions when text is destined
  for `core/setting/`: hyphens only (no em/en dashes), and the Google-Docs-
  export backslash-escaping style for literal Markdown characters.
- Invented terms are used unglossed and bolded on first mention, not
  over-explained - match that confidence level rather than adding
  hand-holding exposition the existing chapters don't have.
- Race lore is out of scope here until the rewrite is scoped - track it in
  `kb/issues/`, don't treat `core/character/races/` as a canon input.
