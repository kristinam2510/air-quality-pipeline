# Phase 6 — Silver Layer Documentation
## Air Quality Data Pipeline

## Overview

The Silver Layer is the cleaned and standardized layer of the Air Quality Data Pipeline.

It transforms raw Bronze data stored in ClickHouse into reliable analytical tables using dbt.

The purpose of this layer is:

- Standardize column names
- Clean raw data
- Handle missing values
- Create structured tables for analytics
- Provide trusted datasets for the Gold Layer

---

# Architecture


CSV Files
|
|
v
Bronze Layer (ClickHouse Raw Tables)
|
|
v
Silver Layer (dbt Transformations)
|
|
v
Gold Layer (Analytics)


---

# Tools Used

| Tool | Purpose |
|---|---|
| ClickHouse | Data warehouse |
| dbt | Transformation framework |
| SQL | Data transformations |
| Python | Data ingestion |
| Airflow | Pipeline orchestration |

---

# Bronze to Silver Mapping

| Bronze Table | Silver Table | Description |
|---|---|---|
| bronze.city_day_raw | silver.air_quality_clean | Daily city-level air quality |
| bronze.city_hour_raw | silver.city_hour_clean | Hourly city-level air quality |
| bronze.station_raw | silver.station_clean | Monitoring station information |
| bronze.station_day_raw | silver.station_day_clean | Daily station measurements |
| bronze.station_hour_raw | silver.station_hour_clean | Hourly station measurements |

---

# Silver Tables

## 1. air_quality_clean

Source:


bronze.city_day_raw


Purpose:

Stores cleaned daily air quality measurements.

Columns:

- City
- Date
- PM25
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3
- Benzene
- Toluene
- Xylene
- AQI
- AQI_Bucket


Transformation:

- Standardized date format
- Removed invalid AQI records
- Prepared pollutant values for analytics


---

## 2. city_hour_clean

Source:


bronze.city_hour_raw


Purpose:

Stores hourly city-level pollution measurements.

Columns:

- City
- Datetime
- PM25
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3
- Benzene
- Toluene
- Xylene
- AQI
- AQI_Bucket


Transformation:

- Standardized datetime column
- Removed invalid AQI records
- Prepared hourly pollution trends


---

## 3. station_clean

Source:


bronze.station_raw


Purpose:

Stores air quality monitoring station details.

Columns:

- station_id
- station_name
- city
- state
- status
- source_file
- batch_id
- load_timestamp


Transformation:

- Standardized station metadata
- Added ingestion metadata


---

## 4. station_day_clean

Source:


bronze.station_day_raw


Purpose:

Stores daily measurements from monitoring stations.


Transformation:

- Preserved station measurements
- Standardized structure
- Added analytical readiness


---

## 5. station_hour_clean

Source:


bronze.station_hour_raw


Purpose:

Stores hourly station measurements.


Transformation:

- Standardized datetime handling
- Prepared for time-series analysis


---

# dbt Models

Location:


models/
|
├── silver/
│
├── air_quality_clean.sql
├── city_hour_clean.sql
├── station_clean.sql
├── station_day_clean.sql
└── station_hour_clean.sql


---

# Materialization Strategy

All Silver models use:


materialized='table'


ClickHouse Engine:


ReplacingMergeTree()


Ordering keys:

| Table | Order By |
|---|---|
| air_quality_clean | City, Date |
| city_hour_clean | City, Datetime |
| station_clean | station_id |
| station_day_clean | StationId, Date |
| station_hour_clean | StationId, Datetime |

---

# Data Quality Testing

dbt tests implemented:

## Not Null Tests

Ensures important fields exist.

Examples:


City
Date
StationId
station_id


---

## Unique Tests

Ensures station identifiers are unique.

Example:


station_id


---

# Test Results

Command:


dbt test


Result:


PASS=8
WARN=0
ERROR=0
SKIP=0


All Silver layer quality checks passed.

---

# Row Count Validation

Expected Silver row counts:

| Table | Approximate Rows |
|---|---:|
| air_quality_clean | 29,531 |
| city_hour_clean | 1,415,750 |
| station_clean | 229 |
| station_day_clean | 216,070 |
| station_hour_clean | 5,178,166 |

---

# dbt Documentation

Generated using:


dbt docs generate


Generated files:


target/
├── manifest.json
└── catalog.json


These files contain:

- Model metadata
- Column information
- Lineage information
- Database relationships


---

# Phase 6 Completion Status

| Task | Status |
|---|---|
| Silver models created | ✅ |
| Bronze-Silver mapping completed | ✅ |
| dbt transformations completed | ✅ |
| Data quality tests passed | ✅ |
| Documentation generated | ✅ |


---

# Next Phase

## Phase 7 — Gold Layer

The Gold Layer will create analytics-ready tables:

- City pollution ranking
- AQI trends
- Pollution summaries
- Station performance metrics

Architecture after completion:


Bronze
|
v
Silver
|
v
Gold
|
v
Dashboard / Analytics

