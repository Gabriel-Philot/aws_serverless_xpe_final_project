
-- btc_lines can change for ect with the coin -> ETC
with 
base_cripto as ( 

SELECT 
  coin, 
  regularmarketprice,
  date_format(CAST(dateingestion_sp AS timestamp), '%Y-%m-%d') AS datecoin
FROM 
    "xpe-pa"."crypto-cryptos"
WHERE 
    coin = 'BTC'
ORDER BY 
    dateingestion_sp DESC

)

SELECT * FROM base_cripto; 


-- btc_card

with 
base_cripto as ( 

SELECT 
  coin, 
  coinname, 
  currency, 
  marketcap, 
  regularmarketprice,
  cast(round(regularmarketchangepercent,1) AS VARCHAR) || '%' AS regularmarketchangepercent
FROM 
    "xpe-pa"."crypto-cryptos"
WHERE 
    dateingestion_sp = (SELECT MAX(dateingestion_sp) FROM "xpe-pa"."crypto-cryptos")
    AND coin = 'BTC'

)

SELECT * FROM base_cripto;

-- cripto_last update

SELECT
   DATE_ADD('hour', 3, CAST(dateingestion_sp AS TIMESTAMP)) as updated_timestamp
   FROM
    "xpe-pa"."crypto-cryptos"
WHERE 
    dateingestion_sp = (SELECT MAX(dateingestion_sp) FROM "xpe-pa"."crypto-cryptos")
    AND coin = 'BTC'