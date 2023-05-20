#!/bin/bash

if [ ! -f ./midi/bin/activate ]; then
    python3 -m venv ./midi
fi

source ./midi/bin/activate

pip3 install -r ./requirements.txt