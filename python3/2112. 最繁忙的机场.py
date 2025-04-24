import pandas as pd


def airport_with_most_traffic(flights: pd.DataFrame) -> pd.DataFrame:

    df = flights.copy().rename(columns={"departure_airport": "arrival_airport", "arrival_airport": "departure_airport"})
    df = pd.concat([flights, df])
    df = df.groupby(by="departure_airport", as_index=False)["flights_count"].sum()
    df["rank"] = df["flights_count"].rank(method="dense", ascending=False)
    df = df[df["rank"] == 1][["departure_airport"]].rename(columns={"departure_airport": "airport_id"})

    return df    
