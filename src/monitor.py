# src/monitor.py
def compare_snapshots(old, new):
    if old is None:
        old = {}

    events = {"created": [], "deleted": [], "modified": []}

    old_files = set(old.keys())
    new_files = set(new.keys())

    for f in sorted(new_files - old_files):
        events["created"].append(f)

    for f in sorted(old_files - new_files):
        events["deleted"].append(f)

    for f in sorted(old_files & new_files):
        old_meta = old.get(f, {})
        new_meta = new.get(f, {})
        old_hash,new_hash = old_meta.get("hash"),new_meta.get("hash")
        old_mtime,new_mtime = old_meta.get("mtime"),new_meta.get("mtime")

        if old_hash != new_hash or old_mtime != new_mtime:
            events["modified"].append(f)

    return events
