import pandas as pd


def count_passengers_in_bus(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(passengers, buses, "cross")
##    df["flag"] = df.apply(axis=1, func=lambda x: 1 if x["arrival_time_x"] <= x["arrival_time_y"] else 0)
##    df = df[df["flag"] == 1]
    df = df[df["arrival_time_x"] <= df["arrival_time_y"]]
    df = df.groupby("passenger_id", as_index=False)["arrival_time_y"].min()
    df = df.groupby("arrival_time_y", as_index=False).agg(
        passengers_cnt=("passenger_id", "count")
    )
    df = pd.merge(buses, df, left_on="arrival_time", right_on="arrival_time_y", how="left")
    df = df.sort_values(by="bus_id")[["bus_id", "passengers_cnt"]]
    df = df.fillna(0)

    return df
