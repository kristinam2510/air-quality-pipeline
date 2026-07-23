# Phase 2 — PostgreSQL Staging Layer Setup


## Objective

Create PostgreSQL staging environment for metadata management and pipeline logging.


## Architecture
CSV Files

|

v

PostgreSQL Staging Layer



## Database

Database:


air_quality_pipeline



## Schema


staging



## Tables Created


### staging.air_quality_files

Purpose:

Stores dataset file metadata.


Columns:

- file_id
- file_name
- file_path
- file_size
- record_count
- file_type
- ingestion_status
- created_at



### staging.pipeline_logs

Purpose:

Stores pipeline execution logs.


Columns:

- log_id
- pipeline_name
- task_name
- status
- start_time
- end_time
- records_processed
- error_message
- created_at



## Dataset Metadata Loaded

Files:

- city_day.csv
- city_hour.csv
- station_day.csv
- station_hour.csv
- stations.csv



## Status

Phase 2 Completed
