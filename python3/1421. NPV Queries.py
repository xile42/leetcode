import pandas as pd


def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(queries, npv, how="left", on=["id", "year"])
    df.fillna(0, inplace=True)

    return df
