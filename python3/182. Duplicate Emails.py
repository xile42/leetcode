import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:

    from collections import Counter

    emails = person["email"].tolist()
    counter = Counter(emails)
    results = list()
    for k, v in counter.items():
        if v >= 2:
            results.append(k)

    return pd.DataFrame({"Email": results})
