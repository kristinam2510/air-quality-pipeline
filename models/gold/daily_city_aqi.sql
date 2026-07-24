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
    count(AQI) AS total_records
FROM {{ ref('air_quality_clean') }}
WHERE AQI IS NOT NULL
AND isFinite(AQI)
GROUP BY
    City,
    Date
