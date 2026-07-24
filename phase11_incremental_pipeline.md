# Phase 11 — Incremental Pipeline Optimization

## Objective

Optimize the data pipeline by implementing incremental processing.

Instead of processing the complete dataset (6.8M+ records) on every pipeline run, the pipeline processes only newly added records.

This improves:

- Pipeline execution speed
- Resource utilization
- Scalability
- Production readiness

---

# Current Approach

Before optimization:

```
New Data
   |
   ↓
Full dbt Refresh
   |
   ↓
Process Entire Dataset
(6.8 Million+ records)
```

Problem:

- Repeated computation
- Longer execution time
- Higher resource consumption

---

# Optimized Approach

After incremental implementation:

```
New Data
   |
   ↓
Check latest timestamp
   |
   ↓
Process only new records
   |
   ↓
Append to existing table
```

---

# Technology Used

| Component | Technology |
|---|---|
| Transformation | dbt |
| Database | ClickHouse |
| Materialization | Incremental Models |
| Storage Layer | Gold Layer |

---

# dbt Incremental Model

Example:

```sql
{{ config(
    materialized='incremental',
    engine='MergeTree()',
    order_by=['City','Date']
) }}

SELECT
    City,
    Date,
    avg(AQI) AS avg_aqi,
    max(AQI) AS max_aqi,
    min(AQI) AS min_aqi,
    count() AS total_records
FROM silver.air_quality_clean

{% if is_incremental() %}

WHERE Date >
(
    SELECT max(Date)
    FROM {{ this }}
)

{% endif %}

GROUP BY
    City,
    Date
```

---

# Incremental Logic

The model checks:

```sql
SELECT max(Date)
FROM existing_table
```

Then loads:

```sql
WHERE Date > previous_max_date
```

Only new records are processed.

---

# Performance Improvement

## Before

```
Every run:

6.8M records processed
```

## After

```
Every run:

Only new records processed
```

Benefits:

- Faster execution
- Reduced computation
- Better scalability
- Production-ready architecture

---

# Validation

Check row count:

```sql
SELECT count()
FROM gold.daily_city_aqi;
```

Check latest processed date:

```sql
SELECT max(Date)
FROM gold.daily_city_aqi;
```

---

# Phase 11 Deliverable

Completed:

✅ dbt incremental models  
✅ Optimized data processing  
✅ Reduced pipeline computation  
✅ Production-ready ingestion strategy  

---

# Conclusion

Incremental processing enables the air quality pipeline to efficiently handle continuous data ingestion by processing only new records while maintaining previously transformed data.
