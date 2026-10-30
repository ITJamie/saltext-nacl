"""
    Unit tests for the saltext.nacl.runners.nacl module
"""

import saltext.nacl.runners.nacl
from unittest.mock import patch


def test_fips_mode():
    """
    Nacl runner doesn't load when fips_mode is True
    """
    opts = {"fips_mode": True}
    with patch("saltext.nacl.runners.nacl.__opts__", opts, create=True):
        ret = saltext.nacl.runners.nacl.__virtual__()
        assert ret == (False, "nacl runner not available in FIPS mode")
