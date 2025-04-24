import pandas as pd


def find_subordinates(employees: pd.DataFrame) -> pd.DataFrame:

    ceo_id = employees[employees["manager_id"].isna()].iloc[0]["employee_id"]
    ceo_salary = employees[employees["manager_id"].isna()].iloc[0]["salary"]

    df = employees
    df = df[df["manager_id"].notna()]
    df["hierarchy_level"] = 0
    cur_level = 1
    cur_target = [ceo_id]
    while True:
        df["hierarchy_level"] = df.apply(axis=1, func=lambda x: x["hierarchy_level"] if x["manager_id"] not in cur_target else cur_level)
        cur_target = df[df["manager_id"].isin(cur_target)]["employee_id"].tolist()
        cur_level += 1
        if not cur_target:
            break

    df["salary_difference"] = df["salary"] - ceo_salary
    df = df.rename(columns={"employee_id": "subordinate_id", "employee_name": "subordinate_name"})
    df = df.sort_values(["hierarchy_level", "subordinate_id"], ascending=True)
    df = df[df["hierarchy_level"] != 0]

    return df[["subordinate_id", "subordinate_name", "hierarchy_level", "salary_difference"]]
