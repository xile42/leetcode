import pandas as pd


def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:

    orders = orders[orders["order_date"].dt.year == 2019]
    df = pd.merge(users, orders, left_on="user_id", right_on="buyer_id", how="left")
    df = df.groupby(["user_id", "join_date"], as_index=False)["order_id"].count()
    df = df.rename(columns={"user_id": "buyer_id", "order_id": "orders_in_2019"})

    return df[["buyer_id", "join_date", "orders_in_2019"]]
