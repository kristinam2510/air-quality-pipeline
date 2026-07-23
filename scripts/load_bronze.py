import pandas as pd
from clickhouse_driver import Client
from datetime import datetime
import uuid
import os


# =====================================
# ClickHouse connection
# =====================================

client = Client(
    host="localhost",
    user="default",
    password="clickhouse123",
    database="bronze"
)


# =====================================
# Config
# =====================================

file_path = "data/city_day.csv"

table_name = "bronze.air_quality_raw"


# =====================================
# Metadata
# =====================================

batch_id = str(uuid.uuid4())
load_timestamp = datetime.now()


# =====================================
# Read CSV
# =====================================

print("Loading file:", file_path)

df = pd.read_csv(file_path)

print("Rows loaded:", len(df))


# =====================================
# Rename columns
# =====================================

df.rename(
    columns={
        "PM2.5": "PM25"
    },
    inplace=True
)


# =====================================
# Metadata columns
# =====================================

df["source_file"] = os.path.basename(file_path)

df["batch_id"] = batch_id

df["load_timestamp"] = load_timestamp


# =====================================
# Replace NaN
# =====================================

df = df.where(pd.notnull(df), None)


# =====================================
# Date conversion
# =====================================

df["Date"] = pd.to_datetime(
    df["Date"]
).dt.date


# =====================================
# String conversions
# =====================================

string_columns = [
    "City",
    "AQI_Bucket",
    "source_file",
    "batch_id"
]


for col in string_columns:
    df[col] = df[col].apply(
        lambda x: str(x) if x is not None else None
    )


# =====================================
# Column order
# =====================================

columns = [
    "City",
    "Date",
    "PM25",
    "PM10",
    "NO",
    "NO2",
    "NOx",
    "NH3",
    "CO",
    "SO2",
    "O3",
    "Benzene",
    "Toluene",
    "Xylene",
    "AQI",
    "AQI_Bucket",
    "source_file",
    "batch_id",
    "load_timestamp"
]


df = df[columns]


# =====================================
# Convert to tuples
# =====================================

data = [
    tuple(row)
    for row in df.itertuples(
        index=False,
        name=None
    )
]


print("Prepared rows:", len(data))


# =====================================
# Insert
# =====================================

client.execute(
    f"""
    INSERT INTO {table_name}
    VALUES
    """,
    data
)


print("==============================")
print("Bronze ingestion completed")
print("Rows inserted:", len(data))
print("Batch:", batch_id)
print("==============================")
