variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "zone" {
  description = "The GCP zone for the VM instance"
  type        = string
  default     = "europe-west3-a"
}
