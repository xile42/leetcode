import pandas as pd


def customer_order_frequency(customers: pd.DataFrame, product: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    orders["flag1"] = orders["order_date"].apply(func=lambda x: True if str(x)[:7] in ["2020-06"] else False)
    orders["flag2"] = orders["order_date"].apply(func=lambda x: True if str(x)[:7] in ["2020-07"] else False)
    orders = orders[orders["flag1"] | orders["flag2"]]
    df = pd.merge(orders, product, on="product_id", how="left")
    df["value1"] = df.apply(axis=1, func=lambda x: 0 if not x["flag1"] else x["quantity"] * x["price"])
    df["value2"] = df.apply(axis=1, func=lambda x: 0 if not x["flag2"] else x["quantity"] * x["price"])
    df = df.groupby(by="customer_id", as_index=False).agg({
        "value1": "sum",
        "value2": "sum",
    })
    df = df[(df["value1"] >= 100) & (df["value2"] >= 100)]
    df = pd.merge(df, customers, on="customer_id", how="left")

    return df[["customer_id", "name"]]
