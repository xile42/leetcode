import pandas as pd


def find_cutoff_score(schools: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:

##    exam = exam.sort_values(by="score", ascending=False)
    df = pd.merge(schools, exam, how="cross")
##    df["flag"] = df.apply(axis=1, func=lambda x: 1 if x["student_count"] <= x["capacity"] else 0)
##    df = df[df["flag"] == 1].groupby(by="school_id", as_index=False)["score"].min()
    df = df[df["student_count"] <= df["capacity"]].groupby(by="school_id", as_index=False)["score"].min()
    df = pd.merge(schools, df, on="school_id", how="left")
    df = df.fillna(-1)

    return df[["school_id", "score"]]
