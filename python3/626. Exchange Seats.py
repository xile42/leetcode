import pandas as pd


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:

    seat["id"] = seat["id"].apply(lambda x: x-1 if x % 2 == 0 else (x+1 if x != seat["id"].max() else x))
    return seat.sort_values(by="id")
