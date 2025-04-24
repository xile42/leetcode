import pandas as pd


def func(x):

    x = sorted(set(x), reverse=True)
    return set(x[:3])


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    if len(employee) == 0 or len(department) == 0:
        return pd.DataFrame({
            "Department": [],
            "Employee": [],
            "Salary": [],
        })

    employee["top3"] = employee["salary"]
    employee["top3"] = employee.groupby("departmentId", as_index=False)["top3"].transform(func=lambda x: [func(x)] * len(x))
    employee["flag"] = employee.apply(axis=1, func=lambda x: True if x["salary"] in x["top3"] else False)
    employee = employee[employee["flag"]][["departmentId", "name", "salary"]]
    df = pd.merge(employee, department, left_on="departmentId", right_on="id", how="left")
    df = df[["name_y", "name_x", "salary"]].rename(columns={
        "name_y": "Department",
        "name_x": "Employee",
        "salary": "Salary",
    })

    return df
