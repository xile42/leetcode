import pandas as pd


def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:

    logs["diff"] = logs["log_id"] - logs["log_id"].rank(method="dense", ascending=True).astype(int)
    logs["start_id"] = logs["log_id"]
    logs["end_id"] = logs["log_id"]
    df = logs.groupby(by="diff", as_index=False).agg({
        "start_id": "min",
        "end_id": "max"
    })

    return df[["start_id", "end_id"]].sort_values(by="start_id")
