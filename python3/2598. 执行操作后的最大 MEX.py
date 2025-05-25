class Solution:

    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        c = Counter([i % value for i in nums])
        mn = min(c[v] for v in range(value))
        ans = 0
        for i in range(value):
            if c[i] == mn:
                break
        ans = mn * value + i

        return ans
