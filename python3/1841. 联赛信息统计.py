import pandas as pd


def league_statistics(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:

    matches["home_score"] = matches.apply(axis=1, func=lambda x: 3 if x["home_team_goals"] > x["away_team_goals"] else (0 if x["home_team_goals"] < x["away_team_goals"] else 1))
    matches["away_score"] = matches.apply(axis=1, func=lambda x: 3 if x["home_team_goals"] < x["away_team_goals"] else (0 if x["home_team_goals"] > x["away_team_goals"] else 1))
    
    df1 = matches.groupby("home_team_id", as_index=False).agg(
        home_count=("home_team_goals", "count"),
        goal_for=("home_team_goals", "sum"),
        goal_against=("away_team_goals", "sum"),
        points=("home_score", "sum")
    ).rename(columns={"home_team_id": "team_id"})
    
    df2 = matches.groupby("away_team_id", as_index=False).agg(
        away_count=("away_team_goals", "count"),
        goal_for=("away_team_goals", "sum"),
        goal_against=("home_team_goals", "sum"),
        points=("away_score", "sum")
    ).rename(columns={"away_team_id": "team_id"})
    
    df3 = pd.merge(df1, df2, how="outer", on="team_id").fillna(0)
    df3["matches_played"] = df3["home_count"] + df3["away_count"]
    df3["points"] = df3["points_x"] + df3["points_y"]
    df3["goal_for"] = df3["goal_for_x"] + df3["goal_for_y"]
    df3["goal_against"] = df3["goal_against_x"] + df3["goal_against_y"]
    df3["goal_diff"] = df3["goal_for"] - df3["goal_against"]

    df = pd.merge(df3, teams, on="team_id", how="left")
    df = df.sort_values(by=["points", "goal_diff", "team_name"], ascending=[False, False, True])

    return df[["team_name", "matches_played", "points", "goal_for", "goal_against", "goal_diff"]]

