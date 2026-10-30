import pytest

import saltext.nacl.pillar.nacl_mod as nacl_pillar


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"this_does_not_exist.please_replace_it": lambda: True},
    }
    return {
        nacl_pillar: module_globals,
    }


def test_replace_this_this_with_something_meaningful():
    assert "this_does_not_exist.please_replace_it" in nacl_pillar.__salt__
    assert nacl_pillar.__salt__["this_does_not_exist.please_replace_it"]() is True
