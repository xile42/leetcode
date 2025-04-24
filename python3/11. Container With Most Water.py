class Solution:

    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
        


##class Solution:
##
##    def maxArea(self, height: List[int]) -> int:
##
##        # # Brute Force
##        # from collections import defaultdict
##        # idx_map = defaultdict(list)
##        # for idx, value in enumerate(height):
##        #     idx_map[value].append(idx)
##        # height_sorted = sorted(idx_map.keys(), reverse=True)
##        #
##        # result = 0
##        # for small_one in height_sorted[::-1]:
##        #     for large_one in height_sorted:
##        #         if large_one < small_one:
##        #             break
##        #         for small_idx in idx_map[small_one]:
##        #             for large_idx in idx_map[large_one]:
##        #                 result = max(result, small_one * abs(large_idx - small_idx))
##        #
##        # return result
##
##        left = 0
##        right = len(height) - 1
##        max_result = 0
##        while left < right:
##            result = min(height[left], height[right]) * (right - left)
##            max_result = max(max_result, result)
##            if height[left] <= height[right]:
##                left += 1
##            else:
##                right -= 1
##
##        return max_result
##
