import pandas as pd


def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:

    df = employees
    df["rank"] = employees.groupby("dept")["salary"].rank(method="dense", ascending=False)
    df = df[df["rank"] == 2].sort_values("emp_id")[["emp_id", "dept"]]

    return df
