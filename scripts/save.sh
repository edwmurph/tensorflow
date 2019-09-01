#!/bin/bash

# Script to update conda dependencies in environment.yml

if ! [[ $PWD == */tensorflow ]]; then
  echo 'ERROR: must be in root dir of tensorflow project to run save script.'
  exit 1
fi;

#setup_conda
. "/anaconda3/etc/profile.d/conda.sh"

# make sure to use --prefix flag since using local conda
conda env export --prefix ./.env > environment.yml
