#!/bin/bash

# Tear down the container and remove db and migrations
docker compose stop
rm -rfv data/*
rm -rfv migrations

# Clean up all containers, fresh build
docker container prune -f
docker compose up -d

# Wait for Flask, run migrations
sleep 15
source .env
docker exec -ti "$FLASK_CONTAINER_NAME" flask db init
docker exec -ti "$FLASK_CONTAINER_NAME" flask db migrate
docker exec -ti "$FLASK_CONTAINER_NAME" flask db upgrade

# copy and run sql file to postgres container
docker cp ./sql/init.sql "$POSTGRES_CONTAINER_NAME":/tmp/init.sql
docker exec -u "$POSTGRES_USER" "$POSTGRES_CONTAINER_NAME" psql "$POSTGRES_DB" "$POSTGRES_USER" -f /tmp/init.sql

# launch website and pgcli
open http://localhost:"$FLASK_PORT"
sleep 5
pgcli "postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@localhost:5432/$POSTGRES_DB"
