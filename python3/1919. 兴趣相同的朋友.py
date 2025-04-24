import pandas as pd


def leetcodify_similar_friends(listens: pd.DataFrame, friendship: pd.DataFrame) -> pd.DataFrame:

    df = listens.drop_duplicates()
    df = df.groupby(["user_id", "day"], as_index=False)["song_id"].agg(func=lambda x: set(x.tolist()))
##    df = pd.merge(df, df, how="cross")
    df = pd.merge(df, df, how="inner", on="day")
##    df = df[(df["user_id_x"] < df["user_id_y"]) & (df["day_x"] == df["day_y"])]
    df = df[df["user_id_x"] < df["user_id_y"]]
    df["cnt"] = df.apply(axis=1, func=lambda x: len(x["song_id_x"] & x["song_id_y"]))
    df = df[df["cnt"] >= 3]
    df = df.rename(columns={"user_id_x": "user1_id", "user_id_y": "user2_id"})
    df = df[["user1_id", "user2_id"]].drop_duplicates()

    df = pd.merge(df, friendship, how="inner")

    return df
