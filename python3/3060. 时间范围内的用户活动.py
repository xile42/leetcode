import pandas as pd


def user_activities(sessions: pd.DataFrame) -> pd.DataFrame:

    def f(df):

        df = df.sort_values(["user_id", "session_start"])
        df["f"] = (df["user_id"] == df.shift(1)["user_id"]) & ((df["session_start"] - df.shift(1)["session_end"]) <= pd.Timedelta(hours=12))
        df = df[df["f"] == True]["user_id"]

        return df

    user_id1 = f(sessions[sessions["session_type"] == "Viewer"])
    user_id2 = f(sessions[sessions["session_type"] == "Streamer"])

    df = pd.DataFrame({"user_id": user_id1.tolist() + user_id2.tolist()})
    df = df.drop_duplicates().sort_values("user_id")

    return df
