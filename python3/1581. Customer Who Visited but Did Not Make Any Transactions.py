import pandas as pd


def func(x):

    result = 0
    for i in x:
        if pd.isna(i):
            result += 1
    return result


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(visits, transactions, how="left", on="visit_id")
    df = df.groupby(by="customer_id", as_index=False)["transaction_id"].agg(func)
    df = df[df["transaction_id"] > 0][["customer_id", "transaction_id"]]
    df.rename(columns={"transaction_id": "count_no_trans"}, inplace=True)

    return df
