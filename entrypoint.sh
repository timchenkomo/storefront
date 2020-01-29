#!/bin/bash
poetry run uvicorn main:APP --host 0.0.0.0 --port ${PORT}
