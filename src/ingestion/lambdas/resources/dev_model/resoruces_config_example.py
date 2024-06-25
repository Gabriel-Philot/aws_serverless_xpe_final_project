# --------------  Static variables -----------------
BUCKET = "empty_bucket"
REGION_NAME = "us-east-2"

# DEV
LOG_PREFIX = "dev/logs"

# PROD
#LOG_PREFIX = "prod/logs"
 
## ------------------ Mobile variables------------------

#DEV -> CHANGE HERE !!!
source = "source_value"
type_Assets = "type_Value???"
base_url = "base_urlvalue"
name_fun = "fun_name_value"


RAW_PREFIX = f"dev/raw/{source}/{type_Assets}/date_ingestion="
TRUSTED_PREFIX = f"dev/trusted/{source}/{type_Assets}"
BASE_URL = f"{base_url}"
NAME_FUN = f"{name_fun}"
