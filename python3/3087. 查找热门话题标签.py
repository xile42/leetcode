import re
import pandas as pd


def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:

    df = tweets[tweets["tweet_date"].dt.month == 2]
    df["hashtag"] = df["tweet"].apply(func=lambda x: re.findall(r"#[a-zA-Z0-9]+", x)[0])
    df = df.groupby("hashtag", as_index=False).agg(
        hashtag_count=("tweet_id", "count")
    )
##    df["rank"] = df["hashtag_count"].rank(method="min", ascending=False)
##    df = df[df["rank"] <= 3][["hashtag", "hashtag_count"]].sort_values(["hashtag_count", "hashtag"], ascending=False)

    df = df[["hashtag", "hashtag_count"]].sort_values(["hashtag_count", "hashtag"], ascending=False)
    df = df.iloc[:3]

    return df
