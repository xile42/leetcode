import pandas as pd


def global_ratings_change(team_points: pd.DataFrame, points_change: pd.DataFrame) -> pd.DataFrame:

    df = team_points.copy().sort_values(by=["points", "name"], ascending=[False, True])
    df["rank_ori"] = df["points"].rank(method="first", ascending=False)

    df1 = points_change.groupby("team_id")["points_change"].sum()
    df = pd.merge(df, df1, on="team_id", how="left").fillna(0)
    df["points"] = df["points"] + df["points_change"]
    df = df.sort_values(by=["points", "name"], ascending=[False, True])
    df["rank"] = df["points"].rank(method="first", ascending=False)
    df["rank_diff"] = -(df["rank"] - df["rank_ori"])

    return df[["team_id", "name", "rank_diff"]]
