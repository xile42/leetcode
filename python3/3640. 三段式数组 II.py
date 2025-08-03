max = lambda x, y: x if x > y else y
min = lambda x, y: x if x < y else y


class Solution:

    def maxSumTrionic(self, nums: List[int]) -> int:

        segs = list()
        ts = list()
        n = len(nums)

        def check(pre, suf, t):
            if t == 1:
                return pre < suf
            elif t == -1:
                return pre > suf
            return pre == suf

        s = 0
        while s + 1 < n:
            e = s + 1
            t = 1 if nums[e] > nums[s] else (-1 if nums[e] < nums[s] else 0)  # 1 单调增, -1 单调减, 0 不变
            while e < n and check(nums[e - 1], nums[e], t):
                e += 1
            e -= 1
            segs.append([s, e])
            ts.append(t)
            s = e

        start_max = defaultdict(lambda: -inf)
        end_max = defaultdict(lambda: -inf)
        decrease_seg_value = dict()
        acc_all = list(accumulate(nums))

        for i, ((s, e), t) in enumerate(zip(segs, ts)):
            if t == 1:
                acc_min = inf
                cur = 0
                for k in range(s, e + 1):
                    cur += nums[k]
                    if k >= s + 1:
                        start_max[i] = max(start_max[i], cur)
                    if k <= e - 2:
                        acc_min = min(acc_min, cur)
                end_max[i] = max(end_max[i], cur - min(acc_min, 0))
            elif t == -1:
                decrease_seg_value[i] = acc_all[e] - (0 if s == 0 else acc_all[s - 1])
            else:
                continue

        ans = -inf
        for i in range(len(ts) - 2):
            if ts[i] == 1 and ts[i + 1] == -1 and ts[i + 2] == 1:
                to_sub_s, to_sub_e = segs[i + 1]
                to_sub = nums[to_sub_s] + nums[to_sub_e]
                ans = max(ans, end_max[i] + decrease_seg_value[i + 1] + start_max[i + 2] - to_sub)

        return ans  # 题目保证有解
