class Solution:

    def largestCombination(self, candidates: List[int]) -> int:

        cnt = Counter()
        for n in candidates:
            for i in range(n.bit_length()):
                if n & (1 << i):
                    cnt[i] += 1

        return max(cnt.values())
