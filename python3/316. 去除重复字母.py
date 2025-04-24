class Solution:

    def removeDuplicateLetters(self, s: str) -> str:

        cnt = Counter(s)
        vis = set()
        st = list()
        for c in s:
            while st and c not in st and c < st[-1] and cnt[st[-1]] > 0:
                st.pop(-1)
            if c not in st:
                st.append(c)
            cnt[c] -= 1

        return "".join(st)
