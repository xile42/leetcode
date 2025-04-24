import pandas as pd


def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    
    df = follow.groupby(by="followee", as_index=False)["follower"].count()
    df.rename(columns={"follower": "num"}, inplace=True)
    df = pd.merge(follow[["follower"]].drop_duplicates(), df, how="left", left_on="follower", right_on="followee")
    df = df[df["num"].notna()][["follower", "num"]]
    df.sort_values(by="follower", ascending=True, inplace=True)

    return df
