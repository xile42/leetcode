import pandas as pd


def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:

    candidates["flag"] = candidates["skill"].apply(func=lambda x: 1 if x == "Python" else (2 if x == "Tableau" else (3 if x == "PostgreSQL" else 0)))
    df = candidates.groupby(by="candidate_id", as_index=False)["flag"].sum()
    df = df[df["flag"] == 6][["candidate_id"]].sort_values(by="candidate_id", ascending=True)

    return df
