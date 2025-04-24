import pandas as pd


def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(sales, product, on="product_id", how="left")
    df["v"] = df["price"] * df["quantity"]
    df = df.groupby(by=["user_id", "product_id"], as_index=False)["v"].sum()
    df["max"] = df.groupby(by="user_id", as_index=False)["v"].transform("max")
    df = df[df["v"] == df["max"]][["user_id", "product_id"]]

    return df
