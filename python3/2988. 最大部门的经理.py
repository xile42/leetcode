import pandas as pd


def find_manager(employees: pd.DataFrame) -> pd.DataFrame:

    df1 = employees[employees["position"] == "Manager"]
    df2 = employees.groupby("dep_id", as_index=False).agg(
        count=("emp_id", "count")
    )
    df2["rank"] = df2["count"].rank(method="dense", ascending=False)
    df2 = df2[df2["rank"] == 1][["dep_id"]]
    df = pd.merge(df2, df1, on="dep_id", how="left")
    df = df.sort_values("dep_id")[["emp_name", "dep_id"]].rename(columns={"emp_name": "manager_name"})

    return df
