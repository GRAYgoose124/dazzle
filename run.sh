#!/bin/bash

# Variables
build=false
production=false

# getopts block
while getopts ":bpds:rh" opt; do
  case $opt in
    b)
      echo "Building..."
      build=true
      ;;
    p)
      production=true
      ;;
    d)
      echo "Running in daemon mode"
      daemon="-d"
      ;;
    s)
      # if arg then stop only web container
      if [ "$OPTARG" = "web" ]; then
        echo "Stopping web container"
        docker-compose stop web
        exit 0
      else
        echo "Stopping containers"
        docker-compose down
        exit 0
      fi
      ;;
    r)
      echo "Removing containers"
      docker-compose down
      docker-compose rm
      exit 0
      ;;
    h)
      echo "Usage: run.sh [-b] [-p] [-d] [-s] [-r] [-h]"
      echo "  -b        build the application"
      echo "  -p        run in production mode"
      echo "  -d        run in daemon mode"
      echo "  -s [web]  stop dazzle (or just the web container)"
      echo "  -r        remove the application"
      echo "  -h        display this help message"
      exit 0
      ;;
    \?)
      echo "Invalid option: -$OPTARG, use -h" >&2
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
  docker-compose -f docker-compose.yml -f production.yml up $daemon
else
  docker-compose up $daemon
fi
