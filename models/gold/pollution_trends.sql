{{ config(
    materialized='table',
    schema='gold',
    engine='MergeTree()',
    order_by='(City, Date)'
) }}

SELECT
    City,
    Date,
    avg(PM25) AS avg_pm25,
    avg(PM10) AS avg_pm10,
    avg(NO2) AS avg_no2,
    avg(CO) AS avg_co,
    avg(SO2) AS avg_so2,
    avg(O3) AS avg_o3
FROM {{ ref('air_quality_clean') }}
WHERE isFinite(PM25)
AND isFinite(PM10)
AND isFinite(NO2)
AND isFinite(CO)
AND isFinite(SO2)
AND isFinite(O3)
GROUP BY
    City,
    Date

