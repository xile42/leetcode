import pandas as pd


def median_frequency(numbers: pd.DataFrame) -> pd.DataFrame:

    ns = numbers["num"].tolist()
    fs = numbers["frequency"].tolist()
    nums = list()
    for i in range(len(ns)):
        nums += [ns[i] for _ in range(fs[i])]
    nums.sort()
    if len(nums) & 1:
        result = nums[(len(nums) - 1) // 2]
    else:
        result = round(mean(nums[len(nums) // 2 - 1:len(nums) // 2 + 1]), 1)

    return pd.DataFrame({
        "median": [result]
    })
    
    
