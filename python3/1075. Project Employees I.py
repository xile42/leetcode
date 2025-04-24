import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(project, employee, how="left", on="employee_id")
    df = df.groupby(by="project_id", as_index=False)["experience_years"].mean().round(2)
    df.rename(columns={"experience_years": "average_years"}, inplace=True)

    return df[["project_id", "average_years"]]
