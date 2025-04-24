import datetime
import pandas as pd


def func(x):

    x = x.tolist()
    return 1 if min(x) + datetime.timedelta(days=1) in x else 0


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    df = activity.groupby(by=["player_id"], as_index=False)["event_date"].agg(func)
    value = round(df["event_date"].sum() / len(df), 2)

    return pd.DataFrame({"fraction": [value]})
