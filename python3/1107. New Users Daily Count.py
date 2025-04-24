import pandas as pd


def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:

    now = pd.to_datetime("2019-06-30")
    ago = now - pd.Timedelta(days=90)
    df = traffic[traffic["activity"] == "login"].groupby(by="user_id", as_index=False)["activity_date"].min()
    df = df[(df["activity_date"] >= ago) & (df["activity_date"] <= now)].groupby(by="activity_date", as_index=False)["user_id"].count()
    df = df.rename(columns={
        "activity_date": "login_date",
        "user_id": "user_count"
    })

    return df
