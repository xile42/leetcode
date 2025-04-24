import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    df = activity.sort_values(by=["player_id", "event_date"]).drop_duplicates(subset="player_id", keep="first")

    return df[["player_id", "device_id"]]
