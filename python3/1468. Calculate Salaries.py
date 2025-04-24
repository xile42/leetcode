import pandas as pd


def calculate_salaries(salaries: pd.DataFrame) -> pd.DataFrame:

    df = salaries.groupby("company_id", as_index=False)["salary"].max()
    df["ratio"] = df["salary"].apply(func=lambda x: 1 if x < 1000 else (0.76 if 1000 <= x <= 10000 else 0.51))
    df = pd.merge(salaries, df[["company_id", "ratio"]], on="company_id", how="left")
    df["salary"] = (df["salary"] * df["ratio"]).apply(func=lambda x: int(x+0.5))

    return df[["company_id", "employee_id", "employee_name", "salary"]]
