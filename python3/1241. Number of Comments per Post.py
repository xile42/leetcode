import pandas as pd


def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:

    submissions.drop_duplicates(inplace=True)
    df1 = submissions[submissions["parent_id"].isna()]
    df2 = submissions[~ submissions["parent_id"].isna()]
    df = pd.merge(df1, df2, how="left", left_on="sub_id", right_on="parent_id")
    df = df.groupby("sub_id_x", as_index=False)["sub_id_y"].nunique()
    df.rename(columns={
        "sub_id_x": "post_id",
        "sub_id_y": "number_of_comments",
    }, inplace=True)

    return df
