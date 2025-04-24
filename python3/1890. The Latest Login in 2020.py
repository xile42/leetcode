import pandas as pd


def latest_login(logins: pd.DataFrame) -> pd.DataFrame:

    df = logins[logins["time_stamp"].dt.year == 2020]
    df = df.sort_values(by="time_stamp", ascending=False)
    df = df.drop_duplicates(subset="user_id", keep="first")
    df.rename(columns={"time_stamp": "last_stamp"}, inplace=True)

    return df
