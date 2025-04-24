import pandas as pd


def friends_with_no_mutual_friends(friends: pd.DataFrame) -> pd.DataFrame:

    df = friends.copy().rename(columns={"user_id1": "user_id2", "user_id2": "user_id1"})
    df = pd.concat([friends, df])
    df = df.groupby("user_id1", as_index=False).agg(
        friends1=("user_id2", lambda x: x.tolist())
    )
    friends = pd.merge(friends, df, on="user_id1", how="left")
    df = df.rename(columns={"user_id1": "user_id2", "friends1": "friends2"})
    df = pd.merge(friends, df, on="user_id2", how="left")
    df["common"] = df.apply(axis=1, func=lambda x: len(set(x["friends1"]) & set(x["friends2"])))
    df = df[df["common"] == 0][["user_id1", "user_id2"]].sort_values(["user_id1", "user_id2"])

    return df
