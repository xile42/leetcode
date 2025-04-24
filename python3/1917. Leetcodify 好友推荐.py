import pandas as pd


def recommend_friends(listens: pd.DataFrame, friendship: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(listens, listens, on=["day", "song_id"], how="left")
    df = df[df["user_id_x"] != df["user_id_y"]]
    df = df.rename(columns={"user_id_x": "user1_id", "user_id_y": "user2_id"})
    df = df.groupby(["user1_id", "user2_id", "day"], as_index=False).agg(
        cnt=("song_id", "nunique")
    )
    df = df[df["cnt"] >= 3][["user1_id", "user2_id"]].drop_duplicates()
    rm = pd.concat([friendship, friendship.rename(columns={"user1_id": "user2_id", "user2_id": "user1_id"})])
    df = df[~ ( df.apply(tuple, axis=1).isin(rm.apply(tuple, axis=1)) )]
    df = df.drop_duplicates()
    df = df.rename(columns={"user1_id": "user_id", "user2_id": "recommended_id"})

    return df[["user_id", "recommended_id"]]
