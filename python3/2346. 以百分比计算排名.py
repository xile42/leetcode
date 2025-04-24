import pandas as pd


def compute_rating(students: pd.DataFrame) -> pd.DataFrame:

    students["rank"] = students.groupby("department_id", as_index=False)["mark"].rank(method="min", ascending=False)
    df = students.groupby("department_id", as_index=False).agg(
        count=("student_id", "count")
    )
    df = pd.merge(students, df, on="department_id", how="left")
    df["percentage"] = df.apply(axis=1, func=lambda x: 100 * (x["rank"] - 1) / (x["count"] - 1)).round(2)
    df = df.fillna(0)

    return df[["student_id", "department_id", "percentage"]]
