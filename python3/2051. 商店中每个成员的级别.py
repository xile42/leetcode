import pandas as pd


def find_categories(members: pd.DataFrame, visits: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(visits, purchases, on="visit_id", how="left")
    df = df.groupby(by="member_id", as_index=False).agg(
        amounts=("charged_amount", "count"),
        times=("visit_id", "count")
    )
    df["score"] = 100 * df["amounts"] / df["times"]
    df["category"] = df.apply(axis=1, func=lambda x: "Bronze" if x["times"] == 0 else ("Diamond" if x["score"] >= 80 else ("Gold" if 50 <= x["score"] < 80 else "Silver")))
    df = pd.merge(members, df, on="member_id", how="left")[["member_id", "name", "category"]]
    df = df.fillna("Bronze")
    df = df.sort_values(by="member_id")

    return df
