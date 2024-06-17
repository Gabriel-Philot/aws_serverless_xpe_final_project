
-- Model: dbml about our v0 tables in the aws_glue_catalog.

-- crypto-cryptos
-- div_hist
-- stockapi
-- webscrap-fiis-fiis


Table stock_api {
  regularmarketprice double
  regularmarketchange double
  regularmarketvolume bigint
  averagedailyvolume10day string
  averagedailyvolume3month string
  currency string
  fiftytwoweekhigh double
  fiftytwoweeklow double
  longname string
  shortname string
  symbol string
  twohundreddayaverage string
  twohundreddayaveragedate string
  twohundreddayaveragechange string
  date_ingestion int
  dateingestion_sp string
  processing_date timestamp
  data_col_calc string
  daily_return double
}

Table historical_dividend {
  date string
  symbol string
  close float
  adjustedclose float
  volume int
  last_dividend_date string
  last_dividend_rate float
}

Table stock_dividend {
  stock_symbol string
  dividend_symbol string
}



Ref: stock_api.symbol < stock_dividend.stock_symbol
Ref: historical_dividend.symbol < stock_dividend.dividend_symbol