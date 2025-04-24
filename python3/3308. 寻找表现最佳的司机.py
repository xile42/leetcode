import pandas as pd


def get_top_performing_drivers(drivers: pd.DataFrame, vehicles: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(vehicles, trips, on="vehicle_id", how="left")
    df = pd.merge(df, drivers[["driver_id", "accidents"]], on="driver_id", how="left")
    df = df.groupby(["driver_id", "fuel_type"], as_index=False).agg(
        rating=("rating", "mean"),
        distance=("distance", "sum"),
        accidents=("accidents", "mean")
    )
    df["rating"] = df["rating"].round(2)
    df = df.sort_values(["fuel_type", "rating", "distance", "accidents"], ascending=[True, False, False, True])
    df = df.dropna().drop_duplicates(subset="fuel_type", keep="first")[["fuel_type", "driver_id", "rating", "distance"]]

    return df    
