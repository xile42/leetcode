import pandas as pd


def find_overlapping_shifts(employee_shifts: pd.DataFrame) -> pd.DataFrame:

    df = employee_shifts.sort_values(["employee_id", "start_time"]).reset_index()
    df["id"] = df.index
    df = pd.merge(df, df, "cross")
    df = df[(df["id_x"] < df["id_y"]) & (df["employee_id_x"] == df["employee_id_y"]) & (df["end_time_x"] >= df["start_time_y"])]
    df = df.rename(columns={"employee_id_x": "employee_id"})
    df = df.groupby("employee_id", as_index=False).agg(
        overlapping_shifts=("start_time_x", "count")
    )

    return df
