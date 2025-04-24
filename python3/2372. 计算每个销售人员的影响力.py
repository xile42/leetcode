import pandas as pd


def calculate_influence(salesperson: pd.DataFrame, customer: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(customer, sales, on="customer_id", how="left")
    df = df.groupby("salesperson_id", as_index=False).agg(
        total=("price", "sum")
    )
    df = pd.merge(salesperson, df, on="salesperson_id", how="left")
    df = df.fillna(0)

    return df[["salesperson_id", "name", "total"]]
