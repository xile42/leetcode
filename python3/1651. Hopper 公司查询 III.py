import pandas as pd


def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:

    base = pd.DataFrame({"month": list(range(1, 13))})

    df = pd.merge(accepted_rides, rides, on="ride_id", how="left")
    df = df[df["requested_at"].dt.year == 2020]
    df["month"] = df["requested_at"].dt.month
    df = df.groupby("month", as_index=False).agg(
        average_ride_distance=("ride_distance", "sum"),
        average_ride_duration=("ride_duration", "sum")
    )
    df = pd.merge(base, df, on="month", how="left").fillna(0)
    df = df.rolling(3).mean().round(2)
    df["month"] -= 1
    df = df[df["month"] >= 1].sort_values("month")

    return df
