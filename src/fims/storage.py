import json
import os
import time
import hashlib

SNAPSHOT_DIR= "snapshots"

def _ensure_dir():
    if not os.path.exists(SNAPSHOT_DIR):
        os.makedirs(SNAPSHOT_DIR, exist_ok=True)

def _folder_id(folder_path):
    abspath = os.path.abspath(folder_path)
    h = hashlib.sha256(abspath.encode("utf-8")).hexdigest()
    return h[:16]

def _snapshot_filename(folder_path):
    _ensure_dir()
    folder_id= _folder_id(folder_path)
    ts=int(time.time())
    return os.path.join(SNAPSHOT_DIR,f"{folder_id}_{ts}.json")

def save_snapshot(folder_path,files_dict):
    _ensure_dir()
    snapshot={"folder":os.path.abspath(folder_path) ,"created_at":int(time.time()) ,"files":files_dict}
    fname=_snapshot_filename(folder_path)
    with open(fname,"w",encoding="utf-8") as f:
        json.dump(snapshot,f,indent=2,ensure_ascii=False)
    return fname


def load_latest_snapshot_for_folder(folder_path):
    _ensure_dir()
    folder_id=_folder_id(folder_path)
    candidates=[]

    for fn in os.listdir(SNAPSHOT_DIR):
        if fn.startswith(folder_id+"_") and fn.endswith(".json"):
            full=os.path.join(SNAPSHOT_DIR, fn)
            try:
                with open(full,"r",encoding="utf-8") as f:
                    snap=json.load(f)
                candidates.append((snap.get("created_at",0),full,snap))
            except Exception:
                continue
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][2]

def list_snapshots():
    _ensure_dir()
    out=[]
    for fn in sorted(os.listdir(SNAPSHOT_DIR),reverse=True):
        full=os.path.join(SNAPSHOT_DIR,fn)
        try:
            with open(full,"r",encoding="utf-8") as f:
                snap=json.load(f)
                out.append({
                    "file":full,
                    "folder":snap.get("folder"),
                    "created_at":snap.get("created_at"),
                })
        except Exception:
            continue
    return out