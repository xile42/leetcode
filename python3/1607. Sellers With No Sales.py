import pandas as pd


def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:

    orders["year"] = orders.apply(axis=1, func=lambda x: 1 if str(x["sale_date"])[:4] == "2020" else 0)
    df = orders.groupby(by="seller_id", as_index=False)["year"].sum()
    df = pd.merge(seller, df, on="seller_id", how="left")
    df.fillna(0, inplace=True)
    df = df[df["year"] == 0][["seller_name"]].sort_values(by="seller_name")

    return df
