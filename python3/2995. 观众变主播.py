import pandas as pd


def count_turned_streamers(sessions: pd.DataFrame) -> pd.DataFrame:

    df = sessions

    df1 = df[df["session_type"] == "Streamer"][["user_id"]].drop_duplicates()

    df2 = df.sort_values(["user_id", "session_start"])
    df2 = df2.drop_duplicates(subset="user_id", keep="first")
    df2 = df2[df2["session_type"] == "Viewer"][["user_id"]].drop_duplicates()

    users = pd.merge(df1, df2, how="inner")

    df = df[df["session_type"] == "Streamer"].groupby("user_id", as_index=False).agg(
        sessions_count=("user_id", "count")
    )

    result = pd.merge(users, df, on="user_id", how="left")
    result = result.sort_values(["sessions_count", "user_id"], ascending=False)

    return result
