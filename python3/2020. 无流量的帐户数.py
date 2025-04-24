import pandas as pd


def find_target_accounts(subscriptions: pd.DataFrame, streams: pd.DataFrame) -> pd.DataFrame:

    df1 = subscriptions[(subscriptions["start_date"].dt.year == 2021) | (subscriptions["end_date"].dt.year == 2021)][["account_id"]].drop_duplicates()
    df2 = streams[streams["stream_date"].dt.year == 2021].groupby("account_id", as_index=False).agg(
        count=("session_id", "count")
    )
    df = pd.merge(df1, df2, on="account_id", how="left")
    df = df.fillna(0)
    result = df[df["count"] == 0]["account_id"].nunique()

    return pd.DataFrame({
        "accounts_count": [result]
    })
