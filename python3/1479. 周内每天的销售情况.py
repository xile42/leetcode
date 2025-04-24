import pandas as pd


def sales_by_day(orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:

    d = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    base1 = pd.DataFrame({"item_category": items["item_category"].unique()})
    base2 = pd.DataFrame({"dow": d})
    base = pd.merge(base1, base2, how="cross")
    df = pd.merge(orders, items, on="item_id", how="left")
    df["dow"] = df["order_date"].dt.day_of_week
    df["dow"] = df["dow"].apply(func=lambda x: d[x])
    df = df.groupby(["dow", "item_category"], as_index=False).agg(count=("quantity", "sum"))
    df = pd.merge(base, df, on=["dow", "item_category"], how="left").fillna(0)
    df = pd.pivot(df, index="item_category", columns="dow", values="count")
    df = df.reset_index()
    df = df.rename(columns={"item_category": "CATEGORY"})
    df = df.sort_values("CATEGORY")
    df = df[["CATEGORY"] + d]

    return df
