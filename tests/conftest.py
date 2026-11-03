"""Shared configuration for the extension test suites."""

import os

import pytest
import salt.config

FIPS_TESTRUN = os.environ.get("FIPS_TESTRUN", "0") == "1"


@pytest.fixture(scope="session")
def salt_factories_config():
    return {"inject_sitecustomize": "COVERAGE_PROCESS_START" in os.environ, "start_timeout": 120}


@pytest.fixture
def minion_opts(tmp_path):
    opts = salt.config.minion_config(None, minion_id="nacl-test-minion")
    opts.update(
        {
            # These tests exercise NaCl, not machine inventory or DNS probes.
            "skip_grains": True,
            "root_dir": str(tmp_path),
            "pki_dir": str(tmp_path / "pki"),
            "cachedir": str(tmp_path / "cache"),
            "sock_dir": str(tmp_path / "run"),
        }
    )
    return opts
