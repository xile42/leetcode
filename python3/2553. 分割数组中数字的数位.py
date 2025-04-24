class Solution:

    def separateDigits(self, nums: List[int]) -> List[int]:

        ans = list()
        for n in nums:
            ans += list(map(int, str(n)))

        return ans
