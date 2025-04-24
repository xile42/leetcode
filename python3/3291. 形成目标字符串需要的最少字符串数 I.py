def min(a: int, b: int) -> int:
    return a if a < b else b


class Trie:

    def __init__(self):

        self.next = dict()

    def generate(self, words):

        for w in words:
            cur = self
            for c in w:
                if c not in cur.next:
                    cur.next[c] = Trie()
                    cur = cur.next[c]
                else:
                    cur = cur.next[c]

    def check(self, tar):

        cur = self
        for c in tar:
            if c not in cur.next:
                return False
            cur = cur.next[c]

        return True


class Solution:

    def minValidStrings(self, words: List[str], target: str) -> int:

        trie = Trie()
        trie.generate(words)

        @cache
        def dfs(s):

            if trie.check(s):
                return 1

            ans = inf
            cur = trie
            for idx, c in enumerate(s):
                if ans == 2:
                    break
                if c in cur.next:
                    t = dfs(s[idx+1:])
                    if t != -1:
                        ans = min(ans, t + 1)
                    cur = cur.next[c]
                else:
                    break

            return ans if ans < inf else -1

        return dfs(target)
