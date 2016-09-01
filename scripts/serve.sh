#!/usr/bin/env bash
source ${1}

pushd ${SERVER_DIRECTORY}
python -m SimpleHTTPServer ${SERVER_PORT}
popd
