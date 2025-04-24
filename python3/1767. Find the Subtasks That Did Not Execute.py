import pandas as pd


def find_subtasks(tasks: pd.DataFrame, executed: pd.DataFrame) -> pd.DataFrame:

    df = pd.DataFrame({"subtask_id": range(1, 21)})
    df = pd.merge(tasks, df, how="cross")
    df = df[df["subtasks_count"] >= df["subtask_id"]]

    executed["flag"] = 1
    df = pd.merge(df, executed, on=["task_id", "subtask_id"], how="left")
    df.fillna(0, inplace=True)
    df = df[df["flag"] == 0][["task_id", "subtask_id"]]

    return df
