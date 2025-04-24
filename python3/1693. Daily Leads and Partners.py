import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:

    df = daily_sales.groupby(by=["date_id", "make_name"]).nunique()
    df.rename(columns={"lead_id": "unique_leads", "partner_id": "unique_partners"}, inplace=True)
    df.reset_index(inplace=True)

    return df
