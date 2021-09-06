#!/bin/bash

set -eu

HERE="$(dirname "$(readlink -f "$BASH_SOURCE")")"
REPO_HOME="$(realpath "${HERE}/..")"

cd "${REPO_HOME}"

source "${REPO_HOME}/scripts/library/venv.sh"
use_venv "type_check" frozen_type_check_requirements.txt

python3 -m mypy
