import pandas as pd

def products_price(products: pd.DataFrame) -> pd.DataFrame:

    df = products.pivot(index="product_id", columns="store", values="price")
    df = df.reset_index()

    return df
