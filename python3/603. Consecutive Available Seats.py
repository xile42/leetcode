import pandas as pd


def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:

    df = cinema[(cinema["free"] == True) & ((cinema["free"].shift(1) == True) | (cinema["free"].shift(-1) == True))][["seat_id"]].sort_values(by="seat_id", ascending=True)

    return df
