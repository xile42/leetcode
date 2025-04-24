import pandas as pd


def rectangles_area(points: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(points, points, how="cross")
    df = df[(df["id_x"] < df["id_y"]) & (df["x_value_x"] != df["x_value_y"]) & (df["y_value_x"] != df["y_value_y"])]
    df["AREA"] = df.apply(axis=1, func=lambda x: abs(x["x_value_x"] - x["x_value_y"]) * abs(x["y_value_x"] - x["y_value_y"]))
    df = df.rename(columns={
        "id_x": "P1",
        "id_y": "P2",
    })
    df = df[["P1", "P2", "AREA"]]
    df = df.sort_values(["AREA", "P1", "P2"], ascending=[False, True, True])

    return df
