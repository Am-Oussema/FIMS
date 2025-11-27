from hash_utils import compute_hash
import tempfile
import os

def test_compute_hash():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"hello world")
        f.flush()
        fname = f.name
    h = compute_hash(fname)
    assert isinstance(h, str) and len(h) == 64
    os.remove(fname)
