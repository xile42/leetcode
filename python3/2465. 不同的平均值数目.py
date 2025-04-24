class Solution:

    def distinctAverages(self, nums: List[int]) -> int:

        sn = sorted(nums)
        ans = set()
        idx = 0
        while idx < len(nums) // 2:
            ans.add((sn[idx] + sn[-(idx + 1)]) / 2)
            idx += 1

        return len(ans)
