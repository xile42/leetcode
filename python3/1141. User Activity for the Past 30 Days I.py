import datetime
import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:

    df = activity.groupby(by="activity_date", as_index=False)["user_id"].nunique()
    df = df[(df["activity_date"] <= "2019-07-27") & (df["activity_date"] + datetime.timedelta(days=30) > "2019-07-27")]
    df.rename(columns={"activity_date": "day", "user_id": "active_users"}, inplace=True)

    return df
