variable "project_name" {
  type = string
}

variable "environment" {
  type = string
}

variable "machine_type" {
  type    = string
  default = "e2-small"
}

variable "zone" {
  type    = string
  default = "us-central1-a"
}

variable "disk_size_gb" {
  type    = number
  default = 20
}

variable "network" {
  type    = string
  default = "default"
}

variable "subnetwork" {
  type    = string
  default = "default"
}

variable "ssh_user" {
  type = string
}

variable "ssh_public_key" {
  type = string
}
