import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(employee, employee, how="inner", left_on="managerId", right_on="id")
    df = df[df["salary_x"] > df["salary_y"]]
    df.rename(columns={"name_x": "Employee"}, inplace=True)

    return df[["Employee"]]
