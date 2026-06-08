#!/bin/bash

echo "Stopping old container..."

docker stop myapp 2>/dev/null
docker rm myapp 2>/dev/null

echo "Building image..."

docker build -t myapp .

echo "Starting container..."

docker run -d \
  --name myapp \
  -p 5000:5000 \
  myapp

g old container..."

docker stop myapp 2>/dev/null
docker rm myapp 2>/dev/null

echo "Building image..."

docker build -t myapp .

echo "Starting container..."

docker run -d \
  --name myapp \
  -p 5000:5000 \
  myapp

echo "Waiting for application startup..."

sleep 5

echo "Running health check..."

./scripts/healthcheck.sh

if [ $? -eq 0 ]; then
    python3 monitor/deployment_recorder.py SUCCESS
    echo "Deployment successful!"
else
    python3 monitor/deployment_recorder.py FAILED

    python3 monitor/incident_report.py "healthcheck failed"

    ./scripts/rollback.sh

    echo "Deployment failed. Rollback completed."
    exit 1
fiecho "Deployment complete!"
