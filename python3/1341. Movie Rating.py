import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:

    df1 = movie_rating.groupby(by="user_id", as_index=False)["rating"].count()
    df1 = pd.merge(df1, users, how="left", on="user_id")
    df1.sort_values(by=["rating", "name"], ascending=[False, True], inplace=True)

    movie_rating["flag"] = movie_rating["created_at"].apply(lambda x: 1 if str(x)[:7] == "2020-02" else 0)
    df2 = movie_rating[movie_rating["flag"] == 1]
    df2 = df2.groupby(by="movie_id", as_index=False)["rating"].mean()
    df2 = pd.merge(df2, movies, how="left", on="movie_id")
    df2.sort_values(by=["rating", "title"], ascending=[False, True], inplace=True)

    return pd.DataFrame({
        "results": [df1.iloc[0]["name"], df2.iloc[0]["title"]]
    })
