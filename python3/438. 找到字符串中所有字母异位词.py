class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:

        cp = Counter(p)
        c = Counter(s[:len(p)])

        left = 0
        ans = list()

        if c == cp:
            ans.append(left)

        for right in range(len(p), len(s)):

            c[s[right]] += 1
            c[s[left]] -= 1
            left += 1

            if c == cp:
                ans.append(left)

        return ans
