class Solution:

    def repeatedCharacter(self, s: str) -> str:

        cnt = [0] * 26
        for c in s:
            if cnt[ord(c)-ord("a")] == 1:
                return c
            cnt[ord(c)-ord("a")] += 1
