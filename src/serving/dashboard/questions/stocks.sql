-- Relative Price Change stocks -> Pos/Nega

WITH base_stock AS (
    SELECT 
        symbol,
        shortname,
        CAST(regularmarketprice AS double) AS regularmarketprice,
        dateingestion_sp
    FROM 
        "xpe-pa".stockapi
),
price_summary AS (
    SELECT
        symbol,
        AVG(regularmarketprice) AS avg_price,
        MAX(dateingestion_sp) AS latest_date
    FROM
        base_stock
    GROUP BY
        symbol
),
latest_prices AS (
    SELECT
        b.symbol,
        b.shortname,
        b.regularmarketprice,
        s.avg_price,
        b.regularmarketprice - s.avg_price AS price_diff
    FROM
        base_stock b
    JOIN
        price_summary s
    ON
        b.symbol = s.symbol
    WHERE
        b.dateingestion_sp = s.latest_date
)
-- Top 10 Positive Variations
SELECT 
    symbol,
    shortname,
    price_diff,
    'positive' AS direction
FROM 
    latest_prices
WHERE 
    price_diff > 0
ORDER BY 
    price_diff DESC
LIMIT 10

-- -- Top 10 Negative Variations
-- SELECT 
--     symbol,
--     shortname,
--     price_diff,
--     'negative' AS direction
-- FROM 
--     latest_prices
-- WHERE 
--     price_diff < 0
-- ORDER BY 
--     price_diff ASC
-- LIMIT 10;
