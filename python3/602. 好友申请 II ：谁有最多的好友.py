import pandas as pd


def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:

    df1 = request_accepted.groupby(by="accepter_id", as_index=False)["requester_id"].nunique()
    df1.rename(columns={"accepter_id": "id", "requester_id": "num1"}, inplace=True)

    df2 = request_accepted.groupby(by="requester_id", as_index=False)["accepter_id"].nunique()
    df2.rename(columns={"accepter_id": "num2", "requester_id": "id"}, inplace=True)

    df = pd.merge(df1, df2, how="outer", on="id")
    df.fillna(0, inplace=True)
    df["num"] = df["num1"] + df["num2"]
    df.sort_values(by="num", inplace=True, ascending=False)

    return df[["id", "num"]].iloc[0:1]
