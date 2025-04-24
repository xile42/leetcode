import pandas as pd


def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(prices, units_sold, how="left")
    df = df[(df["purchase_date"].isna()) | ((df["purchase_date"] >= df["start_date"]) & (df["purchase_date"] <= df["end_date"]))]
    df.fillna(0, inplace=True)
    df["mul"] = df["price"] * df["units"]
    df1 = df.groupby(by="product_id", as_index=False)["mul"].sum()
    df2 = df.groupby(by="product_id", as_index=False)["units"].sum()
    df = pd.merge(df1, df2, on="product_id")
    df["average_price"] = df.apply(axis=1, func=lambda x: 0 if x["units"] == 0 else x["mul"] / x["units"]).round(2)

    return df[["product_id", "average_price"]]
