{{ config(
    materialized='table',
    engine='ReplacingMergeTree()',
    order_by='station_id'
) }}

SELECT
    station_id,
    station_name,
    city,
    state,
    status,
    source_file,
    batch_id,
    load_timestamp
FROM bronze.station_raw
