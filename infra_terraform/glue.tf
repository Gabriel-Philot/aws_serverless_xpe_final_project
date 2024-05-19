
resource "aws_glue_job" "example" {
  name        = "test_script_glue_terraform_clean"
  role_arn    = var.glue_1_arn
  glue_version = "3.0"
  number_of_workers = 3
  worker_type    = "G.1X"
  timeout        = 4

  command {
    name            = "glueetl"
    script_location = var.glue_script_crypto_path
    python_version  = "3"
  }

  default_arguments = {
    "--bucketname"   = var.glue_arguments_bucket
    "--prefixraw"    = var.glue_arguments_prefixraw
    "--prefixtrusted"= var.glue_arguments_prefixtrusted
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


