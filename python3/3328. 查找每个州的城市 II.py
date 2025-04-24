import pandas as pd


def state_city_analysis(cities: pd.DataFrame) -> pd.DataFrame:

    df = cities
    df["matching_letter_count"] = df.apply(axis=1, func=lambda x: x["state"][0] == x["city"][0])
    df = df.sort_values(["state", "city"])
    df = df.groupby("state", as_index=False).agg(
        cities=("city", lambda x: ", ".join(x.tolist())),
        l=("city", lambda x: len(x.tolist())),
        matching_letter_count=("matching_letter_count", "sum")
    )
    df = df[(df["l"] >= 3) & (df["matching_letter_count"] > 0)]
    df = df.sort_values(["matching_letter_count", "state"], ascending=[False, True])[["state", "cities", "matching_letter_count"]]

    return df
