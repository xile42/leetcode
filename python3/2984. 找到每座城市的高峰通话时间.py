import pandas as pd


def peak_calling_hours(calls: pd.DataFrame) -> pd.DataFrame:

    calls["peak_calling_hour"] = calls["call_time"].apply(func=lambda x: x.hour)
    df = calls.groupby(["city", "peak_calling_hour"], as_index=False).agg(
        number_of_calls=("caller_id", "count")
    )
    df["rank"] = df.groupby("city", as_index=False)["number_of_calls"].rank(method="dense", ascending=False)
    df = df[df["rank"] == 1]
    df = df.sort_values(["peak_calling_hour", "city"], ascending=False)

    return df[["city", "peak_calling_hour", "number_of_calls"]]
