# This file demonstrates how to enable Vertex AI services via code
resource "google_project_service" "vertex_ai" {
  project = var.project_id
  service = "aiplatform.googleapis.com"

  disable_on_destroy = false
}

variable "project_id" {
  description = "The GCP Project ID"
  type        = string
}
