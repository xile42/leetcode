import datetime
import pandas as pd


def calculate(df, key, period_state):

    start, end = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d"), datetime.datetime.strptime("2019-12-31", "%Y-%m-%d")
    df = df[(df[key] >= start) & (df[key] <= end)]

    if len(df) == 0:
        return pd.DataFrame({
            "period_state": [],
            "start_date": [],
            "end_date": []
        })

    df["value"] = df[key].apply(func=lambda x: (x-start).days)
    df["rank"] = df[key].rank(method="dense", ascending=True)
    df["flag"] = df["value"] - df["rank"]
    df["start_date"] = df[key]
    df["end_date"] = df[key]
    df = df.groupby(by="flag", as_index=False).agg({
        "start_date": "min",
        "end_date": "max",
    })
    df = df[["start_date", "end_date"]]
    df["period_state"] = period_state

    return df


def report_contiguous_dates(failed: pd.DataFrame, succeeded: pd.DataFrame) -> pd.DataFrame:

    df1 = calculate(failed, "fail_date", "failed")
    df2 = calculate(succeeded, "success_date", "succeeded")
    df = pd.concat([df1, df2])
    df.sort_values(by="start_date", ascending=True, inplace=True)

    return df[["period_state", "start_date", "end_date"]]
