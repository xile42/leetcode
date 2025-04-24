import pandas as pd


def hopper_company(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:

    base = pd.DataFrame({"month": list(range(1, 13))})

    df1 = drivers[drivers["join_date"].dt.year == 2020]
    df1["month"] = df1["join_date"].dt.month
    df1 = df1.groupby("month", as_index=False).agg(
        active_drivers=("driver_id", "count")
    )
    v = len(drivers[drivers["join_date"].dt.year < 2020])
    df1 = pd.merge(base, df1, on="month", how="left").fillna(0)
    df1 = df1.sort_values("month").reset_index(drop=True)
    df1.loc[0, "active_drivers"] += + v
    df1["active_drivers"] = df1["active_drivers"].cumsum()

    df2 = pd.merge(accepted_rides, rides, on="ride_id", how="left")
    df2 = df2[df2["requested_at"].dt.year == 2020]
    df2["month"] = df2["requested_at"].dt.month
    df2 = df2.groupby("month", as_index=False).agg(
        accepted_rides=("ride_id", "count")
    )
    df2 = pd.merge(base, df2, on="month", how="left").fillna(0)

    df = pd.merge(df1, df2, on="month", how="left")
    df = df.sort_values("month")

    return df
