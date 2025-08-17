class Solution:

    def scoreOfParentheses(self, s: str) -> int:

        st = list()
        st.append(0)
        for c in s:
            if c == "(":
                st.append(0)
            else:
                cur = st.pop()
                st.append(st.pop() + max(2 * cur, 1))

        return st[-1]
