import pandas as pd


def find_valid_users(products: pd.DataFrame) -> pd.DataFrame:

    df = pd.melt(products, id_vars="product_id", value_name="store", var_name="price")
    df = df.dropna(how="any")

    return df
