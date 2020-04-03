#!/bin/bash
export PYTHONPATH=.
./wait-for.sh postgres:5432 -t 30 -- echo "Database is up" \
  && poetry run alembic upgrade head \
  && poetry run uvicorn main:APP --host 0.0.0.0 --port ${PORT} --reload
