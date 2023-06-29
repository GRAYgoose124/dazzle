#!/bin/bash

# Variables
build=false
production=false

# getopts block
while getopts ":bp" opt; do
  case $opt in
    b)
      echo "Building..."
      build=true
      ;;
    p)
      production=true
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

# Build the application if requested
if [ "$build" = true ]; then
  docker-compose build --no-cache
fi

# Run the application
if [ "$production" = true ]; then
  echo "Running in production mode"
  docker-compose -f docker-compose.yml -f production.yml up
else
  docker-compose up
fi
