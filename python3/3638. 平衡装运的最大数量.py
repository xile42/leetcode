class Solution:

    def maxBalancedShipments(self, weight: List[int]) -> int:

        st = list()
        ans = 0

        for w in weight:
            if not st or st[-1] <= w:
                st.append(w)
            else:
                ans += 1
                st = list()

        return ans
