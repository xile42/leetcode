class Solution:

    def longestPalindrome(self, words: List[str]) -> int:

        ans = 0
        c = Counter()
        same = set()
        for s in words:
            rs = s[::-1]
            if rs in c:
                ans += 2
                c[rs] -= 1
                if c[rs] == 0:
                    del c[rs]
            else:
                c[s] += 1
            if s == rs:
                same.add(s)

        for s in same:
            if c[s] > 0:
                ans += 1
                break

        return ans * 2
