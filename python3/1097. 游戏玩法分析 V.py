from decimal import Decimal, ROUND_HALF_UP
import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    df = activity.copy()
    df1 = df.groupby("player_id", as_index=False)["event_date"].min()
    df1 = df1.rename(columns={"event_date": "first_login"})
    df1["second_login"] = df1.groupby("player_id")["first_login"].transform(lambda x: x + pd.Timedelta(days=1))
    df = pd.merge(df1, df, left_on=["player_id", "second_login"], right_on=["player_id", "event_date"], how="left")

    df = df.groupby("first_login", as_index=False).agg(
        installs=("player_id", "nunique"),
        Day1_retention=("event_date", "count")
    )
    df = df.rename(columns={"first_login": "install_dt"})
    df["Day1_retention"] = (df["Day1_retention"] / df["installs"]).apply(lambda x: Decimal(str(x)).quantize(Decimal("0.01"), ROUND_HALF_UP))

    return df[["install_dt", "installs", "Day1_retention"]]
##    activity = activity.sort_values(by=["player_id", "event_date"], ascending=True)
##    df = activity.drop_duplicates(subset="player_id", keep="first")
##    df = df.groupby(by="event_date", as_index=False).agg(
##        installs=("player_id", "count")
##    )
##    df["t1"] = df["event_date"] + pd.Timedelta(days=1)
##    df = df.rename(columns={"event_date": "install_dt"})
##    backup = df[["install_dt", "installs"]]
##
##    df1 = activity
##    df1 = df1[(df1["player_id"] == df1.shift(1)["player_id"]) & (df1["event_date"] == df1.shift(1)["event_date"] + pd.Timedelta(days=1)) & (df1.shift(1)["event_date"].isin(backup["install_dt"]))]
##    df = pd.merge(df1, df, left_on="event_date", right_on="t1", how="left").dropna()
##    df = df.groupby(by=["install_dt", "installs"], as_index=False).agg(
##        count=("player_id", "count")
##    )
##    df["Day1_retention"] = df["count"] / df["installs"]
##    df["Day1_retention"] = df["Day1_retention"].apply(func=lambda x: Decimal(str(x)).quantize(Decimal(".00"), rounding=ROUND_HALF_UP))
##    df = pd.merge(backup, df, on=["install_dt", "installs"], how="left").fillna(0)
##
##    return df[["install_dt", "installs", "Day1_retention"]]
