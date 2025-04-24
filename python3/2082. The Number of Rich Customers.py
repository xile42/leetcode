import pandas as pd


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:

    store["flag"] = store["amount"].apply(lambda x: 1 if x > 500 else 0)
    df = store.groupby(by="customer_id", as_index=False)["flag"].sum()

    return pd.DataFrame({
        "rich_count": [len(df[df["flag"] > 0])]
    })
