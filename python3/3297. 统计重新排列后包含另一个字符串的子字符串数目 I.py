class Solution:

    def validSubstringCount(self, word1: str, word2: str) -> int:

        left = ans = 0
        cnt = Counter(word2)
        for right in range(len(word1)):
            cnt[word1[right]] -= 1

            if all(i <= 0 for i in cnt.values()):

                while all(i <= 0 for i in cnt.values()):
                    cnt[word1[left]] += 1
                    left += 1
                left -= 1
                cnt[word1[left]] -= 1
                ans += right + 1 - (right - left)

        return ans
