import pandas as pd


def active_businesses(events: pd.DataFrame) -> pd.DataFrame:

    df1 = events.groupby(by="event_type", as_index=False)["occurrences"].mean()
    df1 = df1.rename(columns={"occurrences": "mean"})
    df2 = events.groupby(by=["business_id", "event_type"], as_index=False)["occurrences"].sum()
    df2 = df2.rename(columns={"occurrences": "sum"})
    df = pd.merge(df2, df1, on="event_type", how="left")
    df["flag"] = df.apply(axis=1, func=lambda x: 1 if x["sum"] > x["mean"] else 0)
    df = df.groupby(by="business_id", as_index=False)["flag"].sum()
    df = df[df["flag"] > 1][["business_id"]]

    return df
