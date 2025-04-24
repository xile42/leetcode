class Solution:

    def maxRepOpt1(self, text: str) -> int:

        mx = Counter(text)
        ans = left = 0
        c = Counter()
        for right in range(len(text)):
            c[text[right]] += 1
            while len(c) > 2 or len(c) == 2 and min(c.values()) > 1:
                c[text[left]] -= 1
                if c[text[left]] == 0:
                    del c[text[left]]
                left += 1
            mx_v = max(c.values())
            mx_k = None
            for k in c:
                if c[k] == mx_v:
                    mx_k = k
            ans = max(ans, min(right - left + 1, mx[mx_k]))

        return ans
