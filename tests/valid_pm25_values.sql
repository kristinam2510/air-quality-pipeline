SELECT *
FROM {{ ref('air_quality_clean') }}

WHERE PM25 < 0

