import pandas as pd


def suspicious_bank_accounts(accounts: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:

    transactions = transactions[transactions["type"] == "Creditor"]
    transactions["month"] = transactions["day"].apply(func=lambda x: pd.to_datetime(str(x)[:7]))
    df = transactions.groupby(by=["account_id", "month"], as_index=False)["amount"].sum()
    df = pd.merge(df, accounts, how="left", on="account_id")
    df = df[df["amount"] > df["max_income"]]
    df = df.sort_values(by=["account_id", "month"])
    df = df[
        (df["account_id"] == df.shift(1)["account_id"]) &
        (df["month"].dt.month == df.shift(1)["month"].dt.month + 1)
    ][["account_id"]].drop_duplicates()

    return df
    
    
