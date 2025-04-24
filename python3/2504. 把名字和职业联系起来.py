import pandas as pd


def concatenate_info(person: pd.DataFrame) -> pd.DataFrame:

    person["name"] = person.apply(axis=1, func=lambda x: x["name"] + "(" + x["profession"][0] + ")")
    person = person.sort_values(by="person_id", ascending=False)[["person_id", "name"]]

    return person
