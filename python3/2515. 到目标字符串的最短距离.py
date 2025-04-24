class Solution:

    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:

        ans = inf
        n = len(words)
        for i, w in enumerate(words):
            if w == target:
                dis = min((startIndex - i + n) % n, (i - startIndex + n) % n)
                ans = min(ans, dis)

        return -1 if ans == inf else ans
