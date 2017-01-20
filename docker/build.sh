#!/usr/bin/env bash
mkdir -p out
cp -r ../sample out/
cp ../dtsql.py out/

docker build -t ainsight/dtsql .
