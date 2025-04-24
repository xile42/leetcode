import pandas as pd


def grand_slam_titles(players: pd.DataFrame, championships: pd.DataFrame) -> pd.DataFrame:

    df = pd.melt(championships, id_vars="year", var_name="name", value_name="player_id")
    df = df.groupby(by="player_id", as_index=False)["year"].count()
    df = pd.merge(df, players, on="player_id", how="left")
    df.rename(columns={
        "year": "grand_slams_count",
    }, inplace=True)

    return df[["player_id", "player_name", "grand_slams_count"]]
