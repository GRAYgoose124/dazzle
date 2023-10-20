#!/bin/bash



while getopts ":bepdsgrh" opt; do
  case $opt in
    b)
      build=true
      ;;
    e)
      echo "copying .env.template to .env"
      cp .env.template .env
      ;;
    p)
      echo "Running in production mode"
      production="-f production.yml"
      ;;
    g)
      echo "Running with GPU"
      # install nvidia-container-toolkit if it is not installed
      if ! dpkg -s nvidia-container-toolkit >/dev/null 2>&1; then
        echo "You need to install nvidia-container-toolkit to use GPU:"
        printf "\nhttps://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html\n\n"
        exit 1
      fi
      gpu="-f gpu-compute.yml"
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
      echo "  -g        run with GPU compute"
      echo "  -e        copy .env.template to .env"
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

args="-f docker-compose.yml ${production} ${gpu}"
if [ "$build" = true ]; then
  echo "Building..."
  if [ "$FORCE_NO_CACHE" = true ]; then
    nocache="--no-cache"
  fi
  docker-compose $args build $nocache
fi

echo "Starting..."
docker-compose $args up $daemon
