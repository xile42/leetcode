import pandas as pd


def find_employees(employees: pd.DataFrame) -> pd.DataFrame:

    df = employees[(employees["salary"] < 30000) & (~employees["manager_id"].isin(employees["employee_id"])) & (~employees["manager_id"].isna())]
    df = df[["employee_id"]].sort_values(by="employee_id")

    return df
