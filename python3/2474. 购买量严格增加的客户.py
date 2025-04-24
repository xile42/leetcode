import pandas as pd


def f(x):

    vs = x.tolist()
    while len(vs) and vs[0] == -1:
        vs.pop(0)
    while len(vs) and vs[-1] == -1:
        vs.pop(-1)

    return True if len(vs) == 1 or all(vs[i] < vs[i + 1] for i in range(len(vs) - 1)) else False


def find_specific_customers(orders: pd.DataFrame) -> pd.DataFrame:

    cids = orders["customer_id"].drop_duplicates()
    df = orders
    df["y"] = df["order_date"].dt.year
    min_y, max_y = df["y"].min(), df["y"].max()
    ys = pd.DataFrame({"y": list(range(min_y, max_y + 1))})
    base = pd.merge(cids, ys, how="cross")

    df = df.groupby(["customer_id", "y"], as_index=False)["price"].sum()
    df = pd.merge(base, df, on=["customer_id", "y"], how="left").fillna(-1)
    df = df.sort_values(["customer_id", "y"])
    df = df.groupby("customer_id", as_index=False)["price"].apply(f)
    df = df[df["price"]][["customer_id"]]

    return df
