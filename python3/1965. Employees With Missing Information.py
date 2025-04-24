import pandas as pd


def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(employees, salaries, on="employee_id", how="outer")
    df = df[df["name"].isna() | df["salary"].isna()][["employee_id"]].sort_values(by="employee_id", ascending=True)

    return df
