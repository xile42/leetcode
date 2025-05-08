class Solution:

    def expressiveWords(self, s: str, words: List[str]) -> int:

        parts = list()
        for c, ite in groupby(s):
            parts.append([c, len(list(ite))])

        ans = 0
        for w in words:

            this_parts = list()
            for c, ite in groupby(w):
                this_parts.append([c, len(list(ite))])
            if len(parts) != len(this_parts):
                continue

            success = True
            for (c1, l1), (c2, l2) in zip(parts, this_parts):
                if c1 != c2 or l1 < l2:
                    success = False
                    break
                diff = l1 - l2
                if diff == 0 or (diff > 0 and l1 >= 3):
                    continue
                success = False
                break

            if success:
                ans += 1

        return ans
