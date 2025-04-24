import pandas as pd


def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:

    df = pd.DataFrame({
        "ids": range(1, customers["customer_id"].max()+1)
    })
    invalid = customers["customer_id"]
    df = df[~ df["ids"].isin(invalid)]

    return df
