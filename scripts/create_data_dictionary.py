import pandas as pd
import os


DATA_PATH = "data"
OUTPUT_FILE = "docs/data_dictionary.md"


with open(OUTPUT_FILE, "w") as f:

    f.write("# Air Quality Dataset Data Dictionary\n\n")


    for file in sorted(os.listdir(DATA_PATH)):

        if file.endswith(".csv"):

            print("Processing:", file)

            df = pd.read_csv(
                os.path.join(DATA_PATH, file),
                low_memory=False
            )


            f.write(f"\n\n## {file}\n\n")


            f.write(
                "| Column | Data Type | Missing Values |\n"
            )

            f.write(
                "|---|---|---|\n"
            )


            for column in df.columns:

                missing = df[column].isnull().sum()

                datatype = df[column].dtype


                f.write(
                    f"| {column} | {datatype} | {missing} |\n"
                )


print("Data dictionary created successfully")
