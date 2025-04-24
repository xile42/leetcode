import pandas as pd


def check(s):

    for word in s.split(" "):
        if word.startswith("DIAB1"):
            return 1

    return 0


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    patients["flag"] = patients["conditions"].apply(check)
    df = patients[patients["flag"] == 1][["patient_id", "patient_name", "conditions"]]

    return df
