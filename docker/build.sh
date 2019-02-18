#!/bin/sh

. ./env.sh

docker build . -t $BINARY:latest
