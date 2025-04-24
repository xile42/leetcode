import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:

    sales.groupby(by="seller_id", as_index=False)["price"].sum()
    df = sales[sales["price"] == sales["price"].max()][["seller_id"]]

    return df
