import pandas as pd


def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:

    df = project.groupby(by="project_id", as_index=False)["employee_id"].count()
    df = df[df["employee_id"] == df["employee_id"].max()]

    return df[["project_id"]]
