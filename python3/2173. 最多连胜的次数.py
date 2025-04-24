import pandas as pd
from itertools import groupby


def f(x):

    s = "".join(["W" if i == "Win" else ("D" if i == "Draw" else "L") for i in x])
    ans = -1
    for c, ite in groupby(s):
        if c == "W":
            ans = max(ans, len(list(ite)))

    return 0 if ans == -1 else ans


def longest_winning_streak(matches: pd.DataFrame) -> pd.DataFrame:
    
    df = matches.sort_values(["player_id", "match_day"])
    df = df.groupby("player_id", as_index=False).agg(
        longest_streak=("result", lambda x: f(x))
    )

    return df
