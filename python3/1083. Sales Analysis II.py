import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(sales, product, on="product_id", how="left")
    df["flag1"] = df.apply(axis=1, func=lambda x: 1 if x["product_name"] == "S8" else 0)
    df["flag2"] = df.apply(axis=1, func=lambda x: 1 if x["product_name"] == "iPhone" else 0)
    df = df.groupby(by="buyer_id", as_index=False).agg({
        "flag1": "sum",
        "flag2": "sum",
    })
    df = df[(df["flag1"] != 0) & (df["flag2"] == 0)][["buyer_id"]]

    return df
