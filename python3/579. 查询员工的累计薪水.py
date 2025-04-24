import pandas as pd


def cumulative_salary(employee: pd.DataFrame) -> pd.DataFrame:

    if len(employee) == 0:
        return pd.DataFrame({
            "id": [],
            "month": [],
            "salary": []
        })

    tmp1 = employee[["id"]].drop_duplicates()
    tmp2 = pd.DataFrame({"month": range(-2, 13)})
    tmp = pd.merge(tmp1, tmp2, "cross")
    df = pd.merge(tmp, employee, on=["id", "month"], how="left")
    
    df = df.sort_values(["id", "month"])
    df = df.groupby("id", as_index=False).rolling(window=3, on="month", min_periods=1).sum()
    df = pd.merge(employee[["id", "month"]], df, on=["id", "month"], how="left")
    df["r"] = df.groupby("id", as_index=False)["month"].rank(method="first", ascending=False)
    df = df[df["r"] != 1]
    df = df.sort_values(["id", "month"], ascending=[True, False])[["id", "month", "salary"]]

    return df
