import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    # wrong understanding, todo: fix
    employee["flag"] = employee.apply(lambda x: x["id"] if pd.isna(x["managerId"]) else x["managerId"], axis=1)
    df = employee.groupby(by="flag", as_index=False)["id"].count()
    df = pd.merge(employee, df, how="left", left_on="id", right_on="flag")
    df = df[df["id_y"] >= 5][["name"]]

    return df
