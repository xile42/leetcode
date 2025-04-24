import numpy as np
import pandas as pd


def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:

    survey_log["f1"] = survey_log["action"].apply(func=lambda x: 1 if x == "show" else 0)
    survey_log["f2"] = survey_log["action"].apply(func=lambda x: 1 if x == "answer" else 0)
    df = survey_log.groupby(by="question_id", as_index=False).agg({
        "f1": "sum",
        "f2": "sum"
    })
    df["ratio"] = df["f2"] / df["f1"]

    if len(df) == 0:
        return pd.DataFrame({
            "survey_log": []
        })

    df = df[~ np.isinf(df["ratio"])].sort_values(by=["ratio", "question_id"], ascending=[False, True])

    return pd.DataFrame({
        "survey_log": [df.iloc[0]["question_id"]] if len(df) > 0 else []
    })
