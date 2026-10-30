"""NaCl encryption for Salt, distributed as an independently maintained extension."""

from importlib.metadata import version
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
__version__ = version("saltext.nacl")
