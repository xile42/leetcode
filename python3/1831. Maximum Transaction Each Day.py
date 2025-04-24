import pandas as pd


def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:

    transactions["ds"] = transactions["day"].dt.strftime("%Y-%m-%d")
    transactions["rank"] = transactions.groupby(by="ds", as_index=False)["amount"].rank(method="dense", ascending=False)
    df = transactions[transactions["rank"] == 1][["transaction_id"]].sort_values(by="transaction_id")

    return df
