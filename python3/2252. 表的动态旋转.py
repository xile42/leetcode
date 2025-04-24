import pandas as pd


def dynamic_pivoting_table(products: pd.DataFrame) -> pd.DataFrame:

    df = pd.pivot(products, index="product_id", columns="store", values="price")
    columns = sorted(set(products["store"].tolist()))
    df = df.reset_index()
    df = df[["product_id"] + columns]

    return df
