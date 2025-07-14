class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:

        st = list()
        for c in s:
            if not st:
                st.append([c, 1])
                continue
            if c == st[-1][0]:
                if st[-1][1] == k - 1:
                    st.pop(-1)
                    continue
                else:
                    st[-1][1] += 1
            else:
                st.append([c, 1])

        ans = list()
        for c, n in st:
            ans += [c] * n

        return "".join(ans)
