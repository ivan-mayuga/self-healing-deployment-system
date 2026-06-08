#!/bin/bash

echo "Starting rollback..."

docker stop myapp 2>/dev/null
docker rm myapp 2>/dev/null

docker run -d \
    --name myapp \
    -p 5000:5000 \
    myapp_backup

echo "Rollback completed."