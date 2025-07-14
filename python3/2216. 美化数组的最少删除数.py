class Solution:

    def minDeletion(self, nums: List[int]) -> int:

        st = list()
        ans = 0
        for n in nums:
            if not st:
                st.append(n)
                continue
            if len(st) & 1:
                if n == st[-1]:
                    ans += 1
                    continue
            st.append(n)

        return ans + (len(st) & 1)
