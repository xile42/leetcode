import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:

    actor_director["flag"] = 1
    df = actor_director.groupby(by=["actor_id", "director_id"], as_index=False)["flag"].sum()
    df = df[df["flag"] >= 3][["actor_id", "director_id"]]

    return df
