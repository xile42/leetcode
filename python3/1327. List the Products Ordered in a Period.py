import pandas as pd


def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    df = orders[(orders["order_date"].dt.year == 2020) & (orders["order_date"].dt.month == 2)].groupby(by="product_id", as_index=False)["unit"].sum()
    df = pd.merge(products, df, on="product_id", how="inner")
    df = df[df["unit"] >= 100][["product_name", "unit"]]

    return df
