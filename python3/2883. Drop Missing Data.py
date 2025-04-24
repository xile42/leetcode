import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:

    df = students.dropna(subset="name", how="any")

    return df
