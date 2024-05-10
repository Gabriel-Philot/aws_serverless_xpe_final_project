import requests
#
def web_scrap_info_money(url):
  """
  Requests of the web screp Infomoney.

 Return: json_file
  """

  try:
    response = requests.get(url)
    
    if response.status_code != 200:
      return False
    
    data = response.json()
    
    return data

  except:
    return False
  


from pydantic import BaseModel
from typing import Optional, List

class Check_webcrap_fiis_infom(BaseModel):
    Id: str
    DateRef: str
    cnpj: str
    ticker: str
    razao_social: Optional[str] = None
    market_cap: Optional[float] = None
    preco_do_etf: Optional[float] = None
    preco_do_etf_tolerancia_de_10dus: Optional[float] = None
    book_value: Optional[float] = None
    pb: Optional[float] = None
    volume_medio_21du: Optional[float] = None
    volume_total_negociado_21du: Optional[float] = None
    giro_21du_pct: Optional[float] = None
    patrimonio_contabil: Optional[float] = None
    quant_cotas: Optional[float] = None
    data_de_referencia_do_informe_mensal: Optional[str] = None
    ret_semana: Optional[float] = None
    ret_mes: Optional[float] = None
    ret_12m: Optional[float] = None
    ultimo_rendimento: Optional[float] = None
    data_ultimo_rendimento: Optional[str] = None
    soma_proventos_12m: Optional[float] = None
    yield_1m: Optional[float] = None
    yield_12m: Optional[float] = None
    tipo_de_investimento: Optional[str] = None
    tipo_de_lastro: Optional[str] = None
    tipo_de_renda: Optional[str] = None
    FII_PVPA: Optional[float] = None
    cotistas: Optional[float] = None 
    valor_cota: Optional[float] = None
    taxa_administracao: Optional[float] = None
    taxa_performance: Optional[str] = None
    riskscore: Optional[float] = None

# Usage


def validate_data(json_data: List[dict]) -> str:

    validated_data = []

    for data in json_data:
        validated_element = Check_webcrap_fiis_infom(**data)
        validated_data.append(validated_element.dict())

    return validated_data