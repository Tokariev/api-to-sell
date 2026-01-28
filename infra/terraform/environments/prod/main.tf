terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.gcp_project_id
  region  = var.region
}

module "compute" {
  source = "../../modules/compute"

  project_name   = "api-to-sell"
  environment    = "prod"
  machine_type   = "e2-medium"
  zone           = "${var.region}-a"
  disk_size_gb   = 30
  ssh_user       = var.ssh_user
  ssh_public_key = var.ssh_public_key
}

output "server_ip" {
  value = module.compute.external_ip
}
