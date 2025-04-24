import pandas as pd


def find_bursty_behavior(posts: pd.DataFrame) -> pd.DataFrame:

    posts = posts[(posts["post_date"].dt.month == 2) & (posts["post_date"].dt.day <= 28)]
    df = pd.merge(posts, posts, how="cross")
    df = df[(df["user_id_x"] == df["user_id_y"]) & (df["post_date_y"].between(df["post_date_x"], df["post_date_x"] + pd.Timedelta(days=6)))]
    df = df.groupby(["user_id_x", "post_id_x"], as_index=False).agg(
        count_7=("post_id_y", "count")
    )
    df = df.groupby("user_id_x", as_index=False)["count_7"].max()
    df = df.rename(columns={"user_id_x": "user_id", "count_7": "max_7day_posts"})

    other = posts.groupby("user_id", as_index=False).agg(
        avg_weekly_posts=("post_id", "count")
    )
    other["avg_weekly_posts"] = other["avg_weekly_posts"] / 4

    df = pd.merge(df, other, on="user_id", how="right").fillna(1)
    df = df[df["max_7day_posts"] >= 2 * df["avg_weekly_posts"]][["user_id", "max_7day_posts", "avg_weekly_posts"]]
    df = df.sort_values("user_id")

    return df
