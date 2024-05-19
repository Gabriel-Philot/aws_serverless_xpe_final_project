from typing import List, Optional
from pydantic import BaseModel, ValidationError

class Stocks_scruct(BaseModel):
    symbol: str
    averageDailyVolume10Day: Optional[int] = None
    averageDailyVolume3Month: Optional[int] = None
    currency: str
    earningsPerShare: Optional[float] = None
    fiftyTwoWeekHigh: Optional[float] = None
    fiftyTwoWeekLow: Optional[float] = None
    marketCap: Optional[int] = None
    priceEarnings: Optional[float] = None
    longName: str
    shortName: str
    regularMarketPrice: Optional[float] = None
    regularMarketChange: Optional[float] = None
    regularMarketChangePercent: Optional[float] = None
    regularMarketDayHigh: Optional[float] = None
    regularMarketDayLow: Optional[float] = None
    regularMarketDayRange: Optional[str] = None
    regularMarketOpen: Optional[float] = None
    regularMarketPreviousClose: Optional[float] = None
    regularMarketTime: Optional[str] = None
    regularMarketVolume: Optional[int] = None
    twoHundredDayAverage: Optional[float] = None
    twoHundredDayAverageChange: Optional[float] = None
    twoHundredDayAverageChangePercent: Optional[float] = None

def validate_data_stocks(data):
    data_dicts = []
    for result in data:
        try:
            stocks = Stocks_scruct(**result)
            data_dicts.append(stocks.dict())
        except ValidationError as e:
            print(f"Validation error: {e}")
            continue
    return data_dicts