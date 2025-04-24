import pandas as pd


def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:

    point.sort_values(by="x", ascending=True, inplace=True)
    point["diff"] = point["x"] - point["x"].shift(1)

    return pd.DataFrame({
        "shortest": [point["diff"].min()],
    })
