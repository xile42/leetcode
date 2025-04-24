import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:

    school_a.rename(columns={"student_id": "member_A_id", "student_name": "member_A"}, inplace=True)
    school_b.rename(columns={"student_id": "member_B_id", "student_name": "member_B"}, inplace=True)
    school_c.rename(columns={"student_id": "member_C_id", "student_name": "member_C"}, inplace=True)

    df = pd.merge(school_a, school_b, how="cross")
    df = pd.merge(df, school_c, how="cross")

    df = df[
        (df["member_A_id"] != df["member_B_id"]) &
        (df["member_B_id"] != df["member_C_id"]) &
        (df["member_C_id"] != df["member_A_id"]) &
        (df["member_A"] != df["member_B"]) &
        (df["member_B"] != df["member_C"]) &
        (df["member_C"] != df["member_A"])
    ][["member_A", "member_B", "member_C"]]

    return df
    
