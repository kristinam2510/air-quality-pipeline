# Production Deployment

## Technologies

- Apache Airflow
- ClickHouse
- dbt
- Metabase
- Docker
- Python

## Pipeline Flow

CSV Files
    ↓
Bronze Layer
    ↓
Silver Layer
    ↓
Gold Layer
    ↓
Metabase Dashboard

## Docker Services

- ClickHouse
- Metabase

## Airflow

The Airflow scheduler automates Bronze layer ingestion and transformation tasks.

## Monitoring

Pipeline execution can be monitored using:

- Airflow DAG status
- dbt logs
- ClickHouse queries

## Backup

ClickHouse data can be backed up using:

- `clickhouse-backup`
- Database snapshots
- CSV exports

## Documentation

All implementation details are available in the `docs` directory.
