#!/bin/sh

. ./env.sh

docker run -p 5000:5000 --env-file=env.sh $BINARY:latest
