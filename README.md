# FIMS — File Integrity Monitoring System

**Short:** Python desktop/CLI tool that snapshots folders (SHA-256) and detects file create/modify/delete events.

## Features (MVP)
- Compute SHA-256 for files and collect size/mtime
- Save per-folder snapshots (history)
- Compare current folder state with latest snapshot
- CLI subcommands: `create`, `compare`, `list`

## Quickstart
```bash
cd FIMS/src
# create snapshot
python main.py create --path "C:\path\to\folder"
# compare folder to snapshot
python main.py compare --path "C:\path\to\folder"
# list saved snapshots
python main.py list