import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    employees["flag1"] = employees["employee_id"].apply(lambda x: 1 if x % 2 != 0 else 0)
    employees["flag2"] = employees["name"].apply(lambda x: 1 if x[0] != "M" else 0)
    employees["bonus"] = 0
    employees.loc[(employees["flag1"] == 1) & (employees["flag2"] == 1), "bonus"] = employees["salary"]
    df = employees[["employee_id", "bonus"]].sort_values(by="employee_id", ascending=True)

    return df
