import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    employees["time"] = employees["out_time"] - employees["in_time"]
    employees = employees.groupby(by=["emp_id", "event_day"]).sum("time")
    employees.reset_index(inplace=True)
    employees.rename(columns={"time": "total_time", "event_day": "day"}, inplace=True)

    return employees[["emp_id", "total_time", "day"]]
