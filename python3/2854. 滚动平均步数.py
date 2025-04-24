import pandas as pd


def rolling_average(steps: pd.DataFrame) -> pd.DataFrame:

    df = steps.sort_values(["user_id", "steps_date"])
    df["rolling_average"] = ((df["steps_count"] + df.shift(1)["steps_count"] + df.shift(2)["steps_count"]) / 3).round(2)
    df = df[(df["user_id"] == df.shift(1)["user_id"]) & (df.shift(1)["user_id"] == df.shift(2)["user_id"]) & (df["steps_date"] == df.shift(1)["steps_date"] + pd.Timedelta(days=1)) & (df.shift(1)["steps_date"] == df.shift(2)["steps_date"] + pd.Timedelta(days=1))]
    df = df[["user_id", "steps_date", "rolling_average"]].sort_values(["user_id", "steps_date"])

    return df
