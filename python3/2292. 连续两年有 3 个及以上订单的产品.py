import pandas as pd


def find_valid_products(orders: pd.DataFrame) -> pd.DataFrame:

    orders["purchase_date"] = orders["purchase_date"].dt.year
    orders = orders.groupby(by=["product_id", "purchase_date"], as_index=False)["quantity"].count()
    df = orders.sort_values(by=["product_id", "purchase_date"], ascending=True)
    df = df[(df["product_id"] == df.shift(1)["product_id"]) & (df.shift(1)["quantity"] >= 3) & (df["quantity"] >= 3) & ((df["purchase_date"] - df.shift(1)["purchase_date"]) == 1)]
    df = df[["product_id"]].drop_duplicates()

    return df
