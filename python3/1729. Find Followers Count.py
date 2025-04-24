import pandas as pd


def count_followers(followers: pd.DataFrame) -> pd.DataFrame:

    followers = followers.groupby(by="user_id", as_index=False)["follower_id"].count()
    followers.rename(columns={"follower_id": "followers_count"}, inplace=True)
    followers = followers[["user_id", "followers_count"]]

    return followers
