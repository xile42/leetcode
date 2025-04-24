import pandas as pd


def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:

    a = len(new_york[new_york["score"] >= 90])
    b = len(california[california["score"] >= 90])

    return pd.DataFrame({
        "winner": ["New York University" if a > b else ("California University" if a < b else "No Winner")]
    })
