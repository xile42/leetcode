import pandas as pd


def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(boxes, chests, on="chest_id", how="left")
    df = df.fillna(0)
    apples = df["apple_count_x"].sum() + df["apple_count_y"].sum()
    oranges = df["orange_count_x"].sum() + df["orange_count_y"].sum()

    return pd.DataFrame({
        "apple_count": [apples],
        "orange_count": [oranges]
    })
