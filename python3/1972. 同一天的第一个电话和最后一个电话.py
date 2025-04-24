import pandas as pd


def same_day_calls(calls: pd.DataFrame) -> pd.DataFrame:

    df = calls.copy()
    df = df.rename(columns={"caller_id": "recipient_id", "recipient_id": "caller_id"})
    df = pd.concat([df, calls])
    df["t"] = df["call_time"].apply(func=lambda x: str(x)[:10])
    df["r"] = df.groupby(["t", "caller_id"], as_index=False)["call_time"].rank(method="dense", ascending=True)
    df.index = df["recipient_id"]
    df["min"] = df.groupby(["t", "caller_id"], as_index=False)["r"].transform("idxmin")
    df["max"] = df.groupby(["t", "caller_id"], as_index=False)["r"].transform("idxmax")
    df = df.reset_index(drop=True)
    df = df[df["min"] == df["max"]][["caller_id"]].drop_duplicates()
    df = df.rename(columns={"caller_id": "user_id"})

    return df

