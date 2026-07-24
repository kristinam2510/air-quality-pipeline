{{ config(
    materialized='table',
    engine='ReplacingMergeTree()',
    order_by='(City, Datetime)'
) }}

SELECT

    City,

    Datetime,

    PM25,
    PM10,
    NO,
    NO2,
    NOx,
    NH3,
    CO,
    SO2,
    O3,
    Benzene,
    Toluene,
    Xylene,
    AQI,
    AQI_Bucket

FROM bronze.city_hour_raw
WHERE AQI IS NOT NULL
