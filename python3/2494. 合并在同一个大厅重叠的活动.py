import pandas as pd


def f(df):

    data = df.values
    cur = data[0]
    result = list()
    for other in data[1:]:
        if cur[-1] >= other[1]:
            cur = [cur[0], cur[1], max(cur[-1], other[-1])]
        else:
            result.append(cur)
            cur = other
    result.append(cur)

    return pd.DataFrame({"hall_id": [i[0] for i in result], "start_day": [i[1] for i in result], "end_day": [i[2] for i in result]})
        

def merge_events(hall_events: pd.DataFrame) -> pd.DataFrame:

    df = hall_events.sort_values(["hall_id", "start_day"])
    df = df.groupby("hall_id", as_index=False)[["hall_id", "start_day", "end_day"]].apply(f).reset_index(drop=True)

    return df
