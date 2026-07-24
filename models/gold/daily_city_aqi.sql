{{ config(
    materialized='incremental',
    engine='MergeTree()',
    order_by=['City','Date']
) }}

SELECT
    City,
    Date,
    avgIf(AQI, isFinite(AQI)) AS avg_aqi,
    maxIf(AQI, isFinite(AQI)) AS max_aqi,
    minIf(AQI, isFinite(AQI)) AS min_aqi,
    countIf(isFinite(AQI)) AS total_records

FROM silver.air_quality_clean

{% if is_incremental() %}

WHERE Date >
(
    SELECT max(Date)
    FROM {{ this }}
)

{% endif %}

GROUP BY
    City,
    Date
