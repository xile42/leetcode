class Solution:

    def numberOfSubstrings(self, s: str) -> int:

        c = Counter()
        ans = left = 0
        n = len(s)
        for right in range(n):
            c[s[right]] += 1
            while all(c[k] > 0 for k in ["a", "b", "c"]):
                c[s[left]] -= 1
                left += 1
            ans += left

        return ans
