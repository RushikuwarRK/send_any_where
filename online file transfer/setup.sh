#!/bin/bash

# Install requirements
pip install -r requirements.txt

# Check if the install was successful
if [ $? -eq 0 ]; then
    echo "Requirements installed successfully. Starting app.py in 5 seconds..."
    sleep 5
    python app.py
else
    echo "Failed to install requirements."
    exit 1
fi
