#!/bin/bash

# Create a Python virtual environment named "env"
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

#Install Dependencies
pip3 install flask
pip3 install openai
pip3 install gunicorn

# Start App
gunicorn -b 0.0.0.0:5000 app:app




