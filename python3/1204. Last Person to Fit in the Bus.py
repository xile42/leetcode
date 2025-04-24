import pandas as pd


def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:

    queue["prefix_sum"] = 0
    queue.sort_values(by="turn", ascending=True, inplace=True)
    queue.reset_index(inplace=True)
    for idx in range(len(queue)):
        queue.loc[idx, "prefix_sum"] = queue.iloc[idx]["weight"] if idx == 0 else queue.iloc[idx]["weight"] + queue.iloc[idx-1]["prefix_sum"]
    queue = queue[queue["prefix_sum"] <= 1000].sort_values(by="prefix_sum", ascending=False)

    return pd.DataFrame({
        "person_name": [queue.iloc[0]["person_name"]]
    })
