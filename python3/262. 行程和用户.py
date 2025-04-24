import pandas as pd


def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    valid = users[users["banned"] != "Yes"]["users_id"]
    df = trips
    df = df[(df["client_id"].isin(valid)) & (df["driver_id"].isin(valid)) & (df["request_at"].between("2013-10-01", "2013-10-03"))]
    df["flag"] = df["status"].apply(func=lambda x: 1 if x != "completed" else 0)
    df = df.groupby("request_at", as_index=False).agg(
        sum=("flag", "sum"),
        count=("flag", "count")
    )
    df["Cancellation Rate"] = (df["sum"] / df["count"]).round(2)
    df = df.rename(columns={"request_at": "Day"})
    df = df[["Day", "Cancellation Rate"]]
    
    return df
