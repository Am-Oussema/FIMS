from fims.hashing import compute_hash


def test_compute_hash(tmp_path):
    file = tmp_path / "ex.txt"
    file.write_text("hello")
    h = compute_hash(str(file))
    assert isinstance(h, str)
    assert len(h) == 64
