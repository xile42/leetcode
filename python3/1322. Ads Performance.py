import pandas as pd


def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:

    click = ads.groupby("ad_id")["action"].agg(lambda x: sum([1 if i == "Clicked" else 0 for i in x])).rename("click", inplace=True)
    view = ads.groupby("ad_id")["action"].agg(lambda x: sum([1 if i == "Viewed" else 0 for i in x])).rename("view", inplace=True)
    df = pd.concat([click, view], axis=1).reset_index()
    df["ctr"] = df.apply(lambda row: 0 if row["click"] + row["view"] == 0 else round(100 * row["click"] / (row["click"] + row["view"]), 2), axis=1)
    df = df[["ad_id", "ctr"]]
    df.sort_values(by=["ctr", "ad_id"], ascending=[False, True], inplace=True)

    return df
