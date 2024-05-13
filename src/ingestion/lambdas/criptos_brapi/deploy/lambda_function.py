# Lambda function AWS

# Imports
import time
import pandas as pd
from io import StringIO
from pandas import json_normalize
from datetime import datetime, timedelta
from log_manager import S3LogManager
from util import control_sucess, infer_schema, convert_to_string
from json_upload import write_json_to_s3
from api_requests import Brapi_STOCKS_API, Brapi_notSTOCKS__API
from cripto_modules import validate_coin_data

# Variables imports [!WARNING] dont forget to change in config.py file.
from config import BASE_URL, REGION_NAME, \
    BUCKET, RAW_PREFIX, LOG_PREFIX, NAME_FUN, TOKEN_GENERATOR, TICKERS


# V0 inicial structure for logging ect
def lambda_handler(event, context):
    inicio = time.perf_counter()
    control = "OK"
    timestamp_SP = datetime.now() - timedelta(hours=3)
    timestamp_SP_api_pull = timestamp_SP - timedelta(days=1)
    
    # loop df ... [!WARNING] if dont use it change in row 58
    #df_append = pd.DataFrame()

    # api class for requests
    params = {
    'coin': 'BTC,ETC',
    'currency': 'BRL',
    'token': TOKEN_GENERATOR,
    }


    api = Brapi_notSTOCKS__API(
    url=BASE_URL,
    params=params
    )
    
    # --------------------Api requests wra wrangling
    # ------------------- Use Try and execept

    #for date in get_previous_business_days(5):
        #json_result = api_request_instance.get_routes(date)
    try:
        data = api.get_other_quotes()['coins']
        schema = infer_schema(data)
        check_json = validate_coin_data(data)
    # ----------------- execept + control_var for logs management
    except Exception as e:
        control = f'Error msg: {e}'
        print(
            "{project_name}: The request returned 0 items. Original message: {msg}".format(
                msg=e
            )
        )

                            
        # except Exception as e:
        #     control = f'Error msg: {e}'
        #     print("Lighthouse - Chile - Beetrack - API returned 0 lines")

    # -------------------------- usual final strucuture for uploading and logging the ingestion.
    
    sucess_var = control_sucess(control)

    file_s3= 0
    if control == "OK":
        file_s3, file_size = write_json_to_s3(check_json, BUCKET, RAW_PREFIX, timestamp_SP)
        print(f"LIGHTHOUSE: Json file saved to S3 at: \n {file_s3}")
        print(f"LIGHTHOUSE: Json file size: {file_size} bytes")

    fim = time.perf_counter()
    log_manager = S3LogManager(BUCKET, LOG_PREFIX, control)
    time_var = round((fim - inicio),2)
    log_manager.add_log_entry(NAME_FUN, sucess_var, time_var, control, file_size)

# ! lambda_handler('','') !