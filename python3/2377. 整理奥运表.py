import pandas as pd


def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:

    olympic.sort_values(by=["gold_medals", "silver_medals", "bronze_medals", "country"], ascending=[False, False, False, True], inplace=True)

    return olympic
