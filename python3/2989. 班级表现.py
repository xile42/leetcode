import pandas as pd


def class_performance(scores: pd.DataFrame) -> pd.DataFrame:

    scores["all"] = scores["assignment1"] + scores["assignment2"] + scores["assignment3"]
    result = scores["all"].max() - scores["all"].min()

    return pd.DataFrame({
        "difference_in_score": [result]
    })
