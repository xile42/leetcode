class Solution:

    def findBuildings(self, heights: List[int]) -> List[int]:

        st = list()
        ans = list()
        for i, n in enumerate(heights[::-1]):
            if not st or st[-1] < n:
                st.append(n)
                ans.append(len(heights) - 1 - i)

        return ans[::-1]
