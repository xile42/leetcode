import pandas as pd


def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:

    salary.sort_values(by=["emp_id", "salary"], ascending=[True, False], inplace=True)
    salary.drop_duplicates(subset="emp_id", keep="first", inplace=True)

    return salary
    
