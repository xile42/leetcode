import pandas as pd


def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:

    base = pd.DataFrame({"month": list(range(1, 13))})
    df1 = drivers[drivers["join_date"].dt.year == 2020]
    df1["month"] = df1["join_date"].dt.month
    df1 = df1.groupby("month", as_index=False).agg(
        available=("driver_id", "count")
    )
    df1 = pd.merge(base, df1, on="month", how="left").fillna(0)
    v = len(drivers[drivers["join_date"].dt.year < 2020])
    df1 = df1.reset_index(drop=True)
    df1.loc[0, "available"] += v
    df1["available"] = df1["available"].cumsum()

    df2 = rides[rides["requested_at"].dt.year == 2020]
    df2 = pd.merge(df2, accepted_rides, on="ride_id", how="left")
    df2["month"] = df2["requested_at"].dt.month
    df2 = df2.groupby("month", as_index=False).agg(
        ride_count=("driver_id", "nunique")
    )
    df2 = pd.merge(base, df2, on="month", how="left").fillna(0)

    df = pd.merge(df1, df2, on="month", how="left")
    df["working_percentage"] = df.apply(axis=1, func=lambda x: 0 if x["available"] == 0 else 100 * x["ride_count"] / x["available"]).round(2)
    df = df.sort_values("month")
    df = df[["month", "working_percentage"]]

    return df
