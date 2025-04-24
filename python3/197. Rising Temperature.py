import pandas as pd
import datetime


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:

    weather.sort_values(by="recordDate", inplace=True)
    df = weather[(weather["temperature"] > weather.shift(1)["temperature"]) & (weather["recordDate"] == weather.shift(1)["recordDate"] + datetime.timedelta(days=1))][["id"]]

    return df
