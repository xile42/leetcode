import pandas as pd

def generate_the_invoice(products: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:

    base = pd.merge(purchases, products, on="product_id", how="left")
    base["price"] = base["quantity"] * base["price"]
    df = base.groupby("invoice_id", as_index=False)["price"].sum()
    df = df.sort_values(["price", "invoice_id"], ascending=[False, True])
    v = df.iloc[0]["invoice_id"]
    result = base[base["invoice_id"] == v][["product_id", "quantity", "price"]]

    return result
