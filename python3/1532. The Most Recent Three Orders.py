import pandas as pd


def recent_three_orders(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    orders.sort_values(by=["customer_id", "order_date"], ascending=[True, False], inplace=True)
    orders["rank"] = orders.groupby(by="customer_id")["order_date"].rank(method="dense", ascending=False)
    df = orders[orders["rank"] <= 3]
    df = pd.merge(df, customers, on="customer_id", how="left")
    df.sort_values(by=["name", "customer_id", "order_date"], ascending=[True, True, False], inplace=True)
    df.rename(columns={"name": "customer_name"}, inplace=True)

    return df[["customer_name", "customer_id", "order_id", "order_date"]]
