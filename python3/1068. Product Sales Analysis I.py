import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(left=sales, right=product, left_on="product_id", right_on="product_id", how="left")

    return df[["product_name", "year", "price"]]
