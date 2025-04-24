import pandas as pd


def most_frequently_products(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:

    df = orders.groupby(by=["customer_id", "product_id"], as_index=False)["order_id"].count()
    df["rank"] = df.groupby(by=["customer_id"], as_index=False)["order_id"].rank(method="dense", ascending=False)
    df = df[df["rank"] == 1]
    df = pd.merge(df, products, on="product_id", how="left")

    return df[["customer_id", "product_id", "product_name"]]
