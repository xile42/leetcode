import pandas as pd


def second_most_recent(user_activity: pd.DataFrame) -> pd.DataFrame:

    df = user_activity
    df["r"] = user_activity.groupby("username", as_index=False)["endDate"].rank("dense", ascending=False)
    df = df[df["r"] <= 2]
    df = df.sort_values("r", ascending=False)
    df = df.drop_duplicates(subset="username", keep="first")

    return df[["username", "activity", "startDate", "endDate"]]
 
