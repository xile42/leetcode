import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:

    sales["flag"] = sales["sale_date"].apply(lambda x: 0 if (str(x) >= "2019-01-01" and str(x) <= "2019-03-31") else 1)
    df = sales.groupby(by="product_id", as_index=False)["flag"].sum()
    df = df[df["flag"] == 0][["product_id"]]

    df = pd.merge(df, product)
    df = df[["product_id", "product_name"]]

    return df
