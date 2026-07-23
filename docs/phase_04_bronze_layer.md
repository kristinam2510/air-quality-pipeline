# Phase 4 — Bronze Layer Implementation

## Objective
Store raw air quality data in ClickHouse without transformation.

## Architecture

Airflow
   |
ClickHouse Bronze Layer
   |
MergeTree Tables


## Database

bronze


## Tables Created

- city_day_raw
- city_hour_raw
- station_day_raw
- station_hour_raw
- station_raw


## Metadata Columns

Added:

- source_file
- batch_id
- load_timestamp


## Validation Results

| Table | Rows |
|---|---:|
| city_day_raw | 29531 |
| city_hour_raw | 707875 |
| station_day_raw |108035 |
| station_hour_raw |2589083 |
| station_raw |460 |

## Status

Bronze ingestion completed successfully.
