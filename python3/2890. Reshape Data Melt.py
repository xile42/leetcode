import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:

    df = pd.melt(report, id_vars="product", value_name="sales", var_name="quarter")

    return df
