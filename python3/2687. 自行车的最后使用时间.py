import pandas as pd


def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:

    df = bikes.groupby(by="bike_number", as_index=False)["end_time"].max()
    df.sort_values(by="end_time", ascending=False, inplace=True)

    return df
        
