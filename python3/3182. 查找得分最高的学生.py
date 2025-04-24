import pandas as pd


def find_top_scoring_students(enrollments: pd.DataFrame, students: pd.DataFrame, courses: pd.DataFrame) -> pd.DataFrame:

    courses["count"] = courses.groupby("major", as_index=False)["course_id"].transform("count")
    enrollments["flag"] = enrollments["grade"].apply(func=lambda x: 1 if x == "A" else 0)
    df = pd.merge(students, courses, on="major", how="left")
    df = pd.merge(df, enrollments, on=["student_id", "course_id"], how="left")
    df["flag"] = df.groupby(["student_id", "major"], as_index=False)["flag"].transform("sum")
    df = df[df["flag"] == df["count"]][["student_id"]].sort_values("student_id").drop_duplicates()

    return df
