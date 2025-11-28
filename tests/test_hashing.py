<<<<<<< HEAD
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
=======
from fims.hashing import compute_hash

def test_compute_hash(tmp_path):
    file = tmp_path / "ex.txt"
    file.write_text("hello")
    h = compute_hash(str(file))
    assert isinstance(h, str)
    assert len(h) == 64
>>>>>>> dev
