import pandas as pd


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:

    stocks["flag"] = [-1 if i == "Buy" else 1 for i in stocks["operation"]]
    stocks["price"] = stocks["flag"] * stocks["price"]
    df = stocks.groupby(by="stock_name", as_index=False)["price"].sum()
    df.rename(columns={"price": "capital_gain_loss"}, inplace=True)

    return df
