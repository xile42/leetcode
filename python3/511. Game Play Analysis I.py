import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    activity.sort_values(by="event_date", inplace=True)
    activity.drop_duplicates(subset="player_id", keep="first", inplace=True)
    activity.rename(columns={"event_date": "first_login"}, inplace=True)

    return activity[["player_id", "first_login"]]
