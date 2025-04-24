import pandas as pd


def count_trusted_contacts(customers: pd.DataFrame, contacts: pd.DataFrame, invoices: pd.DataFrame) -> pd.DataFrame:

    valid_emails = customers.email
    contacts["valid"] = contacts.contact_email.isin(valid_emails)
    df1 = contacts.groupby("user_id", as_index=False).agg(
        contacts_cnt=("contact_name", "count"),
        trusted_contacts_cnt=("valid", "sum")
    )
    df2 = pd.merge(invoices, customers, left_on="user_id", right_on="customer_id", how="left")
    df = pd.merge(df2[["invoice_id", "price", "customer_name", "user_id"]], df1[["user_id", "contacts_cnt", "trusted_contacts_cnt"]], on="user_id", how="left")
    df = df.sort_values("invoice_id", ascending=True)
    df = df[["invoice_id", "customer_name", "price", "contacts_cnt", "trusted_contacts_cnt"]].fillna(0)

    return df
