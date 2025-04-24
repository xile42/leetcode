import pandas as pd


def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:

    df = students[~students["department_id"].isin(departments["id"])][["id", "name"]]

    return df
