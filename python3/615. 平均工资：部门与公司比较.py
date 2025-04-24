import pandas as pd


def average_salary(salary: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:

    salary["pay_month"] = salary["pay_date"].apply(func=lambda x: str(x)[:4] + "-" + str(x)[5:7])
    average = salary.groupby("pay_month", as_index=False)["amount"].mean()

    df = pd.merge(salary, employee, on="employee_id", how="left")
    df = df.groupby(by=["pay_month", "department_id"], as_index=False).agg(
        d_amount=("amount", "mean")
    )
    df = pd.merge(df, average, on="pay_month", how="left")

    df["comparison"] = df.apply(axis=1, func=lambda x: "same" if x["amount"] == x["d_amount"] else ("higher" if x["d_amount"] > x["amount"] else "lower"))

    return df[["pay_month", "department_id", "comparison"]]
