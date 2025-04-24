import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(orders, company, on="com_id", how="left")
    df = pd.merge(df, sales_person, on="sales_id", how="outer")
    df["flag"] = df["name_x"].apply(lambda x: 1 if x == "RED" else 0)
    df = df.groupby(by="name_y", as_index=False)["flag"].sum()
    df = df[df["flag"] == 0][["name_y"]]
    df.rename(columns={"name_y": "name"}, inplace=True)

    return df
