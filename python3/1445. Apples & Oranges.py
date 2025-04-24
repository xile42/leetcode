import pandas as pd


def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:

    df = pd.pivot(sales, columns="fruit", index="sale_date", values="sold_num")
    df.fillna(0, inplace=True)
    df["diff"] = df["apples"] - df["oranges"]
    df.sort_values(by="sale_date", inplace=True)
    df.reset_index(inplace=True)

    return df[["sale_date", "diff"]]
