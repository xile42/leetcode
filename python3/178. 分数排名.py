import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores.sort_values(by="score", ascending=False, inplace=True)
    scores.reset_index(inplace=True)
    scores["rank"] = 1
    for idx in range(1, len(scores)):
        if scores.loc[idx, "score"] == scores.loc[idx-1, "score"]:
            scores.loc[idx, "rank"] = scores.loc[idx-1, "rank"]
        else:
            scores.loc[idx, "rank"] = scores.loc[idx-1, "rank"] + 1

    return scores[["score", "rank"]]
