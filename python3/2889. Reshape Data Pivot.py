import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:

    df = weather.pivot(columns="city", index="month", values="temperature")

    return df
