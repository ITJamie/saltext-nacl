"""Development commands; CI calls the same underlying tools directly."""

import nox


@nox.session
def tests(session):
    session.install("salt==3008.5", "--no-deps")
    session.install("-e", ".[tests]")
    session.run("python", "tools/test.py", *session.posargs)


@nox.session
def lint(session):
    session.install("ruff", "bandit")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", "--check", ".")
    session.run("bandit", "-q", "-r", "src")


@nox.session
def docs(session):
    session.install("salt==3008.5", "--no-deps")
    session.install("-e", ".[tests,docs]")
    session.run("sphinx-build", "-W", "--keep-going", "-b", "html", "docs", "docs/_build/html")


@nox.session(name="build")
def build_package(session):
    session.install("build", "twine")
    session.run("python", "-m", "build")
    session.run("python", "-m", "twine", "check", "dist/*")
