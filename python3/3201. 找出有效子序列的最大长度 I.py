class Solution:

    def maximumLength(self, nums: List[int]) -> int:

        odd = even = 0
        for n in nums:
            if n & 1:
                odd += 1
            else:
                even += 1

        ans1 = 0
        cur = 0
        for n in nums:
            if n & 1 == cur:
                ans1 += 1
                cur = 1 - cur

        ans2 = 0
        cur = 1
        for n in nums:
            if n & 1 == cur:
                ans2 += 1
                cur = 1 - cur

        return max(odd, even, ans1, ans2)
