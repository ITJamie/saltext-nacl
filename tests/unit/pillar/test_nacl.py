"""
    Unit tests for the saltext.nacl.pillar.nacl module
"""

import saltext.nacl.pillar.nacl
from unittest.mock import patch


def test_fips_mode():
    """
    Nacl pillar doesn't load when fips_mode is True
    """
    opts = {"fips_mode": True}
    with patch("saltext.nacl.pillar.nacl.__opts__", opts, create=True):
        ret = saltext.nacl.pillar.nacl.__virtual__()
        assert ret == (False, "nacl pillar data not available in FIPS mode")
