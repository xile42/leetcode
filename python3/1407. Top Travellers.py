import pandas as pd


def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:

    df = rides.groupby(by="user_id", as_index=False)["distance"].sum()
    df = pd.merge(users, df, how="left", left_on="id", right_on="user_id")
    df.fillna(0, inplace=True)
    df.sort_values(by=["distance", "name"], ascending=[False, True], inplace=True)
    df = df[["name", "distance"]].rename(columns={
        "distance": "travelled_distance",
    })

    return df
