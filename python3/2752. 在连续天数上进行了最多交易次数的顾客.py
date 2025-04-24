import pandas as pd


def find_customers(transactions: pd.DataFrame) -> pd.DataFrame:

    df = transactions
    df = df.sort_values(["customer_id", "transaction_date"])
    df["r"] = df.groupby("customer_id", as_index=False)["transaction_date"].rank("dense")
    df["t"] = df.apply(axis=1, func=lambda x: x["transaction_date"] - pd.Timedelta(days=x["r"]))
    df = df.groupby(["customer_id", "t"], as_index=False).agg(
        count=("transaction_id", "count")
    )
    df["m"] = df["count"].max()
    df = df[df["count"] == df["m"]]
    df = df.drop_duplicates()
    df = df.sort_values("customer_id")
    
    return df[["customer_id"]]
