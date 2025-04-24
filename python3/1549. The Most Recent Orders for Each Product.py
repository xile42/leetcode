import pandas as pd


def most_recent_orders(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:

    valid = orders.sort_values(by="order_date", ascending=False).drop_duplicates(subset="product_id", keep="first")[["product_id", "order_date"]]
    df = pd.merge(valid, orders, on=["product_id", "order_date"], how="left")
    df = pd.merge(df, products, how="left", on="product_id")
    df.sort_values(by=["product_name", "product_id", "order_id"], ascending=[True, True, True], inplace=True)

    return df[["product_name", "product_id", "order_id", "order_date"]]
