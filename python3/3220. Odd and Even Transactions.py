import pandas as pd


def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:

    transactions["even_sum"] = 0
    transactions["odd_sum"] = 0
    transactions["even_sum"] = transactions[transactions["amount"] % 2 == 0]["amount"]
    transactions["odd_sum"] = transactions[transactions["amount"] % 2 != 0]["amount"]

    df = transactions.groupby(by="transaction_date", as_index=False)[["even_sum", "odd_sum"]].sum()
    df = df[["transaction_date", "odd_sum", "even_sum"]]
    df.sort_values(by="transaction_date", ascending=True, inplace=True)

    return df
