class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:

        n = len(part)

        if n == 1:
            return s.replace(part, "")

        st = list()
        for c in s:
            if not st or c != part[-1] or len(st) < n - 1:
                st.append(c)
                continue
            if "".join(st[-n + 1:]) == part[:-1]:
                del st[-n + 1:]
                continue
            else:
                st.append(c)

        return "".join(st)
