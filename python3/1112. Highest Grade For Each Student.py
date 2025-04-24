import pandas as pd


def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:

    enrollments.sort_values(by=["grade", "course_id"], ascending=[False, True], inplace=True)
    enrollments.drop_duplicates(subset="student_id", keep="first", inplace=True)
    enrollments.sort_values(by="student_id", inplace=True)

    return enrollments
