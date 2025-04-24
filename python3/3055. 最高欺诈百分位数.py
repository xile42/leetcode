import math
import pandas as pd


def top_percentile_fraud(fraud: pd.DataFrame) -> pd.DataFrame:

    df = fraud.groupby("state", as_index=False).agg(
        count=("policy_id", "count")
    )
    df["thres"] = (df["count"] * 0.05).apply(math.ceil)
    df = pd.merge(fraud, df, on="state", how="left")
    df["rank"] = df.groupby("state", as_index=False)["fraud_score"].rank("min", ascending=False)
    df = df[df["rank"] <= df["thres"]][["policy_id", "state", "fraud_score"]].sort_values(["state", "fraud_score", "policy_id"], ascending=[True, False, True])

    return df
    
