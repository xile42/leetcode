class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        cnt = Counter(s1)
        k = len(s1)
        for i, c in enumerate(s2):
            if c in cnt:
                cnt[c] -= 1
            if i >= k:
                if s2[i - k] in cnt:
                    cnt[s2[i - k]] += 1
            if i >= k - 1 and all(i == 0 for i in cnt.values()):
                return True

        return False
