# Phase 7 — Data Quality Testing
## Air Quality Data Pipeline

## Overview

The Data Quality Testing phase ensures that the Silver Layer contains reliable, accurate, and consistent data before moving into the Gold Layer.

Testing is performed using:

- dbt tests
- SQL validation queries
- Data quality checks

The objective is to detect:
- Missing values
- Duplicate records
- Invalid measurements
- Data consistency issues

---

# Data Quality Architecture


Bronze Layer
|
|
v
Silver Layer (dbt Models)
|
|
v
Data Quality Tests
|
|
v
Validated Silver Layer


---

# Tools Used

| Tool | Purpose |
|---|---|
| dbt | Automated data testing |
| ClickHouse SQL | Manual validation queries |
| Python | Additional validation scripts |

---

# Tests Implemented

## 1. Null Checks

Null checks ensure that important columns contain valid values.

### air_quality_clean

Checked columns:

| Column | Reason |
|---|---|
| City | Required for city-level analysis |
| Date | Required for time-based analysis |
| AQI | Required for air quality calculations |

Example:

```yaml
- name: City
  tests:
    - not_null
city_hour_clean

Checked columns:

Column	Reason
City	Identifies measurement location
Datetime	Required for hourly analysis
station_clean

Checked columns:

Column	Reason
station_id	Required station identifier
city	Required station location
station_day_clean

Checked columns:

Column	Reason
StationId	Links measurements to stations
Date	Required for daily trends
station_hour_clean

Checked columns:

Column	Reason
StationId	Station identification
Datetime	Hourly timestamp validation
2. Duplicate Checks

Duplicate records can affect analytics accuracy.

A uniqueness test was added for station identifiers.

Example:

- name: station_id
  tests:
    - unique

This ensures every monitoring station has a unique identifier.

3. Range Validation

Range checks verify that numerical measurements contain valid values.

AQI Validation

Rule:

AQI >= 0

Validation query:

SELECT *
FROM silver.air_quality_clean
WHERE AQI < 0;

Expected result:

0 rows
PM2.5 Validation

Rule:

PM25 >= 0

Validation query:

SELECT *
FROM silver.air_quality_clean
WHERE PM25 < 0;

Expected result:

0 rows
dbt Test Configuration

Location:

models/
└── silver/
    └── schema.yml

The schema file contains:

Model descriptions
Column descriptions
Not-null tests
Unique tests
Running Data Quality Tests

Command:

dbt test

Expected output:

PASS
WARN=0
ERROR=0
Manual Validation Queries
Check Missing AQI Values
SELECT count()
FROM silver.air_quality_clean
WHERE AQI IS NULL;
Check Missing City Values
SELECT count()
FROM silver.air_quality_clean
WHERE City IS NULL;
Check Duplicate Stations
SELECT
    station_id,
    count()

FROM silver.station_clean

GROUP BY station_id

HAVING count() > 1;

Expected:

0 rows
Validation Results
Check	Status
Null checks	✅ Passed
Unique station IDs	✅ Passed
AQI range validation	✅ Passed
PM2.5 range validation	✅ Passed
Silver layer validation	✅ Completed
