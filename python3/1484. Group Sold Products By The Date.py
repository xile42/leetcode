import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    df = activities.groupby(by="sell_date", as_index=False)["product"].agg(lambda x: ",".join(sorted(set(x))))
    df["num_sold"] = df["product"].apply(lambda x: len(x.split(",")))
    df.rename(columns={"product": "products"}, inplace=True)
    df = df[["sell_date", "num_sold", "products"]].sort_values(by="sell_date")

    return df
