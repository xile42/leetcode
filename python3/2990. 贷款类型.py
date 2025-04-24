import pandas as pd


def loan_types(loans: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(loans, loans, "cross")
    df = df[(df["user_id_x"] == df["user_id_y"]) & (df["loan_type_x"] == "Refinance") & (df["loan_type_y"] == "Mortgage")]
    df.rename(columns={"user_id_x": "user_id"}, inplace=True)
    df = df[["user_id"]].drop_duplicates(subset="user_id").sort_values(by="user_id", ascending=True)

    return df[["user_id"]]
