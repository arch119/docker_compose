#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
docker run -itd --name=redis redis:alpine
docker run \
    -it \
    --rm \
    -v $DIR/code:/code:rw \
    python:3.4-alpine \
    /bin/sh
