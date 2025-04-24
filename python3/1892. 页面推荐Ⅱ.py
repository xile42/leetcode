import pandas as pd
from operator import add
from functools import reduce
from collections import Counter


def recommend_page(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:

    friendship = pd.concat([friendship, friendship.rename(columns={"user1_id": "user2_id", "user2_id": "user1_id"})])
    base = likes.groupby("user_id", as_index=False)["page_id"].apply(set)
    base = base.rename(columns={"user_id": "user1_id", "page_id": "user1_page"})
    df = pd.merge(friendship, base, on="user1_id", how="left")
    base = base.rename(columns={"user1_id": "user2_id", "user1_page": "user2_page"})
    df = pd.merge(df, base, on="user2_id", how="left")
    df = df.dropna(how="any")
    df["pages"] = df.apply(axis=1, func=lambda x: list(x["user2_page"] - x["user1_page"]))
    df = df.groupby("user1_id", as_index=False)["pages"].apply(func=lambda x: reduce(add, x))
    df["pages"] = df["pages"].apply(func=lambda x: [(k, v) for k, v in Counter(x).items()])
    df = df.explode("pages")
    df = df.dropna(how="any")
    df["page_id"] = df["pages"].apply(func=lambda x: x[0])
    df["friends_likes"] = df["pages"].apply(func=lambda x: x[1])
    df = df.rename(columns={"user1_id": "user_id"})

    return df[["user_id", "page_id", "friends_likes"]]
