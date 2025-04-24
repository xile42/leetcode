import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:

    my_numbers["flag"] = 1
    df = my_numbers.groupby(by="num", as_index=False)["flag"].sum()
    df = df[df["flag"] == 1].sort_values(by="num", ascending=False).reset_index()[["num"]]
    if len(df) == 0:
        return pd.DataFrame({"num": [None]})
    else:
        return df.loc[0:0, :]  # 或者 df.iloc[0:1, :]
