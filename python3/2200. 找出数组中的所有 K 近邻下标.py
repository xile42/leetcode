class Solution:

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        ans = list()
        for i, n in enumerate(nums):
            if n == key:
                ans += list(range(max(0, i - k), min(len(nums) - 1, i + k) + 1))

        return sorted(list(set(ans)))
