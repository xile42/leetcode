class Solution:

    def minNumberOperations(self, target: List[int]) -> int:

        ans = cur = 0
        for n in target:
            if n > cur:
                ans += n - cur
                cur = n
            else:
                cur = n

        return ans
