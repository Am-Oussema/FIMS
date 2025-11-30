import time


def _now_ts():
    return int(time.time())


def compare_snapshots(old_files, new_files):
    if old_files is None:
        old_files = {}

    events = []

    old_set = set(old_files.keys())
    new_set = set(new_files.keys())

    for p in sorted(new_set - old_set):
        meta_new = new_files[p]
        events.append(
            {
                "type": "created",
                "path": p,
                "old_hash": None,
                "new_hash": meta_new.get("hash"),
                "old_size": None,
                "new_size": meta_new.get("size"),
                "timestamp": _now_ts(),
            }
        )

    for p in sorted(old_set - new_set):
        meta_old = old_files[p]
        events.append(
            {
                "type": "deleted",
                "path": p,
                "old_hash": meta_old.get("hash"),
                "new_hash": None,
                "old_size": meta_old.get("size"),
                "new_size": None,
                "timestamp": _now_ts(),
            }
        )

    for p in sorted(old_set & new_set):
        o = old_files[p]
        n = new_files[p]
        try:
            if (
                o.get("hash") != n.get("hash") or
                o.get("size") != n.get("size") or
                o.get("mtime") != n.get("mtime")
            ):
                events.append(
                    {
                        "type": "modified",
                        "path": p,
                        "old_hash": o.get("hash"),
                        "new_hash": n.get("hash"),
                        "old_size": o.get("size"),
                        "new_size": n.get("size"),
                        "timestamp": _now_ts(),
                    }
                )
        except Exception:
            pass
    return events
