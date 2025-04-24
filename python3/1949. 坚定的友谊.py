import pandas as pd


def strong_friendship(friendship: pd.DataFrame) -> pd.DataFrame:

    df = friendship.copy()
    df = df.rename(columns={"user1_id": "user2_id", "user2_id": "user1_id"})
    df = pd.concat([friendship, df])
    df = df.groupby("user1_id", as_index=False).agg(
        friends1=("user2_id", lambda x: x.tolist())
    )
    df["count1"] = df["friends1"].transform(len)

    tmp = pd.merge(friendship, df, on="user1_id", how="left")
    df = df.rename(columns={
        "user1_id": "user2_id",
        "friends1": "friends2",
        "count1": "count2"
    })
    df = pd.merge(tmp, df, on="user2_id", how="left")

    df["common"] = df.apply(axis=1, func=lambda x: list(set(x["friends1"]) & set(x["friends2"])))
    df["common_friend"] = df["common"].transform(len)

    df = df[df["common_friend"] >= 3][["user1_id", "user2_id", "common_friend"]]

    return df
