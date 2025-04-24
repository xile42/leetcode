import pandas as pd


def count_seniors_and_juniors(candidates: pd.DataFrame) -> pd.DataFrame:

    df1 = candidates[candidates["experience"] == "Senior"].sort_values("salary")
    df1["cum"] = df1["salary"].cumsum()
    df2 = candidates[candidates["experience"] == "Junior"].sort_values("salary")
    df2["cum"] = df2["salary"].cumsum()

    remain = 70000
    pick1 = df1[df1["cum"] <= remain]
    l1 = len(pick1)
    remain = 70000 if l1 == 0 else 70000 - pick1.iloc[-1]["cum"]

    pick2 = df2[df2["cum"] <= remain]
    l2 = len(pick2)

    return pd.DataFrame({"experience": ["Senior", "Junior"], "accepted_candidates": [l1, l2]})
