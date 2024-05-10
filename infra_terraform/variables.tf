variable "region" {
  type        = string
  description = "Region for deployment"
  default     = "us-east-2"
}

variable "project_name" {
  type        = string
  description = "Name of project"
}

variable "bucket_sufix" {
  type        = string
  description = "Sufix for bucket name"
  default     = "lambda-teste"
}


variable "db_username" {
  type        = string
  description = "Username for database"
  sensitive   = true
}

variable "db_password" {
  type        = string
  description = "Password for database"
  sensitive   = true
}

variable "aws_profile" {
  type        = string
  description = "AWS profile for credentials"
  sensitive   = true
}