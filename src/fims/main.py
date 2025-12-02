import argparse
import os
import json
from fims.hashing import scan_folder
from fims.storage import save_snapshot, load_latest_snapshot_for_folder, list_snapshots
from fims.monitor import compare_snapshots


def pretty_print_events(events):
    if not events:
        print("[*] No changes detected.")
        return
    print("\n=== Changes Detected ===")
    counts = {"created": 0, "deleted": 0, "modified": 0}

    for e in events:
        counts[e["type"]] += 1
    print(
        f"CREATED: {counts['created']}, MODIFIED: {counts['modified']}, DELETED: {counts['deleted']}\n"
    )

    for e in events:
        t = e["type"].upper()
        path = e["path"]
        print(f"[{t}] {path}")
        if e["type"] == "modified":
            print(f"    old_hash: {e['old_hash']} -> new_hash: {e['new_hash']}")
            print(f"    old_size: {e['old_size']} -> new_size: {e['new_size']}")
        elif e["type"] == "created":
            print(f"    hash: {e['new_hash']} size: {e['new_size']}")
        else:
            print(f"    old_hash: {e['old_hash']} old_size: {e['old_size']}")


def cmd_create(args):
    folder = args.path
    if not os.path.isdir(folder):
        print(f"[-] Error: folder '{folder}' does not exist.")
        return
    print("[*] Scanning folder for snapshot:", folder)
    files = scan_folder(folder)
    saved = save_snapshot(folder, files)
    print("[+] Snapshot saved to:", saved)


def cmd_compare(args):
    folder = args.path
    if not os.path.isdir(folder):
        print(f"[-] Error: folder '{folder}' does not exist.")
        return

    print("[*] Loading latest snapshot for folder ...")
    snapshot = load_latest_snapshot_for_folder(folder)
    if snapshot is None:
        print("[-] No snapshot found for this folder. Create one first with: ")
        print(f'    python main.py create --path "{folder}"')
        return
    snap_folder = snapshot.get("folder")
    if os.path.abspath(snap_folder) != os.path.abspath(folder):
        print(
            "[-] Snapshot does not match folder. Create a new snapshot for this folder."
        )
        return

    old_files = snapshot.get("files", {})
    print("[*] Scanning current folder ...")
    new_files = scan_folder(folder)
    events = compare_snapshots(old_files, new_files)
    pretty_print_events(events)
    # print JSON summary if requested
    if args.json:
        print("\nJSON summary:")
        print(json.dumps(events, indent=2))


def cmd_list(args):
    snaps = list_snapshots()
    if not snaps:
        print("[*] No snapshots saved yet.")
        return
    print("Saved snapshots (most recent first):")
    for s in snaps:
        print(
            f"- {s.get('file')} (folder={s.get('folder')}, created_at={s.get('created_at')})"
        )


def main():
    parser = argparse.ArgumentParser(
        description="FIMS - File Integrity Monitoring System"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="Create snapshot for a folder")
    p_create.add_argument("--path", required=True, help="Folder to snapshot")
    p_create.set_defaults(func=cmd_create)

    p_compare = sub.add_parser("compare", help="Compare folder with latest snapshot")
    p_compare.add_argument("--path", required=True, help="Folder to compare")
    p_compare.add_argument(
        "--json", action="store_true", help="Also print JSON summary"
    )
    p_compare.set_defaults(func=cmd_compare)

    p_list = sub.add_parser("list", help="List saved snapshots")
    p_list.set_defaults(func=cmd_list)

    args = parser.parse_args()
    args.func(args)


def cli_entry():
    import sys

    main(sys.argv[1:])


if __name__ == "__main__":
    main()
