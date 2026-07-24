SELECT
    City,
    Date,
    count(*) AS duplicates

FROM {{ ref('air_quality_clean') }}

GROUP BY
    City,
    Date

HAVING count(*) > 1
