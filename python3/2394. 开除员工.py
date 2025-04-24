import pandas as pd


def employees_with_deductions(employees: pd.DataFrame, logs: pd.DataFrame) -> pd.DataFrame:

    logs["time"] = logs["out_time"] - logs["in_time"]
    logs["time"] = logs["time"].apply(func=lambda x: x.seconds)
    logs["time"] = logs["time"].apply(func=lambda x: x // 60 + 1 if x % 60 != 0 else x // 60)
    logs = logs.groupby("employee_id", as_index=False)["time"].sum()
    df = pd.merge(employees, logs, on="employee_id", how="left").fillna(0)
    df["needed"] = df["needed_hours"] * 60
    df = df[df["time"] < df["needed"]][["employee_id"]]

    return df
