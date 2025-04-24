import pandas as pd


def median_employee_salary(employee: pd.DataFrame) -> pd.DataFrame:

    df = employee
    df["count"] = df.groupby("company")["id"].transform("count")
    df["target"] = (df["count"] + 1) / 2
    df["rank"] = df.groupby("company")["salary"].rank(method="first", ascending=False)
    df = df[(df["rank"] - df["target"]).between(-0.5, 0.5)]
    df = df[["company", "salary"]]
    df = pd.merge(df, employee, on=["company", "salary"], how="left")
    df = df.groupby(["company", "salary"], as_index=False)["id"].min()
    df = df[["id", "company", "salary"]]

    return df
