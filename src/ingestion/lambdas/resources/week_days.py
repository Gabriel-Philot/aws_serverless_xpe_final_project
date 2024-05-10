from datetime import datetime, timedelta
from pandas.tseries.offsets import BDay
import pandas as pd



def get_previous_business_days(n):
    """
    Retorna uma lista com as datas dos últimos `n-1` dias úteis,
    incluindo a sexta-feira anterior caso o domingo seja a data mais antiga.
    """
    today = datetime.now().date()  - timedelta(days=1)  - timedelta(hours=3)
    dates = pd.date_range(end=today, periods=n, freq='B')
    
    # Se a data mais antiga for um domingo, adicionar a sexta-feira anterior
    if dates[0].weekday() == 6:  # Domingo é 6
        dates = pd.date_range(end=dates[-1] + BDay(1), periods=n+1, freq='B')
    
    return [date.date() for date in dates]