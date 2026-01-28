variable "gcp_project_id" {
  type = string
}

variable "region" {
  type    = string
  default = "us-central1"
}

variable "ssh_user" {
  type = string
}

variable "ssh_public_key" {
  type = string
}
