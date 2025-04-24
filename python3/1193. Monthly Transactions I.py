import pandas as pd


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:

    transactions["month"] = transactions["trans_date"].apply(lambda x: str(x)[:7])
    transactions["trans_count"] = 1
    transactions["approved_count"] = transactions["state"].apply(lambda x: 1 if x == "approved" else 0)
    transactions["approved_total_amount"] = transactions.apply(lambda x: x["amount"] if x["approved_count"] == 1 else 0, axis=1)
    df = transactions.groupby(by=["month", "country"], as_index=False, dropna=False).agg({
        "trans_count": "sum",
        "approved_count": "sum",
        "approved_total_amount": "sum",
        "amount": "sum"
    })
    df.rename(columns={"amount": "trans_total_amount"}, inplace=True)

    return df[["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"]]
