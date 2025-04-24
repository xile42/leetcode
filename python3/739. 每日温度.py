class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        st = list()
        for i, t in enumerate(temperatures):
            if not st:
                st.append([t, i])
            while st and t > st[-1][0]:
                tt, j = st.pop(-1)
                ans[j] = i - j
            st.append([t, i])

        return ans
