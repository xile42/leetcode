import pandas as pd


def employees_of_same_salary(employees: pd.DataFrame) -> pd.DataFrame:

    df = employees.groupby("salary", as_index=False).agg(
        count=("employee_id", "count")
    )
    df = df[df["count"] > 1]
    df["team_id"] = df["salary"].rank(method="dense")
    df = pd.merge(employees, df, on="salary", how="left")
    df = df.dropna(axis=0, how="any")
    df = df.sort_values(by=["team_id", "employee_id"], ascending=True)

    return df[["employee_id", "name", "salary", "team_id"]]
