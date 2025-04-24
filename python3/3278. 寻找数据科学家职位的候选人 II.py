import pandas as pd


def find_best_candidates(candidates: pd.DataFrame, projects: pd.DataFrame) -> pd.DataFrame:

    need = projects.groupby("project_id", as_index=False).agg(
        need=("skill", "nunique")
    )
    df = pd.merge(candidates, projects, on="skill", how="left")
    df["score"] = df.apply(axis=1, func=lambda x: 10 if x["proficiency"] > x["importance"] else (-5 if x["proficiency"] < x["importance"] else 0))
    df = df.groupby(["candidate_id", "project_id"], as_index=False).agg(
        score=("score", "sum"),
        flag=("skill", "count")
    )
    df = pd.merge(df, need, on="project_id", how="left")
    df = df[df["flag"] == df["need"]]
    df["score"] += 100
    df = df.sort_values(["project_id", "score", "candidate_id"], ascending=[True, False, True]).drop_duplicates(subset="project_id", keep="first")
    df = df.sort_values("project_id")[["project_id", "candidate_id", "score"]]

    return df
