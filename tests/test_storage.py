import os
from fims.storage import save_snapshot, load_latest_snapshot_for_folder, list_snapshots


def test_save_and_load_snapshot(tmp_path, monkeypatch):
    # Redirect SNAPSHOT_DIR → a temporary directory for testing
    monkeypatch.setattr("fims.storage.SNAPSHOT_DIR", str(tmp_path))

    # Fake folder to snapshot
    folder = tmp_path / "myfolder"
    folder.mkdir()

    files = {"a.txt": {"hash": "aaa", "size": 3, "mtime": 1000}}

    # Save snapshot
    saved_file = save_snapshot(str(folder), files)
    assert os.path.exists(saved_file)

    # Load snapshot back
    snap = load_latest_snapshot_for_folder(str(folder))
    assert snap is not None
    assert snap["folder"] == os.path.abspath(str(folder))
    assert "files" in snap
    assert snap["files"]["a.txt"]["hash"] == "aaa"


def test_list_snapshots(tmp_path, monkeypatch):
    # Use temporary directory for snapshots
    monkeypatch.setattr("fims.storage.SNAPSHOT_DIR", str(tmp_path))

    # Add one snapshot
    folder = tmp_path / "testfolder"
    folder.mkdir()
    save_snapshot(str(folder), {})

    # List snapshots
    snaps = list_snapshots()
    assert len(snaps) == 1
    assert snaps[0]["file"].endswith(".json")
