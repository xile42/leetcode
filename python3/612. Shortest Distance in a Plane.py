import math
import pandas as pd


def f(x, y, x1, y1):

    return round(math.sqrt(abs(x - x1) ** 2 + abs(y - y1) ** 2), 2)


def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:

    if len(point2_d) == 0:
        return pd.DataFrame({
            "shortest": [df.iloc[0]["d"]]
        })

    df = point2_d.copy()
    df = df.rename(columns={"x": "x1", "y": "y1"})
    df = pd.merge(point2_d, df, how="cross")
    df = df[~ ((df["x"] == df["x1"]) & (df["y"] == df["y1"]))]
    df["d"] = df.apply(axis=1, func=lambda row: f(row["x"], row["y"], row["x1"], row["y1"]))
    df.sort_values(by="d", ascending=True, inplace=True)

    return pd.DataFrame({
        "shortest": [df.iloc[0]["d"]]
    })
