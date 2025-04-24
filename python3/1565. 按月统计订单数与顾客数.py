import pandas as pd

def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:

    orders["month"] = orders["order_date"].apply(func=lambda x: str(x)[:7])
    df = orders[orders["invoice"] > 20].groupby(by="month", as_index=False).agg({
            "order_id": "nunique",
            "customer_id": "nunique"
        })
    df.rename(columns={
            "order_id": "order_count",
            "customer_id": "customer_count"
        }, inplace=True)

    return df[["month", "order_count", "customer_count"]]
    
