import pandas as pd


def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:

    person["country_code"] = person["phone_number"].apply(func=lambda x: x[:3])
    df1 = pd.merge(person, country, on="country_code", how="left")

    global_avg = calls["duration"].mean()
    df2 = calls.copy()
    df2["caller_id"] = calls["callee_id"]
    df2 = pd.concat([calls, df2])
    df2 = pd.merge(df2[["caller_id", "duration"]], df1, left_on="caller_id", right_on="id", how="left")

    df = df2.groupby(by="name_y", as_index=False)["duration"].mean()
    df = df[df["duration"] > global_avg][["name_y"]].rename(columns={"name_y": "country"})

    return df
