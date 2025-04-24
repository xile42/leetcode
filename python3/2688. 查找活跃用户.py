import pandas as pd


def find_active_users(users: pd.DataFrame) -> pd.DataFrame:

    df = users.sort_values(["user_id", "created_at"])
    df = df[(df["user_id"] == df.shift(1)["user_id"]) & (df["created_at"] <= df.shift(1)["created_at"] + pd.Timedelta(days=7))]
    df = df[["user_id"]].drop_duplicates()

    return df
