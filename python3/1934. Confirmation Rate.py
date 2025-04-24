import pandas as pd


def func(x):

    count = 0
    for action in x:
        if action == "confirmed":
            count += 1

    return round(count / len(x), 2)


def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:

    df = confirmations.groupby(by="user_id", as_index=False)["action"].agg(func)
    df = pd.merge(signups, df, how="left", on="user_id")[["user_id", "action"]]
    df.rename(columns={"action": "confirmation_rate"}, inplace=True)
    df.fillna(0.00, inplace=True)

    return df
