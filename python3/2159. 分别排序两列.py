import pandas as pd


def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:

##    wrong! this will include index
##    data["first_col"] = data["first_col"].sort_values(ascending=True)
##    data["second_col"] = data["second_col"].sort_values(ascending=False)

    return pd.DataFrame({
        "first_col": data["first_col"].sort_values(ascending=True).tolist(),
        "second_col": data["second_col"].sort_values(ascending=False).tolist()
    })
