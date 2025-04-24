import pandas as pd


def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(sales, product, on="product_id", how="left")
    df["spending"] = df["quantity"] * df["price"]
    df = df.groupby(by="user_id", as_index=False)["spending"].sum()
    df.sort_values(by=["spending", "user_id"], ascending=[False, True], inplace=True)

    return df
