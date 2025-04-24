class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(start):

            if start >= len(s):
                return True

            success = False
            for w in wordDict:
                if s[start:].startswith(w):
                    if dfs(start+len(w)):
                        success = True
                        break

            return success

        return dfs(0)
