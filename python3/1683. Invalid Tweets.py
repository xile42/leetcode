import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    tweets["length"] = tweets["content"].apply(lambda x: len(x))
    df = tweets[tweets["length"] > 15][["tweet_id"]]
    # df = tweets[tweets["content"].str.len() > 15][["tweet_id"]]

    return df
