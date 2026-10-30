import pytest

import saltext.nacl.runners.nacl_mod as nacl_runner


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"this_does_not_exist.please_replace_it": lambda: True},
    }
    return {
        nacl_runner: module_globals,
    }


def test_replace_this_this_with_something_meaningful():
    assert "this_does_not_exist.please_replace_it" in nacl_runner.__salt__
    assert nacl_runner.__salt__["this_does_not_exist.please_replace_it"]() is True
