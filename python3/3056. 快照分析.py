import pandas as pd


def snap_analysis(activities: pd.DataFrame, age: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(activities, age, how="left", on="user_id")
    df1 = df[df["activity_type"] == "open"].groupby("age_bucket", as_index=False).agg(
        open_time=("time_spent", "sum")
    )
    df2 = df[df["activity_type"] == "send"].groupby("age_bucket", as_index=False).agg(
        send_time=("time_spent", "sum")
    )
    df = pd.merge(df1, df2, how="outer", on="age_bucket").fillna(0)
    df["send_perc"] = df.apply(axis=1, func=lambda x: 100 * x["send_time"] / (x["send_time"] + x["open_time"])).round(2)
    df["open_perc"] = df.apply(axis=1, func=lambda x: 100 * x["open_time"] / (x["send_time"] + x["open_time"])).round(2)
    
    return df[["age_bucket", "send_perc", "open_perc"]]
