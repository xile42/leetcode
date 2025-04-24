import pandas as pd


def maximize_items(inventory: pd.DataFrame) -> pd.DataFrame:

    df = inventory
    v1 = df[df["item_type"] == "prime_eligible"]["square_footage"].sum()
    c1 = df[df["item_type"] == "prime_eligible"]["square_footage"].count()
    v2 = df[df["item_type"] != "prime_eligible"]["square_footage"].sum()
    c2 = df[df["item_type"] != "prime_eligible"]["square_footage"].count()
    n1, r = divmod(500000, v1)
    n2, r = divmod(r, v2)

    result = pd.DataFrame({
        "item_type": ["prime_eligible", "not_prime"],
        "item_count": [n1 * c1, n2 * c2],
    })
    result = result.sort_values("item_count", ascending=False)

    return result
