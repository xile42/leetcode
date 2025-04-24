import pandas as pd


def immediate_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    delivery["flag"] = delivery.apply(axis=1, func=lambda x: 1 if x["customer_pref_delivery_date"] == x["order_date"] else 0)
    df = delivery.groupby("order_date", as_index=False).agg(
        imm=("flag", "sum"),
        all=("flag", "count")
    )
    df["immediate_percentage"] = (df["imm"] * 100 / df["all"]).round(2)
    df = df.sort_values("order_date")

    return df[["order_date", "immediate_percentage"]]
