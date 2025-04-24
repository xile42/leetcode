import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    df = sales.groupby(by="product_id", as_index=False)["quantity"].sum()
    df.rename(columns={"quantity": "total_quantity"}, inplace=True)

    return df[["product_id", "total_quantity"]]
