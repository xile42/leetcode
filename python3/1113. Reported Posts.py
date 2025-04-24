import pandas as pd


def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:

    df = actions[(actions["action_date"] == "2019-07-04") & (actions["action"] == "report")]
    df = df.groupby(by="extra", as_index=False)["post_id"].nunique()
    df.rename(columns={
        "extra": "report_reason",
        "post_id": "report_count"
    }, inplace=True)

    return df
