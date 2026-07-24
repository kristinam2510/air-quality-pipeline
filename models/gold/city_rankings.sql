{{ config(
    materialized='table',
    schema='gold',
    engine='MergeTree()',
    order_by='City'
) }}

SELECT

    City,

    avg(AQI) AS average_aqi,

    count() AS measurement_days

FROM silver.air_quality_clean

GROUP BY

    City

ORDER BY

    average_aqi DESC
