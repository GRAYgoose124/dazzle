#!/bin/bash

SCRIPT_NAME=$(echo $1 | cut -d':' -f1 | tr '/' '_').sh

echo "Running init script $SCRIPT_NAME"
if [ -f "/init_scripts/$SCRIPT_NAME" ]; then
    bash "/init_scripts/$SCRIPT_NAME";
fi