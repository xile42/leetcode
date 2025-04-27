# # 超时
# class Solution:
#
#     def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
#
#         n = len(nums)
#         acc_nums = list(accumulate(nums))
#         acc_cost = list(accumulate(cost))
#
#         @cache
#         def f(i, used):  # 当前该切i开始的数组了，已经用了used次
#
#             if i >= n:
#                 return 0
#
#             ans = inf
#             for j in range(i, n):  # [i, j]
#                 v1 = acc_nums[j] + k * (used + 1)
#                 v2 = acc_cost[j] - (0 if i == 0 else acc_cost[i - 1])
#                 score = v1 * v2 + f(j + 1, used + 1)
#                 ans = min(ans, score)
#
#             return ans
#
#         ans = f(0, 0)
#         f.cache_clear()
#
#         return ans


class Solution:

    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:

        n = len(nums)
        acc_nums = list(accumulate(nums))
        acc_cost = list(accumulate(cost))

        @cache
        def f(i):  # 我都是正着写dp，不像灵神倒着写，丫的这破题想到优化思想了，还要倒着写！差点载坑里QAQ

            if i < 0:
                return 0

            ans = inf
            for j in range(i + 1):  # [j, i]
                v1 = acc_nums[i]
                v2 = acc_cost[i] - (0 if j == 0 else acc_cost[j - 1])
                v3 = k * (acc_cost[-1] - (0 if j == 0 else acc_cost[j - 1]))
                score = v1 * v2 + v3 + f(j - 1)
                if score < ans:
                    ans = score

            return ans

        ans = f(n - 1)
        f.cache_clear()

        return ans
