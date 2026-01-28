resource "google_compute_instance" "api_server" {
  name         = "${var.project_name}-${var.environment}"
  machine_type = var.machine_type
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "cos-cloud/cos-stable"
      size  = var.disk_size_gb
    }
  }

  network_interface {
    network    = var.network
    subnetwork = var.subnetwork

    access_config {}
  }

  metadata = {
    ssh-keys = "${var.ssh_user}:${var.ssh_public_key}"
  }

  tags = ["http-server", "https-server"]
}

resource "google_compute_firewall" "allow_http" {
  name    = "${var.project_name}-${var.environment}-allow-http"
  network = var.network

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["http-server", "https-server"]
}
