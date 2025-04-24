# class Solution:
#
#     # def findMaximumScore(self, nums: List[int]) -> int:
#     def findMaximumScore(self, nums) -> int:
#
#         l = len(nums)
#         dp = [0 for _ in range(l)]
#
#         for idx in range(l):
#             dp[idx] = idx * nums[0]
#
#         for idx in range(2, l):
#             for jdx in range(1, idx):  # from j to i, (i-j)*nums[j]
#                 dp[idx] = max(dp[jdx] + (idx-jdx) * nums[jdx], dp[idx])
#         print(dp)
#         return dp[-1]


class Solution:
    def findMaximumScore(self, nums) -> int:

        if len(nums) == 1:
            return 0

        result = 0
        pre_max = nums[0]
        result += pre_max
        for idx in range(1, len(nums)-1):
            value = nums[idx]
            if pre_max >= value:
                result += pre_max
            else:
                result += value
                pre_max = value

        return result


if __name__ == '__main__':

    foo = Solution()
    print(foo.findMaximumScore([4,3,1,3,2]))
