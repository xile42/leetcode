class Solution:

    def countHillValley(self, nums: List[int]) -> int:

        ns = list()
        for n, ite in groupby(nums):
            ns.append(n)

        ans = 0
        for idx in range(1, len(ns) - 1):
            if ns[idx - 1] > ns[idx] and ns[idx + 1] > ns[idx]:
                ans += 1
            elif ns[idx - 1] < ns[idx] and ns[idx + 1] < ns[idx]:
                ans += 1

        return ans
