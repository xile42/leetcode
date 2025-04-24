class Solution:

    def rearrangeCharacters(self, s: str, target: str) -> int:

        ans = inf
        c1, c2 = Counter(s), Counter(target)
        for k in c2.keys():
            ans = min(ans, c1[k] // c2[k])

        return ans
