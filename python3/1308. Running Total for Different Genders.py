import pandas as pd


def running_total(scores: pd.DataFrame) -> pd.DataFrame:

    df = scores.sort_values(["gender", "day"], ascending=True)
    df = scores.groupby(["gender", "day"], as_index=False).agg(
        total=("score_points", "sum")
    )
    df.loc[df["gender"] == "F", "total"] = df.loc[df["gender"] == "F", "total"].cumsum()
    df.loc[df["gender"] == "M", "total"] = df.loc[df["gender"] == "M", "total"].cumsum()
    df = df[["gender", "day", "total"]]

    return df
