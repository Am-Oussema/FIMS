from fims.monitor import compare_snapshots


def test_created_file():
    old = {}
    new = {
        "a.txt": {"hash": "h1", "size": 10, "mtime": 100},
    }

    events = compare_snapshots(old, new)
    assert len(events) == 1

    e = events[0]
    assert e["type"] == "created"
    assert e["path"] == "a.txt"
    assert e["new_hash"] == "h1"
    assert e["old_hash"] is None


def test_deleted_file():
    old = {
        "a.txt": {"hash": "h1", "size": 10, "mtime": 100},
    }
    new = {}

    events = compare_snapshots(old, new)
    assert len(events) == 1

    e = events[0]
    assert e["type"] == "deleted"
    assert e["path"] == "a.txt"
    assert e["old_hash"] == "h1"
    assert e["new_hash"] is None


def test_modified_file():
    old = {
        "a.txt": {"hash": "h1", "size": 10, "mtime": 100},
    }
    new = {
        "a.txt": {"hash": "h2", "size": 20, "mtime": 200},
    }

    events = compare_snapshots(old, new)
    assert len(events) == 1

    e = events[0]
    assert e["type"] == "modified"
    assert e["path"] == "a.txt"
    assert e["old_hash"] == "h1"
    assert e["new_hash"] == "h2"


def test_no_changes():
    old = {
        "a.txt": {"hash": "h1", "size": 10, "mtime": 100},
    }
    new = {
        "a.txt": {"hash": "h1", "size": 10, "mtime": 100},
    }

    events = compare_snapshots(old, new)
    assert events == []
