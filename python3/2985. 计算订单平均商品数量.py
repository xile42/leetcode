import pandas as pd


def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:

    orders["t"] = orders["item_count"] * orders["order_occurrences"]
    result = round(orders["t"].sum() / orders["order_occurrences"].sum(), 2)

    return pd.DataFrame({
        "average_items_per_order": [result]
    })
