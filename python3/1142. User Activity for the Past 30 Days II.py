import datetime
import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:

    df = activity[(activity["activity_date"] > "2019-06-27") & (activity["activity_date"] <= "2019-07-27")]
    session_count = df["session_id"].nunique()
    user_count = df["user_id"].nunique()

    if user_count == 0:
        return pd.DataFrame({
            "average_sessions_per_user": [0]
        })

    return pd.DataFrame({
        "average_sessions_per_user": [round(session_count / user_count, 2)]
    })
