class Solution:

    def maxValue(self, nums: List[int], k: int) -> int:

        def findORs(nums: List[int], k: int) -> List[set[int]]:
            dp = list()
            prev = [set() for _ in range(k + 1)]
            prev[0].add(0)
            for i, num in enumerate(nums):
                for j in range(min(k - 1, i + 1), -1, -1):
                    for x in prev[j]:
                        prev[j + 1].add(x | num)
                dp.append(prev[k].copy())
            return dp

        A = findORs(nums, k)
        B = findORs(nums[::-1], k)

        ans = 0
        for i in range(k - 1, len(nums) - k):
            ans = max(ans, *(a ^ b for a in A[i] for b in B[-i - 2]))

        return ans
