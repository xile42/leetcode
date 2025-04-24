import pandas as pd


def change_null_values(coffee_shop: pd.DataFrame) -> pd.DataFrame:

    for idx in range(len(coffee_shop)):
        if pd.isna(coffee_shop.iloc[idx]["drink"]):
            coffee_shop.loc[idx, "drink"] = coffee_shop.iloc[idx-1]["drink"]

    return coffee_shop
