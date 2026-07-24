SELECT *
FROM {{ ref('air_quality_clean') }}

WHERE AQI < 0
