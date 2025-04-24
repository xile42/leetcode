import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:

    df = logs[(logs["num"] == logs["num"].shift(1)) & (logs["num"] == logs["num"].shift(2))][["num"]].drop_duplicates()
    df.rename(columns={"num": "ConsecutiveNums"}, inplace=True)

    return df
