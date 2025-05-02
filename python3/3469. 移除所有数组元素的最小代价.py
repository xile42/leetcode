class Solution:

    def minCost(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def f(idx, pre):

            if idx >= n:
                return pre if pre else 0

            if n - idx + int(pre is not None) < 3:
                ns = [-inf if pre is None else pre] + nums[idx:]
                return max(ns)

            if pre is None:
                next_idx = idx + 3
                ns = nums[idx:idx + 3]
            else:
                next_idx = idx + 2
                ns = [pre] + nums[idx:idx + 2]

            # 两种情况，大中||小，中小||大
            ns.sort()
            v1 = ns[2] + f(next_idx, ns[0])  # 大中||小
            v2 = ns[1] + f(next_idx, ns[2])  # 中小||大
            ans = min(v1, v2)

            # print("f({}, {}), v1: {}, v2: {}, ns: {}, next_idx: {}".format(idx, pre, v1, v2, ns, next_idx))
            return ans

        ans = f(0, None)

        return ans
