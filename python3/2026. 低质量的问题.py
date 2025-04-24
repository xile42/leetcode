import pandas as pd


def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:

    problems["rate"] = problems["likes"] / (problems["likes"] + problems["dislikes"])
    df = problems[problems["rate"] < 0.6][["problem_id"]].sort_values(by="problem_id", ascending=True)

    return df    
