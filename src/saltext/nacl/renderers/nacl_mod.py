"""
Salt renderer module
"""

import logging

log = logging.getLogger(__name__)

__virtualname__ = "nacl"


def __virtual__():
    # To force a module not to load return something like:
    #   return (False, "The nacl renderer module is not implemented yet")
    return __virtualname__
