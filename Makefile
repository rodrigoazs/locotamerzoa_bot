SHELL:=/bin/bash

.PHONY: tests

run:
	pipenv run python app.py

install-dev:
	pip install -U pip virtualenv==20.0.23 pipenv
	pipenv install --dev
