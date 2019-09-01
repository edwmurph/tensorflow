#!/bin/bash

# Script to update conda env with updated environment.yml

if ! [[ $PWD == */tensorflow ]]; then
  echo 'ERROR: must be in root dir of tensorflow project to run save script.'
  exit 1
fi;

#setup_conda
. "/anaconda3/etc/profile.d/conda.sh"

conda activate ./.env

conda env update --prefix ./.env --file environment.yml  --prune

