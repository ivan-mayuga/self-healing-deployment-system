#!/bin/bash

echo "Checking application health..."

response=$(curl -s http://localhost:5000/health)

if echo "$response" | grep -q "healthy"; then
    echo "HEALTHY"
    exit 0
else
    echo "UNHEALTHY"
    exit 1
fi
