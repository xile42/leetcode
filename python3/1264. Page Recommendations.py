import pandas as pd


def page_recommendations(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:

    valid_user1 = friendship[(friendship["user1_id"] == 1)]["user2_id"]
    valid_user2 = friendship[(friendship["user2_id"] == 1)]["user1_id"]
    valid_user = pd.concat([valid_user1, valid_user2])
    invalid_page = likes[likes["user_id"] == 1]["page_id"]

    df = likes[(likes["user_id"].isin(valid_user)) & (~likes["page_id"].isin(invalid_page))][["page_id"]].rename(columns={"page_id": "recommended_page"}).drop_duplicates(subset="recommended_page")

    return df
