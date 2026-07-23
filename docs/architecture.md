# Air Quality Data Pipeline Architecture


## Overview

Pipeline follows Medallion Architecture:

Source → Bronze → Silver → Gold


---

# Source Layer

Input:

CSV Files

- city_day.csv
- city_hour.csv
- station_day.csv
- station_hour.csv
- stations.csv



---

# Bronze Layer

Technology:

ClickHouse


Purpose:

Store raw data without transformation.


Tables:
bronze.city_day_raw

bronze.city_hour_raw

bronze.station_day_raw

bronze.station_hour_raw

bronze.stations_raw



Additional Metadata:

- batch_id
- source_file
- ingestion_timestamp



---

# Silver Layer

Technology:

dbt + ClickHouse


Purpose:

Clean and transform raw data.


Operations:

- Data type conversion
- Null handling
- Duplicate removal
- Standardization
- Quality checks


Tables:
silver.city_air_quality

silver.station_air_quality




---

# Gold Layer

Purpose:

Analytics-ready datasets.


Tables:
gold.daily_aqi_summary

gold.city_pollution_analysis

gold.station_performance




---

# Data Flow

CSV Files

|

v

Airflow DAG

|

v

ClickHouse Bronze

|

v

dbt Transformations

|

v

Silver Tables

|

v

Gold Analytics




# Tools Used


| Tool | Purpose |
|-|-|
| Airflow | Pipeline orchestration |
| ClickHouse | Data warehouse |
| dbt | Transformation |
| Python | Data processing |
| Git | Version control |

Save.
