import pandas as pd


def calculate_trapped_rain_water(heights: pd.DataFrame) -> pd.DataFrame:

    if len(heights) == 0:
        return pd.DataFrame({"total_trapped_water": 0})

    hs = heights["height"].tolist()
    
    pre = [0] * len(hs)
    suf = [0] * len(hs)
    pre[0] = hs[0]
    for i in range(1, len(hs)):
        pre[i] = max(pre[i - 1], hs[i])
    suf[-1] = hs[-1]
    for i in range(len(hs) - 2, -1, -1):
        suf[i] = max(suf[i + 1], hs[i])

    ans = 0
    for i in range(len(hs)):
        ans += min(pre[i], suf[i]) - hs[i]

    return pd.DataFrame({"total_trapped_water": [ans]})
