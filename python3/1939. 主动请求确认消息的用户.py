import pandas as pd


def f(args):

    args = sorted(list(args))
    for idx in range(len(args) - 1):
        if args[idx+1] <= args[idx] + pd.Timedelta(days=1):
            return 1

    return 0


def find_requesting_users(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:

    df = confirmations.groupby("user_id", as_index=False)["time_stamp"].agg(func=f)
    df = df[df["time_stamp"] == 1][["user_id"]]

    return df
