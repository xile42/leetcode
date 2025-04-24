import pandas as pd


def find_top_scoring_students(students: pd.DataFrame, courses: pd.DataFrame, enrollments: pd.DataFrame) -> pd.DataFrame:

    students = students.rename(columns={"major": "student_major"})
    courses = courses.rename(columns={"major": "course_major"})
    courses["cnt"] = courses["mandatory"].apply(lambda x: 1 if x == "Yes" else 0)
    base = courses.groupby("course_major", as_index=False)["cnt"].sum()

    df1 = pd.merge(
        enrollments[["student_id", "course_id", "grade"]],
        courses[["course_id", "course_major", "cnt"]],
        on="course_id", how="left"
    )
    df1 = pd.merge(
        df1,
        students[["student_id", "student_major"]],
        on="student_id", how="left"
    )
    df1 = df1[df1["course_major"] == df1["student_major"]]
    df2 = df1.copy()
    df3 = df1.copy()
    df4 = df1.copy()

    df1["bx_sum"] = df1.groupby("student_id", as_index=False)["cnt"].transform("sum")
    df1 = df1[["student_id", "student_major", "bx_sum"]]
    df1 = pd.merge(df1, base, left_on="student_major", right_on="course_major", how="left")
    res1 = set(df1[df1["bx_sum"] == df1["cnt"]]["student_id"].tolist())

    df2 = df2[df2["cnt"] == 0].groupby("student_id", as_index=False)["cnt"].count()
    res2 = set(df2[df2["cnt"] >= 2]["student_id"].tolist())

    df3 = df3[df3["cnt"] == 1]
    df3["bx_grade"] = df3["grade"].apply(func=lambda x: 1 if x != "A" else 0)
    df3 = df3.groupby("student_id", as_index=False)["bx_grade"].sum()
    res3 = set(df3[df3["bx_grade"] == 0]["student_id"].tolist())

    df4 = df4[df4["cnt"] == 0]
    df4["bx_grade"] = df4["grade"].apply(func=lambda x: 1 if x != "A" and x != "B" else 0)
    df4 = df4.groupby("student_id", as_index=False)["bx_grade"].sum()
    res4 = set(df4[df4["bx_grade"] == 0]["student_id"].tolist())

    df5 = enrollments.groupby("student_id", as_index=False)["GPA"].mean()
    res5 = set(df5[df5["GPA"] >= 2.5]["student_id"].tolist())

    res = res1 & res2 & res3 & res4 & res5

    df = pd.DataFrame({"student_id": list(res)})
    df = df.sort_values("student_id")

    return df
