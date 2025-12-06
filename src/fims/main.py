import argparse
import json
import os
from typing import Any, Dict, List, Optional
from importlib.metadata import version

from fims.logging_config import logger
from fims.hashing import scan_folder
from fims.monitor import compare_snapshots
from fims.storage import list_snapshots, load_latest_snapshot_for_folder, save_snapshot


def pretty_print_events(events: List[Dict[str, Any]]) -> None:
    if not events:
        logger.info("No changes detected.")
        return

    logger.info("=== Changes Detected ===")
    counts = {"created": 0, "deleted": 0, "modified": 0}
    for e in events:
        counts[e["type"]] += 1
    logger.info(
        f"CREATED: {counts['created']}, MODIFIED: {counts['modified']}, DELETED: {counts['deleted']}"
    )
    logger.info("-" * 140)

    for e in events:
        t, path = e["type"].upper(), e["path"]
        logger.info(f"[{t}] {path}")

        if e["type"] == "modified":
            logger.info(f"    old_hash: {e['old_hash']} -> new_hash: {e['new_hash']}")
            logger.info(f"    old_size: {e['old_size']} -> new_size: {e['new_size']}")
        elif e["type"] == "created":
            logger.info(f"    hash: {e['new_hash']} size: {e['new_size']}")
        elif e["type"] == "deleted":
            logger.info(f"    old_hash: {e['old_hash']} old_size: {e['old_size']}")


def cmd_create(args: argparse.Namespace) -> int:
    folder = args.path
    if not os.path.isdir(folder):
        logger.error(f"folder '{folder}' does not exist.")
        return 1

    logger.info(f"Scanning folder for snapshot: {folder}")
    files = scan_folder(folder)
    saved = save_snapshot(folder, files)
    logger.info(f"Snapshot saved to: {saved}")

    return 0


def cmd_compare(args: argparse.Namespace) -> int:
    folder = args.path

    if not os.path.isdir(folder):
        logger.error(f"folder '{folder}' does not exist.")
        return 1

    logger.info("Loading latest snapshot for folder ...")
    snapshot = load_latest_snapshot_for_folder(folder)

    if snapshot is None:
        logger.error("No snapshot found for this folder. Create one first:")
        logger.info(f'    fims create --path "{folder}"')
        return 1

    snap_folder = snapshot.get("folder")
    if os.path.abspath(snap_folder) != os.path.abspath(folder):
        logger.error("Snapshot does not match folder. Create a new one.")
        return 1

    old_files = snapshot.get("files", {})
    logger.info("Scanning current folder ...")
    new_files = scan_folder(folder)
    events = compare_snapshots(old_files, new_files)
    pretty_print_events(events)
    # print JSON summary if requested
    if args.json:
        print("\nJSON summary:")
        print(json.dumps(events, indent=2))

    return 0


def cmd_list(args: argparse.Namespace) -> int:
    snaps = list_snapshots()

    if not snaps:
        logger.info("No snapshots saved yet.")
        return 0

    logger.info("Saved snapshots (most recent first):")
    for s in snaps:
        logger.info(
            f"- {s.get('file')} "
            f"(folder={s.get('folder')}, created_at={s.get('created_at')})"
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="FIMS - File Integrity Monitoring System"
    )
    parser.add_argument(
        "--version", action="version", version=f"FIMS {version('fims')}"
    )

    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="Create snapshot for a folder")
    p_create.add_argument("--path", required=True, help="Folder to snapshot")
    p_create.set_defaults(func=cmd_create)

    p_compare = sub.add_parser("compare", help="Compare folder with latest snapshot")
    p_compare.add_argument("--path", required=True, help="Folder to compare")
    p_compare.add_argument("--json", action="store_true", help="Print JSON summary")
    p_compare.set_defaults(func=cmd_compare)

    p_list = sub.add_parser("list", help="List saved snapshots")
    p_list.set_defaults(func=cmd_list)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


def cli_entry() -> None:
    import sys

    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    cli_entry()
