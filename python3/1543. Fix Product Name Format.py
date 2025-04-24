import pandas as pd


def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:

    sales["sale_date"] = sales["sale_date"].apply(func=lambda x: str(x)[:7])
    sales["product_name"] = sales["product_name"].apply(func=lambda x: x.strip().lower())
    df = sales.groupby(by=["sale_date", "product_name"], as_index=False)["sale_id"].count()
    df.rename(columns={"sale_id": "total"}, inplace=True)
    df.sort_values(by=["product_name", "sale_date"], ascending=[True, True], inplace=True)

    return df[["product_name", "sale_date", "total"]]
