from typing import Optional

from pydantic import BaseModel

class Coin(BaseModel):
    currency: str
    currencyRateFromUSD: float
    coinName: str 
    coin: str
    regularMarketChange: float
    regularMarketPrice: float
    regularMarketChangePercent: float
    regularMarketDayLow: float
    regularMarketDayHigh: float 
    regularMarketDayRange: str
    regularMarketVolume: float
    marketCap: float
    regularMarketTime: str
    coinImageUrl: Optional[str] = None

def validate_coin_data(data):

    data_dicts = []

    for result in data:
        coin = Coin(**result)
        
        data_dicts.append(coin.dict())

    return data_dicts