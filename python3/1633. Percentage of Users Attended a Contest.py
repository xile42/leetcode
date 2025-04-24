import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:

    n = len(users)
    df = register.groupby(by="contest_id", as_index=False)["user_id"].agg(lambda x: 100 * len(x) / n).round(2)
    df.rename(columns={"user_id": "percentage"}, inplace=True)
    df.sort_values(by=["percentage", "contest_id"], ascending=[False, True], inplace=True)

    return df
