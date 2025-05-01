class Solution:

    def findLonely(self, nums: List[int]) -> List[int]:

        c = Counter(nums)
        s = set(nums)
        ans = list()
        for n in s:
            if c[n] == 1 and n - 1 not in s and n + 1 not in s:
                ans.append(n)

        return ans
