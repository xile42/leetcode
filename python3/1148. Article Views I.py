import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:

    df = views[views["author_id"] == views["viewer_id"]][["author_id"]].drop_duplicates(keep="first")
    df.rename(columns={"author_id": "id"}, inplace=True)
    df.sort_values(by="id", ascending=True, inplace=True)

    return df