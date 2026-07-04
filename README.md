# Ressam

Ressam is a crunchy, lethal alternative to other TTRPGs, set in a world balanced around an early-1500s baseline - matchlock firearms sit alongside plate armor, magic is feared and regulated. Combat is the heart of the game; everything outside of it is meant to be played loosely, "rulings not rules."

**Read the rules on the [Wiki](https://github.com/Levianeer/Ressam-TTRPG/wiki).**

## For contributors

`core/` is the source of truth for all rules content and is mirrored automatically to the Wiki on every push to `main`. Don't edit the Wiki directly - those edits will be overwritten on the next sync.

Some files under `core/equipment/`, `core/magic/arcane/`, `core/magic/divine/`, and `core/feats/` are generated from structured YAML in `data/` via `scripts/build.py` and must not be hand-edited either.

See [CLAUDE.md](CLAUDE.md) for the full data-driven content pipeline.

See [CREDITS.md](CREDITS.md) for attribution.
