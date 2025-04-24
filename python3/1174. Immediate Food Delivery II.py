import pandas as pd


def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    df = delivery.sort_values(by="order_date", ascending=True).drop_duplicates(subset="customer_id", keep="first")
    df["immediate_percentage"] = df.apply(axis=1, func=lambda x: 1 if x["order_date"] == x["customer_pref_delivery_date"] else 0)
    value = round(100 * df["immediate_percentage"].sum() / len(df["immediate_percentage"]), 2)

    return pd.DataFrame({"immediate_percentage": [value]})
