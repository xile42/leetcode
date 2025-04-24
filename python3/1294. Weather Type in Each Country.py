import pandas as pd


def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(weather, countries, on="country_id", how="left")
    df = df[(df["day"] >= "2019-11-01") & (df["day"] <= "2019-11-30")]
    df["value"] = df["weather_state"].apply(func=lambda x: float(x))
    df = df.groupby(by="country_name", as_index=False)["value"].mean()
    df["weather_type"] = df["value"].apply(func=lambda x: "Cold" if x <= 15 else ("Hot" if x >= 25 else "Warm"))

    return df[["country_name", "weather_type"]]
