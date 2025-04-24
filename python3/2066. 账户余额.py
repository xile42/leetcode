import pandas as pd


def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:

    transactions["amount"] = transactions.apply(axis=1, func=lambda x: x["amount"] if x["type"] == "Deposit" else -x["amount"])
    df = transactions.sort_values(by=["account_id", "day"], ascending=True)
    df["balance"] = df.groupby(by="account_id", as_index=False)["amount"].cumsum()

    return df[["account_id", "day", "balance"]]
