import pandas as pd


def find_pairs(relations: pd.DataFrame) -> pd.DataFrame:

    df = relations.groupby("user_id", as_index=False).agg(
        follows=("follower_id", lambda x: x.tolist())
    )
    df = pd.merge(df, df, "cross")
    df = df[df["user_id_x"] < df["user_id_y"]]
    df["common"] = df.apply(axis=1, func=lambda x: len(set(x["follows_x"]) & set(x["follows_y"])))
    df["rank"] = df["common"].rank(method="dense", ascending=False)
    df = df.rename(columns={"user_id_x": "user1_id", "user_id_y": "user2_id"})
    df = df[df["rank"] == 1][["user1_id", "user2_id"]]

    return df
