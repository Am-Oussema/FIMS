import argparse
from hash_utils import scan_folder
from storage import save_snapshot, load_snapshot
from monitor import compare_snapshots
import os

def main():
    parser=argparse.ArgumentParser(description="FIMS - File Integrity Monitoring System")
    parser.add_argument("--path", required=True, help="Folder to monitor")
    parser.add_argument("--snapshot", action="store_true",help="Create a fresh snapshot")
    args = parser.parse_args()

    folder=args.path
    
    if not os.path.isdir(folder):
        print(f"[-] Error: The folder '{folder}' does not exist.")
        return

    if args.snapshot:
        print("[+] Creating new snapshot ...")
        try:
            snapshot=scan_folder(folder)
        except:
            return "Error during the snapchot"
        save_snapshot(folder,snapshot)
        print("[+] Snapshot saved.")
        return
    
    print("[+] Loading old snapshot...")
    old_snapshot = load_snapshot()
    if old_snapshot is None:
        print("[-] No snapshot found.")
        return
    
    os_folder=old_snapshot["folder_path"]
    os_files=old_snapshot["files"]
    if os_folder!=folder:
        print("[*] Create a new snapshot for this folder:")
        print(f"    python main.py --path \"{folder}\" --snapshot")
        return
    
    print("[+] Scanning current folder...")
    new = scan_folder(folder)

    print("[+] Comparing...")
    events = compare_snapshots(os_files, new)
    for k,v in events.items():
        print(f"{k.upper()}: {len(v)}")
        for item in v:
            print(f" - {item}")

if __name__=="__main__":
    main()