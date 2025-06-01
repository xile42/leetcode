class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        l = len(nums)
        ans = [-1] * l
        st = list()

        for i, n in enumerate(nums + nums):

            while st and n > st[-1][-1]:
                ii, nn = st.pop(-1)
                if ii < l:
                    ans[ii] = n
            st.append([i, n])

        return ans
