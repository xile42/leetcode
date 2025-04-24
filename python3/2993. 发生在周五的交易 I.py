import pandas as pd


def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:

    purchases["dow"] = purchases["purchase_date"].dt.day_of_week
    df = purchases[purchases["dow"] == 4]
    df = df.groupby("purchase_date", as_index=False)["amount_spend"].sum()
    df = df.sort_values("purchase_date")
    df["week_of_month"] = df["purchase_date"].dt.day // 7 + 1
    df = df.rename(columns={"amount_spend": "total_amount"})

    return df[["week_of_month", "purchase_date", "total_amount"]]
