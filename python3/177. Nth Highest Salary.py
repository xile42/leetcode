import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    employee.drop_duplicates(subset="salary", keep="first", inplace=True)
    if N > len(employee) or N <= 0:
        return pd.DataFrame({"getNthHighestSalary({})".format(N): [None]})

    employee.sort_values(by="salary", ascending=False, inplace=True)
    return pd.DataFrame({"getNthHighestSalary({})".format(N): [employee.iloc[N-1]["salary"]]})
