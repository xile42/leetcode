import pandas as pd


def monthly_transactions(transactions: pd.DataFrame, chargebacks: pd.DataFrame) -> pd.DataFrame:

    transactions["month"] = transactions["trans_date"].apply(func=lambda x: str(x)[:7])
    chargebacks["month"] = chargebacks["trans_date"].apply(func=lambda x: str(x)[:7])
    df1 = transactions[transactions["state"] == "approved"]
    df1 = df1.groupby(["country", "month"], as_index=False).agg(
        approved_count=("id", "count"),
        approved_amount=("amount", "sum")
    )
    df2 = pd.merge(chargebacks, transactions[["id", "country", "amount"]], left_on="trans_id", right_on="id", how="left")
    df2 = df2.groupby(["country", "month"], as_index=False).agg(
        chargeback_count=("trans_id", "count"),
        chargeback_amount=("amount", "sum")
    )

    df = pd.merge(df1, df2, on=["country", "month"], how="outer")
    df = df.fillna(0)

    return df[["month", "country", "approved_count", "approved_amount", "chargeback_count", "chargeback_amount"]]
