import pandas as pd


def f(x):

    x = x.values
    ans = 0
    e_id = x[0][0]
    
    for _, s, e in x:

        cnt1 = 0
        cnt2 = 0
        for _, ss, ee in x:
            if ss <= s < ee:
                cnt1 += 1
            if ss < e <= ee:
                cnt2 += 1

        ans = max(ans, cnt1, cnt2)

    groups = list()
    cur = x[0][1:]
    for _, s, e in x[1:]:
        if s <= cur[1]:
            cur[1] = max(cur[1], e)
        else:
            groups.append(cur)
            cur = [s, e]
    groups.append(cur)

    total_time = sum([(i[1] - i[0]).seconds for i in groups])
    hours = int(total_time / 3600)

    return pd.DataFrame({"employee_id": [e_id], "total_task_hours": hours, "max_concurrent_tasks": ans})


def find_total_duration(tasks: pd.DataFrame) -> pd.DataFrame:

    df = tasks
    df = df.sort_values(["employee_id", "start_time"])
    df = df.groupby("employee_id", as_index=False)[["employee_id", "start_time", "end_time"]].apply(f).reset_index(drop=True)

    df = df.sort_values("employee_id")

    return df
