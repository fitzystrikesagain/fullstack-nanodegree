#!/bin/bash

source config.env
docker compose down
docker build .
docker compose up --build --force-recreate -d
sleep 5
open http://localhost:"$FLASK_PORT"

export PGPASSFILE=$PWD/.pgpass
if command -v pgcli >/dev/null
then
  pgcli -h "$POSTGRES_LOCALHOST" -U "$POSTGRES_USER" "$POSTGRES_DB"
  exit
  fi

