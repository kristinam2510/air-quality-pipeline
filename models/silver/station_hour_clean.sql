{{ config(
    materialized='table',
    engine='ReplacingMergeTree()',
    order_by='(StationId, Datetime)'
) }}

SELECT *

FROM bronze.station_hour_raw
