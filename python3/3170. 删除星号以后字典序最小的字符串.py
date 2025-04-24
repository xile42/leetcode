class Solution:

    def clearStars(self, s: str) -> str:

        st = [[] for _ in range(26)]
        h = []
        for idx, char in enumerate(s):
            if char == "*":
                for _st in st:
                    if _st:
                        _st.pop(-1)
                        break
            else:
                st[ord(char) - ord("a")].append([idx, char])

        results = list()
        for _st in st:
            results += _st
        results.sort()

        return "".join([char for _, char in results])
