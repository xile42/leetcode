class Solution:
    
    def makeGood(self, s: str) -> str:

        st = list()
        for char in s:
            if len(st):
                a = 1 if char.isupper() else 0
                b = 1 if st[-1].isupper() else 0
                if a + b == 1 and char.lower() == st[-1].lower():
                    st.pop(-1)
                    continue
            st.append(char)

        return "".join(st)
