class Solution:

    def smallestSubsequence(self, s: str) -> str:

        left = Counter(s)
        st = list()
        for c in s:
            left[c] -= 1
            if c in st:
                continue
            while st and c < st[-1] and left[st[-1]]:
                st.pop(-1)
            st.append(c)
            
        return "".join(st)
