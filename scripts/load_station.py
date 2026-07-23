import pandas as pd
from clickhouse_driver import Client
import uuid
from datetime import datetime


# ClickHouse connection
client = Client(
    host='localhost',
    user='default',
    password='YOUR_PASSWORD',
    database='bronze'
)


# File path
file_path = "data/stations.csv"


print("Loading stations.csv")


# Read CSV
df = pd.read_csv(file_path)


print("Rows loaded:", len(df))


# Rename columns to match ClickHouse
df = df.rename(columns={
    "StationId": "station_id",
    "StationName": "station_name",
    "City": "city",
    "State": "state"
})


# Add missing columns
df["latitude"] = None
df["longitude"] = None


# Metadata columns
df["source_file"] = "stations.csv"
df["batch_id"] = str(uuid.uuid4())


# Select final order matching table
df = df[
    [
        "station_id",
        "station_name",
        "city",
        "state",
        "latitude",
        "longitude",
        "source_file",
        "batch_id"
    ]
]


# Convert dataframe to list of tuples
data = [
    tuple(row)
    for row in df.to_numpy()
]


print("Prepared rows:", len(data))


# Insert
client.execute(
    """
    INSERT INTO bronze.station_raw
    (
        station_id,
        station_name,
        city,
        state,
        latitude,
        longitude,
        source_file,
        batch_id
    )
    VALUES
    """,
    data
)


print("Station data inserted successfully")
