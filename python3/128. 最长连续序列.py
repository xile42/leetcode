class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        s = set(nums)
        ans = 1
        for n in s:
            if n - 1 in s:
                continue
            e = n
            while e + 1 in s:
                e += 1

            ans = max(ans, e - n + 1)

        return ans
