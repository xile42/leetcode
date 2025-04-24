import pandas as pd


def orders_above_average(orders_details: pd.DataFrame) -> pd.DataFrame:

    df = orders_details.groupby(by="order_id", as_index=False).agg(
        mean=("quantity", "mean"),
        max=("quantity", "max")
    )
    m = df["mean"].max()
    df = df[df["max"] > m][["order_id"]]

    return df
