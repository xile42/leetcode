import pandas as pd


def geography_report(student: pd.DataFrame) -> pd.DataFrame:

    df = student.sort_values("name")
    df["r"] = df.groupby("continent", as_index=False).rank(method="first")
    df = df.pivot(index="r", columns="continent", values="name").reset_index()

    for col in ["America", "Asia", "Europe"]:
        if col not in df.columns:
            df[col] = [None for _ in range(len(df))]

    return df[["America", "Asia", "Europe"]]
