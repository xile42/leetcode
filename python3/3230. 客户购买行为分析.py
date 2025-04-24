from decimal import Decimal, ROUND_HALF_UP
import pandas as pd


def analyze_customer_behavior(transactions: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(transactions, products, on="product_id", how="left")
    df["v"] = df["amount"]
    df = df.sort_values(["customer_id", "transaction_date"])
    
    df1 = df.groupby(["customer_id", "category"], as_index=False).agg(
        count=("transaction_id", "count"),
        last_date=("transaction_date", "max")
    )
    df1["max"] = df1.groupby("customer_id", as_index=False)["count"].transform("max")
    df1 = df1[df1["count"] == df1["max"]].sort_values(["customer_id", "last_date"], ascending=False).drop_duplicates(subset=["customer_id"], keep="first")
    df1 = df1.rename(columns={"category": "top_category"})

    df = df.groupby("customer_id", as_index=False).agg(
        total_amount=("v", "sum"),
        transaction_count=("transaction_id", "count"),
        unique_categories=("category", "nunique"),
    )
    
    df["avg_transaction_amount"] = (df["total_amount"] / df["transaction_count"]).apply(func=lambda x: Decimal(str(x)).quantize(Decimal("0.01"), ROUND_HALF_UP))
    df["loyalty_score"] = ((df["transaction_count"] * 10) + (df["total_amount"] / 100)).apply(func=lambda x: Decimal(str(x)).quantize(Decimal("0.01"), ROUND_HALF_UP))
    df["total_amount"] = df["total_amount"].round(2)

    df = pd.merge(df, df1, on="customer_id")
    df = df.sort_values(["loyalty_score", "customer_id"], ascending=[False, True])

    return df[["customer_id", "total_amount", "transaction_count", "unique_categories", "avg_transaction_amount", "top_category", "loyalty_score"]]
