import pandas as pd


def find_quiet_students(student: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:

    exam["rank"] = exam.groupby(by="exam_id", as_index=False)["score"].rank(method="dense", ascending=False)
    exam["top1"] = exam.groupby(by="exam_id", as_index=False)["rank"].transform("max")
    exam["topn"] = exam.groupby(by="exam_id", as_index=False)["rank"].transform("min")
    exam["flag"] = exam.apply(axis=1, func=lambda x: 1 if (x["rank"] == x["top1"] or x["rank"] == x["topn"]) else 0)
    df = exam.groupby(by="student_id", as_index=False)["flag"].sum()
    df = df[df["flag"] == 0][["student_id"]]
    df = pd.merge(df, student, how="left", on="student_id")[["student_id", "student_name"]]

    return df
