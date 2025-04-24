import pandas as pd


def tournament_winners(players: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:

    df = matches.copy()
    df = df.rename(columns={
        "first_player": "second_player",
        "second_player": "first_player",
        "first_score": "second_score",
        "second_score": "first_score"
    })
    df = pd.concat([matches[["first_player", "first_score"]], df[["first_player", "first_score"]]])
    df = df.rename(columns={"first_player": "player_id", "first_score": "score"})

    df = pd.merge(df, players, on="player_id", how="left")
    df = df.groupby(by=["group_id", "player_id"], as_index=False)["score"].sum()
    df = df.sort_values(by=["score", "player_id"], ascending=[False, True])
    df = df.drop_duplicates(subset="group_id", keep="first")

    return df[["group_id", "player_id"]]
