import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    examinations["attended_exams"] = 1
    examinations = examinations.groupby(by=["student_id", "subject_name"], as_index=False)["attended_exams"].sum()
    df = pd.merge(students, subjects, how="cross")
    df = pd.merge(df, examinations, how="left", on=["student_id", "subject_name"])
    df["attended_exams"].fillna(0, inplace=True)
    df.sort_values(by=["student_id", "subject_name"], ascending=True, inplace=True)

    return df
