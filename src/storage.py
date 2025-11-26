import json
import os

SNAPSHOT_FILE= "snapshot.json"

def save_snapshot(folder,data,path=SNAPSHOT_FILE):

    with open(path,"w") as f:
        snapshot={
            "folder_path":folder,
            "files":data
        }
        json.dump(snapshot,f,indent=4)

def load_snapshot(path=SNAPSHOT_FILE):
    if not os.path.exists(path):
        return None
    with open(path,"r") as f:
        return json.load(f)