import pandas as pd


def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    df = vote.groupby(by="candidateId", as_index=False)["id"].count()
    df.rename(columns={"id": "count"}, inplace=True)
    df = pd.merge(df, candidate, left_on="candidateId", right_on="id", how="left")
    df = df.sort_values(by="count", ascending=False)

    return pd.DataFrame({
        "name": [df.iloc[0]["name"]]
    })
