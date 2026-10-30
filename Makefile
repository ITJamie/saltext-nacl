.PHONY: tests lint docs build

tests:
	nox -s tests

lint:
	nox -s lint

docs:
	nox -s docs

build:
	nox -s build
