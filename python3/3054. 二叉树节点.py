import pandas as pd


def binary_tree_nodes(tree: pd.DataFrame) -> pd.DataFrame:

    df = tree.dropna().groupby("P", as_index=False).agg(
        children=("N", "count")
    ).rename(columns={"P": "N"})
    df = pd.merge(tree, df, on="N", how="left")
    df["children"] = df["children"].fillna(0)
    df["Type"] = df.apply(axis=1, func=lambda x: "Root" if pd.isna(x["P"]) else ("Leaf" if x["children"] ==0 else "Inner"))
    df = df.sort_values("N")

    return df[["N", "Type"]]
