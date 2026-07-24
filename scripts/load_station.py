import pandas as pd
from clickhouse_driver import Client
import uuid


client = Client(
    host='localhost',
    user='default',
    password='clickhouse123',
    database='bronze'
)


file_path = "data/stations.csv"

print("Loading stations.csv")


# Read CSV correctly
df = pd.read_csv(file_path, encoding="utf-8-sig")


print("Rows loaded:", len(df))


# Rename columns
df = df.rename(columns={
    "StationId": "station_id",
    "StationName": "station_name",
    "City": "city",
    "State": "state",
    "Status": "status"
})


# Fill missing status values
df["status"] = df["status"].fillna("")


# Metadata
df["source_file"] = "stations.csv"
df["batch_id"] = str(uuid.uuid4())


# Select columns matching ClickHouse
df = df[
    [
        "station_id",
        "station_name",
        "city",
        "state",
        "status",
        "source_file",
        "batch_id"
    ]
]


data = [
    tuple(row)
    for row in df.to_numpy()
]


print("Prepared rows:", len(data))


client.execute(
    """
    INSERT INTO bronze.station_raw
    (
        station_id,
        station_name,
        city,
        state,
        status,
        source_file,
        batch_id
    )
    VALUES
    """,
    data
)


print("Station data inserted successfully")
