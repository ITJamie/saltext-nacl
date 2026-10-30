"""Run outside the checkout using a clean interpreter with the built wheel installed."""

from importlib.metadata import requires
from pathlib import Path
from tempfile import TemporaryDirectory

import salt.config
import salt.loader
from packaging.requirements import Requirement

from saltext.nacl import PACKAGE_ROOT
from saltext.nacl.utils import nacl as extension_nacl

assert "site-packages" in PACKAGE_ROOT.parts, PACKAGE_ROOT
assert Path(extension_nacl.__file__).resolve().is_relative_to(PACKAGE_ROOT)
for dependency in requires("saltext.nacl"):
    requirement = Requirement(dependency)
    if requirement.name == "salt":
        assert requirement.marker is not None and "extra" in str(requirement.marker)
with TemporaryDirectory() as directory:
    opts = salt.config.master_config(None)
    opts.update({"pki_dir": directory, "cachedir": str(Path(directory) / "cache")})
    utils = salt.loader.utils(opts)
    functions = salt.loader.minion_mods(opts, utils=utils)
    runner = salt.loader.runner(opts, utils=utils)
    for loader, name in [
        (functions, "nacl.enc"),
        (runner, "nacl.enc"),
        (salt.loader.render(opts, functions), "nacl"),
        (salt.loader.pillars(opts, functions), "nacl"),
    ]:
        assert Path(loader[name].__code__.co_filename).resolve().is_relative_to(PACKAGE_ROOT)
    keys = runner["nacl.keygen"]()
    ciphertext = runner["nacl.enc"]("wheel secret", pk=keys["pk"])
    assert runner["nacl.dec"](ciphertext, sk=keys["sk"]) == b"wheel secret"
    opts["nacl.config"] = {"sk": keys["sk"]}
    functions = salt.loader.minion_mods(opts)
    plaintext = {"secret": "NACL[" + ciphertext.decode() + "]"}
    assert salt.loader.pillars(opts, functions)["nacl"]("wheel-minion", plaintext) == {
        "secret": b"wheel secret"
    }
print(
    "Installed wheel: four plugin loaders and namespaced utility, extension precedence, round trip and external pillar passed"
)
