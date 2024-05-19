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
  default     = "lambda-teste33"
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

# Glue
variable "glue_1_arn" {
  type = string
}

variable "glue_script_crypto_path" {
  type = string
}

# dont fortget to chance here in the future tu use the same structure as the bucket it self.
variable "glue_arguments_bucket" {
  type = string
}

variable "glue_arguments_prefixraw" {
  type = string
}

variable "glue_arguments_prefixtrusted" {
  type = string
}

variable "glue_arguments_TempDir" {
  type = string
}

variable "glue_arguments_extra-py-files" {
  type = string
}

variable "glue_arguments_extra-jars" {
  type = string
}

variable "glue_arguments_name_fun_crypto" {
  type = string
}

variable "glue_arguments_window_crypto" {
  type = string
}

# Lambda
variable "layer_1_arn" {
  type = string
}

variable "layer_2_arn" {
  type = string 
}

variable "iam_bucket_arn" {
  type = string
}

# Path to zip files
variable "zip_path_1" {
  type = string
}

variable "zip_path_2" {
  type = string
}

variable "zip_path_3" {
  type = string
}
