import pandas as pd


def f(x):

    x["prev_year_spend"] = x["curr_year_spend"].shift(1)
    x["yoy_rate"] = ((x["curr_year_spend"] - x["prev_year_spend"]) / x["prev_year_spend"] * 100).round(2)

    return x


def calculate_yoy_growth(user_transactions: pd.DataFrame) -> pd.DataFrame:

    df = user_transactions
    df["year"] = df["transaction_date"].dt.year
    df = df.groupby(["year", "product_id"], as_index=False).agg(
        curr_year_spend=("spend", "sum")
    )
    df = df.sort_values(["product_id", "year"])
    df = df.groupby("product_id", as_index=False)[["product_id", "year", "curr_year_spend"]].apply(f).reset_index(drop=True)

    return df[["year", "product_id", "curr_year_spend", "prev_year_spend", "yoy_rate"]]
