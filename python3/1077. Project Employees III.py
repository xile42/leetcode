import pandas as pd


def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(project, employee, on="employee_id", how="left")
    df["rank"] = df.groupby(by="project_id", as_index=False)["experience_years"].rank(method="dense", ascending=False)
    df = df[df["rank"] == 1][["project_id", "employee_id"]]

    return df
