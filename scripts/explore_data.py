import pandas as pd
import os


DATA_PATH = "data"


for file in os.listdir(DATA_PATH):

    if file.endswith(".csv"):

        print("\n" + "=" * 60)
        print("FILE:", file)
        print("=" * 60)

        df = pd.read_csv(
            os.path.join(DATA_PATH, file),
            low_memory=False
        )

        print("\nRows and Columns:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())
