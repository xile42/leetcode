class Solution:

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        valid = set(string.ascii_lowercase)

        def check(s):

            i = 0
            for c in s:
                if i < len(pattern) and c == pattern[i]:
                    i += 1
                elif c not in valid:
                    return False

            return i == len(pattern)

        ans = [check(s) for s in queries]

        return ans
