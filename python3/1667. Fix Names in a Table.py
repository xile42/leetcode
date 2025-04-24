import pandas as pd


def update(s):

    s = s.lower()
    result = s[:1].upper() + s[1:]

    return result


def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    users["name"] = users["name"].apply(update)
    users.sort_values(by="user_id", ascending=True, inplace=True)

    return users
