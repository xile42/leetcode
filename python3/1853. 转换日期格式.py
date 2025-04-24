import pandas as pd


def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:

    days["day"] = days["day"].apply(func=lambda x: "{}, {} {}, {}".format(x.day_name(), x.month_name(), x.day, x.year))

    return days
