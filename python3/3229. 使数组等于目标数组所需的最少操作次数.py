class Solution:

    def minimumOperations(self, nums: List[int], target: List[int]) -> int:

        n = len(nums)
        ns = [i - j for i, j in zip(target, nums)]
        diff = [0] * n
        diff[0] = ns[0]
        for i in range(1, n):
            diff[i] = ns[i] - ns[i - 1]

        ans = max(sum(i for i in diff if i > 0), -sum(i for i in diff if i < 0))

        return ans
