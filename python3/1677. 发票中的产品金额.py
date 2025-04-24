import pandas as pd

def analyze_products(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(product, invoice, how="left", on="product_id")
    df.fillna(0, inplace=True)
    df = df.groupby(by="name", as_index=False).agg({
        "rest": "sum",
        "paid": "sum",
        "canceled": "sum",
        "refunded": "sum",
    })
    
    df.sort_values(by="name", ascending=True, inplace=True)

    return df[["name", "rest", "paid", "canceled", "refunded"]]
