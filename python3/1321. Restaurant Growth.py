import pandas as pd


def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:

    df = customer.groupby(by="visited_on", as_index=False)["amount"].sum()
    df["amount"] = df["amount"].rolling(7).sum()
    df["average_amount"] = (df["amount"] / 7).round(2)
    df.sort_values(by="visited_on", inplace=True)

    return df.dropna()
