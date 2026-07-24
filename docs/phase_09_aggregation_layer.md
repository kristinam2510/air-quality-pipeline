# Phase 09 — Aggregation Layer Optimization

## Objective

Improve dashboard query performance by creating pre-aggregated analytics tables.

## Technology

ClickHouse AggregatingMergeTree

## Table Created

gold.aqi_summary_agg

## Stored Metrics

- Average AQI
- Maximum AQI
- Minimum AQI
- Total Records

## Source

gold.daily_city_aqi

## Benefits

- Faster dashboard queries
- Reduced repeated calculations
- Optimized analytical workloads

## Validation

Aggregation table successfully created and tested.

Example query:

SELECT
City,
avgMerge(avg_aqi_state),
maxMerge(max_aqi_state),
minMerge(min_aqi_state)
FROM gold.aqi_summary_agg
GROUP BY City;
