import pandas as pd


def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:

    scores = rounds.groupby(by="interview_id", as_index=False)["score"].sum()
    df = pd.merge(candidates, scores, on="interview_id", how="left")
    df = df[(df["years_of_exp"] >= 2) & (df["score"] > 15)][["candidate_id"]]

    return df
