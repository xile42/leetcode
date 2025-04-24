import pandas as pd


def number_of_passengers(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:

    l1 = buses.values
    l2 = passengers["arrival_time"].tolist()

    res = list()
    done = 0
    for bus_id, t, c in l1:
        cnt = sum(i <= t for i in l2)
        away = min(c, cnt - done)
        done += away
        res.append([bus_id, away])

    df = pd.DataFrame({"bus_id": [i[0] for i in res], "passengers_cnt": [i[1] for i in res]})
    df = df.sort_values("bus_id")

    return df
