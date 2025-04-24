import pandas as pd


def find_reporting_people(employees: pd.DataFrame) -> pd.DataFrame:

    df1 = employees.copy()
    df1.rename(columns={"manager_id": "manager_id2"}, inplace=True)
    df = pd.merge(employees, df1, right_on="employee_id", left_on="manager_id", how="left")
    df1.rename(columns={"manager_id2": "manager_id3"}, inplace=True)
    df = pd.merge(df, df1, right_on="employee_id", left_on="manager_id2", how="left")
    df = df[
        (df["employee_id_x"] != 1) & (
            (df["manager_id"] == 1) |
            (df["manager_id2"] == 1) |
            (df["manager_id3"] == 1)
        )
    ][["employee_id_x"]]

    df.rename(columns={"employee_id_x": "employee_id"}, inplace=True)

    return df
