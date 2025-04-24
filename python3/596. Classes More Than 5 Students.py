import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    from collections import Counter

    classes = courses["class"].tolist()
    counter = Counter(classes)
    sorted_kv = sorted(list(counter.items()), key=lambda x: x[-1], reverse=True)
    results = list()
    for k, v in sorted_kv:
        if v >= 5:
            results.append(k)

    if len(results) == 0:
        return pd.DataFrame({"class": []})
    else:
        return pd.DataFrame({"class": results})
