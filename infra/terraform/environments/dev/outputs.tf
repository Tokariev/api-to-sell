output "instance_name" {
  description = "Name of the VM instance"
  value       = google_compute_instance.instance_name.name
}

output "instance_external_ip" {
  description = "External IP address of the VM"
  value       = google_compute_instance.instance_name.network_interface[0].access_config[0].nat_ip
}

output "ssh_command" {
  description = "SSH command to connect to the VM"
  value       = "gcloud compute ssh ${google_compute_instance.instance_name.name} --zone=${var.zone}"
}
