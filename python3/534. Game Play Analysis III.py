import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    df = activity.sort_values(by=["player_id", "event_date"], ascending=[True, True])
    df["games_played_so_far"] = df.groupby(by=["player_id"], as_index=False)["games_played"].cumsum()

    return df[["player_id", "event_date", "games_played_so_far"]]
