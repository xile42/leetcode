import pandas as pd


def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    today = pd.to_datetime("2019-06-23")
    month_ago = today + pd.Timedelta(days=-30)
    year_ago = today + pd.Timedelta(days=-365)
    df1 = books[books.available_from < month_ago]
    df2 = orders[orders["dispatch_date"] >= year_ago].groupby(by="book_id", as_index=False)["quantity"].sum()
    df = pd.merge(df1, df2, on="book_id", how="left")
    df.fillna(0, inplace=True)
    df = df[df["quantity"] < 10][["book_id", "name"]]

    return df
