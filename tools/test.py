"""Run fresh coverage for extension-owned runtime code, including child interpreters."""

import os
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
os.chdir(root)
subprocess.run([sys.executable, "-m", "coverage", "erase"], check=True)
subprocess.run([sys.executable, "-m", "coverage", "run", "-m", "pytest", *sys.argv[1:]], check=True)
subprocess.run([sys.executable, "-m", "coverage", "combine"], check=True)
subprocess.run([sys.executable, "-m", "coverage", "report"], check=True)
subprocess.run([sys.executable, "-m", "coverage", "xml"], check=True)
