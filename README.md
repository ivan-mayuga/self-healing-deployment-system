# Self-Healing Deployment System

## Overview

A production-inspired DevOps project that demonstrates automated software delivery, containerization, infrastructure automation, monitoring, alerting, and Kubernetes-based self-healing deployments.

The project showcases a complete DevOps workflow from code commit to deployment, including automated testing, Docker image publishing, Infrastructure as Code (Terraform), Kubernetes orchestration, rolling updates, rollback capabilities, and Discord-based incident notifications.

## Features

### Application & Containerization

* Dockerized Flask application
* Multi-environment deployment support
* Container lifecycle management

### CI/CD Automation

* GitHub Actions pipeline
* Automated test execution with Pytest
* Automated Docker image builds
* Docker Hub image publishing

### Monitoring & Alerting

* Health check monitoring
* Application metrics endpoint
* Incident detection
* Discord alert notifications
* Deployment and monitoring logs

### Infrastructure as Code

* Terraform-managed infrastructure
* Declarative infrastructure provisioning
* Version-controlled infrastructure

### Kubernetes Operations

* Kubernetes Deployment management
* Kubernetes Service exposure
* Self-healing pod recovery
* Rolling updates
* Automated rollback support
* Replica management
* High-availability deployment strategy

## Technology Stack

* Python / Flask
* Docker
* GitHub Actions
* Pytest
* Docker Hub
* Terraform
* Kubernetes (Kind)
* Discord Webhooks

## Project Architecture

Developer
↓
GitHub Repository
↓
GitHub Actions CI/CD
↓
Automated Testing (Pytest)
↓
Docker Image Build
↓
Docker Hub Registry
↓
Kubernetes Deployment
↓
Self-Healing Pods
↓
Monitoring & Health Checks
↓
Discord Alert Notifications

## Demonstrated DevOps Concepts

* Continuous Integration (CI)
* Continuous Delivery (CD)
* Infrastructure as Code (IaC)
* Containerization
* Automated Testing
* Monitoring & Alerting
* Kubernetes Orchestration
* Self-Healing Infrastructure
* Rolling Updates
* Rollbacks
* Deployment Automation
