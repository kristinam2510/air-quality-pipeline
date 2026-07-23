# Air Quality Dataset Relationships


## 1. city_day.csv

Description:
Daily air quality measurements at city level.

Primary Key:

City + Date


Columns:

- City
- Date
- Pollutant measurements
- AQI
- AQI_Bucket



---

## 2. city_hour.csv

Description:
Hourly air quality measurements at city level.

Primary Key:

City + Datetime


Columns:

- City
- Datetime
- Pollutant measurements
- AQI
- AQI_Bucket



---

## 3. station_day.csv

Description:
Daily measurements collected from monitoring stations.

Primary Key:

StationId + Date


Columns:

- StationId
- Date
- Pollutant measurements
- AQI
- AQI_Bucket



---

## 4. station_hour.csv

Description:
Hourly measurements collected from monitoring stations.

Primary Key:

StationId + Datetime


Columns:

- StationId
- Datetime
- Pollutant measurements
- AQI
- AQI_Bucket



---

## 5. stations.csv

Description:

Monitoring station metadata.

Primary Key:

StationId


Contains:

- StationId
- Station name
- City
- State
- Location information



# Dataset Relationships

       stations.csv
                 |
                 |
             StationId
                 |
    -----------------------------
    |                           |
    |                           |

station_day.csv         station_hour.csv

            City
             |
    -------------------
    |                 |
    |                 |

city_day.csv     city_hour.csv



# Data Grain


| Dataset | Grain |
|---|---|
| city_day | One record per city per day |
| city_hour | One record per city per hour |
| station_day | One record per station per day |
| station_hour | One record per station per hour |
| stations | One record per monitoring station |
