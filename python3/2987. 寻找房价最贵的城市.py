import pandas as pd


def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:

    thres = listings["price"].mean()
    listings = listings.groupby("city", as_index=False)["price"].mean()
    df = listings[listings["price"] > thres][["city"]].sort_values(by="city", ascending=True)
    
    return df
