"""Discovery, precedence and compatibility through real Salt loaders."""

import base64
from importlib.metadata import entry_points, version
from pathlib import Path

import nacl.public
import pytest
import salt.config
import salt.loader
import salt.utils.nacl as core_nacl

from saltext.nacl import PACKAGE_ROOT, __version__
from saltext.nacl.utils import nacl as extension_nacl


def test_package_metadata_and_entry_point():
    assert __version__ == version("saltext.nacl")
    registered = entry_points(group="salt.loader")
    assert any(ep.name == "saltext.nacl" and ep.value == "saltext.nacl" for ep in registered)


def test_loaders_choose_extension(tmp_path):
    opts = salt.config.master_config(None)
    opts.update({"pki_dir": str(tmp_path), "cachedir": str(tmp_path / "cache")})
    utils = salt.loader.utils(opts)
    functions = salt.loader.minion_mods(opts, utils=utils)
    loaders = [
        (functions, "nacl.enc"),
        (salt.loader.runner(opts, utils=utils), "nacl.enc"),
        (salt.loader.render(opts, functions), "nacl"),
        (salt.loader.pillars(opts, functions), "nacl"),
    ]
    for loader, name in loaders:
        loaded = loader[name]
        assert Path(loaded.__code__.co_filename).resolve().is_relative_to(PACKAGE_ROOT)


@pytest.mark.parametrize("box_type", ["sealedbox", "secretbox"])
def test_ciphertext_interoperability(box_type, tmp_path):
    # Deterministic TEST key material; never a deployment key.
    private = nacl.public.PrivateKey(bytes(range(32)))
    kwargs = {
        "opts": {"pki_dir": str(tmp_path)},
        "sk": base64.b64encode(bytes(private)),
        "pk": base64.b64encode(bytes(private.public_key)),
        "box_type": box_type,
    }
    assert (
        extension_nacl.dec(core_nacl.enc("legacy secret", **kwargs), **kwargs) == b"legacy secret"
    )
    assert core_nacl.dec(extension_nacl.enc("new secret", **kwargs), **kwargs) == b"new secret"


def test_shared_utility_is_extension_owned(monkeypatch, tmp_path):
    assert Path(extension_nacl.__file__).resolve().is_relative_to(PACKAGE_ROOT)
    opts = salt.config.minion_config(None)
    opts["pki_dir"] = str(tmp_path)
    functions = salt.loader.minion_mods(opts)
    monkeypatch.setattr(core_nacl, "enc", lambda *args, **kwargs: pytest.fail("Core helper used"))
    keys = extension_nacl.keygen()
    ciphertext = functions["nacl.enc"]("independent", sk=keys["sk"], box_type="secretbox")
    assert functions["nacl.dec"](ciphertext, sk=keys["sk"], box_type="secretbox") == b"independent"
