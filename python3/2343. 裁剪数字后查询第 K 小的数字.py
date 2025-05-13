class Solution:

    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:

        l = len(nums[0])
        results = dict()
        for i in range(1, l + 1):
            results[i] = sorted([[num[-i:], idx] for idx, num in enumerate(nums)])

        ans = list()
        for k, trim in queries:
            ans.append(results[trim][k - 1][1])

        return ans
