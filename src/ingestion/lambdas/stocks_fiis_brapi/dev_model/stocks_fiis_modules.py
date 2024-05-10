from typing import List, Dict, Optional
from pydantic import BaseModel

class Stocks_scruct(BaseModel):

    symbol: str
    averageDailyVolume10Day: int 
    averageDailyVolume3Month: int
    currency: str
    earningsPerShare: float
    fiftyTwoWeekHigh: float
    fiftyTwoWeekLow: float
    marketCap: int
    priceEarnings: Optional[float] = None
    longName: str
    shortName: str
    regularMarketPrice: float
    regularMarketChange: float
    regularMarketChangePercent: float
    regularMarketDayHigh: float
    regularMarketDayLow: float
    regularMarketDayRange: str
    regularMarketOpen: float
    regularMarketPreviousClose: float
    regularMarketTime: str
    regularMarketVolume: int
    twoHundredDayAverage: float 
    twoHundredDayAverageChange: float
    twoHundredDayAverageChangePercent: float
    
def validate_data_stocks(data):

    data_dicts = []

    for result in data:
        stocks = Stocks_scruct(**result)  
        
        data_dicts.append(stocks.dict())


    return data_dicts