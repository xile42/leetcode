import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(employee, department, how="left", left_on="departmentId", right_on="id")
    max_series = df.groupby(by="departmentId", as_index=False)["salary"].transform("max")
    df = df[df["salary"] == max_series]
    df = df[["name_y", "name_x", "salary"]].rename(columns={
        "name_y": "Department",
        "name_x": "Employee",
        "Salary": "Salary",
    })

    return df
