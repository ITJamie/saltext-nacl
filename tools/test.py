"""Run fresh coverage for extension-owned runtime code, including child interpreters."""

import os
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
os.chdir(root)
subprocess.run([sys.executable, "-m", "coverage", "erase"], check=True)
# Preserve diagnostics even when pytest fails; failures must still fail the job.
tests = subprocess.run(
    [sys.executable, "-m", "coverage", "run", "-m", "pytest", *sys.argv[1:]], check=False
)
combined = subprocess.run([sys.executable, "-m", "coverage", "combine"], check=False)
report = subprocess.run([sys.executable, "-m", "coverage", "report"], check=False)
xml = subprocess.run([sys.executable, "-m", "coverage", "xml"], check=False)
sys.exit(tests.returncode or combined.returncode or report.returncode or xml.returncode)
