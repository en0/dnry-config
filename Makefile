PYTHON=python3
TWINE=twine
TEST_PUBLISH_FLAGS=--repository-url https://test.pypi.org/legacy/
PUBLISH_FLAGS=--skip-existing
FILES:=$(wildcard *.py) \
	   $(wildcard dnry/config/*.py) \
	   $(wildcard dnry/config/arg/*.py) \
	   $(wildcard dnry/config/delegate/*.py) \
	   $(wildcard dnry/config/environ/*.py) \
	   $(wildcard dnry/config/in_memory/*.py) \
	   $(wildcard dnry/config/yaml/*.py)
TEST_FILES:=$(FILES) \
	        $(wildcard test/*.py)

.PHONY: help, test, build, publish, publish-test

help:
	@echo "Targets are:"
	@echo " - test: Run all unit tests"
	@echo " - build: Build the dist wheel"
	@echo " - publish: Build and publish the wheel to pypi"
	@echo " - publish-test: Build and publish the wheel to pypi test"

test: $(TEST_FILES)
	@$(PYTHON) -m unittest

publish: build
	@$(TWINE) upload $(PUBLISH_FLAGS) dist/*

publish-test: build
	@$(TWINE) upload $(PUBLISH_FLAGS) $(TEST_PUBLISH_FLAGS) dist/*

build: $(FILES)
	@$(PYTHON) setup.py sdist bdist_wheel