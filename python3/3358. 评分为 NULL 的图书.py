import pandas as pd


def find_unrated_books(books: pd.DataFrame) -> pd.DataFrame:

    df = books
    df = df[df["rating"].isnull()].sort_values("book_id")
    df = df[["book_id", "title", "author", "published_year"]]

    return df
