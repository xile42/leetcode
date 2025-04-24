import re
import pandas as pd


def f(x):

    if "#" not in x:
        return []

    return re.findall("#[a-zA-z]*", x)
    


def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:

    df = tweets[(tweets["tweet_date"].dt.year == 2024) & (tweets["tweet_date"].dt.month == 2)]
    df["hashtag"] = df["tweet"].apply(f)
    df = df[["hashtag"]].explode("hashtag")
    df = df.groupby("hashtag", as_index=False).agg(
        count=("hashtag", "count")
    )
    df = df.sort_values(["count", "hashtag"], ascending=[False, False])
    df["r"] = df["count"].rank(method="first", ascending=False)
    df = df[df["r"] <= 3]

    return df[["hashtag", "count"]]
