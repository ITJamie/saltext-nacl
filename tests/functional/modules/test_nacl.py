import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("nacl.example_function"),
]


@pytest.fixture
def nacl(modules):
    return modules.nacl


def test_replace_this_this_with_something_meaningful(nacl):
    echo_str = "Echoed!"
    res = nacl.example_function(echo_str)
    assert res == echo_str
