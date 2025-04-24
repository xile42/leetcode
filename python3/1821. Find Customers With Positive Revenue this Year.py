import pandas as pd


def find_customers(customers: pd.DataFrame) -> pd.DataFrame:

    df = customers[customers["year"] == 2021].groupby(by=["customer_id", "year"], as_index=False)["revenue"].sum()
    df = df[df["revenue"] > 0][["customer_id"]]

    return df
