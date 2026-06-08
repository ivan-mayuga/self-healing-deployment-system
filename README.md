# Self-Healing Deployment System

## Overview

A DevOps-focused project that automatically deploys, monitors, detects failures, generates incident reports, and performs self-healing actions through automated container restarts and rollback mechanisms.

## Features

- Automated deployment using Bash
- Dockerized Flask application
- Health check automation
- Deployment history tracking
- Incident report generation
- Automatic rollback
- Continuous monitoring
- Self-healing container restart
- Alert notifications
- Monitoring logs

## Project Architecture

Developer
→ deploy.sh
→ Docker Container
→ Health Check

Successful Deployment
→ Deployment History

Failed Deployment
→ Incident Report
→ Rollback

Continuous Monitoring
→ Failure Detection
→ Automatic Restart
→ Alert Notification

## Technologies Used

- Python
- Flask
- Bash
- Docker
- Linux
- JSON

## Running the Project

1. Build and deploy:

./scripts/deploy.sh

2. Start monitoring:

python3 monitor/monitor.py

3. Test self-healing:

docker stop myapp

The monitoring service should detect the failure and automatically restart the container.

## Future Improvements

- GitHub Actions CI/CD
- Docker Compose
- Slack/Discord Notifications
- Kubernetes Deployment
- Prometheus Monitoring
- Grafana Dashboards
