class Solution:

    def numSpecialEquivGroups(self, words: List[str]) -> int:

        cnt = Counter()
        for s in words:
            even = "".join(sorted([c for i, c in enumerate(s) if i % 2 == 0]))
            odd = "".join(sorted([c for i, c in enumerate(s) if i % 2 == 1]))
            key = even + "_" + odd
            cnt[key] += 1

        return len(cnt)
