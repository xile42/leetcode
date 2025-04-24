import pandas as pd


def count_experiments(experiments: pd.DataFrame) -> pd.DataFrame:

    df1 = pd.merge(
        pd.DataFrame({"platform": ["Android", "IOS", "Web"]}),
        pd.DataFrame({"experiment_name": ["Reading", "Sports", "Programming"]}),
        how="cross"
    )
    df2 = experiments.groupby(by=["platform", "experiment_name"], as_index=False).agg(
        num_experiments=("experiment_id", "count")
    )
    df = pd.merge(df1, df2, how="left", on=["platform", "experiment_name"])
    df = df.fillna(0)

    return df
