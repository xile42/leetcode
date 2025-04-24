import pandas as pd
from datetime import datetime


def find_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:

    start = pd.to_datetime(start_date.strftime("%Y-%m-%d")+" 00:00:00")
    end = pd.to_datetime(end_date.strftime("%Y-%m-%d")+" 00:00:00")

    purchases["flag"] = purchases["time_stamp"].apply(func=lambda x: 1 if start <= x <= end else 0)
    df = purchases[(purchases["flag"] == 1) & (purchases["amount"] >= min_amount)]
    result = df[["user_id"]].drop_duplicates(subset="user_id", keep="first").sort_values(by="user_id", ascending=True)

    return result
