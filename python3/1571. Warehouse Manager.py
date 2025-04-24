import pandas as pd


def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:

    products["v"] = products.apply(axis=1, func=lambda x: x["Width"] * x["Length"] * x["Height"])
    df = pd.merge(warehouse, products, on="product_id", how="left")
    df["volume"] = df.apply(axis=1, func=lambda x: x["units"] * x["v"])
    df = df.groupby(by="name", as_index=False)["volume"].sum()
    df.rename(columns={
        "name": "warehouse_name"
    }, inplace=True)

    return df
