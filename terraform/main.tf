terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "app_network" {
  name = "self-healing-network"
}

resource "docker_image" "app" {
  name = var.image_name
}

resource "docker_container" "app" {
  name  = var.container_name
  image = docker_image.app.image_id

  depends_on = [
    docker_image.app,
    docker_network.app_network
  ]

  networks_advanced {
    name = docker_network.app_network.name
  }

  env = [
    "PORT=5000",
    "ENV=dev"
  ]

  labels {
    label = "project"
    value = "self-healing-deployment-system"
  }

  labels {
    label = "managed_by"
    value = "terraform"
  }

  labels {
    label = "environment"
    value = "dev"
  }

  ports {
    internal = var.internal_port
    external = var.external_port
  }

  restart = "unless-stopped"
}