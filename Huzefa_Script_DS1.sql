SELECT *
FROM ds1_ev_cars;

SELECT count(*)
FROM ds1_ev_cars
GROUP BY ;

-- changing the column names:
-- Step 1: Create new table with renamed columns
CREATE TABLE ds1_new_ev_cars AS 
SELECT 
    "battery" AS battery,
    "car_name" AS car_name,
    "car_name_link" AS car_name_link,
    "efficiency" AS efficiency,
    "fast_charge" AS fast_charge,
    "price_de" AS price_de,  -- Special characters handled
    "range" AS ranges_km,
    "top_speed" AS top_speed,
    "acceleration_0_100" AS acceleration_0_100  -- Fixed special characters
FROM ds1_ev_cars;
--------------------------------------------------

--removing NA values:
DELETE FROM ds1_ev_cars WHERE fast_charge = 'NA';

SELECT * FROM ds1_ev_cars WHERE fast_charge = 'NA';
--------------------------------------------------

--creating new table with correct format:
DROP TABLE IF EXISTS ds1_ev_cars1;
CREATE TABLE ds1_ev_cars1 (
        car_name VARCHAR,
        battery NUMERIC NOT NULL, 
        fast_charge NUMERIC NOT NULL,
        ranges_km NUMERIC NOT NULL,
        efficiency NUMERIC NOT NULL,
        top_speed NUMERIC NOT NULL,
        acceleration_0_100 NUMERIC NOT NULL,
        price_de VARCHAR NOT NULL
        );

--filling the data
INSERT INTO ds1_ev_cars1 (
        car_name,
        battery,
        fast_charge,
        ranges_km,
        efficiency,
        top_speed,
        acceleration_0_100,
        price_de
        )
SELECT car_name,
        battery,
        fast_charge,
        ranges_km,
        efficiency,
        top_speed,
        acceleration_0_100,
        price_de
FROM ds1_ev_cars;

--test the new table:
SELECT * FROM ds1_ev_cars1 LIMIT 10;
------------------------------------------------------
-- deleting NA value from column price_de
DELETE FROM ds1_ev_cars1 
WHERE price_de = 'NA';
------------------------------------------------------

--test the new table after removing NA values in Prices_de:
SELECT * FROM ds1_ev_cars1;
------------------------------------------------------

ALTER TABLE ds1_ev_cars1
ALTER COLUMN price_de TYPE NUMERIC
USING CAST(price_de AS NUMERIC);
------------------------------------------------------

--test the new table after removing NA values and formatting in Prices_de:
SELECT * FROM ds1_ev_cars1;
------------------------------------------------------
-- If customer wants best range/fast charge of cars: (Top 10)
-- also adding full charge time in Mins
SELECT car_name,
        battery,
        fast_charge,
        ranges_km,
        efficiency,
        top_speed,
        acceleration_0_100,
        ROUND(((ranges_km/fast_charge)*60),2) AS full_charge_time_mins,
        price_de
FROM ds1_ev_cars1
ORDER BY ranges_km DESC
LIMIT 10;
------------------------------------------------------

-- which car has maximum range
-- also adding full charge time in Mins
SELECT car_name,
        battery,
        fast_charge,
        ranges_km,
        efficiency,
        ROUND(((ranges_km/fast_charge)*60),2) AS full_charge_time_mins,
        price_de
FROM ds1_ev_cars1
ORDER BY ranges_km DESC
LIMIT 1;
------------------------------------------------------

-- which car has minimum range
-- also adding full charge time in Mins
SELECT car_name,
        battery,
        fast_charge,
        ranges_km,
        efficiency,
        ROUND(((ranges_km/fast_charge)*60),2) AS full_charge_time_mins,
        price_de
FROM ds1_ev_cars1
ORDER BY ranges_km ASC
LIMIT 1;
------------------------------------------------------
--(price is not working with DESC/ASC because of formatting issue)
-- If customer wants cheap cars: (Top 10)
SELECT * FROM ds1_ev_cars1
ORDER BY price_de ASC 
LIMIT 10;
-------------------------------------------------------

-- Average price of EV cars:
SELECT round(avg(price_de),2) AS avg_price_ev
FROM ds1_ev_cars1;
-------------------------------------------------------

-- how to calc Median price of EV Cars??
SELECT count(*) FROM ds1_ev_cars1;

SELECT * FROM ds1_ev_cars1
ORDER BY price_de ASC
LIMIT 1 OFFSET (306/2);

-------------------------------------------------------
-- best efficient cars: (Top 10)
SELECT * FROM ds1_ev_cars1
ORDER BY efficiency DESC -- which car has most rating of the vehicle in watt-hours per kilometer (Wh/km)
LIMIT 10;
------------------------------------------------------

-- cars with bigger battery: (Top 10)
SELECT * FROM ds1_ev_cars1
ORDER BY battery DESC
LIMIT 10;
------------------------------------------------------

-- Top 5 fastest EV cars:
SELECT car_name,
        battery,
        fast_charge,
        ranges_km,
        top_speed,
        ROUND(((ranges_km/fast_charge)*60),2) AS full_charge_time_mins,
        price_de
FROM ds1_ev_cars1
ORDER BY top_speed DESC
LIMIT 5;
------------------------------------------------------

-- Avg. range of each brand:
SELECT 
    CASE 
        WHEN POSITION(' ' IN car_name) > 0 
        THEN SUBSTRING(car_name, 1, POSITION(' ' IN car_name) - 1) 
        ELSE car_name 
    END AS Brand, 
    round(AVG(ranges_km)) AS avg_range  
FROM ds1_ev_cars1 
GROUP BY Brand 
ORDER BY avg_range DESC;
-------------------------------------------------------

-- Avg. price of each brand:
SELECT
    CASE 
        WHEN POSITION(' ' IN car_name) > 0 
        THEN SUBSTRING(car_name, 1, POSITION(' ' IN car_name) - 1)
        ELSE Car_name
    END AS Brand, 
    round(AVG(price_de),2) AS avg_price 
FROM ds1_ev_cars1 
GROUP BY Brand 
order by avg_price desc;
-------------------------------------------------------

-- No. of EV Car models per Manufacture:
--(NA Rows are removed)
-- can i do this 
SELECT 
    CASE
        WHEN POSITION(' ' IN car_name) > 0 
        THEN SUBSTRING(car_name, 1, POSITION(' ' IN car_name) - 1)
        ELSE car_name
    END AS Brand, 
    COUNT(*) as count 
FROM ds1_ev_cars1 
GROUP BY Brand 
order by count desc 
;


----------------------------------------

SELECT * FROM ds5_germanygasstations;

SELECT *  FROM DS9_SALES_AND_MARKET_SHARE_FINAL;
-------------------------

--checking datatype for DS1:
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'ds1_ev_cars1';

----------------------------------------
-- update: ds5
-- there is one BERLIN replacing it with Berlin

SELECT * FROM ds5_germanygasstations;

SELECT *
FROM ds5_germanygasstations
WHERE city = 'Berlin';

UPDATE ds5_germanygasstations
SET city = REPLACE(city, ' Berlin', 'Berlin')
WHERE city LIKE '% Berlin%';

SELECT * FROM ds9_sales_and_market_share_final;