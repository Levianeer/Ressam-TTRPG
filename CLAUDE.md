# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **Ressam**, a tabletop RPG (TTRPG) rulebook written in Markdown. Most of the repository is content/rules-authoring - edits to game design text, tables, and formulas, not software. However, the weapons/armor tables, spell lists, and feat lists are **generated from structured YAML data** via a small Python + Jinja2 pipeline (see "Data-driven content pipeline" below) - those specific files are build output, not hand-authored prose.

## Repository structure

- `core/core_rules.md` - foundational mechanics: dice, attributes, skills, checks vs. Ward, HP/dying, carrying capacity, resting, exhaustion, stealth, light/vision. Read this first; nearly every other chapter assumes these definitions.
- `core/character/` - building and advancing a character: `character_creation.md` (step-by-step guide), `races.md`, `careers.md`, `languages.md`, `progression_&_rewards.md`.
- `core/combat/` - `combat.md` (turn structure, action economy, attack/damage rolls, critical hits) and `maneuvers.md` (dashing, shoving, grappling, dodging, etc.).
- `core/magic/` - spellcasting rules split into `magic_overview.md` (universal rules shared by both paths) and `spell_crafting.md`, with two parallel school trees:
  - `magic/arcane/` - arcane schools (aeromancy, geomancy, hydromancy, pyromancy, shadowmancy) plus `arcane_overview.md`. The 5 school files are **generated** (see below); `arcane_overview.md` is hand-authored.
  - `magic/divine/` - divine schools (benediction, cultivation, invocation, necration, subjugation) plus `divine_overview.md`. Same split: the 5 school files are generated, `divine_overview.md` is hand-authored.
- `core/feats/` - feat categories (general, martial, arcane, hybrid, prestige, skill), indexed by `feats_overview.md`. The 6 category files are **generated**; `feats_overview.md` is hand-authored.
- `core/equipment/` - `armor.md` and `weapons.md` are **generated**; `supplies.md` and `alchemy.md` (crafting oils/bombs/salves from ingredients) are hand-authored.
- `core/exploration/` - travel and downtime layer: `traveling.md` (hex travel, mounts), `downtime.md` (revelry/celebrations), `leadership.md` (followers and cohorts).
- `credits.md` - attribution and licensing note.
- `assets/` - currently empty (reserved for future images/handouts).
- `data/`, `scripts/`, `templates/` - the data-driven content pipeline; see below.

## Data-driven content pipeline

Weapons, armor, spells, and feats live as structured YAML in `data/` and are rendered into the corresponding `core/**/*.md` files by `scripts/build.py`. This exists because those four domains are hundreds of repetitive, data-shaped entries (stat blocks, spell headers, feat prerequisites) that are painful to keep consistent by hand and awkward for tooling/AI to query reliably out of freeform prose.

**Do not hand-edit the generated files** - `core/equipment/weapons.md`, `core/equipment/armor.md`, all 5 files under `core/magic/arcane/` except `arcane_overview.md`, all 5 files under `core/magic/divine/` except `divine_overview.md`, and all 6 files under `core/feats/` except `feats_overview.md`. Edits there are silently overwritten the next time someone runs the build. Edit the YAML in `data/` instead.

- **Data** (source of truth): `data/weapons/*.yaml`, `data/armor/*.yaml`, `data/spells/arcane/*.yaml`, `data/spells/divine/*.yaml`, `data/feats/*.yaml` (six normal category files) and `data/feats/prestige.yaml` (the prestige feats, a different shape - no `Benefit`, adds `Ritual`/`Mechanical Changes`).
- **Schema**: `scripts/models.py` (weapons/armor), `scripts/spell_models.py` (spells), `scripts/feat_models.py` (feats) - Pydantic models. Free-text body fields (`effect`, `benefit`, `special`, `mechanical_changes`, feat `extra` sub-fields) store Markdown close to verbatim as YAML block scalars rather than being decomposed further - the internal structure of spell effects and feat benefits (Overcome/Resist pairs, choice-menus, nested sub-effects) varies too much entry-to-entry to model generically, so only the reliably-flat header metadata (name, mana cost, casting time/range/duration, prerequisites) is real structured data.
- **Templates**: `templates/weapons.md.j2`, `templates/armor.md.j2`, `templates/magic/arcane/*.md.j2`, `templates/magic/divine/*.md.j2`, `templates/feats/*.md.j2` - Jinja2. Only the tabular/repeated-entry regions are template-driven; surrounding rules prose (the Weapon Properties glossary, Firearm Rules, school-level passive traits like Shadowmancy's Inaudible, Invocation's Severing ritual, the Prestige Feats Requirements/Restrictions preamble, etc.) is static text baked into the template.
- **Build script**: `scripts/build.py`, run from the repo root as `python scripts/build.py`:
  - no flags: regenerates and writes all `core/**/*.md` output files.
  - `--check`: exits nonzero if any generated output would differ from what's on disk (no write) - use to verify the checked-in `.md` files match `data/`.
  - `--diff`: prints a unified diff of what would change (no write).
  - Workflow: edit YAML in `data/`, run `python scripts/build.py`, commit both the YAML change and the regenerated `.md` diff together.
- **Python environment**: `.venv/` at the repo root has `PyYAML`, `Jinja2`, and `pydantic` installed (`scripts/requirements.txt`) - run scripts with `.venv/bin/python scripts/build.py` (or activate the venv first).
- **One-time migration scripts**: `scripts/_extract_spells.py` and `scripts/_extract_feats.py` parsed the original hand-authored Markdown into the current YAML during migration. They are not part of the ongoing pipeline (nothing imports or runs them automatically) and are kept only as a reference for how the extraction was done.

## Content conventions

- Em Dashes (—) and En Dashes (–) are not used, instead use only Hyphens (-).
- Files are exported from Google Docs, so literal Markdown-special characters are backslash-escaped in the source (e.g. `1d12 \+ Skill Ranks \+ Attribute`, `Ressam is not Dungeons \& Dragons`, `HP \= (END × 3\) \+ 10`). Preserve this escaping style when editing existing text so re-exports/diffs stay clean. For the generated files (weapons/armor/spells/feats), this escaping lives in the YAML data (and is checked in single-quoted or block-scalar form, since double-quoted YAML strings can't hold a bare `\+`/`\-`/`\=`) - preserve it there when editing data instead.
- Formulas and derived stats are given as bolded inline math (e.g. `**Maximum HP = (END × 3) + 10**`) rather than code blocks. Follow this pattern for new formulas.
- Section breaks use a horizontal rule (`---`) between major topics within a chapter.
- Tables are used heavily for skill lists, DC tiers, and comparative mechanics (e.g. Arcane vs. Divine casting) - match existing table shapes when adding related content instead of introducing prose where a table already exists for that topic.
- Core terminology is reused verbatim across chapters (e.g. `Major Action`, `Ward`, `Evasion`, `AR`, `Exhaustion`, `Mana Cost`) - when editing one chapter, check whether the same term/mechanic is defined or referenced elsewhere (`core_rules.md`, `combat.md`, `magic_overview.md`) so definitions stay consistent.
- The game's tone/scope per `core_rules.md`'s foreword: Ressam is a crunchier, more lethal alternative to D&D 5e set in an early-1500s-inspired world (matchlocks alongside plate armor), with combat as the crunchy core and non-combat pillars intentionally kept loose ("rulings not rules"). Keep new mechanical content consistent with that stated design intent rather than adding elaborate subsystems for non-combat pillars.