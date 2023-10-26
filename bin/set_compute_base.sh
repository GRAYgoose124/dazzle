#!/bin/bash

COMPUTE_EXTRA_BASE="python:3.10"
if [ "$1" == "cuda" ]; then
    COMPUTE_EXTRA_BASE="nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04"
elif [ "$1" == "pytorch" ]; then
    COMPUTE_EXTRA_BASE="pytorch/pytorch"
fi

# Ensure .env file exists
# touch .env
# Append or replace BASE_IMAGE value in .env
#grep -q 'BASE_IMAGE=' .env && sed -i "/BASE_IMAGE=/c\BASE_IMAGE=\"$BASE_IMAGE\"" .env || echo "BASE_IMAGE=$BASE_IMAGE" >> .env

echo "set compute extra base: $COMPUTE_EXTRA_BASE"
export COMPUTE_EXTRA_BASE
