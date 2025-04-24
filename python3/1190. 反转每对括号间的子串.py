class Solution:

    def reverseParentheses(self, s: str) -> str:

        st = list()
        for c in s:
            if c == ")":
                part = list()
                while st[-1] != "(":
                    part.append(st.pop(-1))
                st.pop(-1)
                st += part
            else:
                st.append(c)

        return "".join(st)
