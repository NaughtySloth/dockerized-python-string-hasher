#!/bin/bash

set -euo pipefail

usage() {
  echo "Usage: $0 --version-hashing-service <hashing-service-version> --version-web-scraping-service <web-scraping-service-version> [--additional-param-1 <value>] [--help|-h]"
}

OPTIONS=$(getopt -o 'h' -l version-hashing-service:,version-web-scraping-service:,additional-param-1:,help -- "$@")

eval set -- "$OPTIONS"

while true; do
  case "$1" in
    --version-hashing-service) version_hashing_service="$2"; shift 2;;
    --version-web-scraping-service) version_web_scraping_service="$2"; shift 2;;
    --additional-param-1) additional_param_1="$2"; shift 2;;
    -h|--help) usage; exit 0;;
    --) shift; break;;
    *) echo "Invalid option: $1" >&2; usage; exit 1;;
  esac
done

if [[ -z ${version_hashing_service:-} || -z ${version_web_scraping_service:-} ]]; then
  echo "Missing arguments"
  usage
  exit 1
fi

if [[ -n ${additional_param_1:-} ]]; then
  echo "Additional parameter 1: ${additional_param_1}"
fi

# Create a Docker network if it doesn't exist
if ! docker network inspect my-network &>/dev/null; then
  docker network create my-network
fi

# Start the containers in the same network
docker run -d --name hashing-service --network my-network -p 8080:8080 naughtysloth/hashing-service:"${version_hashing_service}"
docker run -d --name web-scraping-service --network my-network naughtysloth/web-scraping-service:"${version_web_scraping_service}"

read -p "Press Enter to continue..."
