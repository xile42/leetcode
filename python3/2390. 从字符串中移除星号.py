class Solution:

    def removeStars(self, s: str) -> str:

        st = list()
        for c in s:
            if c == "*":
                st.pop(-1)
            else:
                st.append(c)

        return "".join(st)
        
