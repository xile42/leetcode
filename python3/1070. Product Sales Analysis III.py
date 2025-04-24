import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    sales["first_year"] = sales.groupby(by="product_id", as_index=False)["year"].transform("min")
    df = sales[sales["first_year"] == sales["year"]][["product_id", "first_year", "quantity", "price"]]

    return df
