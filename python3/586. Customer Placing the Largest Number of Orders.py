import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    from collections import Counter

    ids = orders["customer_number"].tolist()
    counter = Counter(ids)
    sorted_kv = sorted(list(counter.items()), key=lambda x: x[-1], reverse=True)

    if len(sorted_kv) == 0:
        return pd.DataFrame({"customer_number": []})
    else:
        return pd.DataFrame({"customer_number": [sorted_kv[0][0]]})
