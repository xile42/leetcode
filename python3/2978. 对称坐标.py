import pandas as pd


def symmetric_pairs(coordinates: pd.DataFrame) -> pd.DataFrame:

    coordinates["id"] = coordinates.index
    df = pd.merge(coordinates, coordinates, how="cross")
    df = df[df["id_x"] != df["id_y"]]
    df = df[(df["X_x"] == df["Y_y"]) & (df["X_y"] == df["Y_x"])]
    df1 = df[df["X_x"] <= df["Y_x"]][["X_x", "Y_x"]].rename(columns={"X_x": "x", "Y_x": "y"})
    df2 = df[df["X_y"] <= df["Y_y"]][["X_y", "Y_y"]].rename(columns={"X_y": "x", "Y_y": "y"})
    df = pd.concat([df1, df2]).drop_duplicates()
    df = df.sort_values(["x", "y"])

    return df


