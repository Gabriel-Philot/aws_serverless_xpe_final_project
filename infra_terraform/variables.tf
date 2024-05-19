variable "region" {
  type        = string
  description = "Region for deployment"
  default     = "us-east-2"
}

variable "project_name" {
  type        = string
  description = "aws-serverless-architecture-terraform"
}

variable "bucket_sufix" {
  type        = string
  description = "Sufix for bucket name"
  default     = "aws-serverless-architecture-terraform"
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



# Glue
variable "glue_1_arn" {
  type = string
}

variable "glue_script_model_path" {
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

# crypto

variable "glue_arguments_prefixraw_crypto" {
  type = string
}

variable "glue_arguments_prefixtrusted_crypto" {
  type = string
}

variable "glue_arguments_name_fun_crypto" {
  type = string
}

variable "glue_arguments_window_crypto" {
  type = string
}


# stocks

variable "glue_arguments_prefixraw_stocks" {
  type = string
}

variable "glue_arguments_prefixtrusted_stocks" {
  type = string
}

variable "glue_arguments_name_fun_stocks" {
  type = string
}
  
variable "glue_arguments_window_stocks" {
  type = string
}
  
# webscraper_infom

variable "glue_arguments_prefixraw_webscraper_infom" {
  type = string
}
  
variable "glue_arguments_prefixtrusted_webscraper_infom" {
  type = string
}

variable "glue_arguments_name_fun_webscraper_infom" {
  type = string
}
  
variable "glue_arguments_window_webscraper_infom" {
  type = string
}
  