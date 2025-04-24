import pandas as pd


def find_valid_users(purchases: pd.DataFrame) -> pd.DataFrame:

    df = purchases.sort_values(by=["user_id", "purchase_date"], ascending=True)
    df = df[(df["user_id"] == df.shift(1)["user_id"]) & ((df["purchase_date"] - df.shift(1)["purchase_date"]) <= pd.Timedelta(days=7))]
    df = df[["user_id"]].drop_duplicates()

    return df
    
