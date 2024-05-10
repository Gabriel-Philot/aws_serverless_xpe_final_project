from typing import List, Dict
from pydantic import BaseModel
import pandas as pd

class HistoricalPrice(BaseModel):
    date: int
    open: float  
    high: float
    low: float
    close: float
    volume: int
    adjustedClose: float
    
class HistoricalPrices(BaseModel):
    prices: List[HistoricalPrice]
    symbol: str


def process_Df_hist_stocks(data):
    
    historical_prices = pd.DataFrame()

    for result in data:
        symbol = result['symbol']
        prices = [p.dict() for p in [HistoricalPrice(**p) for p in result['historicalDataPrice']]]
        

        df = pd.DataFrame(prices)
        df['symbol'] = symbol
        df['date'] = pd.to_datetime(df.date, unit='s').dt.strftime('%Y-%m-%d')

        historical_prices = pd.concat([historical_prices, df]) \
            .reset_index(drop=True)

    return historical_prices



class InflationPrice(BaseModel):
    date: str
    epochDate: int 
    value: float


class InflationPrices(BaseModel):
    prices: List[InflationPrice]


def process_inflation_hist(data: List[Dict]) -> pd.DataFrame:

    inflation_hist = pd.DataFrame()

    for result in data:
        price = InflationPrice(**result)
        
        df = pd.DataFrame([price.dict()])
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
        # Guess it is the raw data value cause its equal to date column so i wil drop it
        #df['epochDate'] = pd.to_datetime(df['epochDate'], unit='ms').dt.strftime('%Y-%m-%d')
        df = df.drop(columns=['epochDate'])

        inflation_hist = pd.concat([inflation_hist, df]) \
            .reset_index(drop=True)

    return inflation_hist


from typing import List
from pydantic import BaseModel

class CashDividend(BaseModel):
    approvedOn: str 
    assetIssued: str
    isinCode: str
    label: str
    lastDatePrior: str
    paymentDate: str
    rate: float
    relatedTo: str
    remarks: str

class StockDividendsData(BaseModel):
    symbol: str 
    dividends: List[CashDividend]


def process_dividends_df(data_div):

    dividends_data = []
    
    for stock in data_div:
       symbol = stock['symbol']
       dividends = [CashDividend(**d) for d in stock['dividendsData']['cashDividends']]
       dividends_data.append(StockDividendsData(symbol=symbol, dividends=dividends))

    dividends_df = pd.DataFrame()

    for data in dividends_data:
        for dividend in data.dividends:
            dividend_dict = dividend.dict()
            dividend_dict['symbol'] = data.symbol
            
            df = pd.DataFrame(dividend_dict, index=[0])
            dividends_df = pd.concat([dividends_df, df])

    return dividends_df


def move_column(df, col_name, new_position):
    
    # Obtem coluna que será movida
    col = df[col_name]
    
    # Remove a coluna
    df = df.drop(col_name, axis=1)  
    
    # Insere na nova posição
    df.insert(new_position, col_name, col)
    
    return df