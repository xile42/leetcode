import pandas as pd


def find_second_day_signups(emails: pd.DataFrame, texts: pd.DataFrame) -> pd.DataFrame:

    emails["signup_date"] = emails["signup_date"].apply(func=lambda x: pd.to_datetime(str(x)[:10]))
    texts["action_date"] = texts["action_date"].apply(func=lambda x: pd.to_datetime(str(x)[:10]))
    df = pd.merge(emails, texts[texts["signup_action"] == "Verified"], on="email_id", how="inner")
    df = df[df["signup_date"] + pd.Timedelta(days=1) == df["action_date"]][["user_id"]].sort_values(by="user_id", ascending=True)

    return df