terraform {
  required_version = ">= 1.5.0"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nexvion" {
  name         = "sandeep3005/nexvion:latest"
  keep_locally = true
}

resource "docker_container" "nexvion" {
  name  = "nexvion-terraform"
  image = docker_image.nexvion.image_id

  ports {
    internal = 80
    external = 8083
  }
}
