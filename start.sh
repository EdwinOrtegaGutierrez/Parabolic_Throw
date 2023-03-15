#!/bin/bash

set -eu

export PYTHONUNBUFFERED=true

VIRTUALENV=.data/venv

if [ ! -d $VIRTUALENV ]; then
    python3 -m venv $VIRTUALENV
fi

[ -f requirements.txt ] && $VIRTUALENV/bin/pip install -q -r requirements.txt

$VIRTUALENV/bin/python3 server.py