import pandas as pd


def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:

    df = rides[["passenger_id"]].rename(columns={"passenger_id": "driver_id"})
    df["cnt"] = 1
    df = df.groupby("driver_id", as_index=False)["cnt"].sum()
    df = pd.merge(rides, df, on="driver_id", how="left").fillna(0)

    return df[["driver_id", "cnt"]].drop_duplicates()
