import pandas as pd


def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:

    df = rides.groupby(by="user_id", as_index=False)["distance"].sum()
    df = pd.merge(users, df, how="left", on="user_id")
    df.fillna(0, inplace=True)
    df.sort_values(by="user_id", ascending=True, inplace=True)
    df.rename(columns={"distance": "traveled distance"}, inplace=True)

    return df
