import pandas as pd


def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(teams, teams, how="cross")
    df = df[df["team_name_x"] != df["team_name_y"]]
    df = df.rename(columns={"team_name_x": "home_team", "team_name_y": "away_team"})

    return df    
