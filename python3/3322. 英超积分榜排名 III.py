import pandas as pd


def process_team_standings(season_stats: pd.DataFrame) -> pd.DataFrame:

    df = season_stats
    df["points"] = df["wins"] * 3 + df["draws"]
    df["goal_difference"] = df["goals_for"] - df["goals_against"]
    df = df.sort_values(["season_id", "points", "goal_difference", "team_name"], ascending=[True, False, False, True]).reset_index()
    df["id"] = df.index
    df["position"] = df.groupby("season_id", as_index=False)["id"].rank(method="first")

    return df[["season_id", "team_id", "team_name", "points", "goal_difference", "position"]]
