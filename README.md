# Ressam

A crunchier, more lethal alternative to D\&D 5e, set in an early-1500s-inspired world where matchlock firearms sit alongside plate armor. Combat is the crunchy core; everything outside it is kept loose, "rulings not rules."

**Read the rules on the [Wiki](https://github.com/Levianeer/Ressam-TTRPG/wiki).**

## For contributors

`core/` is the source of truth for all rules content and is mirrored automatically to the Wiki on every push to `main`. Don't edit the Wiki directly - those edits will be overwritten on the next sync.

Some files under `core/equipment/`, `core/magic/arcane/`, `core/magic/divine/`, and `core/feats/` are generated from structured YAML in `data/` via `scripts/build.py` and must not be hand-edited either. See [CLAUDE.md](CLAUDE.md) for the full data-driven content pipeline.

See [credits.md](credits.md) for attribution.
