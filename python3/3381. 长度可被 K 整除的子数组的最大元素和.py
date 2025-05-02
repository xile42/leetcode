class Solution:

    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        def f(ns):

            ans = ns[0]
            cur = 0
            for v in ns:
                cur += v
                ans = max(ans, cur)
                if cur < 0:
                    cur = 0

            return ans

        n = len(nums)
        ns = [sum(nums[i*k:(i+1)*k]) for i in range(n // k)]
        ans = max(-inf, f(ns))
        # print("ns", ns)
        # print(ans)
        for shift_idx in range(1, k):
            # print("shift idx", shift_idx)
            for idx in range(len(ns)):
                # print(idx, idx * k + (shift_idx - 1), (idx + 1) * k + shift_idx)
                start = idx * k + (shift_idx - 1)
                end = (idx + 1) * k + (shift_idx - 1)
                start_v = -inf if start >= n else -nums[start]
                end_v = -inf if end >= n else nums[end]
                ns[idx] += start_v
                ns[idx] += end_v
            ans = max(ans, f(ns))
            # print("new ns", ns)
            # print(ans)

        return ans