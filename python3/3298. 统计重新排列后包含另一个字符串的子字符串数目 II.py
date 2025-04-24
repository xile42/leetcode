class Solution:

    def validSubstringCount(self, word1: str, word2: str) -> int:

        left = ans = 0
        cnt = defaultdict(int)
        for c in word2:
            cnt[c] += 1
        diff = len(cnt)
        for right in range(len(word1)):
            cnt[word1[right]] -= 1
            if cnt[word1[right]] == 0:
                diff -= 1
            if diff == 0:
                while diff == 0:
                    cnt[word1[left]] += 1
                    left += 1
                    if cnt[word1[left - 1]] == 1:
                        diff += 1
                ans += left
                left -= 1
                cnt[word1[left]] -= 1
                diff = 0

        return ans
