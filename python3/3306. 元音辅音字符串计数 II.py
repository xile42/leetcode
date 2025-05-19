class Solution:

    def countOfSubstrings(self, word: str, k: int) -> int:

        def f(word, k):

            ans = left = 0
            valid = {"a", "e", "i", "o", "u"}
            counter = Counter()
            cnt = 0
            for right, c in enumerate(word):
                if c in valid:
                    counter[c] += 1
                else:
                    cnt += 1
                while cnt >= k and all(counter[key] > 0 for key in valid):
                    if word[left] in valid:
                        counter[word[left]] -= 1
                    else:
                        cnt -= 1
                    left += 1
                ans += left

            return ans

        return f(word, k) - f(word, k + 1)
