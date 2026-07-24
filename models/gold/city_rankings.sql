{{ config(
    materialized='table'
) }}

SELECT
    City,
    avg(avg_aqi) AS average_aqi,
    count() AS measurement_days

FROM {{ ref('daily_city_aqi') }}

WHERE isFinite(avg_aqi)

GROUP BY City

ORDER BY average_aqi DESC
