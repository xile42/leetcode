import pandas as pd


def waitlist_analysis(flights: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:

    df = passengers.groupby("flight_id").agg(
        count=("passenger_id", "count")
    )
    df = pd.merge(flights, df, on="flight_id", how="left").fillna(0)
    df["booked_cnt"] = df.apply(axis=1, func=lambda x: min(x["count"], x["capacity"]))
    df["waitlist_cnt"] = df.apply(axis=1, func=lambda x: max(0, x["count"] - x["capacity"]))
    df = df.sort_values("flight_id")

    return df[["flight_id", "booked_cnt", "waitlist_cnt"]]
