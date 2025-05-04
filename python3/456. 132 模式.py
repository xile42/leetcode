from sortedcontainers import SortedList


class Solution:

    def find132pattern(self, nums: List[int]) -> bool:

        mn = nums[0]
        right = SortedList(nums[1:])
        for j in range(1, len(nums) - 1):
            j_value = nums[j]
            right.remove(j_value)
            idx = bisect_right(right, mn)
            if idx == len(right) or right[idx] >= j_value:
                mn = min(mn, j_value)
                continue
            else:
                return True


        return False
