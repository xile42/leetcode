import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(left=customers, right=orders, how="left", left_on="id", right_on="customerId")
    df = df[df["id_y"].isna()][["name"]]
    df.rename(columns={"name": "Customers"}, inplace=True)

    return df
