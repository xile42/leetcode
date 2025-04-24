class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:

        ans = 0
        d = defaultdict(int)
        for v in nums:
            if d[k-v] > 0:
                ans += 1
                d[k-v] -= 1
            else:
                d[v] += 1

        return ans
