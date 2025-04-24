import pandas as pd


def total_sales(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:

    df = sales

    df["18"] = df.apply(axis=1, func=lambda x: (min(pd.to_datetime("2018-12-31"), x["period_end"]) - max(pd.to_datetime("2018-01-01"), x["period_start"])).days + 1)
    df["19"] = df.apply(axis=1, func=lambda x: (min(pd.to_datetime("2019-12-31"), x["period_end"]) - max(pd.to_datetime("2019-01-01"), x["period_start"])).days + 1)
    df["20"] = df.apply(axis=1, func=lambda x: (min(pd.to_datetime("2020-12-31"), x["period_end"]) - max(pd.to_datetime("2020-01-01"), x["period_start"])).days + 1)

    df18 = df[df["18"] > 0]
    df18["amount"] = df18["average_daily_sales"] * df["18"]
    df19 = df[df["19"] > 0]
    df19["amount"] = df19["average_daily_sales"] * df["19"]
    df20 = df[df["20"] > 0]
    df20["amount"] = df20["average_daily_sales"] * df["20"]

    df18 = df18.groupby("product_id", as_index=False).agg(
        total_amount=("amount", "sum")
    )
    df18["report_year"] = "2018"
    df18 = pd.merge(df18, product, on="product_id", how="left")
    df19 = df19.groupby("product_id", as_index=False).agg(
        total_amount=("amount", "sum")
    )
    df19["report_year"] = "2019"
    df19 = pd.merge(df19, product, on="product_id", how="left")
    df20 = df20.groupby("product_id", as_index=False).agg(
        total_amount=("amount", "sum")
    )
    df20["report_year"] = "2020"
    df20 = pd.merge(df20, product, on="product_id", how="left")

    df = pd.concat([df18, df19, df20])
    df = df.sort_values(["product_id", "report_year"])

    return df[["product_id", "product_name", "report_year", "total_amount"]]
