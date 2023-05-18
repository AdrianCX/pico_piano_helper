#!/bin/bash

if [ ! -d midi ]; then
    python3 -m venv ./midi
fi

source ./midi/bin/activate

pip3 install -r ./requirements.txt