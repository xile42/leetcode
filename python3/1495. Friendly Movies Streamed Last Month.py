import pandas as pd


def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:

    content["content_id"] = content["content_id"].apply(func=lambda x: int(x))
    df = pd.merge(content, tv_program, on="content_id", how="left")
    df = df[(df["program_date"].dt.strftime("%Y-%m") == "2020-06") & (df["Kids_content"] == "Y") & (df["content_type"] == "Movies")][["title"]].drop_duplicates(subset="title", keep="first")

    return df
