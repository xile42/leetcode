import pandas as pd


def activity_participants(friends: pd.DataFrame, activities: pd.DataFrame) -> pd.DataFrame:

    df = friends.groupby("activity", as_index=False)["id"].count()
    df["max"] = df["id"].max()
    df["min"] = df["id"].min()
    df = df[(df["id"] != df["max"]) & (df["id"] != df["min"])][["activity"]]

    return df
