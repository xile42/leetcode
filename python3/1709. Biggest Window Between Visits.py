import datetime
import pandas as pd


def func(x):

    x = x.tolist()
    results = list()
    for idx in range(1, len(x)):
        results.append(x[idx] - x[idx-1])
    results.append(datetime.datetime.strptime("2021-01-01", "%Y-%m-%d") - x[-1])

    return max(results).days


def biggest_window(user_visits: pd.DataFrame) -> pd.DataFrame:

    user_visits.sort_values(by=["user_id", "visit_date"], inplace=True)
    df = user_visits.groupby(by="user_id", as_index=False)["visit_date"].agg(func=func)
    df.sort_values(by="user_id", inplace=True)
    df.rename(columns={"visit_date": "biggest_window"}, inplace=True)

    return df[["user_id", "biggest_window"]]
