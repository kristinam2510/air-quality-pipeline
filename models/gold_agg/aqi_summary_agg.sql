{{ config(
    materialized='table',
    engine='AggregatingMergeTree()',
    order_by='(City)'
) }}

SELECT

    City,

    avgState(avg_aqi) AS avg_aqi_state,
    maxState(max_aqi) AS max_aqi_state,
    minState(min_aqi) AS min_aqi_state,
    sumState(total_records) AS total_records_state

FROM {{ ref('daily_city_aqi') }}

GROUP BY City
