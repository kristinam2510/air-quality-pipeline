{{ config(
    materialized='table',
    schema='gold',
    engine='MergeTree()',
    order_by='(City, Date)'
) }}

SELECT

    City,

    Date,

    avg(AQI) AS avg_aqi,

    max(AQI) AS max_aqi,

    min(AQI) AS min_aqi,

    count() AS total_records

FROM silver.air_quality_clean

GROUP BY

    City,
    Date
