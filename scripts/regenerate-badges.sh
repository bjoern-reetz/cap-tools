#!/usr/bin/env bash

set -e

poetry run -- python -m pybadges --left-text "" --right-text Ruff --left-color grey --right-color "#261230" --logo ./images/logos/ruff.svg --embed-logo > images/ruff.svg
poetry run -- python -m pybadges --left-text "pre-commit" --right-text enabled --right-color "#0c0" --logo ./images/logos/pre-commit.svg --embed-logo > images/pre-commit.svg
poetry run -- python -m pybadges --left-text license --right-text MIT --right-color "#97ca00" > images/license.svg
poetry run -- python -m pybadges --left-text mypy --right-text checked --right-color "#2a6db2" > images/mypy.svg

if [[ -f .coverage ]]; then
  percent_covered_display=$(poetry run -- coverage json --include "src/*" -o - | jq -r '.totals.percent_covered_display')
  poetry run -- python -m pybadges --left-text coverage --right-text "$percent_covered_display%" > images/coverage.svg
else
  >&2 echo "No coverage report found. Skipping regeneration of coverage badge."
fi
