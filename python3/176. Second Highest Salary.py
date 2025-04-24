import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    employee.drop_duplicates(subset="salary", keep="first", inplace=True)
    if len(employee) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    employee.sort_values(by="salary", ascending=False, inplace=True)
    return pd.DataFrame({"SecondHighestSalary": [employee.iloc[1]["salary"]]})
