from math import ceil
import pandas as pd


def calculate_team_tiers(team_stats: pd.DataFrame) -> pd.DataFrame:

    df = team_stats
    df["points"] = df["wins"] * 3 + df["draws"] * 1
    df["position"] = df["points"].rank(method="min", ascending=False)
    l = len(df)
    df["tier"] = df.apply(axis=1, func=lambda x: "Tier 1" if x["position"] <= ceil(l * 0.33) else ("Tier 2" if x["position"] <= ceil(l * 0.66) else "Tier 3"))
    df = df.sort_values(["points", "team_name"], ascending=[False, True])

    return df[["team_name", "points", "position", "tier"]]
