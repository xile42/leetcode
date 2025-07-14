class Solution:

    def isValid(self, s: str) -> bool:

        st = list()
        for c in s:
            if len(st) < 2:
                st.append(c)
                continue
            if c == "c" and st[-1] == "b" and st[-2] == "a":
                st.pop()
                st.pop()
                continue
            else:
                st.append(c)

        return not st
