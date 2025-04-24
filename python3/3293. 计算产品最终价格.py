import pandas as pd


def calculate_final_prices(products: pd.DataFrame, discounts: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(products, discounts, on="category", how="left").fillna(0)
    df["final_price"] = df["price"] * (100 - df["discount"]) / 100
    df = df.sort_values("product_id")[["product_id", "final_price", "category"]]

    return df
