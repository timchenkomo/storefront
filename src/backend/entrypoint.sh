#!/bin/bash
poetry run alembic upgrade head
poetry run uvicorn main:APP --host 0.0.0.0 --port ${PORT} --reload
