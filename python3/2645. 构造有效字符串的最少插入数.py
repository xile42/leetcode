class Solution:

    def addMinimum(self, word: str) -> int:

        st = list()
        ans = 0

        for c in word:
            if c == "a":
                if not st:
                    st.append(c)
                else:
                    ans += 3 - len(st)
                    st = ["a"]
            elif c == "b":
                if not st:
                    ans += 1
                    st = ["a", "b"]
                elif len(st) == 1:
                    st.append(c)
                else:
                    ans += 3 - len(st) + 1
                    st = ["a", "b"]
            else:
                ans += 2 - len(st)
                st = list()

        ans += 3 - len(st) if st else 0

        return ans
