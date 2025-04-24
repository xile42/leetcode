import pandas as pd


def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:

    df = cinema[cinema["free"] == 1]
    df["r"] = df["seat_id"].rank(method="min")
    df["t"] = df["seat_id"] - df["r"]
    df["consecutive_seats_len"] = df.groupby("t", as_index=False)["seat_id"].transform("count")
    result = df["consecutive_seats_len"].max()
    df = df[df["consecutive_seats_len"] == result]
    df = df.groupby("t").agg(
        first_seat_id=("seat_id", "min"),
        last_seat_id=("seat_id", "max")
    )
    df["consecutive_seats_len"] = result
    df = df.sort_values("first_seat_id")[["first_seat_id", "last_seat_id", "consecutive_seats_len"]]

    return df
