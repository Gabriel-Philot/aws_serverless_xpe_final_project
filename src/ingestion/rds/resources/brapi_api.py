import requests
import logging
from typing import List
from pydantic import BaseModel
import pandas as pd



class Brapi_STOCKS_API:

    def __init__(self, url, tickers, params):
        self.url = url
        self.tickers = tickers
        self.params = params

    def get_quotes(self):
        try:
            ticker_string = ','.join(self.tickers)
            api_url = self.url + ticker_string 
            response = requests.get(api_url, params=self.params)
            
            if response.status_code== 200:
                data = response.json()
                #logging.info("Sucess", response.status_code)  
                return data['results']

                
        except requests.exceptions.RequestException as e:
            return logging.error(f"Request failed: {str(e)} , Request failed with status code {response.status_code}")


class Brapi_notSTOCKS__API:

    def __init__(self, url, params):
        self.url = url
        self.params = params

    def get_other_quotes(self):
        try:
            response = requests.get(self.url, params=self.params)
            if response and response.status_code == 200:
                data = response.json()
                #logging.info("Sucess", response.status_code)  
                return data
            elif response:
                logging.error(f"Request failed with status {response.status_code}")
     
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {str(e)}")