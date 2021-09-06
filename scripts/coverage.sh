#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
REPO_HOME="$(realpath "${HERE}/..")"

cd "${REPO_HOME}"

source "${REPO_HOME}/scripts/library/venv.sh"
use_venv "coverage" frozen_coverage_requirements.txt

python3 -m pytest --cov=tetris --cov-report term-missing
