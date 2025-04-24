import pandas as pd


def active_users(accounts: pd.DataFrame, logins: pd.DataFrame) -> pd.DataFrame:

    df = logins.drop_duplicates().sort_values(["id", "login_date"])
    df["rank"] = df.groupby("id", as_index=False)["login_date"].rank(method="dense", ascending=True)
    df["days"] = df.apply(axis=1, func=lambda x: x["login_date"] - pd.Timedelta(days=x["rank"]))
    df["cnt"] = 1
    df = df.groupby(["id", "days"], as_index=False)["cnt"].sum()
    df = df[df["cnt"] >= 5][["id"]].drop_duplicates()
    df = pd.merge(df, accounts, on="id", how="left")
    df = df.sort_values("id", ascending=True)

    return df
