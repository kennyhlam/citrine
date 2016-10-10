#!/usr/bin/env bash

# start up development server
FLASK_DEBUG=1 FLASK_APP=citrine_server.py flask run --host=0.0.0.0
