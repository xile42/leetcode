import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:

    all_months = ["{}_Revenue".format(month) for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]
    df = department.pivot(index="id", values="revenue", columns="month")
    df.reset_index(inplace=True)
    df.columns = [column if column == "id" else "{}_Revenue".format(column) for column in df.columns]
    for month in all_months:
        if month not in df.columns:
            df[month] = None

    return df
