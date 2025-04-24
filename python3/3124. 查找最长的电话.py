import pandas as pd


def f(x):
    
    t = pd.Timedelta(x, unit="s")

    return "{:02d}:{:02d}:{:02d}".format(t.components.hours, t.components.minutes, t.components.seconds)


def find_longest_calls(contacts: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:

    calls["rank"] = calls.groupby("type", as_index=False)["duration"].rank(method="min", ascending=False)
    df = calls[calls["rank"] <= 3]
    df["duration_formatted"] = df["duration"].apply(f)
    df = pd.merge(df, contacts, left_on="contact_id", right_on="id", how="left")
    df = df.sort_values(["type", "duration", "first_name"], ascending=False)[["first_name", "type", "duration_formatted"]]

    return df
