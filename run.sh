#!/bin/bash

exec python src/fetch_model.py &
exec python src/serve_model.py