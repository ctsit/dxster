#!/usr/bin/env bash
source ${1}

rm ${XML_OUTPUT_PATH}
scp -r ${LOCAL_DIRECTORY}/. ${DEPLOY_USER}@${DEPLOY_HOST}:${DEPLOY_DIRECTORY}/
