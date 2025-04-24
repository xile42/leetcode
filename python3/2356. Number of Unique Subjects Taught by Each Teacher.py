import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    df = teacher.groupby(by="teacher_id").nunique()
    df.rename(columns={"subject_id": "cnt"}, inplace=True)
    df["teacher_id"] = df.index

    return df[["teacher_id", "cnt"]]
