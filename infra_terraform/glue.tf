
resource "aws_glue_job" "stocks" {
  name        = "glue_terraform_stocks"
  role_arn    = var.glue_1_arn
  glue_version = "3.0"
  number_of_workers = 3
  worker_type    = "G.1X"
  timeout        = 4

  command {
    name            = "glueetl"
    script_location = var.glue_script_model_path
    python_version  = "3"
  }

  default_arguments = {
    "--bucketname"   = "${var.project_name}-${var.bucket_sufix}"
    "--prefixraw"    = var.glue_arguments_prefixraw_stocks
    "--prefixtrusted"= var.glue_arguments_prefixtrusted_stocks
    "--namefun"      = var.glue_arguments_name_fun_stocks
    "--windowarg"    = var.glue_arguments_window_stocks
    "--TempDir"      = var.glue_arguments_TempDir
    "--extra-py-files" = var.glue_arguments_extra-py-files
    "--extra-jars"   = var.glue_arguments_extra-jars
  }

  max_retries         = 0
  execution_property {
    max_concurrent_runs = 1
  }
}


resource "aws_glue_job" "crypto" {
  name        = "glue_terraform_crypto"
  role_arn    = var.glue_1_arn
  glue_version = "3.0"
  number_of_workers = 3
  worker_type    = "G.1X"
  timeout        = 4

  command {
    name            = "glueetl"
    script_location = var.glue_script_model_path
    python_version  = "3"
  }

  default_arguments = {
    "--bucketname"   = "${var.project_name}-${var.bucket_sufix}"
    "--prefixraw"    = var.glue_arguments_prefixraw_crypto
    "--prefixtrusted"= var.glue_arguments_prefixtrusted_crypto
    "--namefun"      = var.glue_arguments_name_fun_crypto
    "--windowarg"    = var.glue_arguments_window_crypto
    "--TempDir"      = var.glue_arguments_TempDir
    "--extra-py-files" = var.glue_arguments_extra-py-files
    "--extra-jars"   = var.glue_arguments_extra-jars
  }

  max_retries         = 0
  execution_property {
    max_concurrent_runs = 1
  }
}


resource "aws_glue_job" "webscraper_infom" {
  name        = "glue_terraform_webscraper_infom"
  role_arn    = var.glue_1_arn
  glue_version = "3.0"
  number_of_workers = 3
  worker_type    = "G.1X"
  timeout        = 4

  command {
    name            = "glueetl"
    script_location = var.glue_script_model_path
    python_version  = "3"
  }

  default_arguments = {
    "--bucketname"   = "${var.project_name}-${var.bucket_sufix}"
    "--prefixraw"    = var.glue_arguments_prefixraw_webscraper_infom
    "--prefixtrusted"= var.glue_arguments_prefixtrusted_webscraper_infom
    "--namefun"      = var.glue_arguments_name_fun_webscraper_infom
    "--windowarg"    = var.glue_arguments_window_webscraper_infom
    "--TempDir"      = var.glue_arguments_TempDir
    "--extra-py-files" = var.glue_arguments_extra-py-files
    "--extra-jars"   = var.glue_arguments_extra-jars
  }

  max_retries         = 0
  execution_property {
    max_concurrent_runs = 1
  }
}
