# # 打表
# # 1 ~ n 答案
#
# def f(n):
#
#     if n == 0:
#         return 0
#
#     pre = 0
#     ans = 0
#     for i in range(1, n + 1):
#         cnt = 0
#         cur = i
#         while cur:
#             cur //= 4
#             cnt += 1
#         ans += min(pre, cnt)
#         pre = abs(pre - cnt)
#
#     if pre:
#         ans += pre
#
#     return ans
#
#
# def ff(n):
#
#     cnt = 0
#     while n:
#         n //= 4
#         cnt += 1
#
#     return cnt
from itertools import count

# for i in range(101):
#     print(i, f(i))
#
# for i in range(101):
#     print(i, ff(i))


MX = pow(10, 9) + 7
splits = [1]
need = {1: 1}
while splits[-1] < MX:
    next_split = splits[-1] * 4
    need[next_split] = need[splits[-1]] + 1 if splits[-1] > 1 else need[splits[-1]]
    splits.append(next_split)
print(splits)
print(need)


class Solution:

    def minOperations(self, queries: List[List[int]]) -> int:

        ans = 0

        for l, r in queries:

            split_idx = bisect_left(splits, l)
            cur = l
            counter = Counter()

            print("for l {}, r {}, initial split_idx: {}, split_value: {}".format(l, r, split_idx, splits[split_idx]))
            while True:
                split_value = splits[split_idx]
                cur_right = min(split_value, r)
                cnt = cur_right - cur + (cur_right < split_value)  # 这个区间多少数
                print("[LOOP] cur_right: {}, cnt: {}".format(cur_right, cnt))
                counter[need[split_value]] = cnt
                # this_ans += need[split_value] * (cnt // 2)  # 两两消掉
                # remain = need[split_value] if cnt & 1 else 0  # 剩余
                # this_ans += min(pre, remain)
                # pre = abs(pre - remain)
                # print("[LOOP] remain: {}, pre: {}, updated ans: {}, cur ans: {}".format(remain, pre, need[split_value] * (cnt // 2), this_ans))

                if cur_right < split_value:
                    break
                cur = split_value  # 下个区间开始
                split_idx += 1

            this_ans = 0
            pre = 0
            kvs = sorted([[k, v] for k, v in counter.items()], key=lambda x: x[0], reverse=True)
            for i in range(len(kvs)):
                k, v = kvs[i]
                used = min(v, pre // k)
                pre -= k * used
                v -= used
                this_ans += k * used
                if v:
                    this_ans += k * v // 2
                    remain = 1 if k * v & 1 else 0
                    this_ans += min(pre, remain)
                    pre = abs(pre - remain)
            this_ans += pre

            ans += this_ans
            print(kvs)
            print("[LOOP END] this_ans: {}, ans: {}".format(this_ans, ans))

        return ans
