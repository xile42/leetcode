import pandas as pd


def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(playback, ads, on="customer_id", how="left")
    df["flag"] = df.apply(axis=1, func=lambda x: 1 if not pd.isna(x["timestamp"]) and x["start_time"] <= x["timestamp"] <= x["end_time"] else 0)
    df = df.groupby("session_id", as_index=False)["flag"].sum()
    df = df[df["flag"] == 0][["session_id"]]

    return df
