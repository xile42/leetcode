import pandas as pd


def employees_with_above_avg_workload(project: pd.DataFrame, employees: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(project, employees, on="employee_id", how="left")
    df["mean"] = df.groupby("team", as_index=False)["workload"].transform("mean")
    df = df[df["workload"] > df["mean"]].rename(columns={"name": "employee_name", "workload": "project_workload"})
    df = df.sort_values(["employee_id", "project_id"])

    return df[["employee_id", "project_id", "employee_name", "project_workload"]]
