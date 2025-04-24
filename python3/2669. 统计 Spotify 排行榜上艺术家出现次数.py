import pandas as pd


def count_occurrences(spotify: pd.DataFrame) -> pd.DataFrame:

    df = spotify["artist"].value_counts().reset_index()
    df = df.rename(columns={"count": "occurrences"})
    df = df.sort_values(by=["occurrences", "artist"], ascending=[False, True])

    return df
