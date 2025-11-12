import pandas as pd
import numpy as np

def stalin_sort_descending_all(csv_file: str, output_file: str):
    df = pd.read_csv(csv_file, skiprows=4) #first 4 rows are information

    numeric_cols = df.select_dtypes(include=[np.number]).columns

    if len(numeric_cols) == 0:
        raise ValueError("no number columns")

    sorted_columns = {}

    for col in numeric_cols:
        data = df[col].dropna().tolist()

        if not data:
            continue

        sorted_data = []
        max_value = data[0]
        sorted_data.append(max_value)

        for val in data[1:]:
            if val <= max_value:
                sorted_data.append(val)
                max_value = val

        sorted_columns[f"{col}_stalin_desc"] = sorted_data

    sorted_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in sorted_columns.items()]))

    sorted_df.to_csv(output_file, index=False)
    print("stalin sort worked")
stalin_sort_descending_all("raw_data.csv", "sorted.csv")
