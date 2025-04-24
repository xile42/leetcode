import pandas as pd


def calculate_fees_and_duration(parking_transactions: pd.DataFrame) -> pd.DataFrame:

    df = parking_transactions.copy()
    df["t"] = df["exit_time"] - df["entry_time"]
    df = df.groupby(["car_id", "lot_id"], as_index=False).agg(
        hour=("t", "sum"),
        total_fee_paid=("fee_paid", "sum"),
    )
    df["hour"] = df["hour"].dt.total_seconds() / 3600
    df["max"] = df.groupby("car_id", as_index=False)["hour"].transform("max")
    df1 = df[df["hour"] == df["max"]][["car_id", "lot_id"]]
    df = df.groupby("car_id", as_index=False).agg(
        total_fee_paid=("total_fee_paid", "sum"),
        hour=("hour", "sum")
    )
    df["avg_hourly_fee"] = (df["total_fee_paid"] / df["hour"]).round(2)
    df = pd.merge(df, df1, on="car_id", how="left")
    df = df.rename(columns={"lot_id": "most_time_lot"})

    df = df.sort_values("car_id")[["car_id", "total_fee_paid", "avg_hourly_fee", "most_time_lot"]]

    return df    
