import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    return pd.DataFrame({
        "immediate_percentage": [round(100 * len(delivery[delivery["order_date"] == delivery["customer_pref_delivery_date"]]) / len(delivery), 2)],
    })
