import pandas as pd


def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(left=users, right=transactions, on="account", how="left")
    df = df.groupby(by="name", as_index=False)["amount"].sum()
    df = df[df["amount"] > 10000][["name", "amount"]]
    df.rename(columns={"amount": "balance"}, inplace=True)

    return df
