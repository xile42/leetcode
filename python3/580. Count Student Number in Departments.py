import pandas as pd


def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(department, student, on="dept_id", how="left")
    df = df.groupby(by="dept_name", as_index=False)["student_id"].count()
    df.fillna(0, inplace=True)
    df.sort_values(by=["student_id", "dept_name"], ascending=[False, True], inplace=True)
    df.rename(columns={
        "student_id": "student_number"
    }, inplace=True)

    return df[["dept_name", "student_number"]]
