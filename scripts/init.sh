#!/bin/bash

# Script to setup the environment for working in this project

# USAGE: source this script (via `. ./init.sh`) to:
#   - create env if doesnt exist
#   - switch to local conda env

if ! [[ $PWD == */tensorflow ]]; then
  echo 'ERROR: must be in root dir of tensorflow project to run init script.'
  exit 1
fi;

#setup_conda
. "/anaconda3/etc/profile.d/conda.sh"

if [ ! -d './.env' ]; then
  # if .env dir doesnt exist, create conda env in local project
  # NOTE: future conda commands might need `--prefix ./.env` flag
  conda env create -f environment.yml --prefix ./.env
fi

# activate newly created local env
conda activate ./.env

# if conda env prefix on terminal prompt is too long, execute bash command:
#   conda config --set env_prompt '({name})'
