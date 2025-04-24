import pandas as pd


def number_of_joiners(candidates: pd.DataFrame) -> pd.DataFrame:

    df1 = candidates[candidates["experience"] == "Senior"].sort_values("salary")
    df1["cum"] = df1["salary"].cumsum()
    df2 = candidates[candidates["experience"] == "Junior"].sort_values("salary")
    df2["cum"] = df2["salary"].cumsum()

    rem = 70000
    pick1 = df1[df1["cum"] <= rem]
    rem -= 0 if len(pick1) == 0 else pick1.iloc[-1]["cum"]
    pick2 = df2[df2["cum"] <= rem]

    return pd.concat([pick1[["employee_id"]], pick2[["employee_id"]]])
