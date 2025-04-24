import pandas as pd


def team_size(employee: pd.DataFrame) -> pd.DataFrame:

    employee["team_size"] = employee.groupby(by="team_id", as_index=False)["employee_id"].transform("count")

    return employee[["employee_id", "team_size"]]
