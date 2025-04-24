import pandas as pd


def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:

    df = stadium
    df["f"] = df["people"].apply(func=lambda x: 1 if x >= 100 else 0)
    df = df.sort_values("id")
    df = df[df["f"] == 1]
    df["r"] = df["id"].rank(method="first")
    df["t"] = df["id"] - df["r"]
    df["c"] = df.groupby("t", as_index=False)["id"].transform("count")
    df = df[df["c"] >= 3]
    df.sort_values("visit_date")

    return df[["id", "visit_date", "people"]]
