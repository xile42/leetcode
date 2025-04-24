import pandas as pd


def func(x):

    return 100 * sum([1 if i < 3 else 0 for i in x]) / len(x)


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:

    queries["quality"] = queries["rating"] / queries["position"]
    df1 = queries.groupby(by="query_name", as_index=False)["quality"].mean()
    df2 = queries.groupby(by="query_name", as_index=False)["rating"].agg(func)
    df = pd.merge(df1, df2, on="query_name")
    df.rename(columns={"rating": "poor_query_percentage"}, inplace=True)
    df["quality"] = df["quality"].apply(lambda x: int((x * 100 + 0.5)) / 100)
    df["poor_query_percentage"] = df["poor_query_percentage"].apply(lambda x: int((x * 100 + 0.5)) / 100)

    return df
