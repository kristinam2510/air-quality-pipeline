{{ config(
    materialized='table',
    engine='ReplacingMergeTree()',
    order_by='(StationId, Date)'
) }}

SELECT *

FROM bronze.station_day_raw
