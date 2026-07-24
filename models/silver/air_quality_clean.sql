{{ config(
    materialized='table',
    schema='silver'
) }}

SELECT
    City,
    Date,

    if(isNaN(PM25), NULL, PM25) AS PM25,
    if(isNaN(PM10), NULL, PM10) AS PM10,
    if(isNaN(NO), NULL, NO) AS NO,
    if(isNaN(NO2), NULL, NO2) AS NO2,
    if(isNaN(NOx), NULL, NOx) AS NOx,
    if(isNaN(NH3), NULL, NH3) AS NH3,
    if(isNaN(CO), NULL, CO) AS CO,
    if(isNaN(SO2), NULL, SO2) AS SO2,
    if(isNaN(O3), NULL, O3) AS O3,
    if(isNaN(AQI), NULL, AQI) AS AQI,

    Benzene,
    Toluene,
    Xylene,
    AQI_Bucket

FROM {{ source('bronze','city_day_raw') }}
