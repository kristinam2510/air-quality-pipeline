# Phase 04: Bronze Layer Implementation

## Objective

The objective of this phase was to ingest raw air quality datasets into the ClickHouse Bronze Layer using Apache Airflow orchestration.

The Bronze layer stores raw source data with minimal transformation to preserve the original dataset for downstream processing.

---

# Architecture

Air Quality CSV Files
|
|
v
Apache Airflow DAG
(bronze_ingestion)
|
|

| |
v v
load_bronze load_station
| |
v v
ClickHouse Bronze Layer


---

# Input Datasets

The following air quality datasets were used for Bronze ingestion:

| Dataset | Description |
|---|---|
| city_day.csv | Daily city-level air quality measurements |
| city_hour.csv | Hourly city-level air quality measurements |
| station_day.csv | Daily monitoring station measurements |
| station_hour.csv | Hourly monitoring station measurements |
| stations.csv | Monitoring station metadata |

---

# Bronze Layer Technology Stack

| Component | Technology |
|---|---|
| Workflow Orchestration | Apache Airflow |
| Storage Layer | ClickHouse |
| Data Format | CSV |
| Programming Language | Python |
| Environment | Python Virtual Environment |

---

# Airflow Implementation

## DAG Name


bronze_ingestion


## DAG Location


/home/kristina_m/airflow/dags/bronze_ingestion_dag.py


---

# Airflow Tasks

The Bronze ingestion DAG contains two main tasks.

## 1. load_bronze

Responsible for loading raw air quality measurement datasets:

- city_day.csv
- city_hour.csv
- station_day.csv
- station_hour.csv

Data is loaded into corresponding ClickHouse Bronze tables.

---

## 2. load_station

Responsible for loading station metadata:

- stations.csv

The station information is stored separately for reference and analytical joins.

---

# Airflow Configuration

## Executor


LocalExecutor


## Virtual Environment


~/air_quality_pipeline/pipeline-env


## Scheduler

The Airflow scheduler was configured to execute queued DAG runs and manage task execution.

The Bronze ingestion DAG was successfully triggered and executed through Airflow.

---

# ClickHouse Bronze Layer

Raw datasets were ingested into ClickHouse without applying business transformations.

The following Bronze tables were created:

| Table Name | Description |
|---|---|
| city_day_raw | Raw daily city-level air quality data |
| city_hour_raw | Raw hourly city-level air quality data |
| station_day_raw | Raw daily station-level air quality data |
| station_hour_raw | Raw hourly station-level air quality data |
| station_raw | Raw station metadata |

---

# Data Lineage and Metadata Columns

Additional metadata columns were added to maintain data lineage and ingestion tracking.

| Column | Description |
|---|---|
| source_file | Name of the original source CSV file |
| batch_id | Unique identifier for each ingestion batch |
| load_timestamp | Timestamp when the record was loaded into ClickHouse |

These columns help track:

- Data origin
- Ingestion batches
- Load history
- Data auditing

---

# Bronze Data Flow


CSV Source Files
|
|
v
Airflow bronze_ingestion DAG
|
|
v
Python Ingestion Process
|
|
v
ClickHouse Bronze Tables
|
|
v
Raw Data Available for Transformation


---

# Validation Results

The Bronze layer ingestion was validated by checking the number of records loaded into ClickHouse tables.

Validation Query:

```sql
SELECT count(*) FROM table_name;
Loaded Record Counts
Table	Rows
city_day_raw	29,531
city_hour_raw	707,875
station_day_raw	108,035
station_hour_raw	2,589,083
station_raw	460
Bronze Layer Validation

The following checks were performed:

Validation	Status
ClickHouse connection	Completed
Airflow DAG execution	Completed
CSV ingestion	Completed
Bronze table creation	Completed
Row count verification	Completed
Metadata column addition	Completed
Final Bronze Layer Status

✅ Bronze ingestion completed successfully.

The pipeline successfully achieved:

Automated ingestion using Apache Airflow
Storage of raw data in ClickHouse
Creation of Bronze layer tables
Data lineage tracking using metadata columns
Successful validation of loaded records
Current Pipeline Status
Phase	Status
Project Setup	Completed
Dataset Understanding	Completed
Data Exploration	Completed
ClickHouse Setup	Completed
Bronze Layer Design	Completed
Airflow DAG Development	Completed
Bronze Data Ingestion	Completed
