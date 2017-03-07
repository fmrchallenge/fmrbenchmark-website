#!/bin/sh

if [ ! $1 ]; then
    echo Usage: deploy.sh USER@HOST:PATH
    exit 1
fi

rsync -e ssh -z -r -v --del build/ $1
