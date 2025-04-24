import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:

    views = views.drop_duplicates()
    df = views.groupby(["viewer_id", "view_date"], as_index=False)["article_id"].nunique()
    df = df[df["article_id"] >= 2][["viewer_id"]].sort_values("viewer_id", ascending=True)
    df = df.rename(columns={"viewer_id": "id"})
    df = df[["id"]].drop_duplicates()

    return df
