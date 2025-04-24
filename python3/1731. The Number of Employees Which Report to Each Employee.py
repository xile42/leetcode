import pandas as pd


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:

    df = employees.groupby(by="reports_to", as_index=False).agg({
        "age": "mean",
        "name": "count",
    })
    df.rename(columns={
        "reports_to": "employee_id",
        "age": "average_age",
        "name": "reports_count",
    }, inplace=True)
    df["average_age"] = df["average_age"].apply(lambda x: int(x+0.5))
    df = pd.merge(df, employees, how="left", on="employee_id")[["employee_id", "name", "reports_count", "average_age"]]

    return df
