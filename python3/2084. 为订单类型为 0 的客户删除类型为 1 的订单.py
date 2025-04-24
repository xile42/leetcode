import pandas as pd


def drop_specific_orders(orders: pd.DataFrame) -> pd.DataFrame:

    df = orders.groupby(by="customer_id", as_index=False).agg(
        sum=("order_type", "sum"),
        cnt=("order_type", "count")
    )
    df["flag"] = df.apply(axis=1, func=lambda x: 1 if x["sum"] == x["cnt"] else 0)
    df = pd.merge(orders, df[["customer_id", "flag"]], on="customer_id", how="left")
    df = df[df["order_type"] <= df["flag"]][["order_id", "customer_id", "order_type"]]

    return df
