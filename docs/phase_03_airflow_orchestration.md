# Phase 3 — Airflow Pipeline Orchestration Setup

## Objective

Automate the air quality data pipeline workflow using Apache Airflow.

## Architecture

CSV Dataset
|
↓
PostgreSQL Staging
|
↓
Apache Airflow
|
↓
ClickHouse Bronze Layer
|
↓
dbt Transformation


## DAG Name

air_quality_pipeline

## Workflow


Start

↓

Check Dataset

↓

Validate CSV

↓

Load Data

↓

Trigger dbt

↓

Data Quality Check

↓

Finish


## Tasks Implemented

### check_dataset
Checks availability of required CSV files.

### validate_csv
Validates:
- File existence
- CSV structure
- Required columns

### load_data
Loads raw data into ClickHouse Bronze Layer.

### trigger_dbt
Triggers dbt transformation workflow.

### data_quality_check
Runs final validation checks.

## Airflow Features Implemented

- DAG scheduling
- Task dependency management
- Retry handling
- Execution logging
- Failure handling

## Testing

Command:


airflow dags test air_quality_pipeline 2026-07-23


Result:


Dag run in success state


## Deliverable

Working Airflow DAG successfully created and tested.
