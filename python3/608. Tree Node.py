import numpy as np
import pandas as pd


def tree_node(tree: pd.DataFrame) -> pd.DataFrame:

    tree["type"] = np.where(tree["id"].isin(tree["p_id"]), "Inner", "Leaf")
    tree["type"] = np.where(tree["p_id"].isna(), "Root", tree["type"])

    return tree[["id", "type"]]
