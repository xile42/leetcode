import pandas as pd


def find_third_transaction(transactions: pd.DataFrame) -> pd.DataFrame:

    df = transactions.sort_values(["user_id", "transaction_date"])
    df["flag"] = (df["spend"] > df.shift(1)["spend"]) & (df["spend"] > df.shift(2)["spend"])
    df["rank"] = df.groupby("user_id", as_index=False)["transaction_date"].rank(method="dense")
    df = df[(df["user_id"] == df.shift(1)["user_id"]) & (df["user_id"] == df.shift(2)["user_id"]) & (df["flag"]) & (df["rank"] == 3)]
    df = df.sort_values(["user_id"]).rename(columns={"spend": "third_transaction_spend", "transaction_date": "third_transaction_date"})

    return df[["user_id", "third_transaction_spend", "third_transaction_date"]]
