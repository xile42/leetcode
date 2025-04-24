import pandas as pd


def team_scores(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:

    matches["host_score"] = matches.apply(axis=1, func=lambda x: 3 if x["host_goals"] > x["guest_goals"] else (1 if x["host_goals"] == x["guest_goals"] else 0))
    matches["guest_score"] = matches.apply(axis=1, func=lambda x: 3 if x["host_goals"] < x["guest_goals"] else (1 if x["host_goals"] == x["guest_goals"] else 0))

    df1 = pd.merge(teams, matches, how="left", left_on="team_id", right_on="host_team")
    df1 = df1.groupby(by="team_id", as_index=False)["host_score"].sum()

    df2 = pd.merge(teams, matches, how="left", left_on="team_id", right_on="guest_team")
    df2 = df2.groupby(by="team_id", as_index=False)["guest_score"].sum()

    df = pd.merge(df1, df2, on="team_id", how="outer")
    df = pd.merge(df, teams, on="team_id", how="left")
    df["num_points"] = df.apply(axis=1, func=lambda x: x["host_score"] + x["guest_score"])
    df.sort_values(by=["num_points", "team_id"], ascending=[False, True], inplace=True)

    return df[["team_id", "team_name", "num_points"]]
