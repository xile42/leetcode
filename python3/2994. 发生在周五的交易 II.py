import pandas as pd


def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:

    base = pd.to_datetime("2023-11-01")
    base = [base + pd.Timedelta(days=i) for i in range(30)]
    base = [i for i in base if i.day_of_week == 4]
    base = pd.DataFrame({
        "week_of_month": list(range(1, len(base) + 1)),
        "purchase_date": base
    })

    df = purchases.groupby("purchase_date", as_index=False).agg(
        total_amount=("amount_spend", "sum")
    )
    df = pd.merge(base, df, on="purchase_date", how="left").fillna(0)
    df = df.sort_values("week_of_month")

    return df
