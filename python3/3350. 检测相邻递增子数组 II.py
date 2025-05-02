from typing import List


class Solution:

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        left = ans = 0
        chance = True
        mid = None

        # print(nums)
        for right in range(1, len(nums)):
            if nums[right] <= nums[right - 1]:  # need to use chance
                if chance:
                    # print("in 1: ", left, right, chance, mid)
                    chance = False
                    mid = right
                else:  # 更新left到mid

                    # print("in 2: ", left, right, chance, mid)
                    k1 = mid - left
                    k2 = right - mid
                    k = min(k1, k2)
                    ans = max(ans, k)
                    ans = max(ans, k1 // 2)
                    ans = max(ans, k2 // 2)

                    left = mid
                    mid = right
            else:
                if chance:
                    ans = max(ans, (right - left + 1) // 2)
                # print("in 3: ", left, right, chance, mid)
                continue
        #
        # print("after sliding:", left, right, chance, mid)
        # print("after sliding:", ans)

        if mid is None:
            ans = len(nums) // 2
        else:
            k1 = mid - left
            k2 = len(nums) - mid
            k = min(k1, k2)
            # print(k1, k2, k, ans)
            ans = max(ans, k)
            ans = max(ans, k1 // 2)
            ans = max(ans, k2 // 2)

        return ans


foo = Solution()
print(foo.maxIncreasingSubarrays([8,-4,-1,16,20]))
