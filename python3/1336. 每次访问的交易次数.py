import pandas as pd


def draw_chart(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(visits, transactions, on="user_id", how="left")
    df = df[df["visit_date"] == df["transaction_date"]]
    df = df.groupby(["user_id", "visit_date"], as_index=False).agg(
        transactions_count=("amount", "count")
    )
    df = pd.merge(visits, df, on=["user_id", "visit_date"], how="left").fillna(0)
    df = df.groupby("transactions_count", as_index=False).agg(
        visits_count=("user_id", "count")
    )
    tc_max = df["transactions_count"].max()
    tmp = pd.DataFrame({
        "transactions_count": list(range(tc_max+1))
    })
    df = pd.merge(tmp, df, on="transactions_count", how="left").fillna(0)
    df = df.sort_values("transactions_count")
    
    return df
