import pandas as pd
from pathlib import Path

def preprocess_data():
    ghi_files = Path("data/GHI").rglob("*.csv")

    all_ghi_tables = []
    for file in ghi_files:
        small_table = pd.read_csv(file)
        all_ghi_tables.append(small_table)

    print("Number of files read:", len(all_ghi_tables))
    print(all_ghi_tables[0])

    df_ghi = pd.concat(all_ghi_tables, ignore_index=True)
    print(df_ghi)

    pr_files = Path("data/PR").rglob("*.csv")

    all_pr_tables = []
    for file in pr_files:
        small_table = pd.read_csv(file)
        all_pr_tables.append(small_table)

    print("Number of files read:", len(all_pr_tables))
    print(all_pr_tables[0])

    df_pr = pd.concat(all_pr_tables, ignore_index=True)
    print(df_pr)

    df_merged = pd.merge(df_ghi, df_pr, on="Date")
    print(df_merged)

    df_merged.to_csv("merged_data.csv", index=False)
    print("Saved merged_data.csv")

preprocess_data()