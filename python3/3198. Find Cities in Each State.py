import pandas as pd


def f(args):
    return ", ".join(args.tolist())


def find_cities(cities: pd.DataFrame) -> pd.DataFrame:

    cities = cities.sort_values(by=["state", "city"], ascending=[True, True])
    df = cities.groupby(by="state", as_index=False)["city"].agg(f)
    df = df.rename(columns={"city": "cities"})

    return df