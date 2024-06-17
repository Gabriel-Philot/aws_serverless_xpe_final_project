-- fiis_date_data

SELECT 
    DATE_ADD('hour', 3, MIN(CAST(dateingestion_sp AS TIMESTAMP))) AS datefiis_min,
    DATE_ADD('hour', 3, MAX(CAST(dateingestion_sp AS TIMESTAMP))) AS datefiis_max
FROM 
    "xpe-pa"."webscrap-fiis-fiis";

-- total_fiis_analyzed

SELECT 
    COUNT(DISTINCT ticker) as total_fiis_analyzed
FROM 
    "xpe-pa"."webscrap-fiis-fiis";


-- top5_fiis_variation
WITH base_fiis AS (
    SELECT 
        ticker,
        razao_social,
        market_cap,
        dateingestion_sp
    FROM 
        "xpe-pa"."webscrap-fiis-fiis"
),
variation AS (
    SELECT 
        ticker,
        razao_social,
        MAX(market_cap) - MIN(market_cap) AS market_cap_variation
    FROM 
        base_fiis
    GROUP BY 
        ticker, razao_social
)
SELECT 
    ticker,
    razao_social,
    market_cap_variation
FROM 
    variation
ORDER BY 
    market_cap_variation DESC
LIMIT 5;

-- fiis_YTD profitability

WITH base_fiis AS (
    SELECT 
        ticker,
        ret_12m,
        dateingestion_sp
    FROM 
        "xpe-pa"."webscrap-fiis-fiis"
    WHERE ret_12m < 200  -- Exemplo de filtro para valores anormais
),
latest_data AS (
    SELECT
        ticker,
        MAX(dateingestion_sp) AS latest_date
    FROM 
        base_fiis
    GROUP BY 
        ticker
)
SELECT 
    DISTINCT b.ticker,
    b.ret_12m
FROM 
    base_fiis b
JOIN 
    latest_data l
ON 
    b.ticker = l.ticker AND b.dateingestion_sp = l.latest_date
ORDER BY 
    b.ret_12m DESC
    
limit 10
