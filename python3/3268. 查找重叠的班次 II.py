import pandas as pd


def f(x):

    x = x.values
    e_id = x[0][0]

    ans1 = 0
    for _, s, e in x:
        cnt1 = cnt2 = 0
        for _, ss, ee in x:
            if ss <= s <= ee:
                cnt1 += 1
            if ss <= e <= ee:
                cnt2 += 1
        ans1 = max(ans1, cnt1, cnt2)

    ans2 = 0
    groups = list()
    cur_s, cur_e = x[0][1:]
    one_group = [[cur_s, cur_e]]
    for _, s, e in x[1:]:
        if s <= cur_e:
            one_group.append([s, e])
            cur_s, cur_e = s, max(cur_e, e)
        else:
            groups.append(one_group)
            cur_s, cur_e = s, e
            one_group = [[cur_s, cur_e]]
    groups.append(one_group)

    for one_group in groups:
        
        for i in range(len(one_group)):
            for j in range(i + 1, len(one_group)):
                if one_group[i][-1] > one_group[j][0]:
                    ans2 += (one_group[i][-1] - one_group[j][0]).seconds // 60

    return pd.DataFrame({"employee_id": [e_id], "max_overlapping_shifts": [ans1], "total_overlap_duration": [ans2]})


def calculate_shift_overlaps(employee_shifts: pd.DataFrame) -> pd.DataFrame:

    df = employee_shifts.sort_values(["employee_id", "start_time"])
    df = df.groupby("employee_id", as_index=False)[["employee_id", "start_time", "end_time"]].apply(f).reset_index(drop=True)
    df = df.sort_values("employee_id")

    return df
