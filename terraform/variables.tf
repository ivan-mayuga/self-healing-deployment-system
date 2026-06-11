variable "image_name" {
  description = "Docker image to deploy"
  type        = string
  default     = "manavi27/self-healing-deployment-system:latest"
}

variable "container_name" {
  description = "Container name"
  type        = string
  default     = "self-healing-app"
}

variable "internal_port" {
  description = "Port inside container"
  type        = number
  default     = 5000
}

variable "external_port" {
  description = "Port exposed on host"
  type        = number
  default     = 5000
}
