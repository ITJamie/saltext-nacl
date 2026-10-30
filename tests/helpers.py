"""Small test helpers independent of Salt's repository test suite."""

from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory


@contextmanager
def temporary_file(name):
    with TemporaryDirectory() as directory:
        path = Path(directory) / name
        path.touch()
        yield str(path)
