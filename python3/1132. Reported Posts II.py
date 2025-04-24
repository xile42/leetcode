import pandas as pd


def reported_posts(actions: pd.DataFrame, removals: pd.DataFrame) -> pd.DataFrame:

    actions = actions[(actions["action"] == "report") & (actions["extra"] == "spam")]
    df = pd.merge(actions.drop_duplicates(subset=["post_id", "action_date"], keep="first"), removals, on="post_id", how="left")
    df = df.groupby(by="action_date", as_index=False).agg(
        ratio=("remove_date", lambda x: x.count() /len(x) * 100)
    )
    result = round(df["ratio"].mean(), 2)

    return pd.DataFrame({
        "average_daily_percent": [result]
    })
