import pandas as pd


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    customer.drop_duplicates(keep="first", inplace=True)
    df = pd.merge(product, customer, on="product_key", how="left")
    df = df.groupby(by="customer_id", as_index=False)["product_key"].nunique()
    n = len(product)
    df = df[df["product_key"] == n][["customer_id"]]

    return df
