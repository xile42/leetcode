import pandas as pd


def func(_x):

    x = _x / 60

    if 0 <= x < 5:
        return "[0-5>"
    elif 5 <= x < 10:
        return "[5-10>"
    elif 10 <= x < 15:
        return "[10-15>"
    else:
        return "15 or more"


def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:

    sessions["bin"] = sessions["duration"].apply(func=func)
    sessions["total"] = 1
    df = sessions.groupby(by="bin", as_index=False)["total"].sum()
    base = pd.DataFrame({
        "bin": ["[0-5>", "[5-10>", "[10-15>", "15 or more"]
    })
    df = pd.merge(base, df, on="bin", how="left")
    df.fillna(0, inplace=True)

    return df
