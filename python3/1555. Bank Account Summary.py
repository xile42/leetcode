import pandas as pd


def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:

    df1 = transactions.groupby(by="paid_by", as_index=False)["amount"].sum()
    df1 = df1.rename(columns={"paid_by": "user_id", "amount": "neg"})
    df2 = transactions.groupby(by="paid_to", as_index=False)["amount"].sum()
    df2 = df2.rename(columns={"paid_to": "user_id", "amount": "pos"})

    df = pd.merge(users, df1, how="left", on="user_id")
    df = pd.merge(df, df2, how="left", on="user_id")
    df = df.fillna(0)
    df["credit"] = df["credit"] + df["pos"] - df["neg"]
    df["credit_limit_breached"] = df["credit"].apply(func=lambda x: "Yes" if x < 0 else "No")

    return df[["user_id", "user_name", "credit", "credit_limit_breached"]]
