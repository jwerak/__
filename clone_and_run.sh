#!/bin/bash

SECRETS_FILE=${SECRETS_FILE:-slack-bot.key}

git pull https://github.com/jwerak/__.git

if [ -f ${SECRETS_FILE} ]; then
  source ${SECRETS_FILE}
else
  echo "Secret file not found at location: ${SECRETS_FILE}"
fi

python dunder.py
