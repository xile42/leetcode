import pandas as pd


def find_interview_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    df1 = pd.merge(users, contests, how="cross")
    df1 = df1[(df1["user_id"] == df1["gold_medal"]) | (df1["user_id"] == df1["silver_medal"]) | (df1["user_id"] == df1["bronze_medal"])][["user_id", "contest_id"]]
    df1["rank"] = df1.groupby(by="user_id", as_index=False)["contest_id"].rank(method="dense", ascending=True)
    df1["flag"] = df1["contest_id"] - df1["rank"]
    df1 = df1.groupby(by=["user_id", "flag"], as_index=False).agg(
        count=("contest_id", "count")
    )
    df1 = df1[df1["count"] >= 3][["user_id"]].drop_duplicates()

    df2 = contests.groupby(by="gold_medal", as_index=False).agg(
        count=("contest_id", "count")
    )
    df2 = df2[df2["count"] >= 3][["gold_medal"]].drop_duplicates()
    df2 = df2.rename(columns={"gold_medal": "user_id"})

    df = pd.concat([df1, df2]).drop_duplicates()
    df = pd.merge(df, users, how="left", on="user_id")[["name", "mail"]]

    return df
