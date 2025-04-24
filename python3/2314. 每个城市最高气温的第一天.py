import pandas as pd


def find_the_first_day(weather: pd.DataFrame) -> pd.DataFrame:

    weather["max"] = weather.groupby(by="city_id", as_index=False)["degree"].transform("max")
    df = weather[weather["degree"] == weather["max"]].sort_values(["city_id", "day"])
    df = df.drop_duplicates(subset=["city_id", "degree"], keep="first")

    return df[["city_id", "day", "degree"]]
