import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:

    df1 = employee[employee["primary_flag"] == "Y"][["employee_id", "department_id"]]
    df2 = employee.groupby(by="employee_id", as_index=False)["primary_flag"].count()
    df2 = df2[df2["primary_flag"] == 1][["employee_id"]]
    df2 = pd.merge(df2, employee, on="employee_id", how="left")[["employee_id", "department_id"]]
    df = pd.concat([df1, df2])
    df.drop_duplicates(inplace=True)

    return df
