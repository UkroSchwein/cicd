#!/bin/bash

if [ "$1" == "staging" ]; then
    echo "Deploying to Staging..."
elif [ "$1" == "production" ]; then
    echo "Deploying to Production..."
else
    echo "Invalid environment! Please specify 'staging' or 'production'."
    exit 1
fi
