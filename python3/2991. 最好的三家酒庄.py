import pandas as pd


def top_three_wineries(wineries: pd.DataFrame) -> pd.DataFrame:

    countries = wineries[["country"]].drop_duplicates()
    base = pd.merge(countries, pd.DataFrame({"cat": ["top_winery", "second_winery", "third_winery"]}), how="cross")
    wineries = wineries.groupby(["country", "winery"], as_index=False)["points"].sum()
    df = wineries.sort_values(["country", "points", "winery"], ascending=[True, False, True])
    df["r"] = df.groupby("country", as_index=False)["points"].rank("first", ascending=False)
    df = df[df["r"] <= 3]
    df["cat"] = df["r"].apply(lambda x: "top_winery" if x == 1 else ("second_winery" if x == 2 else "third_winery"))
    df["winery"] = df.apply(axis=1, func=lambda x: "{} ({})".format(x["winery"], str(x["points"])))
    df = pd.merge(base, df, how="left", on=["country", "cat"])
    df["winery"] = df.apply(axis=1, func=lambda x: x["winery"] if not pd.isna(x["winery"]) else ("No second winery" if x["cat"] == "second_winery" else "No third winery"))
    df = pd.pivot(df, index="country", values="winery", columns="cat").reset_index()
    df = df.sort_values("country")

    return df[["country", "top_winery", "second_winery", "third_winery"]]
