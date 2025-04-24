import pandas as pd


def f(x):

    x = x.values
    customer_id, cur_d, cur_a = x[0]
    groups = list()
    one_group = [[cur_d, cur_a]]
    for _, d, a in x[1:]:
        if d == cur_d + pd.Timedelta(days=1) and a > cur_a:
            one_group.append([d, a])
            cur_d, cur_a = d, a
        else:
            groups.append(one_group)
            cur_d, cur_a = d, a
            one_group = [[cur_d, cur_a]]
    if len(one_group):
        groups.append(one_group)

    groups = [i for i in groups if len(i) >= 3]

    return pd.DataFrame({
        "customer_id": customer_id,
        "consecutives": [[i[0][0], i[-1][0]] for i in groups]
    })


def consecutive_increasing_transactions(transactions: pd.DataFrame) -> pd.DataFrame:

    df = transactions.sort_values(["customer_id", "transaction_date"])
    df = df.groupby("customer_id", as_index=False)[["customer_id", "transaction_date", "amount"]].apply(f).reset_index(drop=True)
    df = df.dropna()
    df["consecutive_start"] = df["consecutives"].apply(func=lambda x: x[0])
    df["consecutive_end"] = df["consecutives"].apply(func=lambda x: x[1])
    df = df.sort_values("customer_id")[["customer_id", "consecutive_start", "consecutive_end"]]

    return df
