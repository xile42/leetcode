import pandas as pd


def find_unique_email_domains(emails: pd.DataFrame) -> pd.DataFrame:

    emails["email"] = emails["email"].apply(func=lambda x: x.split("@")[-1])
    df = emails[emails["email"].str.endswith(".com")].groupby("email", as_index=False)["id"].count()
    df = df.sort_values(by="email", ascending=True)
    df = df.rename(columns={"email": "email_domain", "id": "count"})

    return df
