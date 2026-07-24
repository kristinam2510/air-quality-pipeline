{{ config(
    materialized='table',
    engine='ReplacingMergeTree()',
    order_by='(City, Date)'
) }}

SELECT

    City,

    Date,

    coalesce(PM25,0) AS PM25,
    coalesce(PM10,0) AS PM10,
    coalesce(NO,0) AS NO,
    coalesce(NO2,0) AS NO2,
    coalesce(NOx,0) AS NOx,
    coalesce(NH3,0) AS NH3,
    coalesce(CO,0) AS CO,
    coalesce(SO2,0) AS SO2,
    coalesce(O3,0) AS O3,

    Benzene,
    Toluene,
    Xylene,

    AQI,
    AQI_Bucket

FROM bronze.city_day_raw

WHERE AQI IS NOT NULL
