class Solution:

    def longestNiceSubstring(self, s: str) -> str:

        @cache
        def dfs(s):

            if len(s) < 2:
                return str()

            result = None
            for i, c in enumerate(s):
                if (c.isupper() and c.lower() not in s) or (c.islower() and c.upper() not in s):
                    left = dfs(s[:i])
                    right = dfs(s[i+1:])
                    this_result = left if len(left) >= len(right) else right
                    result = this_result if result is None or len(result) < len(this_result) else result

            return s if result is None else result

        result = dfs(s)

        return result
