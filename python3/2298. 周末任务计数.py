import pandas as pd


def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:

    tasks["dow"] = tasks["submit_date"].dt.day_of_week
    weekend_cnt = len(tasks[tasks["dow"] >= 5])
    working_cnt = len(tasks[tasks["dow"] < 5])

    return pd.DataFrame({
        "weekend_cnt": [weekend_cnt],
        "working_cnt": [working_cnt]
    })
