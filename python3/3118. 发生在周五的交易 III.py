import pandas as pd


def friday_purchases(purchases: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    base = pd.to_datetime("2023-11-01")
    days = [base + pd.Timedelta(days=i) for i in range(30)]
    days = [day for day in days if day.day_of_week == 4]
    dts = pd.DataFrame({
        "week_of_month": map(int, range(1, len(days) + 1)),
        "purchase_date": days
    })
    mems = pd.DataFrame({
        "membership": ["Premium", "VIP"]
    })
    result = pd.merge(dts, mems, "cross")

    df = pd.merge(purchases, users, on="user_id", how="left")
    df = pd.merge(df, dts, on="purchase_date", how="outer")
    df["membership"] = df["membership"].astype(str)
    df = df.groupby(by=["week_of_month", "membership"], as_index=False).agg(
        total_amount=("amount_spend", "sum")
    )
    df = pd.merge(result, df, on=["week_of_month", "membership"], how="left").fillna(0)
    df = df.sort_values(["week_of_month", "membership"], ascending=True)[["week_of_month", "membership", "total_amount"]]

    return df
