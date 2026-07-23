# Phase 5 — Kafka Streaming Layer

## Objective
Implement real-time air quality event ingestion using Apache Kafka.

## Architecture

IoT Sensors
      |
      v
Kafka Topic
air_quality_events
      |
      v
Consumer
      |
      v
ClickHouse Bronze Layer


## Kafka Setup

Kafka was deployed using Docker in KRaft mode.

## Topic Created

Topic:
air_quality_events


## Producer Test

Sample event:

{
 "city":"Delhi",
 "pm25":120,
 "time":"2026-07-23"
}


## Consumer Output

Successfully consumed:

{
 "city":"Delhi",
 "pm25":120,
 "time":"2026-07-23"
}

{
 "city":"Pune",
 "pm25":45,
 "time":"2026-07-23"
}


## Status

Kafka streaming infrastructure completed.
