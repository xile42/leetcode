import re
import pandas as pd


def f(s):

    r1 = re.findall(r"@[\w]+", s)
    r2 = re.findall(r"#[\w]+", s)
    l = len(s)

    if len(s) > 140 or len(r1) > 3 or len(r2) > 3:
        return 1
    return 0


def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    tweets["flag"] = tweets["content"].apply(func=f)
    df = tweets[tweets["flag"] == 1][["tweet_id"]].sort_values(by="tweet_id", ascending=True)

    return df    
