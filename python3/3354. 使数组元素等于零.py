class Solution:

    # def f(self, idx, direction, ns):
    #     # print(ns, idx, direction)
    #     if idx < 0 or idx >= len(ns):
    #         if all(i == 0 for i in ns):
    #             self.ans += 1
    #         return
    #
    #     cur = ns[idx]
    #     if cur == 0:
    #         self.f(idx+direction, direction, ns)
    #     else:
    #         ns[idx] -= 1
    #         direction *= (-1)
    #         self.f(idx+direction, direction, ns)
    #
    # def countValidSelections(self, nums: List[int]) -> int:
    #
    #     self.nums = nums
    #     self.ans = 0
    #
    #     for i, v in enumerate(nums):
    #         if v == 0:
    #             self.f(i, 1, nums.copy())
    #             self.f(i, -1, nums.copy())
    #
    #     return self.ans

    def countValidSelections(self, nums: List[int]) -> int:

        ans = 0
        for i, v in enumerate(nums):
            if v == 0:
                l, r = sum(nums[:i]), sum(nums[i+1:])
                if l == r:
                    ans += 2
                elif abs(l - r) == 1:
                    ans += 1

        return ans
