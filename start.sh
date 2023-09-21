#!/bin/bash

# Create a Python virtual environment named "env"
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Start App
gunicorn -b 0.0.0.0:5000 app:app
