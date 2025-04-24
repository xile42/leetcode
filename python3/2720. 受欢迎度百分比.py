import pandas as pd


def popularity_percentage(friends: pd.DataFrame) -> pd.DataFrame:

    df = friends
    df = pd.concat([friends, friends.rename(columns={"user1": "user2", "user2": "user1"})])
    df = df.drop_duplicates()

    total = len(set(df["user1"].tolist() + df["user2"].tolist()))
    df = df.groupby("user1", as_index=False).agg(
        percentage_popularity=("user2", "nunique")
    )
    df["percentage_popularity"] = (df["percentage_popularity"] * 100 / total).round(2)
    df = df.sort_values("user1")

    return df[["user1", "percentage_popularity"]]
