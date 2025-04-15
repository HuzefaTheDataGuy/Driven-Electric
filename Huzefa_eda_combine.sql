------------------------------------------------------
-- DS 9 --
SELECT * FROM DS9_SALES_AND_MARKET_SHARE_FINAL;

-- comparing ev market share (DE, Europe, Global):
SELECT  brand,
        round(sum(germany_bev_share)) AS share_ev_de,
        round(sum(eu_bev_share)) AS share_ev_europe,
        round(sum(global_bev_share)) AS share_ev_global
FROM DS9_SALES_AND_MARKET_SHARE_FINAL
GROUP BY brand;

-- EV share in germany yearly (From HIGH to LOW):
SELECT  YEAR,
        brand,
        germany_bev_share
FROM DS9_SALES_AND_MARKET_SHARE_FINAL
ORDER BY germany_bev_share desc;

-- Total car sales vs EV car sales germany combined:
SELECt  brand,
        sum(germany_market_sales_bev) AS total_car_sales_de,
        sum(global_market_sales_bev) AS total_car_sales_global
FROM DS9_SALES_AND_MARKET_SHARE_FINAL
GROUP BY brand;

-- Which brand is leading in Germany in 2024:
SELECT  brand,
        sum(germany_market_sales_bev) AS total_car_sales_de_2024
FROM DS9_SALES_AND_MARKET_SHARE_FINAL
WHERE YEAR = 2024
GROUP BY brand
ORDER BY total_car_sales_de_2024 desc;

------------------------------------------------------
-- DS 8 --
SELECT * FROM DS8_NEW_EL_CAR_SALES_SHARE_IN_GERMANY;

-- im not sure this is kinda same as DS9

------------------------------------------------------
-- DS 7 --
SELECT * FROM DS7_E_CAR_SALES;

-- Which brand is leading in Germany in 2024:
SELECT  brand,
        bev_sales,
        market_share_per,
        all_sales
FROM DS7_E_CAR_SALES
WHERE brand != 'TOTAL MARKET'
ORDER BY bev_sales desc;

