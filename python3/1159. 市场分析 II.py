import pandas as pd


def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:

    df = orders
    df["rank"] = orders.groupby("seller_id", as_index=False)["order_date"].rank(method="dense")
    df = df[df["rank"] == 2]
    df = pd.merge(df, items, on="item_id", how="left")
    df = pd.merge(users, df, left_on="user_id", right_on="seller_id", how="left")
    df["2nd_item_fav_brand"] = df.apply(axis=1, func=lambda x: "yes" if x["item_brand"] == x["favorite_brand"] else "no")
    df["seller_id"] = df["user_id"]

    return df[["seller_id", "2nd_item_fav_brand"]]
