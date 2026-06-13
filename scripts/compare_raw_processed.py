import pandas as pd
import os

raw_folder = "data/raw"
processed_folder = "data/processed"

for file in os.listdir(raw_folder):

    raw_path = os.path.join(raw_folder, file)

    cleaned_name = file.replace(".csv", "_cleaned.csv")
    processed_path = os.path.join(processed_folder, cleaned_name)

    if os.path.exists(processed_path):

        raw_df = pd.read_csv(raw_path)
        proc_df = pd.read_csv(processed_path)

        print("\n" + "="*60)
        print("FILE:", file)

        print("\nRAW SHAPE:", raw_df.shape)
        print("PROCESSED SHAPE:", proc_df.shape)

        print("\nRAW DUPLICATES:", raw_df.duplicated().sum())
        print("PROCESSED DUPLICATES:", proc_df.duplicated().sum())

        print("\nRAW NULLS:")
        print(raw_df.isnull().sum().sum())

        print("PROCESSED NULLS:")
        print(proc_df.isnull().sum().sum())

        print("\nRAW DTYPES:")
        print(raw_df.dtypes)

        print("\nPROCESSED DTYPES:")
        print(proc_df.dtypes)

        print("\nROWS REMOVED:",
              raw_df.shape[0] - proc_df.shape[0])

        print("COLUMNS ADDED:",
              proc_df.shape[1] - raw_df.shape[1])