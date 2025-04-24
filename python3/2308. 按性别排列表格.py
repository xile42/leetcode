import pandas as pd


def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:

    df = genders.copy()
    df["rank"] = df.groupby(by="gender", as_index=False)["user_id"].rank(method="dense")
    df["flag"] = df.apply(axis=1, func=lambda x: x["rank"] + 0.1 if x["gender"] == "female" else (x["rank"] + 0.2 if x["gender"] == "other" else x["rank"] + 0.3))
    df = df.sort_values(by=["flag"])

    return df[["user_id", "gender"]]
