import pandas as pd


def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:

    df1 = products[products["change_date"] <= "2019-08-16"].sort_values(by="change_date", ascending=True).drop_duplicates(subset="product_id", keep="last")[["product_id", "new_price"]]
    df1.rename(columns={"new_price": "price"}, inplace=True)
    df2 = products.drop_duplicates(subset="product_id", keep="first")
    df = pd.merge(df2, df1, on="product_id", how="left")
    df.fillna(10, inplace=True)

    return df[["product_id", "price"]]
