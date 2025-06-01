class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:

        st = list()
        for i, n in enumerate(nums):
            if not st or st[-1][-1] > n:
                st.append([i, n])

        ans = 0
        j = len(nums) - 1
        while st:
            while st[-1][-1] > nums[j]:
                j -= 1
            ans = max(ans, j - st[-1][0])
            st.pop(-1)

        return ans
