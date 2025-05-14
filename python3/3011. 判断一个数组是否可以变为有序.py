class Solution:

    def canSortArray(self, nums: List[int]) -> bool:

        bits = [v.bit_count() for v in nums]
        ns = list()
        cur = 0
        for c, ite in groupby(bits):
            l = len(list(ite))
            ns.append(sorted(nums[cur:cur + l]))
            cur += l

        for i in range(1, len(ns)):
            if ns[i][0] < ns[i - 1][-1]:
                return False

        return True
