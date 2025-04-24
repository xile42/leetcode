import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    orders["a"] = orders.apply(axis=1, func=lambda x: 1 if x["product_name"] == "A" else 0)
    orders["b"] = orders.apply(axis=1, func=lambda x: 1 if x["product_name"] == "B" else 0)
    orders["c"] = orders.apply(axis=1, func=lambda x: 1 if x["product_name"] == "C" else 0)
    df = orders.groupby(by="customer_id", as_index=False).agg({
        "a": "sum",
        "b": "sum",
        "c": "sum",
    })
    df = df[(df["a"] != 0) & (df["b"] != 0) & (df["c"] == 0)][["customer_id"]]
    df = pd.merge(df, customers, how="left", on="customer_id")

    return df
